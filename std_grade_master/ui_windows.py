#-*- coding:utf8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
# from PyQt5.QtWidgets import QMainWindow
# from PyQt5.QtWidgets import QApplication
from functools import partial
# from data import DATA
# import os
# import sys


class Ui_MainWindow(object):
    def __init__(self, stnames, stfile):
        self.stnames = stnames
        self.wintitle = stfile.split('.')[0]

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
        for i in range(len(self.stnames)):
            exec('self.radioButton_{} = QtWidgets.QRadioButton(self.groupBox)'.format(i))
            if 20 + (i*20) < 540:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 10, 20 + (i*20), 90, 15))
            else:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 90, 20 + (i*20)-520, 90, 15))
            exec('self.radioButton_{}.setObjectName("radioButton_{}")'.format(i, self.stnames[i]))
            # 点击后的反应
            exec('self.radioButton_{}.clicked.connect(partial(self.slot, "{}"))'.format(i, self.stnames[i]))

        # 选择框模块--跳转到一直进步页面
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(300, 500, 90, 25))
        self.upButton.setObjectName("upButton")
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setGeometry(QtCore.QRect(500, 500, 90, 25))
        self.downButton.setObjectName("downButton")
        self.noupdownButton = QtWidgets.QPushButton(self.centralwidget)
        self.noupdownButton.setGeometry(QtCore.QRect(700, 500, 90, 25))
        self.noupdownButton.setObjectName("noupdownButton")
        self.evalButton = QtWidgets.QPushButton(self.centralwidget)
        self.evalButton.setGeometry(QtCore.QRect(300, 530, 90, 25))
        self.evalButton.setObjectName("evalButton")

        # 图像模块
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(250, 80, 600, 400))
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
        MainWindow.setWindowTitle(_translate("MainWindow", self.wintitle))
        self.groupBox.setTitle(_translate("MainWindow", "所有学生"))
        for i in range(len(self.stnames)):
            exec('self.radioButton_{}.setText(_translate("MainWindow", "{}"))'.format(i, self.stnames[i]))
        # self.radioButton.setText(_translate("MainWindow", "毕佳琪"))
        self.upButton.setText(_translate("MainWindow", "一直进步"))
        self.downButton.setText(_translate("MainWindow", "一直退步"))
        self.noupdownButton.setText(_translate("MainWindow", "波动"))
        self.evalButton.setText(_translate("MainWindow", "平均分"))


class Ui_Form_up(object):

    def setupUi(self, Form, upnames):
        self.upnames = upnames
        Form.setObjectName("Form")
        Form.resize(800, 500)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 180, 440))
        self.groupBox.setObjectName("groupBox")

        for i in range(len(self.upnames)):
            exec('self.radioButton_{} = QtWidgets.QRadioButton(self.groupBox)'.format(i))
            if 20 + (i * 20) < 440:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 10, 20 + (i * 20), 90,
                                                                                            15))
            else:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 90, 20 + (i * 20) - 420,
                                                                                            90, 15))
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
        self.groupBox.setTitle(_translate("Form", "一直进步学生"))
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

        for i in range(len(self.downnames)):
            exec('self.radioButton_{} = QtWidgets.QRadioButton(self.groupBox)'.format(i))
            if 20 + (i * 20) < 440:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 10, 20 + (i * 20), 90,
                                                                                            15))
            else:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 90, 20 + (i * 20) - 420,
                                                                                            90, 15))
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
        self.groupBox.setTitle(_translate("Form", "一直退步学生"))
        for i in range(len(self.downnames)):
            exec('self.radioButton_{}.setText(_translate("Form", "{}"))'.format(i, self.downnames[i]))


class Ui_Form_noupdown(object):

    def setupUi(self, Form, noupdownnames):
        self.noupdownnames = noupdownnames
        Form.setObjectName("Form")
        Form.resize(800, 500)

        self.groupBox = QtWidgets.QGroupBox(Form)
        # self.groupBox.setGeometry(QtCore.QRect(20, 30, 250, 440))
        self.groupBox.setObjectName("groupBox")

        for i in range(len(self.noupdownnames)):
            exec('self.radioButton_{} = QtWidgets.QRadioButton(self.groupBox)'.format(i))
            if 20 + (i * 20) < 440:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 10, 20 + (i * 20), 90,
                                                                                            15))
                tmp_xloc = 10 + 90
            elif 20 + (i * 20) < 860:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 90, 20 + (i * 20) - 420,
                                                                                            90, 15))
                tmp_xloc = 90 + 90
            else:
                exec('self.radioButton_{}.setGeometry(QtCore.QRect({}, {}, {}, {}))'.format(i, 170, 20 + (i * 20) - 840,
                                                                                            90, 15))
                tmp_xloc = 170 + 90

            exec('self.radioButton_{}.setObjectName("radioButton_{}")'.format(i, self.noupdownnames[i]))
            # 点击后的反应
            exec('self.radioButton_{}.clicked.connect(partial(self.slot, "{}"))'.format(i, self.noupdownnames[i]))

        self.groupBox.setGeometry(QtCore.QRect(20, 30, tmp_xloc + 5, 440))
        # 图像模块
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        # self.graphicsView.setGeometry(QtCore.QRect(220, 60, 550, 400))
        self.graphicsView.setGeometry(QtCore.QRect(tmp_xloc + 50, 60, 550, 400))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def slot(self, name):
        print('noupdown check: ',name)
        self.graphicsView.setStyleSheet("image: url(:/pic/{}.png);\n"
                                        "border-image: url(:/pic/{}.png);".format(name, name))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "波动学生"))
        for i in range(len(self.noupdownnames)):
            exec('self.radioButton_{}.setText(_translate("Form", "{}"))'.format(i, self.noupdownnames[i]))


class Ui_Form_eval(object):
    def setupUi(self, Form, unit_eval):
        self.unit_eval = unit_eval
        Form.setObjectName("Form")
        Form.resize(500, 140)

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 480, 100))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(len(self.unit_eval)) #几列
        self.tableWidget.setRowCount(1) #几行

        # 行，通过数字标识第几行的位置
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        # 列，通过数字标识第几列的位置
        for i in range(len(self.unit_eval)):
            # 行列表头字段位置
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            # 行列值位置
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(0, i, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # 行，表头名称
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "平均分"))
        # 列，表头名称
        units = [unit for unit in self.unit_eval]
        for i in range(len(self.unit_eval)):
            unit = units[i]
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Form", unit))
            # # (0, {})第一行第n列的值
            item = self.tableWidget.item(0, i)
            item.setText(_translate("Form", str(self.unit_eval.get(unit, 0))))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
