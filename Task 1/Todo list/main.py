import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.tital("Own to do list")

list_frame = tkinter.frame(window)
list_frame.pack()

todo_box = tkinter.listbox(list_frame, )

window.mainloop()


