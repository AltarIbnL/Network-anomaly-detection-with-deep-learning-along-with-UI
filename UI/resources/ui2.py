# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Unframewindow(object):
    def setupUi(self, Unframewindow):
        Unframewindow.setObjectName("Unframewindow")
        Unframewindow.setWindowModality(QtCore.Qt.NonModal)
        Unframewindow.resize(973, 759)
        Unframewindow.setMouseTracking(True)
        Unframewindow.setStatusTip("")
        Unframewindow.setAutoFillBackground(False)
        Unframewindow.setStyleSheet("QListWidget, QListView, QTreeWidget, QTreeView {\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    \n"
"    color: #cccccc;\n"
"    background: #2e2e36;\n"
"}\n"
"\n"
"QListWidget::Item:selected {\n"
"    background: #26262e;\n"
"    color: #fd7e19;\n"
"    border-left: 5px solid #fd9536;\n"
"    \n"
"}\n"
"HistoryPanel:hover {\n"
"    background: rgb(52, 52, 52);\n"
"}\n"
"/**********Title**********/\n"
"QTitleLabel{\n"
"        background-color: Gainsboro;\n"
"        font: 100 10pt;\n"
"}\n"
"\n"
"\n"
"/**********Button**********/\n"
"QTitleButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: black;\n"
"    border: 0px;\n"
"    font: 100 10pt;\n"
"}\n"
"QTitleButton#MinButton:hover,#MaxButton:hover{\n"
"    background-color: #D0D0D1;\n"
"    border: 0px;\n"
"    font: 100 10pt;\n"
"\n"
"\n"
"}\n"
"\n"
"QTitleButton#CloseButton:hover{\n"
"    background-color: #D32424;\n"
"    color: white;\n"
"    border: 0px;\n"
"    font: 100 10pt;\n"
"    \n"
"}\n"
"\n"
"QTitleButton#MinButton{\n"
"    image: url(./resource/short.png);\n"
"    \n"
"}\n"
"QTitleButton#CloseButton{\n"
"     image: url(./resource/exit.png);\n"
"}\n"
"QTitleButton#MaxButton{\n"
"     image: url(./resource/restore.png);\n"
"}\n"
"\n"
"\n"
"")
        Unframewindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Unframewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.left.setMinimumSize(QtCore.QSize(150, 0))
        self.left.setMaximumSize(QtCore.QSize(150, 16777215))
        self.left.setMouseTracking(True)
        self.left.setStyleSheet("background: #2e2e36;")
        self.left.setObjectName("left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon_1 = QtWidgets.QLabel(self.left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_1.sizePolicy().hasHeightForWidth())
        self.icon_1.setSizePolicy(sizePolicy)
        self.icon_1.setMinimumSize(QtCore.QSize(150, 100))
        self.icon_1.setMaximumSize(QtCore.QSize(150, 100))
        self.icon_1.setMouseTracking(True)
        self.icon_1.setStyleSheet("image: url(:/icon/res/OCR识别异常记录.png);\n"
"\n"
"background-color: #2e2e36;")
        self.icon_1.setText("")
        self.icon_1.setWordWrap(False)
        self.icon_1.setObjectName("icon_1")
        self.verticalLayout.addWidget(self.icon_1)
        self.icon_bottom_label = QtWidgets.QLabel(self.left)
        self.icon_bottom_label.setMinimumSize(QtCore.QSize(120, 50))
        self.icon_bottom_label.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.icon_bottom_label.setFont(font)
        self.icon_bottom_label.setStyleSheet("background: #2e2e36;\n"
"color: #cccccc;\n"
"border-bottom:0.5px solid rgb(240, 240, 240,30%);\n"
"\n"
"")
        self.icon_bottom_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.icon_bottom_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.icon_bottom_label.setLineWidth(0)
        self.icon_bottom_label.setScaledContents(False)
        self.icon_bottom_label.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_bottom_label.setObjectName("icon_bottom_label")
        self.verticalLayout.addWidget(self.icon_bottom_label, 0, QtCore.Qt.AlignHCenter)
        self.left_widget = QtWidgets.QListWidget(self.left)
        self.left_widget.setMinimumSize(QtCore.QSize(150, 0))
        self.left_widget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.left_widget.setBaseSize(QtCore.QSize(0, 0))
        self.left_widget.setMouseTracking(True)
        self.left_widget.setStyleSheet("QListWidget, QListView, QTreeWidget, QTreeView {\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    \n"
"    color: #cccccc;\n"
"    background: #2e2e36;\n"
"}\n"
"\n"
"QListWidget::Item:selected {\n"
"    background: #26262e;\n"
"    color: #fd7e19;\n"
"    border-left: 5px solid #fd9536;\n"
"    \n"
"}\n"
"HistoryPanel:hover {\n"
"    background: rgb(52, 52, 52);\n"
"}")
        self.left_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_widget.setSelectionRectVisible(False)
        self.left_widget.setObjectName("left_widget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/test/resource/极速识别.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/test/resource/极速响应.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.left_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/test/resource/文字 (1).png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/test/resource/文字.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.left_widget.addItem(item)
        self.verticalLayout.addWidget(self.left_widget)
        self.horizontalLayout_2.addWidget(self.left)
        self.right_widget = QtWidgets.QWidget(self.centralwidget)
        self.right_widget.setObjectName("right_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_widget = QtWidgets.QWidget(self.right_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_widget.sizePolicy().hasHeightForWidth())
        self.label_widget.setSizePolicy(sizePolicy)
        self.label_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.label_widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_widget.setMouseTracking(True)
        self.label_widget.setStyleSheet("QWidget#label_widget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"\n"
"\n"
"}\n"
"")
        self.label_widget.setObjectName("label_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.label_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.MinButton = QTitleButton(self.label_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MinButton.sizePolicy().hasHeightForWidth())
        self.MinButton.setSizePolicy(sizePolicy)
        self.MinButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.MinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MinButton.setMouseTracking(True)
        self.MinButton.setStyleSheet("")
        self.MinButton.setText("")
        self.MinButton.setFlat(True)
        self.MinButton.setObjectName("MinButton")
        self.horizontalLayout.addWidget(self.MinButton)
        self.MaxButton = QTitleButton(self.label_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MaxButton.sizePolicy().hasHeightForWidth())
        self.MaxButton.setSizePolicy(sizePolicy)
        self.MaxButton.setMinimumSize(QtCore.QSize(40, 0))
        self.MaxButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.MaxButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MaxButton.setMouseTracking(True)
        self.MaxButton.setText("")
        self.MaxButton.setFlat(True)
        self.MaxButton.setObjectName("MaxButton")
        self.horizontalLayout.addWidget(self.MaxButton)
        self.CloseButton = QTitleButton(self.label_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setMinimumSize(QtCore.QSize(40, 0))
        self.CloseButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setMouseTracking(True)
        self.CloseButton.setText("")
        self.CloseButton.setFlat(True)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout.addWidget(self.CloseButton)
        self.verticalLayout_2.addWidget(self.label_widget)
        self.stack_page = QtWidgets.QStackedWidget(self.right_widget)
        self.stack_page.setMinimumSize(QtCore.QSize(0, 0))
        self.stack_page.setObjectName("stack_page")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("QWidget#page{\n"
"    background-color: rgb(245, 249, 252);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_show_camera = QtWidgets.QLabel(self.page)
        self.label_show_camera.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/icon/test/resource/camera.png);")
        self.label_show_camera.setScaledContents(False)
        self.label_show_camera.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_show_camera.setObjectName("label_show_camera")
        self.verticalLayout_7.addWidget(self.label_show_camera)


        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.cam_photo = QtWidgets.QPushButton(self.page)
        self.cam_photo.setMinimumSize(QtCore.QSize(180, 30))
        self.cam_photo.setMaximumSize(QtCore.QSize(180, 30))
        self.cam_photo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cam_photo.setStyleSheet("\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color: rgb(253, 149, 54);\n"
"    \n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 161, 75);\n"
"    border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    font: 9pt \"微软雅黑\"  ;\n"
"}\n"
"")
        self.cam_photo.setObjectName("cam_photo")
        self.gridLayout.addWidget(self.cam_photo, 0, 0, 1, 1)
        self.cam_project = QtWidgets.QPushButton(self.page)
        self.cam_project.setMinimumSize(QtCore.QSize(180, 30))
        self.cam_project.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cam_project.setFont(font)
        self.cam_project.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cam_project.setStyleSheet("\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color: rgb(253, 149, 54);\n"
"    \n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 161, 75);\n"
"    border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    font: 9pt \"微软雅黑\"  ;\n"
"}\n"
"")
        self.cam_project.setObjectName("cam_project")
        self.gridLayout.addWidget(self.cam_project, 0, 3, 1, 1)
        self.cam_deal = QtWidgets.QPushButton(self.page)
        self.cam_deal.setMinimumSize(QtCore.QSize(180, 30))
        self.cam_deal.setMaximumSize(QtCore.QSize(180, 30))
        self.cam_deal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cam_deal.setStyleSheet("\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color: rgb(253, 149, 54);\n"
"    \n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 161, 75);\n"
"    border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    font: 9pt \"微软雅黑\"  ;\n"
"}\n"
"")
        self.cam_deal.setObjectName("cam_deal")
        self.gridLayout.addWidget(self.cam_deal, 0, 2, 1, 1)
        self.cam_open = QtWidgets.QPushButton(self.page)
        self.cam_open.setMinimumSize(QtCore.QSize(180, 30))
        self.cam_open.setMaximumSize(QtCore.QSize(180, 30))
        self.cam_open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cam_open.setStyleSheet("\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color: rgb(253, 149, 54);\n"
"    \n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 161, 75);\n"
"    border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    font: 9pt \"微软雅黑\"  ;\n"
"}\n"
"")
        self.cam_open.setObjectName("cam_open")
        self.gridLayout.addWidget(self.cam_open, 0, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.cam_pic = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.cam_pic.sizePolicy().hasHeightForWidth())
        self.cam_pic.setSizePolicy(sizePolicy)
        self.cam_pic.setMinimumSize(QtCore.QSize(20, 20))
        self.cam_pic.setMaximumSize(QtCore.QSize(20, 20))
        self.cam_pic.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/图片.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cam_pic.setIcon(icon2)
        self.cam_pic.setFlat(True)
        self.cam_pic.setObjectName("cam_pic")
        self.verticalLayout_7.addWidget(self.cam_pic, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_7.setStretch(0, 1)
        self.stack_page.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("QWidget{\n"
"    background-color: rgb(245, 249, 252);\n"
"}\n"
"")
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.r_bottom_widget = QtWidgets.QWidget(self.widget)
        self.r_bottom_widget.setStyleSheet("")
        self.r_bottom_widget.setObjectName("r_bottom_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.r_bottom_widget)
        self.horizontalLayout_3.setContentsMargins(14, 14, 14, 14)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pic_widget = QtWidgets.QWidget(self.r_bottom_widget)
        self.pic_widget.setEnabled(True)
        self.pic_widget.setStyleSheet("QWidget#pic_widget{\n"
"    border:0.5px solid lightgray; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.pic_widget.setObjectName("pic_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pic_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.delete_pic = QtWidgets.QPushButton(self.pic_widget)
        self.delete_pic.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_pic.sizePolicy().hasHeightForWidth())
        self.delete_pic.setSizePolicy(sizePolicy)
        self.delete_pic.setMinimumSize(QtCore.QSize(70, 30))
        self.delete_pic.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.delete_pic.setFont(font)
        self.delete_pic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_pic.setStyleSheet("\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(240, 240, 240);\n"
"    \n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(253, 149, 54);\n"
"    border: 1px solid rgb(253, 149, 54) ;\n"
"    border-radius:7px;\n"
"    font: 9pt \"微软雅黑\"  ;\n"
"}\n"
"")
        self.delete_pic.setFlat(False)
        self.delete_pic.setObjectName("delete_pic")
        self.verticalLayout_4.addWidget(self.delete_pic, 0, QtCore.Qt.AlignRight)
        self.pic_label_1 = QtWidgets.QLabel(self.pic_widget)
        self.pic_label_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_label_1.sizePolicy().hasHeightForWidth())
        self.pic_label_1.setSizePolicy(sizePolicy)
        self.pic_label_1.setStyleSheet("\n"
"image: url(:/icon/test/resource/label_pic.png);\n"
"background-color: rgb(255, 255, 255);")
        self.pic_label_1.setText("")
        self.pic_label_1.setObjectName("pic_label_1")
        self.verticalLayout_4.addWidget(self.pic_label_1)
        self.pic_label_2 = QtWidgets.QLabel(self.pic_widget)
        self.pic_label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_label_2.sizePolicy().hasHeightForWidth())
        self.pic_label_2.setSizePolicy(sizePolicy)
        self.pic_label_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.pic_label_2.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);")
        self.pic_label_2.setObjectName("pic_label_2")
        self.verticalLayout_4.addWidget(self.pic_label_2)
        self.upload_pic = QtWidgets.QPushButton(self.pic_widget)
        self.upload_pic.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_pic.sizePolicy().hasHeightForWidth())
        self.upload_pic.setSizePolicy(sizePolicy)
        self.upload_pic.setMinimumSize(QtCore.QSize(200, 50))
        self.upload_pic.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.upload_pic.setFont(font)
        self.upload_pic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_pic.setStyleSheet("\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color: rgb(253, 149, 54);\n"
"    \n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 161, 75);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    font: 11.5pt \"微软雅黑\"  ;\n"
"}\n"
"")
        self.upload_pic.setFlat(False)
        self.upload_pic.setObjectName("upload_pic")
        self.verticalLayout_4.addWidget(self.upload_pic, 0, QtCore.Qt.AlignHCenter)
        self.spaceitem = QtWidgets.QLabel(self.pic_widget)
        self.spaceitem.setMinimumSize(QtCore.QSize(0, 50))
        self.spaceitem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spaceitem.setText("")
        self.spaceitem.setObjectName("spaceitem")
        self.verticalLayout_4.addWidget(self.spaceitem)
        self.verticalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.setStretch(2, 1)
        self.horizontalLayout_3.addWidget(self.pic_widget)
        self.text_widget = QtWidgets.QWidget(self.r_bottom_widget)
        self.text_widget.setStyleSheet("QWidget#text_widget{\n"
"    border:0.5px solid lightgray; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.text_widget.setObjectName("text_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.text_widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.text_widget)
        self.label_3.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top:2px;\n"
"border-bottom:1px solid lightgray;\n"
"padding-bottom:8px ;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.text_widget)
        self.textEdit.setStyleSheet("border:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setLineWidth(0)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setCursorWidth(0)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.horizontalLayout_3.addWidget(self.text_widget)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.r_bottom_widget)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_6.addWidget(self.widget)
        self.upload_pic_4 = QtWidgets.QPushButton(self.page_2)
        self.upload_pic_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_pic_4.sizePolicy().hasHeightForWidth())
        self.upload_pic_4.setSizePolicy(sizePolicy)
        self.upload_pic_4.setMinimumSize(QtCore.QSize(250, 45))
        self.upload_pic_4.setMaximumSize(QtCore.QSize(250, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.upload_pic_4.setFont(font)
        self.upload_pic_4.setStyleSheet("QPushButton:enabled\n"
"{\n"
"    background-color: rgb(255, 161, 75);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    font: 11.5pt \"微软雅黑\"  ;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color: rgb(253, 149, 54);\n"
"    \n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color: lightgray;\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    font: 11.5pt \"微软雅黑\"  ;\n"
"    \n"
"}")
        self.upload_pic_4.setFlat(False)
        self.upload_pic_4.setObjectName("upload_pic_4")
        self.verticalLayout_6.addWidget(self.upload_pic_4, 0, QtCore.Qt.AlignRight)
        self.stack_page.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stack_page)
        self.horizontalLayout_2.addWidget(self.right_widget)
        Unframewindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Unframewindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 26))
        self.menubar.setObjectName("menubar")
        Unframewindow.setMenuBar(self.menubar)
        self.pic_label_2.setBuddy(self.upload_pic)

        self.retranslateUi(Unframewindow)
        self.stack_page.setCurrentIndex(0)
        # self.upload_pic_4.clicked.connect(Unframewindow.recognize)
        QtCore.QMetaObject.connectSlotsByName(Unframewindow)

    def retranslateUi(self, Unframewindow):
        _translate = QtCore.QCoreApplication.translate
        Unframewindow.setWindowTitle(_translate("Unframewindow", "MainWindow"))
        self.icon_bottom_label.setText(_translate("Unframewindow", "<html><head/><body><p><span style=\" font-weight:600;\">OCR文字识别软件</span></p></body></html>"))
        __sortingEnabled = self.left_widget.isSortingEnabled()
        self.left_widget.setSortingEnabled(False)
        item = self.left_widget.item(0)
        item.setText(_translate("Unframewindow", "文字拍摄"))
        item = self.left_widget.item(1)
        item.setText(_translate("Unframewindow", "文字识别"))
        self.left_widget.setSortingEnabled(__sortingEnabled)
        self.MinButton.setToolTip(_translate("Unframewindow", "最小化"))
        self.MaxButton.setToolTip(_translate("Unframewindow", "最大化"))
        self.CloseButton.setToolTip(_translate("Unframewindow", "关闭窗口"))
        self.label_show_camera.setText(_translate("Unframewindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.cam_photo.setText(_translate("Unframewindow", "打开相机"))
        self.cam_project.setText(_translate("Unframewindow", "识别"))
        self.cam_deal.setText(_translate("Unframewindow", "效果处理"))
        self.cam_open.setText(_translate("Unframewindow", "拍照"))
        self.delete_pic.setText(_translate("Unframewindow", "删除"))
        self.pic_label_2.setText(_translate("Unframewindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">支持JPG,  PNG格式图片</span></p></body></html>"))
        self.upload_pic.setText(_translate("Unframewindow", "上传图片"))
        self.label_3.setText(_translate("Unframewindow", "识别结果"))
        self.textEdit.setHtml(_translate("Unframewindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.upload_pic_4.setText(_translate("Unframewindow", "开始识别"))
from title import QTitleButton
import picture_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Unframewindow = QtWidgets.QMainWindow()
    ui = Ui_Unframewindow()
    ui.setupUi(Unframewindow)
    Unframewindow.show()
    sys.exit(app.exec_())
