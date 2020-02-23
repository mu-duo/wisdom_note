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

def open_book(name = ''):
    '''
    cd the path of the book
           ps:it's necessary before running show_page()
    :param name:
    :return:null
    '''
    global  book_num

    #get the book_name
    if name=='':
        name = input('the book\'s name = ?')
        if name=='':
            name = book_num

    book_num = name


    while (True):
        # 尝试找到路径，找不到会提示路径错误
        try:
            with open(home_path + '/book_' + book_num + '/define.txt') as f:
                global page_px_y
                global page_px_x
                global book_nums
                page_px_y = f.readline()
                page_px_x = f.readline()
                book_nums = f.readline()
                print("书本格式为：", int(page_px_y), '*', int(page_px_x),'页数为：',book_nums)
            break;

        except FileNotFoundError:
            book_num = input('eeror!again, the book_num=?:')

def show_page():
    '''
    show the content of the page
    :return:
    '''
    global page_num
    # open the book
    path = home_path + '/book_' + book_num + '/'
    page_num = input('the page_num = ?:(1 to {})'.format(book_nums))
    path_page = path + 'page' + page_num + '.txt'
    print(path_page)

    while (True):
        try:
            file = open(path_page)
            break;
        except FileNotFoundError:
            page_num = input('again, the page_num = ?:')
            path_page = path + 'page' + page_num + '.txt'

    lines = file.readlines()
    for i in range(len(lines)-1):
        lines[i]=lines[i].strip('\n')

    # judge the page
    if page_star != lines[0] or page_end != lines[-1]:
        print('the check code is error!')

    # get all the data
    data = numpy.zeros((int(page_px_y), int(page_px_x)))
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