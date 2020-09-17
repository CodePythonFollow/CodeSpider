# -*- coding: utf-8 -*-
import pygame
import random
import sys

# 设置游戏窗口的规格
x_screen, y_screen = 1000, 700

class Snake():
    # 初始属性
    def __init__(self):
        self.length = []
        self.head = pygame.K_RIGHT

        for i in range(5):
            self.add_one()

    # 蛇加一格
    def add_one(self):
        left, top = (0, 0)
        if self.length:
            left, top = (self.length[0].left, self.length[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.head == pygame.K_LEFT:
            node.left -= 25
        elif self.head == pygame.K_RIGHT:
            node.left += 25
        elif self.head == pygame.K_UP:
            node.top -= 25
        elif self.head == pygame.K_DOWN:
            node.top += 25
        self.length.insert(0, node)

    # 如果蛇移走就减少一格
    def del_one(self):
        self.length.pop()

    # 死亡判断
    def isdead(self):
        # 撞墙
        if self.length[0].x not in range(x_screen):
            return True
        if self.length[0].y not in range(y_screen):
            return True
        # 撞自己
        if self.length[0] in self.length[1:]:
            return True
        return False

    # 移动的本质就是删除和增加的过程
    def move(self):
        self.add_one()
        self.del_one()

    # 控制方向 curkey 捕捉当前的方向设置
    def control(self, curkey):
        horizontal = [pygame.K_LEFT, pygame.K_RIGHT]
        vertically = [pygame.K_UP, pygame.K_DOWN]
        if curkey in horizontal + vertically:
            if (curkey in horizontal) and (self.head in horizontal):
                return
            elif (curkey in vertically) and (self.head in vertically):
                return
            else:
                self.head = curkey



class Food():
    # 初始位置
    def __init__(self):
        self.rect = pygame.Rect(-25, 0, 25, 25)

    def remove(self):
        self.rect.x = -25

    def set(self):
        if self.rect.x == -25:
            allposx = []
            allposy = []
            # 不靠近墙太近 25~x_screen-25 之间
            for pos in range(50, x_screen - 25, 25):
                allposx.append(pos)
            self.rect.left = random.choice(allposx)
            for pos in range(50, y_screen - 25, 25):
                allposy.append(pos)
            self.rect.top = random.choice(allposy)
            print(self.rect)

# 显示文字
def show_text(screen, pos, text, color, font_bold=False, font_size=60, font_italic=False):
    # 获取系统文字，并设置文字大小
    cur_font = pygame.font.SysFont("微软雅黑", font_size)
    # 设置是否加粗
    cur_font.set_bold(font_bold)
    # 设置是否斜体属性
    cur_font.set_italic(font_italic)
    # 设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    # 绘制文字
    screen.blit(text_fmt, pos)

def main():
    # 初始化pygame
    pygame.init()

    # 设置窗口大小
    screen = pygame.display.set_mode((x_screen, y_screen))

    # 窗口名称
    pygame.display.set_caption("贪吃蛇")

    # 动作
    clock = pygame.time.Clock()

    # 设置窗口标题
    background = pygame.image.load('bg.jpg').convert()

    # 默认成绩和默认状态
    score = 0
    isdead = False

    snack = Snake()
    food = Food()

    # 加载并转换图像
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            # 接收到退出事件后退出程序
            if event.type == pygame.KEYDOWN:
                snack.control(event.key)
                if event.key == pygame.K_SPACE and isdead:
                    return main()

        screen.fill([255, 255, 255])
        # background = pygame.image.load('./th.jpg')
        # screen.blit(background, (0, 0))

        if not isdead:
            snack.move()
        for rect in snack.length:
            # 蛇神颜色
            pygame.draw.rect(screen, (20, 220, 39), rect, 0)

        # 死亡显示文字
        isdead = snack.isdead()
        if isdead:
            show_text(screen, (100, 200), 'You Are Dead', (227, 29, 18), False, 100)
            show_text(screen, (150, 260), 'Press Space To Try again', (0, 0, 22), False, 30)

        # 实物处理 长加25 蛇头接触到实物  分加50
        if food.rect == snack.length[0]:
            score += 50
            food.remove()
            snack.add_one()

        food.set()
        pygame.draw.rect(screen, (136, 0, 24), food.rect, 0)
        # 显示分数文字
        show_text(screen, (50, 500), 'Scores:' + str(score), (223, 223, 223))
        if score <= 300:
            clock.tick(5 + score/50)
        else:
            clock.tick(12)

        pygame.display.update()

main()



