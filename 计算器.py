from tkinter import *

root = Tk()
# 定义面板的大小
root.geometry('250x380')
root.title("计算器")

frame_show = Frame(width=300, height=150, bg='#dddddd')#


# 定义顶部区域
sv = StringVar()
sv.set('0')

# anchor:定义控件的锚点， e代表右边
show_label = Label(frame_show, textvariable=sv, bg='green', \
                   width=12, height=1, font=("黑体", 20, 'bold'),\
                   justify=LEFT, anchor='e')
show_label.pack(padx=10, pady=10)
frame_show.pack()

def delete():
    print("删除")


def fan():
    print("烦了")


def clear():
    print("科利尔")
# 按键区域
frame_bord = Frame(width=400, height=350, bg='#cccccc')
b_del = Button(frame_bord, text="←", width=5,height=1,\
               command=delete)
b_del.grid(row=0, column=0)
button_clear = Button(frame_bord,text = 'C',width = 5,height =1,\
                      command = clear).grid(row = 0,column = 1)
button_fan = Button(frame_bord,text = '±',width = 5,height =1,\
                    command = fan).grid(row = 0,column = 2)
button_ce = Button(frame_bord,text = 'CE',width = 5,height =1,\
                   command = clear).grid(row = 0,column = 3)
num1 = ''
num2 = ''
operator = None

def change(num):
    '''
    按下一个数字需要考虑
    :param num:
    :return:
    '''
    # 假如操作数是None，表明肯定是第一个操作数
    global num1, num2
    if not operator:
        num1 += num
        # 如果是第一个操作数，则只显示第一个操作数
        sv.set(num1)
    else:
        num2 += num
        sv.set(num1+operator+num2)



def operation(op):
    print(op)
b_1 = Button(frame_bord, text='1', width=5, height=2,\
             command=lambda:change("1"))
b_1.grid(row=1, column=0)

b_plus = Button(frame_bord, text='+', width=5, height=2,\
             command=lambda:operation("+"))
b_plus.grid(row=2, column=0)
frame_bord.pack(padx=10, pady=10)

root.mainloop()