import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=5005
BUFFER_SIZE=1024


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP,SERVER_PORT))
    sock_server.listen()
    print("in ascolto")
    while True:
        sock_service,addr=sock_server.accept()
        with sock_service as sock_client:
            while True:
                data=sock_client.recv(BUFFER_SIZE)
                print(data)
                if not data:
                    break
                data=data.decode()
                data=json.loads(data)
                primoNumero=data['primoNumero']
                operazione=data['operazione']
                secondoNumero=data['secondoNumero']
                print(primoNumero,secondoNumero,operazione)
                if operazione=="+":
                    ris=primoNumero+secondoNumero
                elif operazione=="-":
                    ris=primoNumero-secondoNumero
                elif operazione=="*":
                    ris=primoNumero*secondoNumero
                elif operazione=="/":
                    ris=primoNumero/secondoNumero
    
                ris=str(ris)
                print("risul:",ris)
                sock_client.sendall(ris.encode())
    