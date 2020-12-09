import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from cnstd import CnStd
from cnocr import CnOcr
import time

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(350, 350)
        self.setWindowTitle("图片转文字")

        self.label = QLabel(self)
        # self.label.setText("显示图片")
        self.label.setScaledContents(True)
        self.label.setFixedSize(300, 200)
        self.label.move(25, 60)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.move(135, 20)
        btn.clicked.connect(self.openimage)

        self.label_text = QLabel(self)
        self.label_text.setFixedSize(300, 30)
        self.label_text.move(25, 270)
        self.label_text.setTextInteractionFlags(Qt.TextSelectableByMouse) ###可复制

        self.label_wait = QLabel(self)
        self.label_wait.setFixedSize(300, 30)
        self.label_wait.move(25, 300)
        # 标签1的背景填充更改为True，否则无法显示背景
        self.label_wait.setAutoFillBackground(True)
        # # 实例化背景对象，进行相关背景颜色属性设置
        # palette = QPalette()
        # palette.setColor(QPalette.Window, Qt.green)
        # # 标签1加载背景
        # self.label_wait.setPalette(palette)
        # 设置文本居中显示
        self.label_wait.setAlignment(Qt.AlignCenter)
        self.label_wait.setText('tips：识别过程可能会卡住，需几秒到几十秒不等')

        self.std = CnStd()
        self.cn_ocr = CnOcr()

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")

        if imgName and imgType:
            # 实例化背景对象，进行相关背景颜色属性设置
            palette = QPalette()
            palette.setColor(QPalette.Window, Qt.green)
            # 标签1加载背景
            self.label_wait.setPalette(palette)

            box_info_list = self.std.detect(imgName)
            result = ''
            for box_info in box_info_list:
                cropped_img = box_info['cropped_img']  # 检测出的文本框
                # cv2.imshow('1', cropped_img)
                # cv2.waitKey(0)
                ocr_res = self.cn_ocr.ocr_for_single_line(cropped_img)
                result += ''.join(ocr_res)
                # print('ocr result: %s' % ''.join(ocr_res))
            # print(result)
            self.label_text.setText(result)
            self.label_wait.setText('↑点击文字，ctrl+a全选、ctrl+c复制、ctrl+v粘贴')

            jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
            self.label.setPixmap(jpg)

            with open('history.txt', 'a', encoding='utf8') as f:
                f.write(result + '\n')


if __name__ == "__main__":
    try:
        while True:
            app = QtWidgets.QApplication(sys.argv)
            my = picture()
            my.show()
            sys.exit(app.exec_())
    except Exception as e:
        print(e)
        time.sleep(5)

