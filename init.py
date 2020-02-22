'''
本模块用于初始化的各种操作
包含初始路径检查、初始化建立新书本
'''

from define import *
import os

def init_home():
    '''
    check the defalt var
    :return:null
    '''
    if not os.path.exists(home_path):
        os.mkdir(home_path)
        file = open('book/define.txt','w')
        file.close()


def init_book(book_name = '新建教材'):
    '''
    create the new book
    :param book_name:
    :return: null
    '''
    try:
        name = input('请输入文件名：')
        if not name=='':
            book_name = name
        path = home_path + '/book_' + book_name
        os.mkdir(path)
        file = open(path + '/define.txt', mode='w')
        for i in message['head']:
            file.write(str(i) + '\n')
        file.close()
    except FileExistsError:
        print('文件已存在，无法创建')



if __name__ == '__main__':
    init_home()
    init_book('5')



