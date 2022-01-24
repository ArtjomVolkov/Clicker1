from tkinter import*
k=0
def clicker(event):
	global k
	k+=1
	nupp.config(text=k)
def clicker_(event):
	global k
	k-=1
	nupp.config(text=k)
def txt_to_lbl(event):
	text=txt.get()
	lbl.configure(text=text)
	txt.delete(0,END)
def valimine():
	valik=var.get()
	lbl.configure(text=valik)
aken=Tk()
aken.title("𝕮𝖑𝖎𝖈𝖐𝖊𝖗")
aken.geometry("800x600")
nupp=Button(aken, text = "𝕲𝖑𝖔𝖇𝖆𝖑", font="Arial_Bold 100", width=10, fg="white", bg="red",relief=RAISED)  
nupp.place(x=5,y=250)  #side=LEFT
nupp.bind("<Button-1>",clicker)
nupp.bind("<Button-3>",clicker_)
lbl=Label(aken,text="...",height=1,width=10,font="Arial_Bold 100",fg="green", bg="lightblue",relief="solid")
lbl.place(x=1,y=10)
txt=Entry(aken,width=10,font="Arial_Bold 100",fg="green", bg="lightblue",justify=CENTER)
txt.place(x=8,y=100)
txt.bind("<Return>",txt_to_lbl)#Enter
i1=PhotoImage(file="drugs-weekend-mood.gif")
i2=PhotoImage(file="drunk-drugs.gif")
i3=PhotoImage(file="giphy.gif")
var=StringVar()
var.set("Üks")
r1=Radiobutton(aken,image=i1,variable=var,value="Üks",command=valimine)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks",command=valimine)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm",command=valimine)
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
aken.mainloop()
