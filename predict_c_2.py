import time
import pandas as pd
import torch
import nets as my_new_nets
import torch.nn as nn
class predict():
    def __init__(self,path):
        self.path=path
        print('\nreading datset, waiting ...... ')
        self.start = time.time()

        # model1
        self.model=my_new_nets.TPCNN_C(num_class=13,head_payload=True)
        # model = nn.DataParallel(model)
        # torch.backends.cudnn.benchmark = True
        self.model = nn.DataParallel(self.model).cuda()
        self.state = {
                    'state_dict':self.model.state_dict(),  # 模型内部的参数，包括每层的权重，偏置等等
                }
        self.model.load_state_dict(torch.load("./model/pridect/model_best.pth.tar")['state_dict'])
        # print(self.model.load_state_dict(torch.load("./model/TPCCL_C/model_best.pth.tar")['state_dict']))
        self.model.eval()
        self.predicted_all=[]
        # self.predicted=[]
        # self.predicted_label=[]

         #model2
        self.model2=my_new_nets.TPCNN(num_class=13,head_payload=True)
        self.model2=nn.DataParallel(self.model2).cuda()
        self.state2= {
            'state_dict': self.model2.state_dict(),  # 模型内部的参数，包括每层的权重，偏置等等
        }
        self.model2.load_state_dict(torch.load("./model/pridect_tpcnn/model_best.pth.tar")['state_dict'])
        self.model2.eval()
        self.predicted_all2=[]
        # self.predicted2=[]
        # self.predicted_label2=[]

        #model3
        self.model3=my_new_nets.Pccn(num_class=13, head_payload=True)
        self.model3=nn.DataParallel(self.model3).cuda()
        self.state3= {
            'state_dict': self.model3.state_dict(),  # 模型内部的参数，包括每层的权重，偏置等等
        }
        self.model3.load_state_dict(torch.load("./model/pridect_Pccn/model_best.pth.tar")['state_dict'])
        self.model3.eval()
        self.predicted_all3 = []
        #为页面展示制作所建
        self.save_flow_member=[]
        self.save_flow_name=[]
    def softmax(self,x):
      x_exp = x.exp()  # m * n
      partition = x_exp.sum(dim=1, keepdim=True)  # 按列累加, m * 1
      return x_exp / partition  # 广播机制, [m * n] / [m * 1] = [m * n]

#预测函数model1
    def predict(self,data,train=True):
        torch.set_grad_enabled(True)
        outputs =self.model(data, train)
        outputs=self.softmax(outputs)
        _,predicted=torch.max(outputs,1)
        predicted=predicted.cpu().numpy()
        return predicted

#预测函数model2
    def predict2(self,data,train=True):
        torch.set_grad_enabled(True)
        outputs =self.model2(data, train)
        outputs=self.softmax(outputs)
        _,predicted=torch.max(outputs,1)
        predicted=predicted.cpu().numpy()
        return predicted
 #预测函数model3
    def predict3(self,data,train=True):
        torch.set_grad_enabled(True)
        outputs =self.model3(data, train)
        outputs=self.softmax(outputs)
        _,predicted=torch.max(outputs,1)
        predicted=predicted.cpu().numpy()
        return predicted
#保存结果数据
    def save_excel(self,):
        import xlwt
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet('My Worksheet')
        worksheet.write(0,0,label='label')
        worksheet.write(0,1,label='classes')
        for i in range(len(self.save_flow_member)):
            worksheet.write(i+1,0,label=self.save_flow_member[i])
            worksheet.write(i+1,1,label=self.save_flow_name[i])
        workbook.save('./data/show_label.csv')
        data = pd.read_excel('./data/show_label.csv', index_col=0)
        data.to_csv('./data/show_label.csv', encoding='utf-8')

#model1
    def finallmainmodel1(self,):
        file=pd.read_csv(self.path)
        print(file.shape)
        print(len(file))
        for i in range(1, (len(file) //64) + 2):
            # print(i)
            if (i *64) < len(file):
                predict_data = file.values[(i - 1) *64:i *64, 1:]
                predict_data = torch.from_numpy(predict_data)
                predict_data = predict_data.float()
                # print(predict_data.shape)
                predict_data = predict_data.view(predict_data.shape[0], 1, 22, 22)
                predicted = self.predict(predict_data)
                # print(len(predicted))
                for i in range(len(predicted)):
                    if predicted[i]==12:
                        self.predicted_all.append(0)
                    else:
                        self.predicted_all.append(1)
            else:
                predict_data = file.values[len(file)-64:len(file), 1:]
                # predict_label = file.values[len(file)-64:len(file), -1]
                predict_data = torch.from_numpy(predict_data)
                predict_data = predict_data.float()
                # print("11", len(file)-64)
                predict_data = predict_data.view(predict_data.shape[0], 1, 22, 22)
                predicted = self.predict(predict_data, False)
                # print(len(predicted))
                for i in range(len(predicted)):
                    if predicted[i] == 12:
                        self.predicted_all.append(0)
                    else:
                        self.predicted_all.append(1)
#model2
    def finallmainmodel2(self, ):
        file = pd.read_csv(self.path)
        print(file.shape)
        print(len(file))
        for i in range(1, (len(file) // 64) + 2):
            # print(i)
            if (i * 64) < len(file):
                predict_data = file.values[(i - 1) * 64:i * 64, 1:]
                predict_data = torch.from_numpy(predict_data)
                predict_data = predict_data.float()
                # print(predict_data.shape)
                predict_data = predict_data.view(predict_data.shape[0], 1, 22, 22)
                predicted = self.predict2(predict_data)
                # print(len(predicted))
                for i in range(len(predicted)):
                    if predicted[i] == 12:
                        self.predicted_all2.append(0)
                    else:
                        self.predicted_all2.append(1)
            else:
                predict_data = file.values[len(file) - 64:len(file), 1:]
                # predict_label = file.values[len(file)-64:len(file), -1]
                predict_data = torch.from_numpy(predict_data)
                predict_data = predict_data.float()
                # print("11", len(file)-64)
                predict_data = predict_data.view(predict_data.shape[0], 1, 22, 22)
                predicted = self.predict2(predict_data, False)
                # print(len(predicted))
                for i in range(len(predicted)):
                    if predicted[i] == 12:
                        self.predicted_all2.append(0)
                    else:
                        self.predicted_all2.append(1)
#model3
    def finallmainmodel3(self, ):
        file = pd.read_csv(self.path)
        print(file.shape)
        print(len(file))
        for i in range(1, (len(file) // 64) + 2):
            # print(i)
            if (i * 64) < len(file):
                predict_data = file.values[(i - 1) * 64:i * 64, 1:]
                predict_data = torch.from_numpy(predict_data)
                predict_data = predict_data.float()
                # print(predict_data.shape)
                predict_data = predict_data.view(predict_data.shape[0], 1, 22, 22)
                predicted = self.predict3(predict_data)
                # print(len(predicted))
                for i in range(len(predicted)):
                    if predicted[i] == 12:
                        self.predicted_all3.append(0)
                    else:
                        self.predicted_all3.append(1)
            else:
                predict_data = file.values[len(file) - 64:len(file), 1:]
                # predict_label = file.values[len(file)-64:len(file), -1]
                predict_data = torch.from_numpy(predict_data)
                predict_data = predict_data.float()
                # print("11", len(file)-64)
                predict_data = predict_data.view(predict_data.shape[0], 1, 22, 22)
                predicted = self.predict3(predict_data, False)
                # print(len(predicted))
                for i in range(len(predicted)):
                    if predicted[i] == 12:
                        self.predicted_all3.append(0)
                    else:
                        self.predicted_all3.append(1)
    def statistic(self,):
        count0 = 0
        count1 = 0
        for i in range(len(self.predicted_all)):
           if self.judgment(self.predicted_all[i],self.predicted_all2[i],self.predicted_all3[i])==0:
               count0+=1
               self.save_flow_member.append(0)
               self.save_flow_name.append('Normal')
           else:
               count1+=1
               self.save_flow_member.append(1)
               self.save_flow_name.append('Abnormal')
        print("0", count0);print("1", count1);
        print(self.save_flow_member)
        print(self.save_flow_name)
        self.save_excel()
    def judgment(self,pmodel1,pmodel2,pmodel3):
        if (pmodel1==pmodel2==pmodel3 and pmodel1==0) or (pmodel1==pmodel2 and pmodel1==0) or (pmodel1==pmodel3 and pmodel3==0) or (pmodel2==pmodel3 and pmodel2==0):
            return 0
        else:
            return 1



