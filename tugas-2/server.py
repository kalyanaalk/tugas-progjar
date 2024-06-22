import socket
import threading
import logging
import pytz
from datetime import datetime

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.connection.recv(32)
            if data:
                logging.warning(f"[SERVER] received {data} from {self.address}")
                if data.startswith(b"TIME") and data.endswith(b"\r\n"):
                    current_time = datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%H:%M:%S')
                    response = f"JAM {current_time}\r\n".encode('utf-8')
                    logging.warning(f"[SERVER] sending {response} to {self.address}")
                    self.connection.sendall(response)
                elif data.startswith(b"QUIT") and data.endswith(b"\r\n"):
                    logging.warning(f"[SERVER] closing connection with {self.address}")
                    self.connection.close()
                    break
            else:
                self.connection.close()
                break

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 45000))
        self.my_socket.listen(1)
        logging.warning("Server started and listening on port 45000")
        while True:
            connection, client_address = self.my_socket.accept()
            logging.warning(f"connection from {client_address}")
            clt = ProcessTheClient(connection, client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    logging.basicConfig(level=logging.WARNING)
    svr = Server()
    svr.start()

if __name__ == "__main__":
    main()
