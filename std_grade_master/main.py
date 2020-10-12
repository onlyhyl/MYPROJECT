# -*- coding:utf8 -*-

import os
import sys
import time
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from data import DATA
from ui_windows import Ui_MainWindow, Ui_Form_up, Ui_Form_down, Ui_Form_noupdown, Ui_Form_eval
import importlib


def love():
    char = 'forever'
    allChar = []
    for y in range(12, -12, -1):
        lst = []
        lst_con = ''
        for x in range(-30, 30):
            formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
        lst.append(lst_con)
        allChar += lst
    print('\n'.join(allChar))
    time.sleep(5)


def load(stfile, update):
    # 处理数据
    print('check: ', stfile)

    # 加载学生信息
    data = DATA(stfile)
    data.make_data()  # 录入所有学生的姓名成绩
    data.paint(update)  # 把学生的姓名成绩做成图，并写入qt显示图用的资源文件
    data.jinbu()  # 加载一直进步的名单
    data.tuibu()  # 加载一直退步的名单
    data.bodong() # 加载波动的名单
    data.eval() # 加载平均分
    # 把图资源.qrc转为.py加载进程序
    # if not os.path.exists('stpics.py'):
    # if update:
    stfile = data.stfile
    os.system(r'pyrcc5 -o stpics{}.py {}/stpicsqrc.qrc'.format(n, stfile.split('.')[0]))
    return data


def run():
    stfiles = []
    for file in os.listdir('.'):
        if '.' in file:
            if file.split('.')[1] == 'xls' or file.split('.')[1] == 'xlsx':
                stfiles.append(file)

    if stfiles:
        # 选项
        print('-' * 50)
        print('find {} files:'.format(len(stfiles)))
        for i in range(len(stfiles)):
            print('{}: {}'.format(i + 1, stfiles[i]))
            if i == len(stfiles) - 1:
                exitnum = i + 2
                print('{}: exit'.format(exitnum))

        # 选择
        zjpinput = input('choose file to check: ')
        if int(zjpinput) == exitnum:
            print('see u! \n')
            love()
            exit()

        # 读取
        stfile = stfiles[int(zjpinput) - 1]
        if os.path.exists(stfile.replace(' ', '').split('.')[0]):
            update = input('update? (y/n) ')
        else:
            update = 'y'
        if update == 'y' or update == 'Y':
            data = load(stfile, True)
        else:
            data = load(stfile, False)

        stnames = data.names
        upnames = data.upnames
        downnames = data.downnames
        noupdownnames = data.noupdownnames
        unit_eval = data.unit_eval

        # 在while true循环中无法读取图片资源
        # if os.path.exists('stpics.py'):
        #     base_path = getattr(sys, '_METPASS', os.path.dirname(os.path.abspath(__file__)))
        #     sys.path.append(base_path)
        #     import stpics
        module_name = 'stpics{}'.format(n)  # 模块名的字符串
        importlib.import_module(module_name)  # 导入的就是需要导入的那个metaclass
        os.remove(module_name + '.py')

        app = QApplication(sys.argv)

        # 主窗口
        ui = Ui_MainWindow(stnames, stfile)
        mainwindow = QtWidgets.QMainWindow()
        ui.setupUi(mainwindow)
        mainwindow.show()

        # 进步窗口
        class Form_up(QMainWindow, Ui_Form_up):
            def __init__(self):
                super(Form_up, self).__init__()
                self.setupUi(self, upnames)

        myWin_up = Form_up()
        ui.upButton.clicked.connect(myWin_up.show)

        # 退步窗口
        class Form_down(QMainWindow, Ui_Form_down):
            def __init__(self):
                super(Form_down, self).__init__()
                self.setupUi(self, downnames)

        myWin_down = Form_down()
        ui.downButton.clicked.connect(myWin_down.show)

        # 波动窗口
        class Form_noupdown(QMainWindow, Ui_Form_noupdown):
            def __init__(self):
                super(Form_noupdown, self).__init__()
                self.setupUi(self, noupdownnames)
        myWin_noupdown = Form_noupdown()
        ui.noupdownButton.clicked.connect(myWin_noupdown.show)

        # 平均分窗口
        class Form_eval(QMainWindow, Ui_Form_eval):
            def __init__(self):
                super(Form_eval, self).__init__()
                self.setupUi(self, unit_eval)
        myWin_eval = Form_eval()
        ui.evalButton.clicked.connect(myWin_eval.show)

        app.exec_()
        # sys.exit(app.exec_())

    else:
        print('no excel! try to set the excel to "dist". (or call hyl!!! ()\n')
        time.sleep(10)


n = 0
while True:
    # n += 1
    # try:
    run()
    # except Exception as e:
    #     print('error! call hyl!!!  ({})\n'.format(e))
    #     time.sleep(10)
