import socket
import time 
import pickle 

#defining constants 
SERVER = '3.87.195.49'
PORT = 11111
ADDR = (SERVER, PORT) 
DISCONNECT_MESSAGE = '!disconnect' 


def recv_msg(server):
    data, addr = server.recvfrom(1024) 
    data = data.decode('utf-8')
    return data, addr

def send_msg(server, msg, address): 
    msg = bytes(msg.encode('utf-8'))
    server.sendto(msg, address)

def parseandsend(msg):
    
    tokens=msg.split()
    
    #x value
    xaxis_val= tokens[1]
    dec_val = int(xaxis_val, 16)
    #left
    if (112<dec_val<10000):
        horizontal= '-1'
    #right
    elif (10000<dec_val<4294967184):
        horizontal= '1'
    else:
        horizontal= '0'

    #y value
    yaxis_val= tokens[2]
    dec_val = int(yaxis_val, 16)
    #jump
    if (150<dec_val<10000):
        jump= '1'
    else:
        jump= '0'

    button_val=tokens[4]
    dec_val = int (button_val,16)
    if (dec_val==0):
        button ='0'
    elif (dec_val ==1):
        button ='1'
    elif(dec_val==2):
        button ='2'
    else:
        button ='3'
    


    if (tokens[0]=="P1"):
        data= horizontal + " " + jump + " 0 " + button
        file=open("playercontroltext1.txt",'w')
        file.write(data)
        file.close()
        file=open("playercontroltext1.txt",'r')
    
    elif(tokens[0]=="P2"):
        data= horizontal + " " + jump + " 0 " + button
        file=open("playercontroltext2.txt",'w')
        file.write(data)
        file.close()
        file=open("playercontroltext2.txt",'r')


print("[STATUS]Client starting...")
client_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"[STATUS] Connected to server at {SERVER} on {PORT}")

msg = ""
send_msg(client_server, "computer", ADDR) 
connected = True
while True:
    msg, address = recv_msg(client_server)
    print(msg)
    parseandsend(msg)
    