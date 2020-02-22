from define import *
import os

def init_home():
    if not os.path.exists(home_path):
        os.mkdir(home_path)


if __name__ == '__main__':
    init_home()



