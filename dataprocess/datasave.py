import xlsxwriter
import pandas as pd
from dataprocess import  NetDataPrcoess
import xlwt
class savedata():
    def __init__(self,data,filename,pack_number=4,bits_number=121):
        self.data=data
        self.filename=filename
        self.pack_number=pack_number
        self.bits_number=bits_number
    def writedata(self,worksheet,data,size=4, length=121):
        for i in range(len(data)):
            #         print(len(data[i]))
            if len(data[i]) >= size:
                count = 1
                for j in range(size):
                    for k in range(length):
                        if k >= len(data[i][j]):
                            worksheet.write((i + 1), count, 0)
                            count += 1
                        else:
                            worksheet.write((i + 1), count, data[i][j][k])
                            count += 1
            #                 for k in range(0,1):
            #                         worksheet.write((i+1),count,data[i][j][k])
            #                         count+=1
            else:
                number = 0
                count = 1
                h = 0
                #             print(len(data[i]))
                for j in range(len(data[i])):
                    for k in range(length):
                        if k >= len(data[i][j]):
                            worksheet.write((i + 1), count, 0)
                            count += 1
                            number += 1
                        else:
                            worksheet.write((i + 1), count, data[i][j][k])
                            count += 1
                            number += 1
                for nn in range(0, size):
                    for j in range(len(data[i])):
                        for k in range(length):
                            if number <= size*length:
                                if k >= len(data[i][j]):
                                    worksheet.write((i + 1), number, 0)
                                    number += 1
                                else:
                                    worksheet.write((i + 1), number, data[i][j][k])
                                    number += 1
                            else:
                                break
                #             print(number)
                for num in range(number, size*length+1):
                    worksheet.write(i + 1, num, 0)
    def save_data(self, label_data, label_label):
        # 创建一个workbook 设置编码
        dataprocess = NetDataPrcoess.DataPrcoess()
        dataprocess.setDir('data')
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet('My Worksheet')
        worksheet.write(0, 0,label='data')
        worksheet.write(0, 1,label='flowmember')
        worksheet.write(0, 2,label='label')
        worksheet.write(0,3,label='classes')
        for i in range(len(label_data)):
            worksheet.write(i + 1, 0, label=str(label_data[i]))
            worksheet.write(i + 1, 1, label=str(label_label[i]))
        workbook.save('./data/show_data.xls')
        data = pd.read_excel('./data/show_data.xls', index_col=0)
        data.to_csv('./data/show_data.csv', encoding='utf-8')

    def save_excel(self,):   # 储存为excel
        dataprocess = NetDataPrcoess.DataPrcoess()
        dataprocess.setDir("NetData")
        # print("1")
        dataprocess.setDir("./NetData/testdata")
        # print("2")
        # data_data = pd.read_csv(self.path)
        data_data = self.data
        # 返回
        show_data,show_label=dataprocess.writeabnormaldata(data_data,"./NetData/testdata")
        workbook = xlsxwriter.Workbook(self.filename+".xls")   # 创建一个名称为filename的xls文件
        workbook.use_zip64()
        worksheet = workbook.add_worksheet()
        for i in range(0, self.pack_number*self.bits_number):
            label = "%d" % i
            worksheet.write(0, i + 1, label)
        data=dataprocess.getdata("./NetData/testdata")
        self.writedata(worksheet,data)
        workbook.close()
        data=pd.read_excel(self.filename+".xls",index_col=0)
        # data.to_csv(self.filename+".csv", encoding='utf-8')
        data.to_csv(self.filename+".csv", encoding='utf-8')
        #保存用于最后用于显示的文件
        self.save_data(show_data,show_label)
# if __name__ == '__main__':
#
#     data_save=savedata("./benign.pkl",filename="test_data")
#     # data_save=savedata("../UI/benign.csv",filename="test_data")
#     data_save.save_excel()
