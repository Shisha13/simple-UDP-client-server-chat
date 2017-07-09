import socket


class MyServ:
    udp_ip = '127.0.0.1'
    udp_port = 54000
    fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    fd.bind((udp_ip, udp_port))
    list_of_clients = set()

    def start(self):
        while True:
            data,client_address = self.fd.recvfrom(1024)
            self.list_of_clients.add(client_address)
            print(data)
            for addr in self.list_of_clients:
                self.fd.sendto(data, addr)




SERVER = MyServ()
SERVER.start()


