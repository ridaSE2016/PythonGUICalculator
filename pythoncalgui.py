# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:52:31 2020

@author: Rida Hamid
"""

from tkinter import *
root = Tk()

root.title("Calculator")
#for input 
e = Entry(root, width = 40, borderwidth = 5)
e.grid(row = 0 , columnspan = 3, padx = 15, pady=15)


#to display when button clicks
def btn_click(num):
    current = e.get()
    e.delete(0,END)
    
    e.insert(0,str(current) + str(num))
    
    
def btn_clear():
    e.delete(0,END)

def btn_add():
    first_num = e.get()
    global fnum
    global opt
    opt = "addition"
    fnum = int(first_num)
    e.delete(0,END)
    
    
def btn_sub():
    first_num = e.get()
    global fnum
    global opt
    opt = "subtraction"
    fnum = int(first_num)
    e.delete(0,END)
    
def btn_mul():
    first_num = e.get()
    global fnum
    global opt
    opt = "multiplication"
    fnum = int(first_num)
    e.delete(0,END)
 
def btn_div():
    first_num = e.get()
    global fnum
    global opt
    opt = "division"
    fnum = int(first_num)
    e.delete(0,END)
    
    
    
    
    
    
    
    
def btn_equal():
    second_num = e.get() #store
    e.delete(0, END) #clear
    
    if opt == "addition":
         e.insert(0,int(fnum) + int(second_num))
    elif opt == "subtraction":
          e.insert(0,int(fnum) - int(second_num))
    elif opt == "multiplication":
          e.insert(0,int(fnum) * int(second_num))
    elif opt == "division":
          e.insert(0,int(fnum) / int(second_num))
    
    
    
    
btn7 = Button(root, text = "7", padx = 40, pady =20,bg = "black",fg = "white", command=lambda: btn_click(7))
btn8 = Button(root, text = "8", padx = 41, pady = 20,bg = "black",fg = "white", command= lambda:btn_click(8))
btn9 = Button(root, text = "9", padx = 44, pady= 20,bg = "black",fg = "white", command=lambda: btn_click(9))

btn4 = Button(root, text = "4", padx = 40, pady =20,bg = "black",fg = "white", command=lambda:btn_click(4))
btn5 = Button(root, text = "5", padx = 41, pady = 20,bg = "black",fg = "white", command=lambda:btn_click(5))
btn6 = Button(root, text = "6", padx = 44, pady= 20,bg = "black",fg = "white", command=lambda:btn_click(6))


btn1 = Button(root, text = "1", padx = 40, pady =20,bg = "black",fg = "white",command=lambda:btn_click(1))
btn2 = Button(root, text = "2", padx = 41, pady = 20, bg = "black",fg = "white",command=lambda:btn_click(2))
btn3 = Button(root, text = "3", padx = 44, pady= 20, bg = "black",fg = "white",command=lambda:btn_click(3))

btn0= Button(root, text = "0", padx = 87.5, pady =20,bg = "black",fg = "white", command=lambda:btn_click(0))
btn_plus = Button(root, text = "+", padx = 43, pady = 20,bg = "black",fg = "white", command = btn_add)


btn_sub = Button(root, text = "-", padx = 40, pady= 20,bg = "black",fg = "white", command = btn_sub)
btn_mul = Button(root, text = "*", padx = 41, pady= 20, bg = "black",fg = "white",command = btn_mul)
btn_div = Button(root, text = "/", padx = 44, pady= 20, bg = "black",fg = "white", command = btn_div)


btn_clear= Button(root, text = "clear", padx = 77, pady =20,bg = "black",fg = "white",command = btn_clear)
btn_equal = Button(root, text = "=", padx = 44, pady= 20,bg = "black",fg = "white", command = btn_equal)

btn7.grid(row = 1, column = 0)
btn8.grid(row = 1, column = 1)
btn9.grid(row = 1, column = 2)

btn4.grid(row = 2, column = 0)
btn5.grid(row = 2, column = 1)
btn6.grid(row = 2, column = 2)

btn1.grid(row = 3, column = 0)
btn2.grid(row = 3, column = 1)
btn3.grid(row = 3, column = 2)


btn0.grid(row = 4, column = 0, columnspan=2)
btn_plus.grid(row = 4, column = 2)

btn_sub.grid(row = 5, column = 0)
btn_mul.grid(row = 5, column = 1)
btn_div.grid(row = 5, column = 2)
btn_clear.grid(row = 6, column = 0, columnspan =2)
btn_equal.grid(row = 6, column = 2)




root.mainloop()
