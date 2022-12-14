from tkinter import*
w=Tk()
w.geometry("240x240")  ## size
w.title("Elements Dictionary")  ## name the window
w.config(background="red")  ## change background color
l=Label(w,text="que mierda",font=('arial',20,'bold'),fg='blue') ## label
#l.pack()  ## add label to window
l.place(x=0,y=0) ## choose the place of  the label
e=Entry(w)
e.pack()
w.mainloop()  ## place window
