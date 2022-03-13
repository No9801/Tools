#!python3
# -*- coding:utf-8 -*-

import json, math
import tkinter as tk
import numpy as np

from config import unit

def compute_p1(a, n, page):
    pow_num = a ** n
    message = """%.3f 的 %.3f 次方是：
    %.3f""" %(a, n, pow_num)
    pow_message = tk.Text(page)
    pow_message.place(x=unit, y=9*unit, height=2*unit, width=9*unit)
    pow_message.insert(tk.END, message)

def compute_p2(a_1, a_2, b_1, b_2, c_1, c_2, page_2):
    x_array = np.array([[c_1, b_1], [c_2, b_2]])
    y_array = np.array([[a_1, c_1], [a_2, c_2]])
    base_array = np.array([[a_1, b_1], [a_2, b_2]])
    x_det = np.linalg.det(x_array)
    y_det = np.linalg.det(y_array)
    base_det = np.linalg.det(base_array)
    if base_det == 0:
        try:
            if (b_1/b_2) == (c_1/c_2):
                message = "此方程组有无数解"
            else:
                message = "此方程组无解"
        except ZeroDivisionError:
            if c_1 == 0:
                message = "方程的解为：\nx = 0\ny = 0"
            else:
                message = "此方程组无解"
    else:
        x = x_det / base_det
        y = y_det / base_det
        message = "方程的解为：\nx = %.3f\ny = %.3f" %(x, y)
    compute_window = tk.Toplevel(page_2)
    compute_window.title("compute_window")
    compute_window.geometry("%sx%s" %(11*unit, 12*unit))
    compute_message = tk.Message(compute_window, text=message)
    compute_message.place(x=unit, y=unit, height=10*unit, width=9*unit)

def compute_p3(a, b, c, page_3):
    delta = b**2 - 4*a*c
    if delta < 0:
        message = "此方程无解"
    elif delta == 0:
        x = -(b / (2*a))
        message = "此方程的解为：\nx = %s" %(x)
    else:
        x_1 = (-b + math.sqrt(delta)) / (2*a)
        x_2 = (-b - math.sqrt(delta)) / (2*a)
        message = "此方程的解为：\nx_1 = %.3f\nx_2 = %.3f" %(x_1, x_2)
    message_text = tk.Text(page_3)
    message_text.place(x=unit, y=9*unit, height=2*unit, width=9*unit)
    message_text.insert(tk.END, message)  

def compute_p4(a_1, a_2, a_3,
               b_1, b_2, b_3,
               c_1, c_2, c_3,
               d_1, d_2, d_3, page_4):
    x_array = np.array([[d_1, b_1, c_1],
                        [d_2, b_2, c_2],
                        [d_3, b_3, c_3]])
    y_array = np.array([[a_1, d_1, c_1],
                        [a_2, d_2, c_2],
                        [a_3, d_3, c_3]])
    z_array = np.array([[a_1, b_1, d_1],
                        [a_2, b_2, d_2],
                        [a_3, b_3, d_3]])
    base_array = np.array([[a_1, b_1, c_1],
                           [a_2, b_2, c_2],
                           [a_3, b_3, c_3]])
    x_det = np.linalg.det(x_array)
    y_det = np.linalg.det(y_array)
    z_det = np.linalg.det(z_array)
    base_det = np.linalg.det(base_array)
    if base_det == 0:
        message = "此方程有无数解或无解"
    else:
        x = x_det / base_det
        y = y_det / base_det
        z = z_det / base_det
        message = "方程的解为：\nx = %.3f\ny = %.3f\nz = %.3f" %(x, y, z)
    compute_window = tk.Toplevel(page_4)
    compute_window.title("compute_window")
    compute_window.geometry("%sx%s" %(11*unit, 12*unit))
    compute_message = tk.Message(compute_window, text=message)
    compute_message.place(x=unit, y=unit, height=10*unit, width=9*unit)
