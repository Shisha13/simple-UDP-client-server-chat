from Tkinter import*
from Client import client
from threading import Thread


class Window:
    cl = client()
    window = Tk()
    name_label = Label(window, text="Your name: ").grid(row=0, column=0, sticky='w')
    name_entry = Entry(window, bd=3)
    text_box = Text(window)
    message_box = Text(window, borderwidth=5)
    send_button = Button(window, text='SEND', height=2, width=15, bg='blue')
    join_button = Button(window, text='JOIN', height=1, width=10, bg='red')
    Is_Entered = False

    def show(self,event):
        some = self.name_entry.get()
        self.join_button.destroy()
        self.cl.Enter_chat(some)
        self.message_box.focus()
        self.Is_Entered = True

    def send_message(self,event):
        message = self.message_box.get("1.0",END)
        self.cl.send(message)
        self.message_box.delete("1.0",END)
    def receiving(self):
        while True:
            if self.Is_Entered:
                reply = self.cl.recive()
                self.text_box.insert(END,reply+'\n')
            else:
                continue

    def place_and_bind(self):
        self.text_box.place(x=20, y=50, height=250, width=350)
        self.name_entry.grid(row=0, column=1, sticky='w')
        self.message_box.place(x=20, y=350, height=40, width=350)
        self.send_button.bind('<Button-1>', self.send_message)
        self.join_button.bind('<Button-1>', self.show)
        self.join_button.place(x=200, y=1)
        self.send_button.place(x=375, y=350)
        self.window.geometry('500x400')

    def start(self):
        looping_thread = Thread(target=self.window.mainloop)
        recv_thread = Thread(target=self.receiving)
        looping_thread.start()
        recv_thread.start()
        looping_thread.join()
        recv_thread.join()



win = Window()
win.place_and_bind()
win.start()





