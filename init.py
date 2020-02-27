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
        file = open('note/define.txt', 'w')
        file.close()


def init_note(note_name='新建教材'):
    '''
    create the new note
    :param note_name:
    :return: null
    '''
    try:
        name = input('请输入文件名：')
        if not name == '':
            note_name = name
        path = home_path + '/note_' + note_name
        os.mkdir(path)
        file = open(path + '/define.txt', mode='w')
        for i in message['head']:
            file.write(str(i) + '\n')
        file.close()
    except FileExistsError:
        print('文件已存在，无法创建')


def get_var(var_name=''):
    '''
    get a str and return it
    :param var_name:
    :return:
    '''
    var = ''
    while (True):
        if var == '':
            var = input('input the var {}:'.format(var_name))
        else:
            break
        return var


class Note():
    '''
    create a new note
    '''

    def __init__(self, name=NOTE_name, path=HOME_path_note + '/' + NOTE_name, size_y=PAGE_px_y, size_x=PAGE_px_x,
                 note_nums=NOTE_nums):
        '''
        init the new note
        :param name:
        :param path:
        :param size:
        :param note_nums:
        '''
        # 基本参数
        self.name = name
        self.path = path
        self.page = '0'
        self.size_y = size_y
        self.size_x = size_x
        self.note_nums = note_nums
        # 需要传递的数据
        '''
        self.head = [self.size_y,self.size_x,self.note_nums]
        self.data = []
        self.message = {'head':self.head,'data':self.data}
        '''

    def __call__(self, *args, **kwargs):
        '''
        show the info about the note
        :param args:
        :param kwargs:
        :return:
        '''
        print('---------------------------------')
        print('|        all informasion        |')
        print('---------------------------------')
        print('\t\tname:          ', self.name)
        print('\t\tpath:          ', self.path)
        print('\t\tsize:          ', self.size_y, '*', self.size_x)
        print('\t\tpage:          ', self.page)
        print('\t\tnote_nums:     ', self.note_nums)
        print('*********************************')

    def create_note(self, name='new'):
        '''
        create a new note, and the arg is a string
        :param name:
        :return:
        '''
        if name == 'new':
            name = input('input the note\'s name :')
            if name == '':
                name = 'new'
        while (True):
            if os.path.exists(HOME_path_note + '/' + name):
                print('the note is already exsists! please input again!')
                name = input('input the note\'s name :')
            else:
                self.name = name
                self.path = HOME_path_note + '/' + name
                self.size_y = get_var('the size of y')
                self.size_x = get_var('the size of x')
                self.note_nums = get_var('the note_nums')
                os.mkdir(self.path)
                with open(self.path + '/config.txt', 'w') as f:
                    f.write(self.size_y + '\n')
                    f.write(self.size_x + '\n')
                    f.write(self.note_nums + '\n')
                print('已创立新笔记！')
                break
        print('已切换到新笔记中')

    def check_note(self, name='README'):
        '''
        check out the note in the note list
        :param name:
        :return:
        '''
        if name == 'README':
            name = input('input the note\'s name:')
        while (True):
            if name == '':
                name = 'README'
            self.path = HOME_path_note + '/' + name
            try:
                with open(self.path + '/config.txt') as f:
                    self.size_y = f.readline().strip('\n')
                    self.size_x = f.readline().strip('\n')
                    self.note_nums = f.readline().strip('\n')
                break
            except FileNotFoundError:
                print('the note isn\'t exsit!')
                name = input('again,the note\'s name:')

    def show_page(self, page='0'):
        '''
        as a API to the player to show the page's content
        :param page:
        :return:
        '''
        if page == '0':
            page = input('input the page\'s num: ')
        while (True):
            if page == '':
                page = '0'
            try:
                self.page = page
                f = open(self.path + '/{}.txt'.format(page))
                f.close()
                break
            except FileNotFoundError:
                print('the page is not exsit!')
                page = input('again,the page\'s num : ')
        '''
        这里显示图片
        '''
        print('图片被显示啦')
        return self.path, self.page


class Message():
    '''
    类 ： 信息
    传递数据的载体，分为头部信息-（head）、数据信息-（data）
    '''
    def __init__(self, head=[], data=[]):
        self.head = head
        self.data = data

    def __call__(self, *args, **kwargs):
        '''
        显示该实例的内容
        :param args:
        :param kwargs:
        :return: null
        '''
        print('---------------------------------')
        print('|        all informasion        |')
        print('---------------------------------')
        print('\t\tname:          ', self.head)
        print('\t\tpath:          ', self.data)
        print('*********************************')


if __name__ == '__main__':
    note = Note()
    player = Player()
    note()
    note.check_note('1')
    note()
    player.play(note.show_page())
    note()
