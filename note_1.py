class Note():
    '''
    create a new note
    '''

    def __init__(self, size={'y': '80', 'x': '80'}, page='0', path='book/book_123'):
        # 工作路径
        self.path = path + '/note'
        # 目标教材规格
        self.size = size
        # 上次 停留页码
        self.page = page
        # 数据缓冲区
        self.data = []
        pass

    def __call__(self):
        print('--------------------note--------------------------')
        print('     path         :      ', self.path)
        print('     size         :      ', self.size)
        print('     page         :      ', self.page)
        print('     data         :      ', self.data)
        print('---------------------end--------------------------')

    def __repr__(self):
        print('\n\n--------------------调试信息----------------------')
        self.__call__()
        return '---------------------repr-------------------------\n\n'
        pass

    def get_message(self, message):
        self.size = message['head']['size']
        self.page = message['head']['page']
        self.path = message['head']['path']
        self.data = message['data']
        pass

    def send_message(self):
        message = {'head':{},'data':[]}
        message['head']['size'] = self.size
        message['head']['page'] = self.page
        message['head']['path'] = self.path
        message['data'] = self.data
        return message


if __name__ == '__main__':
    mes = {
        'head':
            {
                'path': 'book/book_123',
                'size': {'y': '80', 'x': '50'},
                'page': '25'
            },
        'data':
            [
                [20, 40, 60],
                [80, 54, 75]
            ]
    }
    note = Note()
    print(note)
    note.get_message(mes)
    print(note)
    print(note.send_message())
