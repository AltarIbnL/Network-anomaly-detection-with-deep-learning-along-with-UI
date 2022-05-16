#-*- coding:utf-8 -*-
#!/usr/bin/python
#-*- encoding:utf-8 -*-

import numpy as np 
import time
import pandas as pd 
import torch
import tqdm
import shutil
import torch.optim as optim
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split



def train(train_loader,model,loss_function,optimizer,epoch):
	'''
	train_data: train data,include label in the last dimension
	model: net model 
	loss: type of loss to be used
	optimizer: training optimmizer
	epoch: current epoch
	return: None
	'''
	batch_time =AverageMeter()
	data_time = AverageMeter()
	losses = AverageMeter()
	acc = AverageMeter()
	losses_list=[]
	accuracy_list=[]
	model.train()

	end = time.time()

	for step,(feature,label) in enumerate(train_loader):  # feature 返回的是数据集的数据，label返回的是标签
		feature = Variable(feature).cuda(non_blocking=True)
		label = Variable(label).cuda(non_blocking=True)
		# input feature to train，得到预测标签y_pred
		y_pred = model(feature,train=True)
		# 将输出值输入到损失函数进行处理
		# squeeze()默认将所有的1的维度删除，此时输入的label是[256,1]，squeeze后是[256]，相当于都存放在一个数据里面了
		loss = loss_function(y_pred,label.squeeze())

		# losses_list.append(loss.item()) #保存损失度画图

		# label_sqe = label.squeeze()
		# input the value of loss to the variable losses
		# print(feature.size(0))
		losses.update(loss.item(),feature.size(0))
		# compute accuracy,batch_size = 256,y_pred 的shape(256,12) 分别判断这256个流量里面属于12个分类的准确率
		# 获得本次输入的准确率
		pred_acc,pred_count = accuracy(y_pred.data,label,topk=(1,1))
		acc.update(pred_acc,pred_count)

		# accuracy_list.append(pred_acc) #保存精度画图

		optimizer.zero_grad() # 梯度清0
		loss.backward()
		optimizer.step()


		batch_time.update(time.time() - end,1) #更新时间
		end = time.time()


		if step % 10 == 0:
			print('epoch:[{0}][{1}/{2}]\t'
				  'Time:{batch_time.val:.3f} ({batch_time.avg:.3f})\t'
				  'Loss:{loss.val:.4f} ({loss.avg:.4f})\t'
				  'Accuracy:{acc.val:.3f} ({acc.avg:.3f})'.format(
				  	epoch,step,len(train_loader),batch_time=batch_time,loss=losses,acc=acc
				  	)
				)
	# return accuracy_list,losses_list

def validate(validate_loader,model,loss_function,best_precision,lowest_loss):
	batch_time = AverageMeter()
	losses = AverageMeter()
	acc = AverageMeter()

	#switch to evaluable mode,forbidden batchnormalization and dropout
	model.eval()

	end = time.time()
	for step,(feature,label) in enumerate(validate_loader):
		# feature,label = data
		
		feature = Variable(feature).cuda(non_blocking=True)
		label = Variable(label).cuda(non_blocking=True)

		with torch.no_grad():  # 停止梯度的计算，节省GPU算力和显存
			y_pred = model(feature,train=True)
			loss = loss_function(y_pred,label.squeeze())

		#measure accuracy and record loss
		pred_acc,PRED_COUNT = accuracy(y_pred.data,label,topk=(1,1))
		losses.update(loss.item(),feature.size(0))
		acc.update(pred_acc,PRED_COUNT)

		
		batch_time.update(time.time()-end,1)
		end = time.time()

		if step % 10 == 0:
			print('TrainVal: [{0}/{1}]\t'
				'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
				'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
				'Accuray {acc.val:.3f} ({acc.avg:.3f})'.format(
					step, len(validate_loader), batch_time=batch_time, loss=losses, acc=acc))

	print(' * Accuray {acc.avg:.3f}'.format(acc=acc), '(Previous Best Acc: %.3f)' % best_precision,
		' * Loss {loss.avg:.3f}'.format(loss=losses), 'Previous Lowest Loss: %.3f)' % lowest_loss)
	return acc.avg,losses.avg


def test(test_loader, model, num_class, topk=1, ):
	"""
	test_loader: test data, type of DataLoader
	model: pretrained model
	filename: the file used to save inference result
	"""
	top1_prob = []
	top1_pred_label = []
	topk_prob = []
	topk_pred_label = []
	actual_label = []
	correct = 0
	train = False

	predict_num = torch.zeros((1, num_class))
	acc_num = torch.zeros((1, num_class))
	target_num = torch.zeros((1, num_class))
	topk_predict_num = torch.zeros((1, num_class))
	topk_acc_num = torch.zeros((1, num_class))
	topk_target_num = torch.zeros((1, num_class))

	model.eval()
	for step, (feature, label) in enumerate(test_loader):
		# retrun the testing feature and it label
		feature = Variable(feature)
		label = Variable(label)

		with torch.no_grad():
			y_pred = model(feature, train)
			# 使用softmax预测结果
			smax = nn.Softmax(1)
			smax_out = smax(y_pred)

		probility, pred_label = torch.topk(smax_out, topk)
		p1, l1 = torch.topk(smax_out, 1)  # 返回top1
		# 使用scatter 根据l1.view(-1,1)对全0数组进行分配,对预测最大值的位置置1
		top1_mask = torch.zeros(y_pred.size()).scatter_(1, l1.cpu().view(-1, 1), 1)
		topk_mask = torch.zeros(y_pred.size())
		topk_label_index = pred_label.view(1, -1)
		# 根据输入的batch_size，即feature的行数生成列表
		topk_label_row = np.array([[x] * topk for x in range(feature.size(0))]).reshape(1, -1).tolist()

		topk_mask[topk_label_row, topk_label_index] = 1
		actual_mask = torch.zeros(y_pred.size()).scatter_(1, label.cpu().view(-1, 1), 1)
		top1_acc_mask = top1_mask * actual_mask
		topk_acc_mask = topk_mask * actual_mask
		# 判断正确的数量
		acc_num += top1_acc_mask.sum(0)
		predict_num += top1_mask.sum(0)
		target_num += actual_mask.sum(0)
		topk_acc_num += topk_acc_mask.sum(0)
		topk_predict_num += topk_mask.sum(0)
		topk_target_num += actual_mask.sum(0)

		actual_label += label.squeeze().tolist()
		topk_prob += probility.tolist()
		topk_pred_label += pred_label.tolist()
		top1_prob += p1.tolist()
		top1_pred_label += l1.tolist()

	# 里面储存的是测试集所有数据的预测标签和预测值
	top1_prob = np.array(top1_prob)
	top1_pred_label = np.array(top1_pred_label)
	topk_prob = np.array(topk_prob)
	topk_pred_label = np.array(topk_pred_label)
	actual_label = np.array(actual_label).reshape(-1, 1)
	# acc_num  = tp    target_num = TP+FN   predict_num = tp+fp (预测正确+预测为正确但是错误的)
	recall = acc_num / target_num
	precision = acc_num / predict_num
	F1 = 2 * recall * precision / (recall + precision)
	# accuracy = （TP+TN）/(total example)
	accuracy = acc_num.sum(1) / target_num.sum(1)
	# accuracys = acc_num / target_num
	topk_recall = topk_acc_num / topk_target_num
	topk_precision = topk_acc_num / topk_predict_num
	topk_F1 = 2 * topk_recall * topk_precision / (topk_recall + topk_precision)
	topk_accuracy = topk_acc_num.sum(1) / topk_target_num.sum(1)
	# topk_accuracys = topk_acc_num / topk_target_num

	recall = (recall.numpy() * 100).round(4)
	precision = (precision.numpy() * 100).round(4)
	F1 = (F1.numpy() * 100).round(4)
	accuracy = (accuracy.numpy() * 100).round(4)
	# accuracys = (accuracys.numpy()*100).round(4)
	topk_recall = (topk_recall.numpy() * 100).round(4)
	topk_precision = (topk_precision.numpy() * 100).round(4)
	topk_F1 = (topk_F1.numpy() * 100).round(4)
	topk_accuracy = (topk_accuracy.numpy() * 100).round(4)
	# topk_accuracys = (topk_accuracys.numpy()*100).round(4)

	result = (top1_prob, top1_pred_label, topk_prob, topk_pred_label, actual_label)
	top1_metrics = (accuracy, recall, precision, F1)
	topk_metrics = (topk_accuracy, topk_recall, topk_precision, topk_F1)


	return result, top1_metrics, topk_metrics


def accuracy(y_pred,y_label,topk=(1,)):  # 默认去top1准确率
	""""
	y_pred: the net predected label
	y_label: the actual label
	topk: the top k accuracy
	return: accuracy and data length
	""" 
	final_acc = 0
	maxk = max(topk)

	PRED_COUNT = y_label.size(0)
	#预测准确的数量
	PRED_CORRECT_COUNT = 0
	# 获得y_pred 对12个类别的top k值(此时k=1)，返回prob是按大小排序后的值，pred_label是索引
	prob,pred_label = y_pred.topk(maxk,dim=1,largest=True,sorted=True)
	for x in range(pred_label.size(0)):  # 遍历每一行（即每一个数据流）
		if int(pred_label[x]) == y_label[x]:  # 判断标签是否正确
			PRED_CORRECT_COUNT += 1
	
	if PRED_COUNT == 0:
		return final_acc

	final_acc = PRED_CORRECT_COUNT / PRED_COUNT
	return final_acc*100,PRED_COUNT


def adjust_learning_rate(model,weight_decay,base_lr,lr_decay):
	base_lr = base_lr / lr_decay
	return optim.Adam(model.parameters(),base_lr,weight_decay=weight_decay,amsgrad=True)

def save_checkpoint(state,is_best,is_lowest_loss,filename):
	s_filename = './model/%s/checkpoint.pth.tar' %filename
	torch.save(state,s_filename)
	if is_best:
		shutil.copyfile(s_filename,'./model/%s/model_best.pth.tar' %filename)
	if is_lowest_loss:
		shutil.copyfile(s_filename,'./model/%s/lowest_loss.pth.tar' %filename)


class DealDataSet(Dataset):  # 将数据从numpy转换成tensor
	def __init__(self,data_list,header_payload=True):
		#将数据转换成tensor
		self.x = torch.from_numpy(data_list[:,:-1])
		# 修改数据类型从LongTensor为FloatTensor
		self.x = self.x.type(torch.FloatTensor)
		if header_payload ==True:    # 判断读取的数据是否包含header、payload
			self.x = self.x.view(self.x.shape[0],1,22,22)
		else:
			self.x = self.x.view(self.x.shape[0],1,16,16)
		self.y = torch.from_numpy(data_list[:,[-1]])
		self.y = self.y.type(torch.LongTensor)
		self.len = self.x.shape[0]
		self.xshape = self.x.shape
		self.yshape = self.y.shape


	def __getitem__(self,index):
		return self.x[index],self.y[index]

	def __len__(self):
		return self.len




class AverageMeter(object):
	"""计算和保存当前值与平均值"""
	def __init__(self):
		self.reset()

	def reset(self):
		self.val = 0
		self.avg = 0
		self.sum = 0
		self.count = 0

	def update(self,val,n=1):
		self.val = val
		self.sum += val*n
		self.count += n
		self.avg = self.sum / self.count

class TrainDataSetPayload_2012():

	def __init__(self, ):
		super(TrainDataSetPayload_2012, self).__init__()

	def read_csv(self):
		# payload_benign = pd.read_csv('./2012dataset/label_Bruteforce_SSH.csv')
		payload_nonclassifed = pd.read_csv('./2012dataset/label_non-classifed_attacks.csv')
		payload_inflter = pd.read_csv('./2012dataset/label_Infltering.csv')
		payload_http = pd.read_csv('./2012dataset/label_HTTP.CSV')
		payload_distributedenial = pd.read_csv('./2012dataset/label_Distributed_denial.csv')
		payload_brutessh = pd.read_csv('./2012dataset/label_Bruteforce_SSH.csv')

		# print('finish reading dataset, cost time :',time.time() - start)
		# 剔除第一列
		# benign = payload_benign.values[:, 1:]
		nonclassifed = payload_nonclassifed.values[:, 0:]
		inflter = payload_inflter.values[:, 0:]
		http = payload_http.values[:, 0:]
		distributedenial = payload_distributedenial.values[:, 0:]
		brutessh = payload_brutessh.values[:, 0:]

		return  nonclassifed, inflter, http, distributedenial, brutessh

	def get_item(self):
		nonclassifed, inflter, http, distributedenial, brutessh = self.read_csv()

		# print('shape of benign: ', benign.shape)
		print('shape of nonclassifed: ', nonclassifed.shape)
		print('shape of inflter: ', inflter.shape)
		print('shape of http: ', http.shape)
		print('shape of distributedenial: ', distributedenial.shape)
		print('shape of rutessh: ', brutessh.shape)

		# 剔除最后一列标签
		# x_benign = benign[:, :-1]
		x_nonclassifed = nonclassifed[:, :-1]
		x_inflter = inflter[:, :-1]
		x_http = http[:, :-1]
		x_distributedenial = distributedenial[:, :-1]
		x_brutessh = brutessh[:, :-1]

		# 获取标签
		# y_benign = benign[:, -1]
		y_nonclassifed = nonclassifed[:, -1]
		y_inflter = inflter[:, -1]
		y_http = http[:, -1]
		y_distributedenial = distributedenial[:, -1]
		y_brutessh = brutessh[:, -1]

		# x_tr_benign, x_te_benign, y_tr_benign, y_te_benign = train_test_split(x_benign, y_benign, test_size=0.2,random_state=1)
		x_tr_nonclassifed, x_te_nonclassifed, y_tr_nonclassifed, y_te_nonclassifed = train_test_split(x_nonclassifed,
																									  y_nonclassifed,
																									  test_size=0.2,
																									  random_state=1)
		x_tr_inflter, x_te_inflter, y_tr_inflter, y_te_inflter = train_test_split(x_inflter, y_inflter, test_size=0.2,
																				  random_state=1)
		x_tr_http, x_te_http, y_tr_http, y_te_http = train_test_split(x_http, y_http, test_size=0.2, random_state=1)
		x_tr_distributedenial, x_te_distributedenial, y_tr_distributedenial, y_te_distributedenial = train_test_split(
			x_distributedenial, y_distributedenial, test_size=0.2, random_state=1)
		x_tr_brutessh, x_te_brutessh, y_tr_brutessh, y_te_brutessh = train_test_split(x_brutessh, y_brutessh,
																					  test_size=0.2, random_state=1)

		x_train = np.concatenate(
			(x_tr_nonclassifed, x_tr_inflter, x_tr_http, x_tr_distributedenial, x_tr_brutessh))
		y_train = np.concatenate(
			(y_tr_nonclassifed, y_tr_inflter, y_tr_http, y_tr_distributedenial, y_tr_brutessh))

		x_test = np.concatenate(
			(x_te_nonclassifed, x_te_inflter, x_te_http, x_te_distributedenial, x_te_brutessh))
		y_test = np.concatenate(
			(y_te_nonclassifed, y_te_inflter, y_te_http, y_te_distributedenial, y_te_brutessh))

		return x_train, y_train, x_test, y_test

class TrainDataSetPayload_2012_cat():

	def __init__(self,data_type ):
		self.data_type = data_type
		super(TrainDataSetPayload_2012_cat, self).__init__()

	def read_csv(self):
		if self.data_type==1:
			payload_bengin = pd.read_csv('./data/4/5/label_bengin.CSV')
			payload_nonclassifed = pd.read_csv('./data/4/5/label_non-classifed_attacks.CSV')
			payload_inflter = pd.read_csv('./data/4/5/label_Infltering.CSV')
			payload_http = pd.read_csv('./data/4/5/label_HTTP.CSV')
			payload_distributedenial = pd.read_csv('./data/4/5/label_Distributed_denial.CSV')
			payload_brutessh = pd.read_csv('./data/4/5/label_Bruteforce_SSH.CSV')
		elif self.data_type==2:
			payload_nonclassifed = pd.read_csv('./6/2/label_non-classifed_attacks.csv')
			payload_inflter = pd.read_csv('./6/2/label_Infltering.csv')
			payload_http = pd.read_csv('./6/2/label_HTTP.CSV')
			payload_distributedenial = pd.read_csv('./6/2/label_Distributed_denial.csv')
			payload_brutessh = pd.read_csv('./6/2/label_Bruteforce_SSH.csv')
			# payload_bengin=pd.read_csv("./7/label_bengin.csv")
		# print('finish reading dataset, cost time :',time.time() - start)
		# 剔除第一列
		# benign = payload_benign.values[:, 1:]
		nonclassifed = payload_nonclassifed.values[:, 1:]
		inflter = payload_inflter.values[:, 1:]
		http = payload_http.values[:, 1:]
		distributedenial = payload_distributedenial.values[:, 1:]
		brutessh = payload_brutessh.values[:, 1:]
		bengin=payload_bengin.values[:,1:]


		return  nonclassifed, inflter, http, distributedenial, brutessh ,bengin

	def get_item(self):
		nonclassifed, inflter, http, distributedenial, brutessh, bengin= self.read_csv()

		# print('shape of benign: ', benign.shape)
		print('shape of nonclassifed: ', nonclassifed.shape)
		print('shape of inflter: ', inflter.shape)
		print('shape of http: ', http.shape)
		print('shape of distributedenial: ', distributedenial.shape)
		print('shape of rutessh: ', brutessh.shape)
		print('shape of bengin: ', bengin.shape)

		# 剔除最后一列标签
		# x_benign = benign[:, :-1]
		x_nonclassifed = nonclassifed[:, :-1]
		x_inflter = inflter[:, :-1]
		D_x_inflter=(x_inflter,x_nonclassifed)
		x_inflter=np.concatenate(D_x_inflter,axis=0)
		x_http = http[:, :-1]
		x_distributedenial = distributedenial[:, :-1]
		x_brutessh = brutessh[:, :-1]
		x_bengin=bengin[:,:-1]

		# 获取标签
		y_benign = bengin[:, -1]
		y_nonclassifed = nonclassifed[:, -1]
		y_inflter = inflter[:, -1]
		D_y_inflter=(y_nonclassifed,y_inflter)
		y_inflter=np.concatenate(D_y_inflter,axis=0)
		y_http = http[:, -1]
		y_distributedenial = distributedenial[:, -1]
		y_brutessh = brutessh[:, -1]

		x_tr_benign, x_te_benign, y_tr_benign, y_te_benign = train_test_split(x_bengin, y_benign, test_size=0.2,random_state=1)
		# x_tr_nonclassifed, x_te_nonclassifed, y_tr_nonclassifed, y_te_nonclassifed = train_test_split(x_nonclassifed,
		# 																							  y_nonclassifed,
		# 																							  test_size=0.2,
		# 																							  random_state=1)
		x_tr_inflter, x_te_inflter, y_tr_inflter, y_te_inflter = train_test_split(x_inflter, y_inflter, test_size=0.2,
																				  random_state=1)
		x_tr_http, x_te_http, y_tr_http, y_te_http = train_test_split(x_http, y_http, test_size=0.2, random_state=1)
		x_tr_distributedenial, x_te_distributedenial, y_tr_distributedenial, y_te_distributedenial = train_test_split(
			x_distributedenial, y_distributedenial, test_size=0.2, random_state=1)
		x_tr_brutessh, x_te_brutessh, y_tr_brutessh, y_te_brutessh = train_test_split(x_brutessh, y_brutessh,
																					  test_size=0.2, random_state=1)

		x_train = np.concatenate(
			(x_tr_benign,x_tr_inflter, x_tr_http, x_tr_distributedenial, x_tr_brutessh))
		y_train = np.concatenate(
			(y_tr_benign,y_tr_inflter, y_tr_http, y_tr_distributedenial, y_tr_brutessh))

		x_test = np.concatenate(
			(x_te_benign,x_te_inflter, x_te_http, x_te_distributedenial, x_te_brutessh))
		y_test = np.concatenate(
			(y_te_benign,y_te_inflter, y_te_http, y_te_distributedenial, y_te_brutessh))

		return x_train, y_train, x_test, y_test



