import socket






class client:
    def __init__(self,ip,port):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udp_ip = ip
        self._udp_port = port
        self._Is_Entered = False
        self._NickName = ""


    def Enter_chat(self,some):
        self._NickName = some
        self._sock.sendto(self._NickName + " join the chat!", (self._udp_ip, self._udp_port))
        self._Is_Entered = True

    def send(self,message):
        self._sock.sendto(self._NickName + ": " + message, (self._udp_ip, self._udp_port))


    def recive(self):
        reply, addr = self._sock.recvfrom(1000)
        return reply


