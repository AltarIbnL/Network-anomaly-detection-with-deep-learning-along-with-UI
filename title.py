# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont, QCursor
from PyQt5.Qt import *
import csv
import xlrd
import pandas as pd




class QTitleLabel(QLabel):
    """
    新建标题栏标签类
    """
    def __init__(self, *args):
        # 继承父类的初始化属性，super()内部可写可不写
        # super(QTitleLabel, self).__init__(*args)
        super().__init__(*args)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setFixedHeight(30)


class QTitleButton(QPushButton):
    """
    新建标题栏按钮类
    """
    def __init__(self, *args):
        super(QTitleButton, self).__init__(*args)
        # self.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        self.setFixedWidth(40)
        self.setFlat(True)




def read_csv(filename,tableWidget3):
# filename = '1.csv'

    with open(filename)as csvfile:
        # csv.reader(csvfile, dialect='excel', **fmtparams)返回一个 reader 对象，该对象将逐行遍历 csvfile
        reader = csv.reader(csvfile)
        # 逐行读取CSV
        rows = [row for row in reader]

        for i in range(1, len(rows)):
            rowslist = rows[i]  # 获取excel每行内容
            for j in range(len(rows[i])):
                # 在tablewidget中添加行
                row = tableWidget3.rowCount()
                tableWidget3.insertRow(row)

                # 把数据写入tablewidget中
                newItem = QTableWidgetItem(str(rowslist[j]))
                tableWidget3.setItem(i - 1, j, newItem)

def read_pickle(df,tableWidget3):
    # pickle = 'test2.pkl'
    # df = pd.read_pickle(filename)

    i=1
    for val in df.itertuples(index=False):
        for j in range(len(val)):
            # 在tablewidget中添加行
            row = tableWidget3.rowCount()
            tableWidget3.insertRow(row)

            # 把数据写入tablewidget中
            newItem = QTableWidgetItem(str(val[j]))
            tableWidget3.setItem(i - 1, j, newItem)
        i+=1





if __name__ == '__main__':
    filename = '1.csv'

















