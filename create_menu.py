from tkinter import *
def create_menu_bar(main_window):
    menu_bar = Menu(main_window, bd=3, fg='red', bg='pink')
    filemenu = Menu(menu_bar, tearoff=0)
    filemenu.add_command(label='New', command='')
    filemenu.add_command(label='Open', command='')
    filemenu.add_command(label='Save', command='')
    filemenu.add_command(label='Save_as', command='')
    filemenu.add_command(label='Close', command='')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command='')
    menu_bar.add_cascade(label='File', menu=filemenu)

    editmenu = Menu(menu_bar, tearoff=0)
    editmenu.add_command(label='Cut', command='')
    editmenu.add_command(label='Copy', command='')
    editmenu.add_command(label='Paste', command='')
    editmenu.add_command(label='Select All', command='')
    menu_bar.add_cascade(label='Edit', menu=editmenu)

    helpmenu = Menu(menu_bar, tearoff=0)
    helpmenu.add_command(label='Help Index', command='')
    helpmenu.add_command(label='About...', command='')
    menu_bar.add_cascade(label='Help', menu=helpmenu)
    main_window.config(menu=menu_bar)

