import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=22005
BUFFER_SIZE=1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP,SERVER_PORT))
    print("connesso "+str(SERVER_IP)+" "+str(SERVER_PORT))
    primoNumero=float(input("primoNumero:"))
    operazione=input("inserisci l'operazione (+,-,*,%)")
    secondoNumero=float(input("inserisci il secondo numero"))
    messaggio={'primoNumero':primoNumero,
               'operazione':operazione,
               'secondoNumero':secondoNumero}
    messaggio=json.dumps(messaggio)
    sock_service.sendall(messaggio.encode("UTF-8"))
    data=sock_service.recv(1024)
    print("Risultato: ",data.decode())
    risposta=str(input("fare un altra operazione? si/no"))
