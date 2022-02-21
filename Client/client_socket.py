from distutils.log import error
import socket

class Client:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 1234
        self.address = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        self.server.connect(self.address)
        return self.server.recv(2048).decode()

    def send(self, data):
        try:
            to_send = str(data)
            self.server.send(to_send.encode())
            recived = self.server.recv(2048).decode()
            return recived
            
        except socket.error as e:
            return str(e)

    def get_data(self, player, bullets_rec):
        to_send = str(self.id) + ":" + str(player.x) + "," + str(player.y) + "," + str(bullets_rec)
        data = self.send(to_send)
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])-player.height-400, int(d[2])
        except:
            return 0,0,0