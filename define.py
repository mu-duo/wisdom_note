'''
本模块用于定义各种全局参数
'''
#家目录
home_path = 'book'
#校验码
page_star = '2580'
page_end = '4580'

#书本名及页码
book_num = '0'
page_num = '0'
#纸张尺寸
page_px_x = '80'
page_px_y = '80'
#书本总页码
book_nums = '50'

#数据集，用于传递信息
head = [page_px_y,page_px_x,book_nums]
data = []
message = {'head':head,'data':data}