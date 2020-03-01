class Note():
    '''
    create a new note
    '''

    def __init__(self, size={'y':'80','x':'80'}, page='0', target='book'):
        # 目标教材路径
        self.target = target
        # 目标教材规格
        self.size = size
        #上次 停留页码
        self.page = page
        # 数据缓冲区
        self.data = []
        pass

    def __call__(self):
        print('--------------------note--------------------------')
        print('     target       :      ',self.target)
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
        self.target = message['head']['target']
        self.data = message['data']
        pass

    def send_message(self):
        message = {}
        message['head'] = {}
        message['head']['size'] = self.size
        message['head']['page'] = self.page
        message['head']['target'] = self.target
        message['data'] = self.data
        return message


if __name__ == '__main__':
    mes ={
        'head':
            {
                'target':'book/book_123',
                'size': {'y':'80', 'x':'50'},
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
