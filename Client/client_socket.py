import socket

class Client:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 1234
        self.id = self.get_id()

    def get_id(self):
        self.server.connect((self.host, self.port))
        return self.server.recv(2048).decode()

    def get_data(self, player, bullets_rec, score, life):
        info = str(self.id) + ":" + str(player.x) + "," + str(player.y) + "," + str(bullets_rec) + "," + str(score.score) + "," + str(life.life_p1)
        
        self.server.send(info.encode())
        to_parse = self.server.recv(2048).decode()

        try:
            info = to_parse.split(":")[1].split(",")
            return int(info[0]), int(info[1])-player.height-400, int(info[2]), int(info[3]), int(info[4])
        except:
            return 0,0,0,0,0