import tkinter

from tkinter import *
def click_button(numbers): 
    global operator 
    operator=operator + str(numbers) 
    text_Input.set(operator) 

def clear_button(): 
    global operator 
    operator="" 
    text_Input.set(operator) 

def equal_button(): 
    global operator 
    sumup=str(eval(operator)) 
    text_Input.set(sumup) 
    operator="" 

calculator= Tk()
calculator.geometry('300x400')

calculator.title('Calculator')
calculator.configure(bg= 'skyblue')
operator="" 
text_Input=StringVar() 

e1= Entry(calculator, width= 20, bd= 2, relief= 'solid', font= 'TimesnewRoman 16 bold', fg= 'black', bg= 'white', textvariable=text_Input)
e1.grid(columnspan=4)

b1= Button(calculator, text= '7', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(7))
b1.grid(row= 1, column= 0)

b2= Button(calculator, text= '8', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(8))
b2.grid(row= 1, column= 1)

b3= Button(calculator, text= '9', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(9))
b3.grid(row= 1, column= 2)

b4= Button(calculator, text= '+', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button("+"))
b4.grid(row= 1, column= 3)

b5= Button(calculator, text= '4', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(4))
b5.grid(row= 2, column= 0)

b6= Button(calculator, text= '5', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(5))
b6.grid(row= 2, column= 1)

b7= Button(calculator, text= '6', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(6))
b7.grid(row= 2, column= 2)

b8= Button(calculator, text= '-', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button("-"))
b8.grid(row= 2, column= 3)

b9= Button(calculator, text= '1', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(1))
b9.grid(row= 3, column= 0)

b10= Button(calculator, text= '2', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(2))
b10.grid(row= 3, column= 1)

b11= Button(calculator, text= '3', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button(3))
b11.grid(row= 3, column= 2)

b12= Button(calculator, text= '*', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button("*"))
b12.grid(row= 3, column= 3)

b13= Button(calculator, text= '0', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white')
b13.grid(row= 4, column= 0)

b14= Button(calculator, text= 'C', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=clear_button)
b14.grid(row= 4, column= 1)

b15= Button(calculator, text= '=', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=equal_button)
b15.grid(row= 4, column= 2)

b16= Button(calculator, text= '/', width= 5, height= 3, bd= 2, relief= 'solid', font='TimesnewRoman 14 bold', fg= 'black', bg= 'white', command=lambda:click_button("/"))
b16.grid(row= 4, column= 3)

calculator.mainloop()