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

def Plot_Amplitude_Modulation():
    def plot_AM():
        try:
            Amplitde=[]
            Amplitude_carrier = []
            Amplitude_send=[]
            time_ = []
            m_f = fre_m.get()
            time_period=((1/m_f)*(scale_factor.get()/10))/100000
            for i in range(1,100000,1):
                time_.append(time_period*i)
                Amplitde.append(Amp_m.get()*(np.cos(2*math.pi*m_f*(time_period*i))))
                Amplitude_carrier.append(Amp_c.get()*(np.cos((2*math.pi*fre_c.get()*(time_period*i)))))
                Amplitude_send.append(Amplitude_carrier[i-1]*Amp_sen.get()*Amplitde[i-1]+Amplitude_carrier[i-1])
                #Amplitude_send.append(Amp_c.get()*(1+(Amp_sen.get()*Amp_m.get()*(np.cos(2*3.14*m_f*(time_period*i)))))*(np.cos(2*3.14*fre_c.get()*(time_period*i))))
            print(Amplitude_carrier)
            fig = Figure(figsize=(8, 6), facecolor='pink', edgecolor='green', linewidth=5)
            axis = fig.add_subplot(2, 2, 1)
            axis.plot( time_,Amplitde)
            axis.set_xlabel('time(Sec)')
            axis.set_ylabel('Amplitude(Volt)')
            #axis.title('Amplitude Vs Time of modulating signal')

            carrier_graph = fig.add_subplot(2, 2, 2)
            carrier_graph.plot(time_, Amplitude_carrier)
            carrier_graph.set_xlabel('time(Sec)')
            carrier_graph.set_ylabel('Amplitude(Volt)')
            #carrier_graph.title('Amplitude Vs Time of carrier signal')

            sender_graph=fig.add_subplot(2, 2, 3)
            sender_graph.plot(time_, Amplitude_send)
            sender_graph.set_xlabel('time(Sec)')
            sender_graph.set_ylabel('Amplitude(Volt)')


            #sender_graph.title('Amplitude Vs Time of sender signal')
            #axis.set_ylim(-10, 1 * sc_y + 10)
            #axis.set_xlim(-10, max_range + 10)


            axis.grid(linestyle='-')
            sender_graph.grid(linestyle='-')
            carrier_graph.grid(linestyle='-')


            canvas = FigureCanvasTkAgg(fig, master=modulation_window)
            canvas._tkcanvas.grid(row=7, column=0, columnspan=2, sticky=tk.EW)

            #Amp_sig=Amp_c.get()*(1+(Amp_sen.get()*Amp_m.get())*(cos()))
        except:
            msg.showerror('Input Entry Error','Please Enter Valid Number')

    modulation_window = tk.Tk(className='Amplitude Modulation')
    Amp_c = tk.DoubleVar(modulation_window)
    fre_c=tk.DoubleVar(modulation_window)
    Amp_m=tk.DoubleVar(modulation_window)
    fre_m=tk.DoubleVar(modulation_window)
    Amp_sen = tk.DoubleVar(modulation_window)
    ttk.Label(modulation_window, text='Carrier Signal Amplitude :').grid(row=0, column=0, padx=2, pady=2)
    Entry(modulation_window,textvariable=Amp_c).grid(row=0, column=1, padx=2, pady=2)
    ttk.Label(modulation_window,text='Carrier Signal Frequency :').grid(row=1, column=0, padx=2, pady=2)
    Entry(modulation_window,textvariable=fre_c).grid(row=1,column=1,padx=2,pady=2)
    ttk.Label(modulation_window, text='Modulating Signal Amplitude :').grid(row=2, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=Amp_m).grid(row=2, column=1, padx=2, pady=2)
    ttk.Label(modulation_window, text='Modulating Signal Frequency :').grid(row=3, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=fre_m).grid(row=3, column=1, padx=2, pady=2)
    ttk.Label(modulation_window, text='Amplitude Sensitivity :').grid(row=4, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=Amp_sen).grid(row=4, column=1, padx=2, pady=2)
    scale_factor=tk.DoubleVar(modulation_window)
    ttk.Label(modulation_window,text='scale_factor :').grid(row=5,column=0,padx=2,pady=2,sticky=tk.W,columnspan=2)
    scaleing=Scale(modulation_window,from_=0,to=100,variable=scale_factor,orient=HORIZONTAL).grid(row=5,column=1,padx=2,pady=2,sticky=tk.EW)
    action=ttk.Button(modulation_window,command=plot_AM,text='Plot Graph').grid(row=6,column=0,padx=2,pady=2,sticky=tk.E)

def Plot_Frequency_Modulation():
    def plot_FM():
        try:
            Amplitde=[]
            Amplitude_carrier = []
            Amplitude_send=[]
            Amplitude_phase=[]
            time_ = []
            m_f = fre_m.get()

            time_period=((1/m_f)*scale_factor.get()/10)/10000
            for i in range(1,10000,1):
                time_.append(time_period*i)
                Amplitde.append(Amp_m.get()*(np.cos(2*math.pi*m_f*(time_period*i))))
                Amplitude_carrier.append(Amp_c.get()*(np.cos(2*math.pi*fre_c.get()*(time_period*i))))
                Amplitude_send.append(Amp_c.get()*(np.cos(2*math.pi*fre_c.get()*(time_period*i)+(fre_sen.get()*Amp_m.get()/fre_m.get())*(np.sin(2*math.pi*fre_m.get()*(time_period*i))))))
                #Amplitude_phase.append(Amp_c.get()*(np.cos(2*math.pi*fre_c.get()*(time_period*i)+(fre_sen.get()*Amp_m.get())*(np.cos(2*math.pi*m_f*(time_period*i))))))

            fig = Figure(figsize=(8, 6), facecolor='pink', edgecolor='green', linewidth=1)
            axis = fig.add_subplot(2, 2, 1)
            axis.plot( time_,Amplitde)
            axis.set_xlabel('time(Sec)')
            axis.set_ylabel('Amplitude(Volt)')
            #axis.title('Amplitude Vs Time of modulating signal')

            carrier_graph = fig.add_subplot(2, 2, 2)
            carrier_graph.plot(time_, Amplitude_carrier)
            carrier_graph.set_xlabel('time(Sec)')
            carrier_graph.set_ylabel('Amplitude(Volt)')
            #carrier_graph.title('Amplitude Vs Time of carrier signal')

            sender_graph=fig.add_subplot(2, 2, 3)
            sender_graph.plot(time_, Amplitude_send)
            sender_graph.set_xlabel('time(Sec)')
            sender_graph.set_ylabel('Amplitude(Volt)')

            #Amplitude_ph = fig.add_subplot(2, 2, 4)
            #Amplitude_ph.plot(time_, Amplitude_phase)
            #Amplitude_ph.set_xlabel('time(Sec)')
            #Amplitude_ph.set_ylabel('Amplitude(Volt)')
            #sender_graph.title('Amplitude Vs Time of sender signal')
            #axis.set_ylim(-10, 1 * sc_y + 10)
            #axis.set_xlim(-10, max_range + 10)
            axis.grid(linestyle='-')
            sender_graph.grid(linestyle='-')
            carrier_graph.grid(linestyle='-')
            #Amplitude_ph.grid(linestyle='-')

            canvas = FigureCanvasTkAgg(fig, master=modulation_window)
            canvas._tkcanvas.grid(row=7, column=0, columnspan=3, sticky=tk.EW)
        except:
            msg.showerror('Input Entry Error','Please Enter Valid Number')
    modulation_window = tk.Tk(className='Amplitude Modulation')
    Amp_c = tk.DoubleVar(modulation_window)
    fre_c=tk.DoubleVar(modulation_window)
    Amp_m=tk.DoubleVar(modulation_window)
    fre_m=tk.DoubleVar(modulation_window)
    fre_sen = tk.DoubleVar(modulation_window)
    ttk.Label(modulation_window, text='Carrier Signal Amplitude :').grid(row=0, column=0, padx=2, pady=2)
    Entry(modulation_window,textvariable=Amp_c).grid(row=0, column=1, padx=2, pady=2)
    ttk.Label(modulation_window,text='Carrier Signal Frequency :').grid(row=1, column=0, padx=2, pady=2)
    Entry(modulation_window,textvariable=fre_c).grid(row=1,column=1,padx=2,pady=2)
    ttk.Label(modulation_window, text='Modulating Signal Amplitude :').grid(row=2, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=Amp_m).grid(row=2, column=1, padx=2, pady=2)
    ttk.Label(modulation_window, text='Modulating Signal Frequency :').grid(row=3, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=fre_m).grid(row=3, column=1, padx=2, pady=2)
    ttk.Label(modulation_window, text='frequency Sensitivity :').grid(row=4, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=fre_sen).grid(row=4, column=1, padx=2, pady=2)
    scale_factor = tk.DoubleVar(modulation_window)
    ttk.Label(modulation_window, text='scaling factor : ').grid(row=5, column=0, sticky=tk.E)
    scale_y = Scale(modulation_window, variable=scale_factor, from_=0, to=100, orient=HORIZONTAL).grid(row=5,
                                                                                                       column=1,
                                                                                                       sticky=tk.EW,
                                                                                                       columnspan=2)
    action=ttk.Button(modulation_window,command=plot_FM,text='Plot Graph').grid(row=6,column=0,padx=2,pady=2,sticky=tk.E)

def Plot_Phase_Modulation():
    def plot_PM():
        try:
            Amplitde=[]
            Amplitude_carrier = []
            Amplitude_send=[]
            time_ = []
            m_f = fre_m.get()

            time_period=((1/m_f)*scale_factor.get()/10)/10000
            for i in range(1,10000,1):
                time_.append(time_period*i)
                Amplitde.append(Amp_m.get()*(np.cos(2*math.pi*m_f*(time_period*i))))
                Amplitude_carrier.append(Amp_c.get()*(np.cos(2*math.pi*fre_c.get()*(time_period*i))))
                Amplitude_send.append(Amp_c.get()*(np.cos(2*math.pi*fre_c.get()*(time_period*i)+(phase_sen.get()*Amp_m.get())*(np.cos(2*math.pi*m_f*(time_period*i))))))

            fig = Figure(figsize=(8, 6), facecolor='pink', edgecolor='green', linewidth=1)
            axis = fig.add_subplot(2, 2, 1)
            axis.plot( time_,Amplitde)
            axis.set_xlabel('time(Sec)')
            axis.set_ylabel('Amplitude(Volt)')
            #axis.title('Amplitude Vs Time of modulating signal')

            carrier_graph = fig.add_subplot(2, 2, 2)
            carrier_graph.plot(time_, Amplitude_carrier)
            carrier_graph.set_xlabel('time(Sec)')
            carrier_graph.set_ylabel('Amplitude(Volt)')
            #carrier_graph.title('Amplitude Vs Time of carrier signal')

            sender_graph=fig.add_subplot(2, 2, 3)
            sender_graph.plot(time_, Amplitude_send)
            sender_graph.set_xlabel('time(Sec)')
            sender_graph.set_ylabel('Amplitude(Volt)')

            #Amplitude_ph = fig.add_subplot(2, 2, 4)
            #Amplitude_ph.plot(time_, Amplitude_phase)
            #Amplitude_ph.set_xlabel('time(Sec)')
            #Amplitude_ph.set_ylabel('Amplitude(Volt)')
            #sender_graph.title('Amplitude Vs Time of sender signal')
            #axis.set_ylim(-10, 1 * sc_y + 10)
            #axis.set_xlim(-10, max_range + 10)
            axis.grid(linestyle='-')
            sender_graph.grid(linestyle='-')
            carrier_graph.grid(linestyle='-')
            #Amplitude_ph.grid(linestyle='-')

            canvas = FigureCanvasTkAgg(fig, master=modulation_window)
            canvas._tkcanvas.grid(row=7, column=0, columnspan=3, sticky=tk.EW)
        except:
            msg.showerror('Input Entry Error','Please Enter Valid Number')
    modulation_window = tk.Tk(className='Amplitude Modulation')
    Amp_c = tk.DoubleVar(modulation_window)
    fre_c=tk.DoubleVar(modulation_window)
    Amp_m=tk.DoubleVar(modulation_window)
    fre_m=tk.DoubleVar(modulation_window)
    phase_sen = tk.DoubleVar(modulation_window)
    ttk.Label(modulation_window, text='Carrier Signal Amplitude :').grid(row=0, column=0, padx=2, pady=2)
    Entry(modulation_window,textvariable=Amp_c).grid(row=0, column=1, padx=2, pady=2)
    ttk.Label(modulation_window,text='Carrier Signal Frequency :').grid(row=1, column=0, padx=2, pady=2)
    Entry(modulation_window,textvariable=fre_c).grid(row=1,column=1,padx=2,pady=2)
    ttk.Label(modulation_window, text='Modulating Signal Amplitude :').grid(row=2, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=Amp_m).grid(row=2, column=1, padx=2, pady=2)
    ttk.Label(modulation_window, text='Modulating Signal Frequency :').grid(row=3, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=fre_m).grid(row=3, column=1, padx=2, pady=2)
    ttk.Label(modulation_window, text='Phase Sensitivity :').grid(row=4, column=0, padx=2, pady=2)
    Entry(modulation_window, textvariable=phase_sen).grid(row=4, column=1, padx=2, pady=2)
    scale_factor = tk.DoubleVar(modulation_window)
    ttk.Label(modulation_window, text='scaling factor : ').grid(row=5, column=0, sticky=tk.E)
    scale_y = Scale(modulation_window, variable=scale_factor, from_=0, to=100, orient=HORIZONTAL).grid(row=5,
                                                                                                       column=1,
                                                                                                       sticky=tk.EW,
                                                                                                       columnspan=2)
    action=ttk.Button(modulation_window,command=plot_PM,text='Plot Graph').grid(row=6,column=0,padx=2,pady=2,sticky=tk.E)
