from MyServ import*


ip = "127.0.0.1"
port = 54000


if __name__ == '__main__':
    SERVER = MyServ(ip,port)
    SERVER.start()



