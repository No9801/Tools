#!python3
# -*- coding:utf-8 -*-

import tkinter as tk
import json
from subprocess import Popen

import windows
import change

#import os;os.chdir('E:/1/tools');import tools;tools.main()

from config import unit

def main():
    root = tk.Tk()
    root.title("小工具箱")
    root.geometry("%sx%s" %(11*unit, 12*unit))
    button_1 = tk.Button(root, text="次方计算", command=lambda:windows.page_1(root))
    button_3 = tk.Button(root, text="二元一次方程", command=lambda:windows.page_2(root))
    button_2 = tk.Button(root, text="一元二次方程", command=lambda:windows.page_3(root))
    button_4 = tk.Button(root, text="三元一次方程", command=lambda:windows.page_4(root))
    button_5 = tk.Button(root, text="直角坐标转极坐标", command=lambda:change.window(True))
    button_6 = tk.Button(root, text="极坐标转直角坐标", command=change.window)
    button_7 = tk.Button(root, command=lambda:Popen("./game/eating_snake.exe"))
    button_1.place(x=unit, y=unit, height=2*unit, width=4*unit)
    button_2.place(x=6*unit, y=unit, height=2*unit, width=4*unit)
    button_3.place(x=unit, y=4*unit, height=2*unit, width=4*unit)
    button_4.place(x=6*unit, y=4*unit, height=2*unit, width=4*unit)
    button_5.place(x=unit, y=7*unit, height=2*unit, width=4*unit)
    button_6.place(x=6*unit, y=7*unit, height=2*unit, width=4*unit)
    button_7.place(x=9*unit, y=10*unit, height=unit, width=unit)
    root.mainloop()

if __name__ == '__main__':
    main()
