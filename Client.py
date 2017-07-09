import socket

from time import sleep




class client:
    fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_ip = '127.0.0.1'
    udp_port = 54000
    Is_Entered = False
    NickName = ""

    def Enter_chat(self,some):
        self.NickName = some
        self.fd.sendto(self.NickName + " join the chat!", (self.udp_ip, self.udp_port))
        self.Is_Entered = True

    def send(self,message):
        self.fd.sendto(self.NickName+": "+ message, (self.udp_ip, self.udp_port))


    def recive(self):
        reply, addr = self.fd.recvfrom(1000)
        return reply



