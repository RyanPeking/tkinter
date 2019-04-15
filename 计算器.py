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
# 按键区域
frame_bord = Frame(width=400, height=350, bg='#cccccc')

frame_bord.pack(padx=10, pady=10)








root.mainloop()