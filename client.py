#Question one | multi threaded TCP Server/Client
#Client Side Code
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_Loop = '127.0.0.1'
Port_num = 97
client.connect((IP_Loop ,Port_num))

gi_win = client.recv(2048).decode()
print(gi_win)

while True:
    s_t = input("type the student name: ")
    client.send(s_t.encode()) #send encoded name of student to server
    if s_t == 'exit':
        break
    mesg = client.recv(2048).decode()
    print("score of "+s_t+" is: ", mesg)

client.close()
