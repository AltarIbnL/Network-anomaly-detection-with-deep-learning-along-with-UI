from PyQt5.Qt import *
import ui2 as ui2
import sys
import multiprocessing as mp
import title as title
import UI.cut_pcap as cut_pcap
import dataprocess.datasave as datasave
import predict_c_2 as predict
import pandas as pd
class Mainwindow(ui2.Ui_Unframewindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(None,Qt.FramelessWindowHint)

        # self.setui(self)
        self.setupUi(self)
        self.setWindowTitle('异常流量检测系统')
        self.setWindowIcon(QIcon('./resources/OCR-orange.png'))
        self.page.setStyleSheet("QWidget#page{background-color: rgb(245, 249, 252);}")

        for i in range(2):
            item = self.left_widget.item(i)  # 选中QlistWidget的不同按钮
            item.setSizeHint(QSize(30, 60))  # 设置按钮大小


        self.initDrag()
        self.slot_init()
        self.setCloseButton(True)
        self.setMinMaxButtons(True)
        self.minWidth = 1280
        self.minHeight = 720
        self.setMinimumWidth(self.minWidth)  # 设置主界面最小长宽
        self.setMinimumHeight(self.minHeight)
        self.setMouseTracking(True)  # 设置widget鼠标跟踪
        self.statusBar().hide()  # 隐藏状态栏
        self.label_8.setContentsMargins(5,5,0,0)  #设置label的边界

        self.left_widget.currentRowChanged.connect(self.display)
        #初始化表格数据
        self.tableWidget.setColumnCount(6)  # 设置表格为六列
        self.tableWidget_2.setColumnCount(8)  # 设置表格为六列
        # 创建表头
        self.tableWidget.setHorizontalHeaderLabels(['srcip', 'dstip', 'sport', 'dport', 'proto', 'data'])
        self.tableWidget_2.setHorizontalHeaderLabels(['srcip', 'dstip', 'sport', 'dport', 'proto', 'data','label','class'])
        # 禁止编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.detect_flag = 0

        self.label_7.hide() # 将进度栏的图片隐藏


    def slot_init(self):
        self.read_button.clicked.connect(self.curtail_pcap)
        self.upload_pic_5.clicked.connect(self.startdetection)



    def display(self, index):  # 将stackwidget和 listwidget进行连接
        self.stack_page.setCurrentIndex(index)

    def initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._bottom_drag = False
        self._right_drag = False
        self._left_drag = False
        self._right_bottom_corner_drag = False
        self._left_bottom_corner_drag = False

    def setCloseButton(self, bool):
        # 给widget定义一个setCloseButton函数，为True时设置一个关闭按钮
        if bool == True:
            self.CloseButton.clicked.connect(self.close)  # 按钮信号连接到关闭窗口的槽函数

    def resizeEvent(self, QResizeEvent):
        # 自定义窗口调整大小事件

        # 设置在边缘多少位置范围会触发，如左部拉伸则会在距离左边缘的5，高度为(控件高-5)的高度
        self._left_rect = [QPoint(x, y) for x in range(0, 5)
                           for y in range(5, self.height() - 5)]
        self._right_rect = [QPoint(x, y) for x in range(self.width() - 5, self.width() + 1)
                            for y in range(5, self.height() - 5)]
        self._bottom_rect = [QPoint(x, y) for x in range(5, self.width() - 5)
                             for y in range(self.height() - 5, self.height() + 1)]
        self._right_bottom_corner_rect = [QPoint(x, y) for x in range(self.width() - 5, self.width() + 1)
                                          for y in range(self.height() - 5, self.height() + 1)]
        self._left_bottom_corner_rect = [QPoint(x, y) for x in range(0, 5)
                                         for y in range(self.height() - 5, self.height() + 1)]

    def mouseMoveEvent(self, event):
        # 判断鼠标位置切换鼠标手势
        if event.pos() in self._right_bottom_corner_rect:
            self.setCursor(Qt.SizeFDiagCursor)

        elif event.pos() in self._left_bottom_corner_rect:
            self.setCursor(Qt.SizeBDiagCursor)

        elif event.pos() in self._bottom_rect:
            self.setCursor(Qt.SizeVerCursor)

        elif event.pos() in self._right_rect:
            self.setCursor(Qt.SizeHorCursor)

        elif event.pos() in self._left_rect:
            self.setCursor(Qt.SizeHorCursor)

        else:
            self.setCursor(Qt.ArrowCursor)

        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        if Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(event.pos().x(), self.height())
            event.accept()
        elif Qt.LeftButton and self._left_drag:
            # 左侧调整窗口高度
            if self.width() - event.pos().x() > self.minWidth:
                self.resize(self.width() - event.pos().x(), self.height())
                self.move(self.x() + event.pos().x(), self.y())
            event.accept()
        elif Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self._right_bottom_corner_drag:
            # 右下角同时调整高度和宽度
            self.resize(event.pos().x(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self._left_bottom_corner_drag:
            # 左下角同时调整高度和宽度
            if self.width() - event.pos().x() > self.minWidth:
                self.resize(self.width() - event.pos().x(), event.pos().y())
                self.move(self.x() + event.pos().x(), self.y())
            event.accept()
        elif Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            self.move(event.globalPos() - self.move_DragPosition)
            event.accept()


    def mousePressEvent(self, event):
        # 重写鼠标点击的事件
        if (event.button() == Qt.LeftButton) and (event.pos() in self._right_bottom_corner_rect):
            # 鼠标左键点击右下角边界区域
            self._right_bottom_corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._left_bottom_corner_rect):
            # 鼠标左键点击左下角边界区域
            self._left_bottom_corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._left_rect):
            # 鼠标左键点击左侧边界区域
            self._left_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            # 鼠标左键点击右侧边界区域
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            # 鼠标左键点击下侧边界区域
            self._bottom_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.y() < 30):  # 距离标题最上方小于30时，变为拖拽
            # 鼠标左键点击标题栏区域
            self._move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._right_bottom_corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        self._left_drag = False
        self._left_bottom_corner_drag = False

    def mouseDoubleClickEvent(self, event):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        return QWidget().mouseDoubleClickEvent(event)


    def setMinMaxButtons(self, bool):
        # 给widget定义一个setMinMaxButtons函数，为True时设置一组最小化最大化按钮
        if bool == True:
            # 最小化按钮
            self.MinButton.clicked.connect(self.showMinimized)  # 按钮信号连接到最小化窗口的槽函数
            # 最大化按钮
            self.MaxButton.clicked.connect(self._changeNormalButton)  # 按钮信号连接切换到恢复窗口大小按钮函数

    def _changeNormalButton(self):
        # 切换到恢复窗口大小按钮
        try:
            self.showMaximized()  # 先实现窗口最大化
            # self._MaximumButton.setText(b'\xef\x80\xb2'.decode("utf-8"))  # 更改按钮文本
            self.MaxButton.setToolTip("恢复")  # 更改按钮提示
            self.MaxButton.disconnect()  # 断开原本的信号槽连接
            self.MaxButton.clicked.connect(self._changeMaxButton)  # 重新连接信号和槽
        except:
            pass




    def return_pic(self):
        # 隐藏两个控件
        self.delete_pic.hide()
        self.label_pic.hide()

        # 展示四个控件
        self.pic_label_1.show()
        self.pic_label_2.show()
        self.upload_pic.show()
        self.spaceitem.show()
        self.upload_pic_5.setEnabled(False)  # 取消激活识别按钮

    def select_path(self):
        self.fname_p = QFileDialog.getOpenFileName(self, 'Open file', "", "*.csv;;All Files(*)")
        # print(self.fname)
        if self.fname_p == ('', ''):
            pass
        else:
            self.addrEdit.setText(self.fname_p[0])

            # title.read_csv(self.fname[0],self.tableWidget)
    def getshowdata(self,):
        data_csv_data = pd.read_csv(r"./data/show_data.csv", encoding='gbk', parse_dates=True)
        data_csv_label = pd.read_csv(r"./data/show_label.csv", encoding='gbk', parse_dates=True)
        length = len(data_csv_label) - (data_csv_data['flowmember'].max() - (data_csv_data['flowmember'].max() //64) *64)
        k=(data_csv_data['flowmember'].max() //64) *64
        for i in range(length, len(data_csv_label)):
            data_csv_label['label'][k] = data_csv_label['label'][i]
            data_csv_label['classes'][k] = data_csv_label['classes'][i]
            k+= 1
        j = 1
        i = 0
        count = 0
        while i < len(data_csv_data):
            if data_csv_data['flowmember'][i] == j:
                data_csv_data['label'][i] = data_csv_label['label'][j-1]
                data_csv_data['classes'][i]=data_csv_label['classes'][j-1]
                i += 1
            else:
                j = j + 1
                #         print("i",i)
                if j > data_csv_data['flowmember'].max():
                    break
                data_csv_data['label'][i] = data_csv_label['label'][j-1]
                data_csv_data['classes'][i] = data_csv_label['classes'][j-1]
                i += 1
        return data_csv_data

    def curtail_pcap(self):
        self.label_6.setText('程序正在执行，请稍等')
        integrate = [self.label_5,self.label_6,self.label_7]
        #替换显示的图片
        self.label_5.hide()
        self.label_7.show()
        self.tableWidget.clearContents()

        num_cores = int(mp.cpu_count())
        pool = mp.Pool(num_cores)
        moder = cut_pcap.pcap_cut()  # 继承截取pcap的类,传入
        clip_num = int(self.lineEdit_2.text())  #截取数据包的数量
        # moder.read_pcap2('benign.csv',pool)
        self.data = moder.read_pcap2('save.pkl', pool,clip_num) # 获得pcap提取的流量包的数据
        # csv_path = 'benign.csv'
        # pickle_path = 'save.pkl'
        # title.read_csv(csv_path,self.tableWidget)  #将csv读取到PYQT5
        title.read_pickle(self.data, self.tableWidget)  # 将pickle读取到PYQT5
        QMessageBox.information(self, 'pcap截取', '截取成功！')
        # data_save=datasave.savedata("./"+csv_path,filename="test_data")
        data_save=datasave.savedata(self.data,filename="test_data")

        data_save.save_excel()
        self.label_6.setText('程序未运行')
        self.label_5.show()
        self.label_7.hide()

    def startdetection(self):
        # path=self.addrEdit.text()
        self.tableWidget_2.clearContents()
        path = r'./test_data.csv'
        # print(os.listdir())
        predicted=predict.predict(path)
        predicted.finallmainmodel1()
        predicted.finallmainmodel2()
        predicted.finallmainmodel3()
        predicted.statistic()
        data_csv_data=self.getshowdata()
        self.saveshowdata(data_csv_data)
        # data_orginal = pd.read_csv(r"./save.csv", encoding='gbk', parse_dates=True)
        data_orginal = pd.read_pickle(r"save.pkl")

        data_show = pd.read_csv(r"./data/shown.csv", encoding='gbk', parse_dates=True)
        data_orginal['label'] = 0
        data_orginal['classes']=0
        data_orginal=self.finalldata(data_orginal,data_show)
        self.savelabelshown(data_orginal)
        title.read_csv('./data/shown_finall.csv',self.tableWidget_2)

    def saveshowdata(self,data_csv_data):
        import xlwt
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet('My Worksheet')
        worksheet.write(0,0,label='data')
        worksheet.write(0,1,label='flowmember')
        worksheet.write(0,2,label='label')
        worksheet.write(0,3,label='classes')
        for i in range(len(data_csv_data)):
            worksheet.write(i + 1, 0, label=str(data_csv_data['data'][i]))
            worksheet.write(i + 1, 1, label=str(data_csv_data['flowmember'][i]))
            worksheet.write(i + 1, 2, label=str(data_csv_data['label'][i]))
            worksheet.write(i + 1, 3, label=str(data_csv_data['classes'][i]))
        workbook.save('./data/shown.csv')
        data = pd.read_excel('./data/shown.csv', index_col=0)
        data.to_csv('./data/shown.csv', encoding='utf-8')
    def finalldata(self,data_orginal, data_show):
        for i in range(len(data_orginal)):
            for j in range(len(data_show)):
                if data_orginal['data'][i] == data_show['data'][j]:
                    data_orginal['label'][i]=data_show['label'][j]
                    data_orginal['classes'][i]=data_show['classes'][j]
        return data_orginal
    def savelabelshown(self,data_orginal):
        import xlwt
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet('My Worksheet')
        worksheet.write(0, 0, label='srcip')
        worksheet.write(0, 1, label='dstip')
        worksheet.write(0, 2, label='sport')
        worksheet.write(0, 3, label='dport')
        worksheet.write(0, 4, label='proto')
        worksheet.write(0, 5, label='data')
        worksheet.write(0, 6, label='label')
        worksheet.write(0, 7, label='classes')
        for i in range(len(data_orginal)):
            worksheet.write(i+1,0, label=str(data_orginal['srcip'][i]))
            worksheet.write(i+1,1, label=str(data_orginal['dstip'][i]))
            worksheet.write(i+1,2, label=str(data_orginal['sport'][i]))
            worksheet.write(i+1,3, label=str(data_orginal['dport'][i]))
            worksheet.write(i+1,4, label=str(data_orginal['proto'][i]))
            worksheet.write(i+1,5, label=str(data_orginal['data'][i]))
            worksheet.write(i+1,6, label=str(data_orginal['label'][i]))
            worksheet.write(i+1,7, label=str(data_orginal['classes'][i]))
        workbook.save('./data/shown_finall.csv')
        data = pd.read_excel('./data/shown_finall.csv', index_col=0)
        data.to_csv('./data/shown_finall.csv', encoding='utf-8')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mp.freeze_support()  #避免在打包过程中出现无限弹窗
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())
