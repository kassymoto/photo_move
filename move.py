# -*- coding: utf-8 -*-

import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import datetime
import shutil

# 参照ボタンのイベント
# button1クリック時の処理
def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    dir = filedialog.askdirectory(initialdir = iDir)
    file1.set(dir)

def button2_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    dir = filedialog.askdirectory(initialdir = iDir)
    file2.set(dir)

# button2クリック時の処理
def button3_clicked():
    path_from = file1.get()
    path_to = file2.get()
    for x in os.listdir(path_from):
        direc = os.listdir(path_to)
        times = os.path.getctime(path_from + './' + x)
        date = datetime.date.fromtimestamp(times)

        if not str(date) in direc:
            os.mkdir(path_to + './' + str(date))
        shutil.move(path_from + './' + x , path_to + './' + str(date) +'/'+ x)

    messagebox.showinfo('FileReference Tool', u'参照元\n' + file1.get() +'\n'+u'参照先\n'+ file2.get())

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('FileReference Tool')
    root.resizable(False, False)

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 参照ボタンの作成
    button1 = ttk.Button(frame1, text=u'参照', command=button1_clicked)
    button1.grid(row=0, column=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('From>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)

    #2
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid()

    button2 = ttk.Button(frame2, text=u'参照', command=button2_clicked)
    button2.grid(row=0, column=3)

    s2 = StringVar()
    s2.set('To>>')
    label2 = ttk.Label(frame2, textvariable=s2)
    label2.grid(row=0, column=0)

    file2 = StringVar()
    file2_entry = ttk.Entry(frame2, textvariable=file2, width=50)
    file2_entry.grid(row=0, column=2)

    #3
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid()

    button3 = ttk.Button(frame3, text='Start', command=button3_clicked)
    button3.pack(side=LEFT)

    button4 = ttk.Button(frame3, text='Cancel', command=quit)
    button4.pack(side=LEFT)



    root.mainloop()
