#-*- coding:utf8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow
# from PyQt5.QtWidgets import QApplication
from functools import partial
# from data import DATA
# import os
# import sys


class Ui_MainWindow(object):
    def __init__(self, stnames):
        self.stnames = stnames

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 装选择框的盒子模块
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 180, 540))
        self.groupBox.setObjectName("groupBox")

        # 选择框模块--各个学生
        # self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        # self.radioButton.setGeometry(QtCore.QRect(10, 20, 89, 16))
        # self.radioButton.setObjectName("radioButton")
        tmp = 0
        for i in range(len(self.stnames)):
            exec('self.radioButton_{} = QtWidgets.QRadioButton(self.groupBox)'.format(i))
            if 20 + (i*20) < 540:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 10, 20 + (i*20), 90, 15))
            else:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 90, 20 + (i*20)-520, 90, 15))
                tmp = i
            exec('self.radioButton_{}.setObjectName("radioButton_{}")'.format(i, self.stnames[i]))
            # 点击后的反应
            exec('self.radioButton_{}.clicked.connect(partial(self.slot, "{}"))'.format(i, self.stnames[i]))

        # 选择框模块--跳转到一直进步页面
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(300, 530, 90, 25))
        self.upButton.setObjectName("upButton")
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setGeometry(QtCore.QRect(500, 530, 90, 25))
        self.downButton.setObjectName("downButton")

        # 图像模块
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(250, 90, 600, 400))
        self.graphicsView.setObjectName("graphicsView")

        MainWindow.setCentralWidget(self.centralwidget)

        # 显示在主屏幕上
        self.retranslateUi(MainWindow)

        # self.radioButton.clicked.connect(self.slot1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def slot(self, name):
        print(name)
        self.graphicsView.setStyleSheet("image: url(:/pic/{}.png);\n"
                                        "border-image: url(:/pic/{}.png);".format(name, name))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        for i in range(len(self.stnames)):
            exec('self.radioButton_{}.setText(_translate("MainWindow", "{}"))'.format(i, self.stnames[i]))
        # self.radioButton.setText(_translate("MainWindow", "毕佳琪"))
        self.upButton.setText(_translate("MainWindow", "一直进步"))
        self.downButton.setText(_translate("MainWindow", "一直退步"))


class Ui_Form_up(object):

    def setupUi(self, Form, upnames):
        self.upnames = upnames
        Form.setObjectName("Form")
        Form.resize(800, 500)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 180, 440))
        self.groupBox.setObjectName("groupBox")

        tmp = 0
        for i in range(len(self.upnames)):
            exec('self.radioButton_{} = QtWidgets.QRadioButton(self.groupBox)'.format(i))
            if 20 + (i * 20) < 440:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 10, 20 + (i * 20), 90,
                                                                                            15))
            else:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 90, 20 + (i * 20) - 520,
                                                                                            90, 15))
                tmp = i
            exec('self.radioButton_{}.setObjectName("radioButton_{}")'.format(i, self.upnames[i]))
            # 点击后的反应
            exec('self.radioButton_{}.clicked.connect(partial(self.slot, "{}"))'.format(i, self.upnames[i]))

        # 图像模块
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(220, 60, 550, 400))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)


    def slot(self, name):
        print('up check: ',name)
        self.graphicsView.setStyleSheet("image: url(:/pic/{}.png);\n"
                                        "border-image: url(:/pic/{}.png);".format(name, name))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        for i in range(len(self.upnames)):
            exec('self.radioButton_{}.setText(_translate("Form", "{}"))'.format(i, self.upnames[i]))


class Ui_Form_down(object):

    def setupUi(self, Form, downnames):
        self.downnames = downnames
        Form.setObjectName("Form")
        Form.resize(800, 500)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 180, 440))
        self.groupBox.setObjectName("groupBox")

        tmp = 0
        for i in range(len(self.downnames)):
            exec('self.radioButton_{} = QtWidgets.QRadioButton(self.groupBox)'.format(i))
            if 20 + (i * 20) < 440:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 10, 20 + (i * 20), 90,
                                                                                            15))
            else:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 90, 20 + (i * 20) - 520,
                                                                                            90, 15))
                tmp = i
            exec('self.radioButton_{}.setObjectName("radioButton_{}")'.format(i, self.downnames[i]))
            # 点击后的反应
            exec('self.radioButton_{}.clicked.connect(partial(self.slot, "{}"))'.format(i, self.downnames[i]))

        # 图像模块
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(220, 60, 550, 400))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)


    def slot(self, name):
        print('down check: ',name)
        self.graphicsView.setStyleSheet("image: url(:/pic/{}.png);\n"
                                        "border-image: url(:/pic/{}.png);".format(name, name))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        for i in range(len(self.downnames)):
            exec('self.radioButton_{}.setText(_translate("Form", "{}"))'.format(i, self.downnames[i]))


# # 处理数据
# data = DATA('三（2）班单科 同步学堂U1 成绩统计表.xls')
# data.make_data() #录入所有学生的姓名成绩
# data.paint(True) #把学生的姓名成绩做成图，并写入qt显示图用的资源文件
# data.jinbu() #加载一直进步的名单
# data.tuibu() #加载一直退步的名单
# stnames = data.names
# upnames = data.upnames
# downnames = data.downnames
#
# # 把图资源.qrc转为.py加载进程序
# stfile = data.stfile #excel表名称
# if not os.path.exists('stpics.py'):
#     os.system(r'pyrcc5 -o stpics.py {}/stpicsqrc.qrc'.format(stfile.split('.')[0]))
# if os.path.exists('stpics.py'):
#     base_path = getattr(sys, '_METPASS', os.path.dirname(os.path.abspath(__file__)))
#     sys.path.append(base_path)
#     import stpics
#
#
# app = QApplication(sys.argv)
#
# # 主窗口
# ui = Ui_MainWindow(stnames)
# mainwindow = QtWidgets.QMainWindow()
# ui.setupUi(mainwindow)
# mainwindow.show()
#
#
# # 进步窗口
# class Form_up(QMainWindow, Ui_Form_up):
#     def __init__(self):
#         super(Form_up, self).__init__()
#         self.setupUi(self, upnames)
# myWin_up = Form_up()
# ui.upButton.clicked.connect(myWin_up.show)
#
#
# # 退步窗口
# class Form_down(QMainWindow, Ui_Form_down):
#     def __init__(self):
#         super(Form_down, self).__init__()
#         self.setupUi(self, downnames)
# myWin_down = Form_down()
# ui.downButton.clicked.connect(myWin_down.show)
#
# sys.exit(app.exec_())