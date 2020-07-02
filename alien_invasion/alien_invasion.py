import sys
import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 1
    screen = pygame.display.set_mode((1200, 800))  # 2
    pygame.display.set_caption("Alien Invasion")
    # 设置背景色
    bg_color = (230, 230, 230) # 7
    # 开始游戏的主循环
    while True:  # 3
        # 监视键盘和鼠标事件
        for event in pygame.event.get():  # 4
            if event.type == pygame.QUIT:  # 5
                sys.exit()
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)  # 8
        # 让最近绘制的屏幕可见
        pygame.display.flip()  # 6

run_game()