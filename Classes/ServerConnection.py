import socket
from Classes.Debugger import Debugger
from Classes.Connection import Connection

class ServerConnection:
    def __init__(self, address):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create the socket
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)    # Prevent "Address already in use" error
        self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)    # Remove delay 
        self.setupConnection(address)

    def setupConnection(self, address):
        self.server.bind(address)
        Debugger.info("Listening for new connection...")
        while True:
            self.server.listen() # Listen for new connections
            socket, address = self.server.accept()
            Debugger.info(f"New connection with address {address[0]} on port {address[1]}")
            Connection(socket, address).start()