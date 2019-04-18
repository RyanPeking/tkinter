import tkinter
import time
import random as rd

'''
蜜蜂从上向下运动
可以通过键盘左右控制
'''

step = 0
direction = (1, 1)

x = 0
y = 10

def set_right(e):
    global x
    x += 20

def set_left(e):
    global x
    x -= 20


root_window = tkinter.Tk()
root_window.title("飞机大战")

root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)
root_window.resizable(width=False, height=False)

window_canvas = tkinter.Canvas(root_window, width=480, height=600)
window_canvas.pack()



def main():
    bg_img_name = "../img/background.gif"
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    # tags的作用是，以后我们使用创建好的image可以通过tags使用
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER, \
                               image=bg_img, tags="bg")

    bee_img_name = "../img/bee.gif"
    bee_img = tkinter.PhotoImage(file=bee_img_name)
    # tags的作用是，以后我们使用创建好的image可以通过tags使用
    window_canvas.create_image(50, 50, anchor=tkinter.CENTER, \
                               image=bee_img, tags="bee")

    bee_move()
    root_window.mainloop()

def bee_move():
    global step, x, y

    y += 20
    print(x, y)
    window_canvas.move("bee", x, y)

    step += 1
    window_canvas.after(1000, bee_move)

if __name__ == '__main__':

    main()
