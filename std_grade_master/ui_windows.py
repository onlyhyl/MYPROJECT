#-*- coding:utf8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


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

