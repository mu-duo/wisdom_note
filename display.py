'''
本模块用于显示数据
根据协议将数据读取后显示

1、接收到书本编号后开始运行，等待接收
   数据,直至接收到结束指令
2、协议：
                                                        ----------->book_num
                                ----------->book_note
                                            book_pdf
                                            book_show
                ----->#get the var
                      define.txt
    #book_page1.txt
    page_star
    x y lever
    page_end
                ----->book_page1.txt
                      book_page2.txt
                      book_page3.txt
                      ...
                      book_pagen.txt
                      define.txt
                                ----------->book_note
                                            book_pdf
                                            book_show
                                                        ----------->book_num
'''

# import the modules
import matplotlib.pyplot
import numpy
from define import *

class Player():
    def __init__(self):
        self.size = (PAGE_px_y,PAGE_px_x)
        self.buffer = []

    def __call__(self, *args, **kwargs):
        print('this is a player')

    def play(self, data = ('README','0')):
        #read the config
        with open(data[0]+'/config.txt') as f:
            self.size = (int(f.readline()),int(f.readline()))

        #read the page
        self.buffer = numpy.zeros(self.size)
        print(self.buffer)
        with open(data[0]+'/{}.txt'.format(data[1])) as f:
            f = f.readlines()
            for i in f[1:]:
                i = i.split(' ')
                print((i))
                self.buffer[int(i[0])][int(i[1])] = int(i[2])

        # show the picture
        matplotlib.pyplot.imshow(self.buffer, cmap='Greys', interpolation='None')
        matplotlib.pyplot.show()

'''
已可以显示图片，下一步将图片重叠
'''