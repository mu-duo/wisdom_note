'''
本模块用于定义、初始化各种全局参数
'''
#家目录
HOME_path = 'book'
#校验码
PAGE_start = '2580'

#书本名及页码
BOOK_name = 'README'
PAGE_num = '0'
#纸张尺寸
PAGE_px_x = '80'
PAGE_px_y = '80'
#书本总页码
BOOK_nums = '50'

with open('book/define.txt') as file:
    page_px_y = file.readline()
    page_px_x = file.readline()
    book_nums = file.readline()


#数据集，用于传递信息
head = [page_px_y,page_px_x,book_nums]
for i in range(len(head)-1):
    head[i]=head[i].strip('\n')
data = []
message = {'head':head,'data':data}