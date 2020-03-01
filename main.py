import note_1
import cpm_1

class Wisdom_note():
    def __init__(self):
        self.note = note_1.Note()
        self.cpm = cpm_1.Cpm('456')

    def __call__(self, *args, **kwargs):
        print(self.cpm)
        print(self.note)

    def __repr__(self):
        self.__call__()
        return "****************************************************************"

    def load(self):
        with open(w.cpm.work_path + '/config.wis') as f:
            self.note.size['y'] = f.readline().strip('\n')
            self.note.size['x'] = f.readline().strip('\n')
            self.note.page = f.readline().strip('\n')
        print('加载完毕')

    def check_out(self,book_name = ''):
        self.cpm.check_out(book_name)
        self.load()

    def create_new_book(self, book_name=''):
        pass

    def create_new_note(self, note_name=''):
        pass

    def del_note(self, note_name=''):
        pass

    def del_book(self,book_name=''):
        pass

    def copy_note(self, note_name='0'):



if __name__ == '__main__':
    w = Wisdom_note()
    print(w)
    w.check_out('book_123')
    print(w)