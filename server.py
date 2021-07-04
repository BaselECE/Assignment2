#Question one | multi threaded TCP Server/Client
#Server Side Code
import threading, socket  
s_t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port_num = 97
IP_Loop = '127.0.0.1'
s_t.bind((IP_Loop, Port_num)) #assign an IP address and port number to Server
s_t.listen(97) #server is listening to connections on port 97 | client accepted by server must connect to this port too.
print("server is ready to receive request from client")
print("server Wait a client connection ")
s_g = {'Basel':91, 'Majed':74, 'Yara':86, 'Hala':78, 'Ahmed':65} #creating dictionary includes students information
c_n = 0 #set initial value to c_n variable | c_n is number of clients that connect to this server
c_i = [] #put each client that connects to the server in a list called c_i | c_i contains all clients connected to the server.
def req_func (client_socket,clients,numofclient):
    #test if the 5th client has connected
    if c_n == 5:
        gi_win = "congrats ,you win (IP,Portnumber) of Previously accepted clients" + str(c_i)
        client_socket.send(gi_win.encode())
    else:
        client_socket.send(" ".encode())
    while True:
        try:
            s_n = client_socket.recv(2048).decode() #assign student name that sent by client to s_n variable
            if s_n =='exit':
                break
            else:
                print("Student is: ", s_n)
                s_r = s_g[s_n] #assign score of student that sent by client to s_r variable
                print("result is: ", s_r)
                client_socket.send(str(s_r).encode()) #send encoded information to client 
        except socket.error as rrr:
            print(rrr)
            # test if student information that sent by client not exist in s_g dictionary
        except KeyError as err: 
            print("Student information received are not exist in our dictionary")
            client_socket.send("Student info are not exist in server dictionary".encode())
    client_socket.close()
while True:
    client_socket, client_add = s_t.accept()
    c_i.append(client_add)
    c_n += 1
    thread = threading.Thread(target=req_func, args=(client_socket,c_i,c_n))
    thread.start()
