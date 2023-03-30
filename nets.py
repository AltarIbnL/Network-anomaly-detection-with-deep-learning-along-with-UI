
from __future__ import print_function, division, absolute_import
import os
import torch
import torch.nn as nn
import torch.nn.functional as F

torch.nn.SmoothL1Loss
####-------------------------------------------事先定义
# # 三级平行模型（模型）
class TPCNN(nn.Module):
	def __init__(self, num_class=10, head_payload=False):
		super(TPCNN, self).__init__()
		# 上
		self.uconv1 = nn.Sequential(  #
			nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(16, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		self.uconv2 = nn.Sequential(  #
			nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(32, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		# 中
		self.mconv1 = nn.Sequential(  #
			nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(32, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		# 下
		self.dconv1 = nn.Sequential(  #
			nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(32, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
			nn.MaxPool2d(kernel_size=2)
		)

		self.uconv3 = nn.Sequential(  #
			nn.Conv2d(96, 128, kernel_size=3, stride=1, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(128, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)

		self.mconv2 = nn.Sequential(  #
			nn.Conv2d(96, 128, kernel_size=3, stride=2, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(128, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)

		self.dconv2 = nn.Sequential(  #
			nn.Conv2d(96, 128, kernel_size=3, stride=1, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(128, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)

		self.uconv4 = nn.Sequential(  #
			nn.Conv2d(256, 512, kernel_size=3, stride=2, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(512, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		self.globalconv1 = nn.Sequential(
			nn.Conv2d(896, 1024, kernel_size=3, stride=1, padding=1),
			nn.BatchNorm2d(1024, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU()
		)

		self.dmaxpool = nn.MaxPool2d(kernel_size=2,padding=1)

		#         self.lstm1 = nn.LSTM(256,512, 2)
		#         self.lstm2 = nn.LSTM(self.i_size*2,self.i_size*2, 2)

		self.avpool = nn.AdaptiveAvgPool2d(2)
		#         self.globallstm = nn.LSTM(512, 256, 1)

		self.fc1 = nn.Linear(1024*2*2, 512)
		self.fc2 = nn.Linear(512, num_class)

	def forward(self, x,train):
		# print("x",x.shape)
		# 上
		uout = self.uconv1(x)
		uout = self.uconv2(uout)

		# 中
		mout = self.mconv1(x)

		# 下
		dout = self.dconv1(x)

		# 连接
		# print("uout", uout.shape)
		# print("mout", mout.shape)
		# print("dout", dout.shape)

		out = torch.cat((uout, mout, dout), dim=1)
		# print("out", out.shape)

		# 上
		uout = self.uconv3(out)

		# 中
		mout = self.mconv2(out)
		# 下
		dout = self.dconv2(out)

		# 连接
		# print("uout", uout.shape)
		# print("dout", dout.shape)

		out = torch.cat((uout, dout), dim=1)
		# print("out", out.shape)

		# 上
		uout = self.uconv4(out)

		# 中

		# 下
		dout = self.dmaxpool(out)

		# 连接
		# print("uout", uout.shape)
		# print("mout", mout.shape)
		# print("dout", dout.shape)

		out = torch.cat((uout, mout, dout), dim=1)
		# print("out",out.shape)
		# 最后的网络
		# print("out", out.shape)
		out = self.globalconv1(out)
		out = self.avpool(out)

		# 全连接层
		# print("out", out.shape)
		out=out.view(-1,1024*2*2)
		out = self.fc1(out)
		out = self.fc2(out)

		return out

# 三级平行时序模型
class TPCNN_C(nn.Module):
	def __init__(self, num_class=10, head_payload=False):
		super(TPCNN_C, self).__init__()
		# 上
		self.uconv1 = nn.Sequential(  #
			nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(16, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		self.uconv2 = nn.Sequential(  #
			nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=0, dilation=1, bias=True),
			nn.BatchNorm2d(32, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		# 中
		self.mconv1 = nn.Sequential(  #
			nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=0, dilation=1, bias=True),
			nn.BatchNorm2d(32, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		# 下
		self.dconv1 = nn.Sequential(  #
			nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=0, dilation=1, bias=True),
			nn.BatchNorm2d(32, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
			nn.MaxPool2d(kernel_size=2)
		)
		# 上
		self.uconv3 = nn.Sequential(  #
			nn.Conv2d(96, 128, kernel_size=3, stride=2, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(128, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		# 中
		#         self.mconv2 = nn.Sequential(    #
		#             nn.Conv2d(96,128, kernel_size=3, stride=2, padding=1,dilation=1,bias=True),
		#             nn.BatchNorm2d(128,eps=1e-05,momentum=0.9,affine=True),
		#             nn.ReLU(),
		#             nn.MaxPool2d(kernel_size=2)
		#         )
		self.mlstm = nn.LSTM(48, 8, 2)

	# 下
		self.dconv2 = nn.Sequential(  #
			nn.Conv2d(96, 128, kernel_size=3, stride=2, padding=1, dilation=1, bias=True),
			nn.BatchNorm2d(128, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)

		self.uconv4 = nn.Sequential(  #
			nn.Conv2d(256, 256, kernel_size=2, stride=2, padding=0, dilation=1, bias=True),###______
			nn.BatchNorm2d(256, eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU(),
		)
		self.globalconv1 = nn.Sequential(
			nn.Conv2d(912,912, kernel_size=3, stride=1, padding=1),
			nn.BatchNorm2d(912,eps=1e-05, momentum=0.9, affine=True),
			nn.ReLU()
		)

		self.dmaxpool = nn.MaxPool2d(kernel_size=2)

	#         self.lstm1 = nn.LSTM(256,512, 2)
	#         self.lstm2 = nn.LSTM(self.i_size*2,self.i_size*2, 2)

		self.avpool = nn.AdaptiveAvgPool2d(2)
	#   self.globallstm = nn.LSTM(512, 256, 1)

		self.fc1 = nn.Linear(912* 2*2, 128)
		self.fc2 = nn.Linear(128,num_class)


	def forward(self, x,train):
		# print(x.shape)
		# 上
		uout = self.uconv1(x)
		uout = self.uconv2(uout)
		# 中
		mout = self.mconv1(x)

		# 下
		dout = self.dconv1(x)

		# 连接
		out = torch.cat((uout, mout, dout), dim=1)
		# print("out", out.shape)

		# 上
		uout = self.uconv3(out)

		# 中
		# print(out.shape)
		# m=out.view(64,-1,48)
		m = out.view(out.size(0), -1, 48)
		mout,_= self.mlstm(m)
		# print("mout", mout.shape)

		# 下
		dout = self.dconv2(out)

		# 连接
		# print("uout",uout.shape)
		# print("mout", mout.shape)
		# print("dout", dout.shape)

		out = torch.cat((uout, dout), dim=1)
		# print("out", out.shape)

		# 上
		uout = self.uconv4(out)
		# print("uout",uout.shape)
		# 中

		# 下
		dout = self.dmaxpool(out)
		# print("dout",dout.shape)
		# 连接
		#

		mout = torch.reshape(mout, [mout.size(0), -1, 2, 2])
		dout = torch.reshape(dout, [mout.size(0), -1, 2, 2])
		uout = torch.reshape(uout, [mout.size(0), -1, 2, 2])
		out = torch.cat((uout, mout, dout,), dim=1)

		# 最后的网络
		# print("out", out.shape)
		# print(out.shape)
		out = self.globalconv1(out)
		out = self.avpool(out)

		# 全连接层
		out=out.view(-1,912*2*2)
		# out = out.view(-1, 1024 * 2 * 2)
		out = self.fc1(out)
		out = self.fc2(out)
		# print("out", out.shape)

		return out


#夏本辉师兄模型
class Pccn(nn.Module):
	def __init__(self, num_class=12,head_payload=False):
		super(Pccn, self).__init__()
		self.globe_conv = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1, stride=1, bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
        )
		self.branchA_1 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1, stride=2, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
        )
		self.branchA_2 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1, stride=1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, padding=0, stride=2),
        )
		self.shortcut_1 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=64, kernel_size=1, padding=0, stride=2, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
        )
		self.branchB_1 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=96, kernel_size=3, padding=1, stride=1, bias=False),
            nn.BatchNorm2d(96),
            nn.ReLU(),
        )
		self.branchB_2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=96, kernel_size=3, padding=1, stride=1, bias=False),
            nn.BatchNorm2d(96),
            nn.ReLU(),
        )
		self.shortcut_2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=192, kernel_size=1, padding=0, stride=1, bias=False),
            nn.BatchNorm2d(192),
            nn.ReLU(),
        )
		self.branchC_1 = nn.Sequential(
            nn.Conv2d(in_channels=192, out_channels=256, kernel_size=3, padding=1, stride=2, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(),
        )
		self.branchC_2 = nn.Sequential(
            nn.MaxPool2d(kernel_size=2, padding=1, stride=2),
        )
		self.shortcut_3 = nn.Sequential(
            nn.Conv2d(in_channels=192, out_channels=448, kernel_size=1, padding=0, stride=2, bias=False),
            nn.BatchNorm2d(448),
            nn.ReLU(),
        )
		self.globe_conv_2 = nn.Sequential(
            nn.Conv2d(in_channels=448, out_channels=896, kernel_size=3, padding=1, stride=1, bias=False),
            nn.BatchNorm2d(896),
            nn.ReLU(),
        )
		self.max_pool = nn.Sequential(nn.MaxPool2d(kernel_size=4))
		self.fc = nn.Linear(896, num_class)
	def forward(self, x,train):
		x = self.globe_conv(x)
		out_1 = self.branchA_1(x)
		out_2 = self.branchA_2(x)
		out = torch.cat([out_1, out_2], dim=1)
		x = self.shortcut_1(x)
		out += x
		out = F.relu(out)
		out_1 = self.branchB_1(out)
		out_2 = self.branchB_2(out)
		out = torch.cat([out_1, out_2], dim=1)
		x = self.shortcut_2(x)
		out += x
		out = F.relu(out)
		out_1 = self.branchC_1(out)
		out_2 = self.branchC_2(out)
		# print("out_1",out_1.shape)
		# print("out_2",out_2.shape)
		out = torch.cat([out_1, out_2], dim=1)
		# print("out",out.shape)
		x = self.shortcut_3(x)
		# print("x",x.shape)
		out += x
		out = F.relu(out)
		out = self.globe_conv_2(out)
		out = self.max_pool(out)
		out = out.view(-1, 896 * 1 * 1)
		out = self.fc(out)
		return out