#!python3
# -*- coding:utf-8 -*-

import json
import math
import tkinter as tk
import numpy as np
import pyautogui as pag

import compute

from config import unit

def page_1(root):
    page_1 = tk.Toplevel(root)
    page_1.title("次方计算")
    page_1.geometry("%sx%s" %(11*unit, 12*unit))
    label_1 = tk.Label(page_1, text="底数")
    label_2 = tk.Label(page_1, text="次数")
    label_1.place(x=unit, y=unit, height=unit, width=4*unit)
    label_2.place(x=6*unit, y=unit, height=unit, width=4*unit)
    entry_1 = tk.Entry(page_1)
    entry_2 = tk.Entry(page_1)
    entry_1.place(x=unit, y=2*unit, height=2*unit, width=4*unit)
    entry_2.place(x=6*unit, y=2*unit, height=2*unit, width=4*unit) 

    try:
        button_1 = tk.Button(page_1, text="计算", command=lambda:compute.compute_p1(
        float(entry_1.get()), float(entry_2.get()), page_1))
    except Exception as err:
        pag.alert(err, "Error")
    
    button_1.place(x=7*unit, y=6*unit, height=unit, width=2*unit)

def page_2(root):
    page_2 = tk.Toplevel(root)
    page_2.title("二元一次方程")
    page_2.geometry("%sx%s" %(11*unit, 12*unit))
    label_1 = tk.Label(page_2, text="方程1")
    label_2 = tk.Label(page_2, text="方程2")
    label_3 = tk.Label(page_2, text="x\n系\n数")
    label_4 = tk.Label(page_2, text="y\n系\n数")
    label_5 = tk.Label(page_2, text="常\n数")
    label_1.place(x=3*unit, y=unit, height=unit, width=3*unit)
    label_2.place(x=7*unit, y=unit, height=unit, width=3*unit)
    label_3.place(x=unit, y=3*unit, height=2*unit, width=unit)
    label_4.place(x=unit, y=6*unit, height=2*unit, width=unit)
    label_5.place(x=unit, y=9*unit, height=2*unit, width=unit)
    entry_1 = tk.Entry(page_2)
    entry_2 = tk.Entry(page_2)
    entry_3 = tk.Entry(page_2)
    entry_4 = tk.Entry(page_2)
    entry_5 = tk.Entry(page_2)
    entry_6 = tk.Entry(page_2)
    entry_1.place(x=3*unit, y=3*unit, height=2*unit, width=3*unit)
    entry_2.place(x=7*unit, y=3*unit, height=2*unit, width=3*unit)
    entry_3.place(x=3*unit, y=6*unit, height=2*unit, width=3*unit)
    entry_4.place(x=7*unit, y=6*unit, height=2*unit, width=3*unit)
    entry_5.place(x=3*unit, y=9*unit, height=2*unit, width=3*unit)
    entry_6.place(x=7*unit, y=9*unit, height=2*unit, width=3*unit)
    try:
        button_1 = tk.Button(page_2, text="计算", command=lambda:compute.compute_p2(
                float(entry_1.get()),float(entry_2.get()),
                float(entry_3.get()),float(entry_4.get()),
                float(entry_5.get()),float(entry_6.get()),
                page_2
            ))
    except Exception as err:
        pag.alert(err, "Error")
    
    button_1.place(x=unit, y=unit, height=unit, width=unit)

def page_3(root):
    page_3 = tk.Toplevel(root)
    page_3.title("一元二次方程")
    page_3.geometry("%sx%s" %(11*unit, 12*unit))
    label_1 = tk.Label(page_3, text="二次项系数")
    label_2 = tk.Label(page_3, text="一次项系数")
    label_3 = tk.Label(page_3, text="常数项")
    label_1.place(x=unit, y=unit, height=unit, width=4*unit)
    label_2.place(x=6*unit, y=unit, height=unit, width=4*unit)
    label_3.place(x=unit, y=5*unit, height=unit, width=4*unit)
    entry_1 = tk.Entry(page_3)
    entry_2 = tk.Entry(page_3)
    entry_3 = tk.Entry(page_3)
    entry_1.place(x=unit, y=2*unit, height=2*unit, width=4*unit)
    entry_2.place(x=6*unit, y=2*unit, height=2*unit, width=4*unit)
    entry_3.place(x=unit, y=6*unit, height=2*unit, width=4*unit)

    try:
        button_1 = tk.Button(page_3, text="计算", command=lambda:compute.compute_p3(
            float(entry_1.get()),
            float(entry_2.get()),
            float(entry_3.get()),
            page_3
        ))
    except Exception as err:
        pag.alert(err, "Error!")

    button_1.place(x=8*unit, y=7*unit, height=unit, width=2*unit)

def page_4(root):
    page_4 = tk.Toplevel(root)
    page_4.title("三元一次方程")
    page_4.geometry("%sx%s" %(15*unit, 15*unit))
    label_1 = tk.Label(page_4, text="方程1")
    label_2 = tk.Label(page_4, text="方程2")
    label_3 = tk.Label(page_4, text="x\n系\n数")
    label_4 = tk.Label(page_4, text="y\n系\n数")
    label_5 = tk.Label(page_4, text="z\n系\n数")
    label_1.place(x=3*unit, y=unit, height=unit, width=3*unit)
    label_2.place(x=7*unit, y=unit, height=unit, width=3*unit)
    label_3.place(x=unit, y=3*unit, height=2*unit, width=unit)
    label_4.place(x=unit, y=6*unit, height=2*unit, width=unit)
    label_5.place(x=unit, y=9*unit, height=2*unit, width=unit)
    entry_1 = tk.Entry(page_4)
    entry_2 = tk.Entry(page_4)
    entry_3 = tk.Entry(page_4)
    entry_4 = tk.Entry(page_4)
    entry_5 = tk.Entry(page_4)
    entry_6 = tk.Entry(page_4)
    entry_1.place(x=3*unit, y=3*unit, height=2*unit, width=3*unit)
    entry_2.place(x=7*unit, y=3*unit, height=2*unit, width=3*unit)
    entry_3.place(x=3*unit, y=6*unit, height=2*unit, width=3*unit)
    entry_4.place(x=7*unit, y=6*unit, height=2*unit, width=3*unit)
    entry_5.place(x=3*unit, y=9*unit, height=2*unit, width=3*unit)
    entry_6.place(x=7*unit, y=9*unit, height=2*unit, width=3*unit)

    #new
    label_6 = tk.Label(page_4, text="方程3")
    label_7 = tk.Label(page_4, text="常\n数")
    entry_7 = tk.Entry(page_4)
    entry_8 = tk.Entry(page_4)
    entry_9 = tk.Entry(page_4)
    entry_10 = tk.Entry(page_4)
    entry_11 = tk.Entry(page_4)
    entry_12 = tk.Entry(page_4)
    label_6.place(x=11*unit, y=unit, height=unit, width=3*unit)
    label_7.place(x=unit, y=12*unit, height=2*unit, width=unit)
    entry_7.place(x=11*unit, y=3*unit, height=2*unit, width=3*unit)
    entry_8.place(x=11*unit, y=6*unit, height=2*unit, width=3*unit)
    entry_9.place(x=11*unit, y=9*unit, height=2*unit, width=3*unit)
    entry_10.place(x=11*unit, y=12*unit, height=2*unit, width=3*unit)
    entry_11.place(x=7*unit, y=12*unit, height=2*unit, width=3*unit)
    entry_12.place(x=3*unit, y=12*unit, height=2*unit, width=3*unit)
    #end new

    try:
        button_1 = tk.Button(page_4, text="计算", command=lambda:compute.compute_p4(
                float(entry_1.get()),float(entry_2.get()), float(entry_7.get()),
                float(entry_3.get()),float(entry_4.get()), float(entry_8.get()),
                float(entry_5.get()),float(entry_6.get()), float(entry_9.get()),
                float(entry_12.get()), float(entry_11.get()), float(entry_10.get()),
                page_4
            ))
    except Exception as err:
        pag.alert(err, "Error")
    
    button_1.place(x=unit, y=unit, height=unit, width=unit)    
