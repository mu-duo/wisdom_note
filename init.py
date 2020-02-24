'''
本模块用于初始化的各种操作
包含初始路径检查、初始化建立新书本
'''

from define import *
import os
from display import *

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

def get_var(var_name = ''):
    '''
    get a str and return it
    :param var_name:
    :return:
    '''
    var = ''
    while(True):
        if var == '':
            var = input('input the var {}:'.format(var_name))
        else:
            break
        return var

class Book():
    '''
    create a new book
    '''
    def __init__(self,name = BOOK_name,path = HOME_path+'/'+BOOK_name,size_y = PAGE_px_y,size_x = PAGE_px_x,book_nums = BOOK_nums):
        '''
        init the new book
        :param name:
        :param path:
        :param size:
        :param book_nums:
        '''
        #基本参数
        self.name = name
        self.path = path
        self.page = '0'
        self.size_y = size_y
        self.size_x = size_x
        self.book_nums = book_nums
        #需要传递的数据
        '''
        self.head = [self.size_y,self.size_x,self.book_nums]
        self.data = []
        self.message = {'head':self.head,'data':self.data}
        '''

    def __call__(self, *args, **kwargs):
        '''
        show the info about the book
        :param args:
        :param kwargs:
        :return:
        '''
        print('---------------------------------')
        print('|        all informasion        |')
        print('---------------------------------')
        print('\t\tname:          ',self.name)
        print('\t\tpath:          ',self.path)
        print('\t\tsize:          ',self.size_y,'*',self.size_x)
        print('\t\tpage:          ',self.page)
        print('\t\tbook_nums:     ',self.book_nums)
        print('*********************************')

    def create_book(self,name = 'new'):
        '''
        create a new book, and the arg is a string
        :param name:
        :return:
        '''
        if name == 'new':
            name = input('input the book\'s name :')
            if name == '':
                name = 'new'
        while(True):
            if os.path.exists(HOME_path+'/'+name):
                print('the book is already exsists! please input again!')
                name = input('input the book\'s name :')
            else:
                self.name = name
                self.path = HOME_path+'/'+name
                self.size_y = get_var('the size of y')
                self.size_x = get_var('the size of x')
                self.book_nums = get_var('the book_nums')
                os.mkdir(self.path)
                with open(self.path+'/config.txt','w') as f:
                    f.write(self.size_y+'\n')
                    f.write(self.size_x+'\n')
                    f.write(self.book_nums+'\n')
                print('已创立新笔记！')
                break
        print('已切换到新笔记中')


    def check_book(self,name = 'README'):
        '''
        check out the book in the book list
        :param name:
        :return:
        '''
        if name == 'README':
            name = input('input the book\'s name:')
        while (True):
            if name == '':
                name = 'README'
            self.path = HOME_path + '/' + name
            try:
                with open(self.path + '/config.txt') as f:
                    self.size_y = f.readline().strip('\n')
                    self.size_x = f.readline().strip('\n')
                    self.book_nums = f.readline().strip('\n')
                break
            except FileNotFoundError:
                print('the book isn\'t exsit!')
                name = input('again,the book\'s name:')

    def show_page(self,page = '0'):
        '''
        as a API to the player to show the page's content
        :param page:
        :return:
        '''
        if page == '0':
            page = input('input the page\'s num: ')
        while(True):
            if page == '':
                page = '0'
            try:
                self.page = page
                f = open(self.path+'/{}.txt'.format(page))
                f.close()
                break
            except FileNotFoundError:
                print('the page is not exsit!')
                page = input('again,the page\'s num : ')
        '''
        这里显示图片
        '''
        print('图片被显示啦')
        return self.path,self.page

class Message():
    def __init__(self,head = [],data = []):
        self.head = head
        self.data = data

    def __call__(self, *args, **kwargs):
        print('---------------------------------')
        print('|        all informasion        |')
        print('---------------------------------')
        print('\t\tname:          ', self.head)
        print('\t\tpath:          ', self.data)
        print('*********************************')

if __name__ == '__main__':
    book = Book()
    player = Player()
    book()
    book.check_book('book_123')
    book()
    player.play(book.show_page())
    book()



