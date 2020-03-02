class Book():
    def __init__(self,path = 'book/book_123'):
        self.path = path + '/book'
        self.page = '0'

    def __call__(self, *args, **kwargs):
        print('------------------------book------------------------')
        print('work path     :      ', self.path)
        print('page          :      ',self.page)
        print('------------------------end-------------------------')

    def __repr__(self):
        print('\n\n--------------------调试信息----------------------')
        self.__call__()
        return '---------------------repr-------------------------\n\n'

    def load_book(self):
        print('load book succefully!')
        pass

    def close_book(self):
        print('close the book')
        pass

    def check_out(self,book_path=''):
        self.path = book_path

    def add_book(self,book_path=''):
        print('the new book is created!')
        pass

    def del_book(self,book_path = ''):
        print('the book is deleded!')
        pass

    def get_message(self,message):
        self.path = message['head']['path']
        self.page = message['head']['page']

    def send_message(self):
        message = {'head':{},'data':[]}
        message['head']['path'] = self.path

if __name__ == '__main__':
    b = Book()
    b.load_book()
    b.check_out('book/new')
    b.close_book()
    print(b)
