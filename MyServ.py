import socket




class MyServ:
    def __init__(self,ip,port):
        self._udp_ip = ip
        self._udp_port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((self._udp_ip, self._udp_port))
        self._list_of_clients = set()



    def start(self):
        while True:
            data,client_address = self._sock.recvfrom(1024)
            self._list_of_clients.add(client_address)
            for addr in self._list_of_clients:
                self._sock.sendto(data, addr)




