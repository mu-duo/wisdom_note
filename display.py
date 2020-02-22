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

def open_book(book_name = ''):
    global  book_num
    book_num = input('the book\'s name = ?')
    while (True):
        # 尝试找到路径，找不到会提示路径错误
        try:
            with open(home_path + '/book_' + book_num + '/define.txt') as f:
                page_px_x = int(f.readline())
                page_px_y = int(f.readline())
                print("书本格式为：", page_px_y, '*', page_px_x)
            break;

        except FileNotFoundError:
            book_num = input('again, the book_num=?:')

def show_page():
    global page_num
    # open the book
    path = home_path + '/book_' + book_num + '/'
    page_num = input('the page_num = ?:')
    path_page = path + 'page' + page_num + '.txt'

    while (True):
        try:
            file = open(path_page)
            break;
        except FileNotFoundError:
            page_num = input('again, the page_num = ?:')
            path_page = path + 'page' + page_num + '.txt'

    lines = file.readlines()

    # judge the page
    if page_star != int(lines[0]) or page_end != int(lines[-1]):
        print('校验码对不上！！！')

    # get all the data
    data = numpy.zeros((page_px_y, page_px_x))
    # get all the data
    for i in lines[1:len(lines) - 2]:
        data_tem = i.split(' ')
        y = int(data_tem[0])
        x = int(data_tem[1])
        lever = int(data_tem[2])
        data[y][x] = lever
        file.close()

    # show the picture
    matplotlib.pyplot.imshow(data, cmap='Greys', interpolation='None')
    matplotlib.pyplot.show()

if __name__ == '__main__':
    while(True):
        open_book()
        show_page()
'''
已可以显示图片，下一步将图片重叠
'''