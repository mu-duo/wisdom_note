'''
本模块用于接收硬件传输数据
根据协议将数据储存

1、接收到书本编号后开始运行，等待接收
   数据,直至接收到结束指令

'''
import numpy



class Reciver():
    def __init__(self):
        self.size_y = 0
        self.size_x = 0
        self.flag = False
        self.data = {'flag':self.flag,'data':numpy.zeros(self.size_y,self.size_x)}
        pass

    def __call__(self, *args, **kwargs):
        '''
        显示reciver的内容
        :param args:
        :param kwargs:
        :return:
        '''
        pass

    def send_data(self):
        '''
        定时传递内容给note实例，
        :return:
        '''
        pass

