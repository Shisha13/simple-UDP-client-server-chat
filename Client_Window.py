from Tkinter import*
from Client import client
from threading import Thread
import tkMessageBox


class Window:
    def __init__(self,ip,port):
        self.__cl = client(ip, port)
        self.__GUI_WINDOW = Tk()
        self.__name_label = Label(self.__GUI_WINDOW, text="Your name: ").grid(row=0, column=0, sticky='w')
        self.__name_entry = Entry(self.__GUI_WINDOW, bd=3)
        self.__text_box = Text(self.__GUI_WINDOW)
        self.__message_box = Text(self.__GUI_WINDOW, borderwidth=5)
        self. __send_button = Button(self.__GUI_WINDOW, text='SEND', height=2, width=15, bg='blue')
        self.__join_button = Button(self.__GUI_WINDOW, text='JOIN', height=2, width=15, bg='red')
        self.__create_room_button = Button(self.__GUI_WINDOW, text='CREATE ROOM', height=2, width=15, bg='red')
        self.__rooms = Listbox(self.__GUI_WINDOW, height=1, width=19, selectmode=SINGLE)
        self.__Is_Entered = False


    def join(self,event):
        some = self.__name_entry.get()
        self.__join_button.destroy()
        self.__cl.Enter_chat(some)
        self.__message_box.focus()
        self.__Is_Entered = True

    def send_message(self,event):
        message = self.__message_box.get("1.0", END)
        self.__cl.send(message)
        self.__message_box.delete("1.0", END)
    def receiving(self):
        while True:
            if self.__Is_Entered:
                reply = self.__cl.recive()
                self.__text_box.insert(END, reply + '\n')
            else:
                continue


    def place_and_bind(self):
        self.__text_box.place(x=20, y=50, height=250, width=350)
        self.__name_entry.grid(row=0, column=1, sticky='w')
        self.__message_box.place(x=20, y=350, height=40, width=350)
        self.__send_button.bind('<Button-1>', self.send_message)
        self.__join_button.bind('<Button-1>', self.join)
        self.__join_button.place(x=200, y=1)
        self.__send_button.place(x=375, y=350)
        self.__GUI_WINDOW.geometry('500x400')


    def start(self):
        looping_thread = Thread(target=self.__GUI_WINDOW.mainloop)
        recv_thread = Thread(target=self.receiving)
        looping_thread.start()
        recv_thread.start()
        looping_thread.join()
        recv_thread.join()


