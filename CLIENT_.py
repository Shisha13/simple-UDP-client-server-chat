from Client_Window import Window

ip = "127.0.0.1"
port = 54000

if __name__ == '__main__':

    app = Window(ip,port)
    app.place_and_bind()
    app.start()