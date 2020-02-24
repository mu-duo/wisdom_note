'''
本模块用于定义、初始化各种全局参数
'''
import os


#笔记的家目录
HOME_path_note= 'note'
#校验码
PAGE_start = '2580'

#笔记名及页码
NOTE_name = 'README'
PAGE_num = '0'
#纸张尺寸
PAGE_px_x = '80'
PAGE_px_y = '80'
#笔记总页码
NOTE_nums = '50'


'''
初始化操作，检查路径是否存在
'''
try:
    with open('note/define.txt','r') as file:
        page_px_y = file.readline().strip('\n')
        page_px_x = file.readline().strip('\n')
        note_nums = file.readline().strip('\n')
except FileNotFoundError:
    if not os.path.exists('note'):
        os.mkdir('note')
    with open('note/define.txt', 'w+') as file:
        file.write('800\n')
        file.write('600\n')
        file.write('50\n')
        page_px_y = file.readline().strip('\n')
        page_px_x = file.readline().strip('\n')
        note_nums = file.readline().strip('\n')

