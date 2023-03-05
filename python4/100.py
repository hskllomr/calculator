import tkinter

pencere=tkinter.Tk()
pencere.title("Calculator")
expression=""

def add(value):#tıklanan sayıları birleştir
    global expression
    expression += value
    label_result.config(text=expression)#sayıyı üste yazdır
def clear():
    global expression
    expression=""
    label_result.config(text=expression)#ekranı temizle
def calculate():#heaplama fonksiyonu
    global expression
    result=""
    result=eval(expression)
    label_result.config(text=result)


label_result=tkinter.Label(pencere,text="")
label_result.grid(row=0,column=0,columnspan=4)

button=tkinter.Button(pencere,text='1',command=lambda:add("1"))
button.grid(row=1,column=0)

button2=tkinter.Button(pencere,text='2',command=lambda:add("2"))
button2.grid(row=1,column=1)

button3=tkinter.Button(pencere,text='3',command=lambda:add("3"))
button3.grid(row=1,column=2)

button_divide=tkinter.Button(pencere,text='/',command=lambda :add("/"))
button_divide.grid(row=1,column=3)

button4=tkinter.Button(pencere,text='4',command=lambda:add("4"))
button4.grid(row=2,column=0)

button5=tkinter.Button(pencere,text='5',command=lambda:add("5"))
button5.grid(row=2,column=1)

button5=tkinter.Button(pencere,text='6',command=lambda:add("6"))
button5.grid(row=2,column=2)

button_divide1=tkinter.Button(pencere,text='*',command=lambda :add("*"))
button_divide1.grid(row=2,column=3)

button6=tkinter.Button(pencere,text='7',command=lambda:add("7"))
button6.grid(row=3,column=0)

button7=tkinter.Button(pencere,text='8',command=lambda:add("8"))
button7.grid(row=3,column=1)

button8=tkinter.Button(pencere,text='9',command=lambda:add("9"))
button8.grid(row=3,column=2)

button9=tkinter.Button(pencere,text='-',command=lambda:add("-"))
button9.grid(row=3,column=3)

button9=tkinter.Button(pencere,text='C',command=lambda: clear())
button9.grid(row=4,column=0)

button10=tkinter.Button(pencere,text='0',command=lambda: add("0"))
button10.grid(row=4,column=1)

button11=tkinter.Button(pencere,text='.',command=lambda: add("."))
button11.grid(row=4,column=2)

button12=tkinter.Button(pencere,text='+',command=lambda: add("+"))
button12.grid(row=4,column=3)

button13=tkinter.Button(pencere,text='=',command=lambda: calculate())
button13.grid(row=5,column=0,rowspan=4)

pencere.mainloop()