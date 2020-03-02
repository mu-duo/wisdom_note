import note_1
import cpm_1
import book_1

class Wisdom_note():
    def __init__(self):
        self.note = note_1.Note()
        self.book = book_1.Book()
        self.cpm = cpm_1.Cpm()

    def __call__(self, *args, **kwargs):
        print(self.cpm)
        print(self.note)
        print(self.book)

    def __repr__(self):
        self.__call__()
        return "****************************************************************"

    def check_out(self,book_name = ''):
        self.cpm.check_out(book_name)
        self.cpm.load()
        self.cpm.check_out(book_name)
        self.note.get_message(self.cpm.send_message())
        self.book.get_message(self.cpm.send_message())

    def create_new_book(self, book_name=''):
        pass

    def create_new_note(self, note_name=''):
        pass

    def del_note(self, note_name=''):
        pass

    def del_book(self,book_name=''):
        pass

    def copy_note(self, note_name='0'):
        pass



if __name__ == '__main__':
    w = Wisdom_note()
    print(w)
    w.check_out('new')
    print(w)