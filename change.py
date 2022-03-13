#!python3
# -*-coding=utf-8-*-

import tkinter as tk
import math
import shelve
import json
import numpy as np
import pyautogui as pag

from config import unit

shelf_file = shelve.open("./data/data")
sin_vec = shelf_file["sin_vec"]
shelf_file.close()

def to_rad(deg):
    return (deg/180)*math.pi

def to_deg(rad):
    return (rad/math.pi)*180

def sin_to_deg(sin_num):
    if (sin_num<0) or (sin_num>1):
        raise ValueError("The number must be greater than 0, less than 1!")
    angle_vec = abs(sin_vec - sin_num)
    angle_deg = list(angle_vec).index(angle_vec.min())
    angle_deg /= 100
    return angle_deg

def r_th_to_x_y(r, th):
    x = r * math.cos(to_rad(th))
    y = r * math.sin(to_rad(th))
    return x, y

def x_y_to_r_th(x, y):
    r = abs(complex(x, y))
    if (x==0) or (y==0):
        if x == 0:
            if y > 0:
                th = 90
            elif y < 0:
                th = 270
            else:
                th = 0
        else:
            if x > 0:
                th = 0
            else:
                th = 180
    else:
        alpha = sin_to_deg(y/r)
        if x > 0:
            if y > 0:
                th = alpha
            else:
                th = 360 - alpha
        else:
            if y > 0:
                th = 180 - alpha
            else:
                th = 180 + alpha
    return r, th 

def window(x_y=False):
    window = tk.Tk()
    if x_y:
        window.title("直角坐标转极坐标")
        label_1 = tk.Label(window, text="x")
        label_2 = tk.Label(window, text="y")
    else:
        window.title("极坐标转直角坐标")
        label_1 = tk.Label(window, text="r")
        label_2 = tk.Label(window, text="theta(°)")
    window.geometry("%sx%s" %(11*unit, 12*unit))
    entry_1 = tk.Entry(window)
    entry_2 = tk.Entry(window)
    label_1.place(x=unit, y=unit, height=unit, width=4*unit)
    label_2.place(x=6*unit, y=unit, height=unit, width=4*unit)
    entry_1.place(x=unit, y=2*unit, height=2*unit, width=4*unit)
    entry_2.place(x=6*unit, y=2*unit, height=2*unit, width=4*unit)


    def compute():
        try:
            a = float(entry_1.get())
            b = float(entry_2.get())
        except Exception as err:
            pag.alert(err, "Error")
        if x_y:
            r_num, th_num= x_y_to_r_th(a, b)
            message = "(%.3f, %.3f) 的极坐标是：(%.3f, %.3f)" %(a, b, r_num, th_num)
        else:
            x_num, y_num= r_th_to_x_y(a, b)
            message = "(%.3f, %.3f) 的直角坐标是：(%.3f, %.3f)" %(a, b, x_num, y_num)
        window_message = tk.Text(window)
        window_message.place(x=unit, y=9*unit, height=2*unit, width=9*unit)
        window_message.insert(tk.END, message)

        
    button_1 = tk.Button(window, text="计算", command=compute)
    button_1.place(x=7*unit, y=6*unit, height=unit, width=2*unit)
