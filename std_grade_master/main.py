import os
import sys
import time
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from data import DATA
from ui_windows import Ui_MainWindow, Ui_Form_up, Ui_Form_down

def run():
    stfiles = []
    for file in os.listdir('.'):
        if '.' in file:
            if file.split('.')[1] == 'xls' or file.split('.')[1] == 'xlsx':
                stfiles.append(file)

    if stfiles:
        print('find {} files:'.format(len(stfiles)))
        for i in range(len(stfiles)):
            print('{}: {}'.format(i+1, stfiles[i]))
        zjpinput = input('choose file to check:')
        try:
            if len(stfiles) > 1:
                stfile = stfiles[int(zjpinput)-1]
            else:
                stfile = stfiles[0]

            # 处理数据
            print('check: ', stfile)

            data = DATA(stfile)
            data.make_data()  # 录入所有学生的姓名成绩
            data.paint()  # 把学生的姓名成绩做成图，并写入qt显示图用的资源文件
            data.jinbu()  # 加载一直进步的名单
            data.tuibu()  # 加载一直退步的名单
            stnames = data.names
            upnames = data.upnames
            downnames = data.downnames

            # 把图资源.qrc转为.py加载进程序
            stfile = data.stfile  # excel表名称
            if not os.path.exists('../stpics.py'):
                os.system(r'pyrcc5 -o stpics.py {}/stpicsqrc.qrc'.format(stfile.split('.')[0]))
            if os.path.exists('../stpics.py'):
                base_path = getattr(sys, '_METPASS', os.path.dirname(os.path.abspath(__file__)))
                sys.path.append(base_path)
                import stpics

            app = QApplication(sys.argv)

            # 主窗口
            ui = Ui_MainWindow(stnames)
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

            sys.exit(app.exec_())
        except Exception as e:
            print('error! call hyl!!!  ({})\n'.format(e))

    else:
        print('no excel! try to set the excel to "dist". (or call hyl!!! ()\n')
        time.sleep(10)

while True:
    try:
        run()
    except Exception as e:
        print('error! call hyl!!!  ({})\n'.format(e))
        time.sleep(10)