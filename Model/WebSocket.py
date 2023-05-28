from websocket_server import WebsocketServer
from threading import Thread


class WebSocket:
    def __init__(self, receiveCallback):
        HOST = "127.0.0.1"
        PORT = 5587

        self.receiveCallback = receiveCallback

        self.server = WebsocketServer(HOST, PORT)
        self.server.set_fn_new_client(self.newClient)
        self.server.set_fn_client_left(self.clientLeft)
        self.server.set_fn_message_received(self.messageReceived)

    # Called for every client connecting (after handshake)
    def newClient(self, client, server):
        # print("New client connected and was given id %d" % client['id'])
        # server.send_message_to_all("Hey all, a new client has joined us")
        pass

    # Called for every client disconnecting
    def clientLeft(self, client, server):
        # print("Client(%d) disconnected" % client['id'])
        pass

    # Called when a client sends a message
    def messageReceived(self, client, server, message):
        self.receiveCallback(message)

        # if len(message) > 200:
        #     message = message[:200]+'..'
        # print("Client(%d) said: %s" % (client['id'], message))
        # server.send_message_to_all("Client(%d) said: %s" % (client['id'], message))

    def run(self):
        t = Thread(target=self.server.run_forever)
        t.start()


if __name__ == "__main__":
    def printMSG(msg):
        print(f"PRINT MSG {msg}")

    obj = WebSocket(printMSG)
