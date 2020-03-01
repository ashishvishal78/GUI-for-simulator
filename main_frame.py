import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import Menu
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import create_menu
import Modulation_package as mod

main_window=tk.Tk(className='Device Simulator')

create_menu.create_menu_bar(main_window)

def plot_resistor():
    sc_x=1
    sc_y=1
    '''def sel():
        sc_x=str(scale_factor_x.get())
        sc_y=scale_factor_y.get()
        print(sc_x,sc_y)'''

    def click_me():
        volt = []
        current = []
        resistance = resist.get()
        if(resistance==0):
            msg.showerror('Division by Zero', 'Enter resitance value greater than 0')
            return
        sc_x = scale_factor_x.get()
        sc_y = scale_factor_y.get()
        print(sc_x, sc_y)
        max_range=max(100,int(sc_x))
        for i in range(0,max_range,1):
            hel=i/resistance
            if(hel>sc_y):
                break
            volt.append(i)
            current.append(hel)


        fig = Figure(figsize=(8,6), facecolor='pink', edgecolor='green', linewidth=5)
        axis = fig.add_subplot(1, 1, 1)
        axis.plot(volt, current)
        axis.set_ylim(-10,1*sc_y+10)
        axis.set_xlim(-10, max_range+10)
        axis.set_xlabel('voltage')
        axis.set_ylabel('current')
        plt.title('Current vs Voltage graph')
        axis.grid(linestyle='-')
        canvas = FigureCanvasTkAgg(fig, master=resistor_window)
        canvas._tkcanvas.grid(row=4,column=0,columnspan=2,sticky=tk.EW)
    resistor_window=tk.Tk(className='Resistor I-V plotting')
    ttk.Label(resistor_window,text='Enter Resistance value :').grid(row=0,column=0,padx=20,pady=20,sticky=tk.E)
    resist=tk.DoubleVar(resistor_window)
    resist.set(1)
    r_entered=Entry(resistor_window,textvariable=resist).grid(row=0,column=1,padx=20,pady=20,sticky=tk.W)

    #r_entered.focus()
    action = ttk.Button(resistor_window, text="plot graph",command=click_me).grid(row=3, column=0,padx=20,pady=20,sticky=tk.E)

    scale_factor_y = DoubleVar(resistor_window)
    scale_factor_x = DoubleVar(resistor_window)
    ttk.Label(resistor_window,text='scaling factor x: ').grid(row=1,column=0,sticky=tk.E)
    ttk.Label(resistor_window,text='scaling factor y: ').grid(row=2,column=0,sticky=tk.E)

    scale_y = Scale(resistor_window, variable=scale_factor_x, from_=0, to=1000, orient=HORIZONTAL).grid(row=1,column=1,sticky=tk.EW, columnspan=3)
    scale_x = Scale(resistor_window, variable=scale_factor_y, from_=0, to=1000, orient=HORIZONTAL).grid(row=2,column=1,sticky=tk.EW, columnspan=3)
    #button = Button(resistor_window, text="Get Scale Value", command=sel).grid(row=2,column=1)

    resistor_window.mainloop()
def plot_modulation():
    mod.Plot_Amplitude_Modulation()
def plot_frequency_modulation():
    mod.Plot_Frequency_Modulation()
def Plot_Phase_Modulation():
    mod.Plot_Phase_Modulation()

plot_detail=LabelFrame(main_window,width=350,highlightcolor='pink',highlightbackground='pink',bd=10,bg='Aqua').grid(row=0,column=0,padx=20,pady=10)
Label(plot_detail,text='Choose Any One to Plot Graph',fg='Black',font='Didot').grid(row=0,column=0)
button1=tk.Button(plot_detail,bg='LightSlateGray',command=plot_resistor,font='Courier',activebackground='blue',activeforeground='red',text='resistor',width=20,height=2).grid(row=1,column=0,padx=5,pady=5)
button2=tk.Button(plot_detail,bg='LightSlateGray',command=plot_modulation,font='courier',activebackground='blue',activeforeground='red',text='Amplitude Modulation',width=20,height=2).grid(row=2,column=0,padx=5,pady=5)
button3=tk.Button(plot_detail,bg='LightSlateGray',command=plot_frequency_modulation,font='courier',activebackground='blue',activeforeground='red',text='Frequency Modulation',width=20,height=2).grid(row=3,column=0,padx=5,pady=5)
button4=tk.Button(plot_detail,bg='LightSlateGray',command=Plot_Phase_Modulation,font='courier',activebackground='blue',activeforeground='red',text='Phase Modulation',width=20,height=2).grid(row=4,column=0,padx=5,pady=5)

main_window.mainloop()