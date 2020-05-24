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
from tkinter import filedialog as fd
import create_menu


def plot_diode():
    diode_window = tk.Tk(className='Diode Simulation')
    # icon_background(modulation_window,photo)
    diode_window.configure(background='AntiqueWhite1')
    fig = Figure(figsize=(15, 6), facecolor='pink', edgecolor='green', linewidth=1)
    canvas = FigureCanvasTkAgg(fig, master=diode_window)
    create_menu.create_menu_bar1(diode_window, canvas)
    diode_window.resizable(False, False)


    electron_density_p = tk.DoubleVar(diode_window)
    hole_density_p = tk.DoubleVar(diode_window)
    electron_density_n = tk.DoubleVar(diode_window)
    hole_density_n = tk.DoubleVar(diode_window)
    ttk.Label(diode_window, text='Electron density of p side    ').grid(row=0, column=0, sticky=tk.W)
    Entry(diode_window, textvariable=electron_density_p).grid(row=0, column=1, sticky=tk.W)
    ttk.Label(diode_window, text='Hole Density of n side    ').grid(row=1, column=0, sticky=tk.W)
    Entry(diode_window, textvariable=hole_density_p).grid(row=1, column=1, sticky=tk.W)
    ttk.Label(diode_window, text='Electron density of p side    ').grid(row=2, column=0, sticky=tk.W)
    Entry(diode_window, textvariable=electron_density_n).grid(row=2, column=1, sticky=tk.W)
    ttk.Label(diode_window, text='Hole Density of n side    ').grid(row=3, column=0, sticky=tk.W)
    Entry(diode_window, textvariable=hole_density_n).grid(row=3, column=1, sticky=tk.W)


    tk.Label(diode_window, text='Select to plot Graph').grid(row=0, column=2, sticky=tk.W)
    f_bias = tk.IntVar(diode_window)
    check1 = tk.Checkbutton(diode_window, text="Forward Bias", variable=f_bias)  # ,state='disabled')
    check1.deselect()
    check1.grid(row=1, column=2, sticky=tk.W)
    r_bias = tk.IntVar(diode_window)
    check2 = tk.Checkbutton(diode_window, text="Reverse Bias", variable=r_bias)
    check2.select()
    check2.grid(row=2, column=2, sticky=tk.W)