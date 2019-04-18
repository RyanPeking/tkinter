# -*- coding: utf-8 -*-

import random
import tkinter


class RandomBall(object):
    '''
    定义运动的球的类
    '''

    def __init__(self, canvas, scrwidth, scrheight):
        '''
        :param canvas: 画布，所有的内容都应该在画布上呈现
        :param scrwidth: 屏幕的宽度
        :param scrheight: 屏幕的高度
        '''

        self.canvas = canvas
        # 定义球的初始位置，它的初始位置应该是随机的，此处所表示的坐标圆心坐标
        self.xpos = random.randint(10, int(scrwidth - 20))
        self.ypos = random.randint(10, int(scrheight - 20))

        # 定义球运动的速度
        self.xspeed = random.randint(4, 20)
        self.yspeed = random.randint(4, 20)

        # 定义屏幕大小
        self.scrwidth = scrwidth
        self.scrheight = scrheight

        # 定义球的半径，值随机
        self.radius = random.randint(20, 100)

        # 定义球的颜色，一般使用RGB；一些系统中也可以使用英文表示；在此用lambda表示
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def draw_ball(self):
        '''
        用定义的初始函数来画球
        '''

        # tkinter没有画圆函数，只有画椭圆的函数，利用确定左上角坐标和右下角坐标来唯一确定椭圆的形状
        # 左上角横坐标：圆心横坐标减椭圆1/2长轴，左上角纵坐标：圆心纵坐标减1/2椭圆短轴
        # 利用画椭圆来画圆
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):

        # 每次移动，球都有一个新的坐标
        self.xpos = self.xpos + self.xspeed
        self.ypos = self.ypos + self.yspeed

        # 当球撞了墙之后的动作
        if self.xpos + self.radius >= self.scrwidth:
            self.xspeed *= -1
        if self.ypos + self.radius >= self.scrheight:
            self.yspeed *= -1
        if self.xpos - self.radius <= 0:
            self.xspeed *= -1
        if self.ypos - self.radius <= 0:
            self.yspeed *= -1
        self.canvas.move(self.item, self.xspeed, self.yspeed)


class ScreenSaver:

    def __init__(self, num_balls):
        self.balls = list()
        self.num_balls = random.randint(6, 20)
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)
        # self.root.attributes('-alpha', 0.3)
        self.root.bind('<Motion>', self.myquit)
        self.root.bind('<Key>', self.myquit)

        # 得到屏幕大小的规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # 创建画布
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(num_balls):
            ball = RandomBall(self.canvas, scrwidth=w, scrheight=h)
            ball.draw_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        self.canvas.after(200, self.run_screen_saver)

    def myquit(self, event):
        # 自我销毁，停止运行
        self.root.destroy()


if __name__ == '__main__':
    ScreenSaver(20)