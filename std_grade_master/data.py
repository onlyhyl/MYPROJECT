# -*- coding:utf8 -*-
import xlrd
import matplotlib.pyplot as plt
# from matplotlib.pyplot import MultipleLocator
import os


class DATA():
    def __init__(self, stfile):
        self.stfile = stfile
        self.units = []
        self.names = []
        self.name_prices = {}
        self.upnames = []
        self.downnames = []
        self.noupdownnames = []
        self.unit_eval = {}


    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def is_Chinese(self, word):
        try:
            float(word)
        except ValueError:
            for ch in word:
                if '\u4e00' <= ch <= '\u9fff':
                    return True
        return False

    def make_data(self):
        print('dealing stu message...')
        data = xlrd.open_workbook(self.stfile)
        self.stfile = self.stfile.replace(' ', '')
        table = data.sheets()[0]
        nrows = table.nrows

        name_to_paixu = {}
        for n in range(2, nrows):
            data = table.row_values(n, start_colx=0, end_colx=None)
            if n == 2:
                index = data.index('姓名')
                for i in range(index + 1, len(data)):
                    if data[i] != '':
                        self.units.append(data[i])
                    else:
                        break
            for i in range(len(data)):
                if i != 0:
                    if self.is_number(data[i - 1]) and self.is_Chinese(data[i]) and data[i] != '缺考':
                        tmp_price = []
                        num = int(data[i - 1])
                        name = str(num) + ' ' + data[i]
                        name_to_paixu[name] = num
                        for j in range(i + 1, len(data)):
                            if self.is_number(data[j]) or data[j] == '缺考':
                                if data[j] != '缺考':
                                    tmp_price.append(int(data[j]))
                                else:
                                    tmp_price.append(0)
                            else:
                                break
                        self.name_prices[name] = tmp_price
        print('all std message:', self.name_prices)
        name_to_paixu = sorted(name_to_paixu.items(), key=lambda item: item[1])
        for name in name_to_paixu:
            self.names.append(name[0])
        print('end dealing!')

    def paint(self, update):
        if update:
            print('drawing stu message...')
            if not os.path.exists(self.stfile.split('.')[0]):
                os.mkdir(self.stfile.split('.')[0])
            # if not os.path.exists(self.stfile.split('.')[0] + '/stpicsqrc.qrc'): # 通过main判断是否需要更新
            f = open(self.stfile.split('.')[0] + '/stpicsqrc.qrc', 'w', encoding='utf8')
            f.write(str('<RCC>' + '\n' + '<qresource prefix="pic">' + '\n'))
            for name in self.names:
                print(name)
                prices = self.name_prices[name]

                # 这里是全部人的
                y = prices
                x = self.units
                plt.rcParams['font.sans-serif'] = ['SimHei']
                plt.rcParams['axes.unicode_minus'] = False
                plt.title("{}".format(name), fontsize=15)
                plt.plot(x, y)
                plt.plot(x, [90 for _ in range(len(x))],color='g',linewidth=1) # 90分线
                plt.ylim(ymax=100, ymin=0)
                # y_major_locator = MultipleLocator(100)
                # ax = plt.gca()
                # ax.yaxis.set_major_locator(y_major_locator)
                for a, b in zip(x, y):
                    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
                plt.savefig('{}/{}'.format(self.stfile.split('.')[0], name))
                # plt.show()
                plt.cla()
                f.write('<file>{}.png</file>'.format(name) + '\n')

            f.write('</qresource>' + '\n' + '</RCC>')
            f.close()
            print('end drawing!')

    def jinbu(self):
        for name in self.names:
            # print(name)
            prices = self.name_prices[name]

            # 判断进步多少次，在全部人的基础上抽图
            up = 0
            for i in range(len(prices)):
                if i != len(prices) - 1:
                    if prices[i + 1] > prices[i]:
                        up += 1

            if up == len(prices) - 1:
                self.upnames.append(name)

    def tuibu(self):
        for name in self.names:
            # print(name)
            prices = self.name_prices[name]

            # 判断退步多少次，在全部人的基础上抽图
            down = 0
            for i in range(len(prices)):
                if i != len(prices) - 1:
                    if prices[i + 1] < prices[i]:
                        down += 1

            if down == len(prices) - 1:
                self.downnames.append(name)

    def bodong(self):
        for name in self.names:
            if name not in self.upnames or name not in self.downnames:
                self.noupdownnames.append(name)

    def eval(self):
        for i in range(len(self.units)):
            unit = self.units[i]
            tmp = 0
            for name in self.names:
                tmp += self.name_prices[name][i]
            tmp_eval = tmp / len(self.names)
            self.unit_eval[unit] = round(tmp_eval , 2)

# if __name__ == '__main__':
#     a = DATA()
#     a.make_data()
#     a.paint()
#     os.system(r'pyrcc5 -o z/uppics.py z/uppics.qrc')
