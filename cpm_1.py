class Cpm():
    '''
    中央处理模块
    '''
    def __init__(self, work_path='', flush_time=0, home = 'book'):
        '''
        :param work_path: 工作路径
        :param flush_time:  刷新间隔
        '''
        # set the home psth
        self.home = home + '/'
        # the abs path
        self.work_path = self.home + work_path
        # flush tehe buffer
        self.flush_time = flush_time
        # data and head
        self.message = {'head':{}, 'data':[]}

    def __call__(self, *args, **kwargs):
        print('-------the info of cpm-------\n')
        print('work path     :      ',self.work_path)
        print('flush time    :      ',self.flush_time)
        print('message head  :      ',self.message['head'])
        print('message data  :      ',self.message['data'])

    def __repr__(self):
        print('this is a repr()')
        self.__call__()
        return 'repr end'

    def __str__(self):
        print('this is a str()')
        self.__call__()
        return 'str end'

    def get_message(self,message):
        '''
        接收端口
        :param message: 传递的信息
        :return:
        '''
        self.message['head'] = message['head']
        self.message['data'] = message['data']

    def send_message(self):
        '''
        发送端口
        :return: message
        '''
        return self.message

    def check_out(self,book_name):
        '''
        切换工作路径
        :param book_name: 工作的路径
        :return:
        '''
        self.work_path = self.home + book_name
        pass

if __name__ == '__main__':
    cpm = Cpm()
    print(cpm)
    cpm.get_message({'head':{'path':'c://wisdom'},'data':[[1,2,3],[4,5,6]]})
    print(cpm)
    print(cpm.send_message())
    cpm.check_out('math')
    print(cpm)
