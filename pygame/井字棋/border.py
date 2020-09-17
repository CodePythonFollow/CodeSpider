'''棋盘模块'''


class Border(object):

    def __init__(self):
        # 棋盘数据
        self.border_data = [" "] * 9
        # 可移动列表
        self.movable_list = list(range(9))

    # 显示棋盘
    def show_border(self):
        for i in (0, 3, 6):
            print('      |      |      ')
            print('  %d   |  %d   |   %d  ' % (i, i + 1, i + 2))
            print('      |      |      ')
            if i != 6:
                print('-'*23)


if __name__ == "__main__":
    # 棋盘测试
    border = Border()
    border.show_border()
