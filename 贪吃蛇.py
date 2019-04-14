import queue
import random
import threading

import time
from tkinter import Tk, Button, Canvas


class Food():
    def __init__(self, queue):
        self.queue = queue
        self.new_food()

    def new_food(self):
        '''
        功能：产生一个食物
        产生一个食物的过程就是随机产生一个食物坐标的过程
        :return:
        '''
        # 注意横纵坐标产生的范围
        x = random.randrange(5, 480, 10)
        y = random.randrange(5, 480, 10)

        self.position = x,y # position存放食物的位置
        self.exppos = x-5, y-5, x+5, y+5
        # 队列，就是一个不能够随意访问内部元素，只能从头弹出一个元素
        # 并只能从队尾追加元素的list
        # 把一个食物产生的消息放入队列
        # 消息的格式，自己定义
        # 我的定义是：消息是一个dict，k代表消息类型，v代表此类型的数据
        self.queue.put({"food": self.exppos})

class Snake(threading.Thread):
    '''
    蛇的功能：
        1. 蛇能动，由我们的上下左右按键控制
        2. 蛇每次动，都需要重新计算蛇头的位置
        3. 检测是否游戏完事的功能
    '''
    def __init__(self, world, queue):
        threading.Thread.__init__(self)

        self.world = world
        self.queue = queue
        self.points_earned = 0
        self.food = Food(queue)
        self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]
        self.start()
        self.direction = 'Left'

    def run(self):
        if self.world.is_game_over:
            self._delete()

        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            time.sleep(0.5)
            self.move()

    def move(self):
        '''
        负责蛇的移动
        1. 重新计算蛇头的坐标
        2. 当蛇头跟食物相遇，则加分，重新生成食物，通知world，加分
        3. 否则，蛇需要动
        :return:
        '''
        new_snake_point = self.cal_new_pos()#重新计算蛇头位置

        # 蛇头位置跟食物位置相同
        if self.food.position == new_snake_point:
            self.points_earned += 1#得分加1
            self.queue.put({"points_earned": self.points_earned})
            self.food.new_food()
        else:
            # 需要注意蛇的信息的保存方式
            self.snake_points.pop(0)
            # 判断程序是否退出，因为新的蛇可能撞墙
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)
    def cal_new_pos(self):
        last_x, last_y = self.snake_points[-1]
        if self.direction == "Up":
            new_snake_point = last_x, last_y - 10# 每次移动10个像素
        elif self.direction == "Down":
            new_snake_point = last_x, last_y + 10
        elif self.direction == "Right":
            new_snake_point = last_x + 10, last_y
        elif self.direction == "Left":
            new_snake_point = last_x - 10, last_y
        return new_snake_point

    def key_pressed(self, e):
        # keysym是按键名称
        self.direction = e.keysym

    def check_game_over(self, snake_point):
        '''
        判断依据是蛇头是否和墙相撞
        :param snake_point:
        :return:
        '''
        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over':True})

class World(Tk):
    def __init__(self, queue):
        Tk.__init__(self)

        self.queue = queue
        self.is_game_over = False

        # 定义画板
        self.canvas = Canvas(self, width=500, height=300, bg='gray')
        self.canvas.pack()

        self.snake = self.canvas.create_line((0,0), (0,0), fill="black",width=10)
        self.food = self.canvas.create_rectangle(0,0,0,0,fill='#FFCC4C', outline='#FFCC4C')

        self.points_earned = self.canvas.create_text(450, 20, fill='white', text='score:0')
        self.queue_handler()

    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)

                if task.get("game_over"):
                    self.game_over()
                if task.get("move"):
                    points = [x for point in task['move'] for x in point]
                    # 重新绘制蛇
                    self.canvas.coords(self.snake, *points)

                # 同样道理，还需要处理食物，得分
                if task.get("food"):
                    self.canvas.coords(self.food, *task['food'])
                elif task.get("points_earned"):
                    self.canvas.itemconfigure(self.points_earned, text='SCORE:{}'.format(task['points_earned']))

        except queue.Empty:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        '''
        游戏结束，清理现场
        :return:
        '''
        self.is_game_over = True
        self.canvas.create_text(200, 150, fill='white', text="Game Over")
        qb = Button(self,text="Quit", command=self.destroy)
        # rb = Button(self, text="Again", command=lambda:self.__init__(self.queue))
        self.canvas.create_window(200, 180, anchor='nw', window=qb)
        # self.canvas.create_window(200, 220, anchor='nw', window=rb)
if __name__ == '__main__':
    q = queue.Queue()
    world = World(q)

    snake = Snake(world, q)

    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.bind('<Key-Down>', snake.key_pressed)
    world.bind('<Key-Up>', snake.key_pressed)

    world.mainloop()