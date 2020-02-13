'''
本模块用于接收硬件传输数据
根据协议将数据储存

1、接收到书本编号后开始运行，等待接收
   数据,直至接收到结束指令
2、协议：
                                ----------->book
                    #get the var
                    define.txt
    #book_page1.txt
    page_star
    page_num
    x y lever
    page_end
              ----->book_page1.txt
                    book_page2.txt
                    book_page3.txt
                    ...
                    book_pagen.txt
                    define.txt
                                 ----------->book
'''