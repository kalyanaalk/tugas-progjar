import socket

def main():
    server_address = ('localhost', 45000)
    print(f"connecting to {server_address[0]} port {server_address[1]}")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    
    try:
        while True:
            message = input("Enter your message (TIME or QUIT): ")
            if message.upper() == 'QUIT':
                sock.sendall(b'QUIT\r\n')
                break
            elif message.upper() == 'TIME':
                sock.sendall(b'TIME\r\n')
                data = sock.recv(1024)
                print(f"Received: {data.decode('utf-8').strip()}")
            else:
                print("Invalid command. Use TIME or QUIT.")
    finally:
        print("closing socket")
        sock.close()

if __name__ == "__main__":
    main()
