import socket,pygame,Sgeneration,json,io
from _thread import *
import pickle
pygame.init()
Sgeneration.init()
#gameDisplay = pygame.display.set_mode((550,550))
ip = "0.0.0.0"
port  = 1500
buff = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,port))
global humans,cubes
cubes = Sgeneration.cubes.list
humans = []
def oof():
    None
def threaded_client(conn):
    try:
        while True:
            g = conn.recv(buff).decode("utf-8")
            if "PC " in g: #Pixel Change
                g = g.replace("PC ","")
                m = g.split("|")
                c = m[1].split(",")
                Sgeneration.generate.change((int(c[0]),int(c[1]),int(c[2])),int(m[0]))
                print(g)
                for x in humans:
                    x.send(g.encode())
            pygame.display.update()
            #data = conn.recv(buff)
                    
            #g=  pickle.loads(data) #color,index0
            #cubes[g[1]][2] = g[0]
    except:
        humans.remove(conn)
        print("{} left".format(str(len(humans)+1)))
def  stuffs():
    while True:
        #cubes = Sgeneration.cubes.list
        s.listen()
        conn,data = s.accept()
        if not conn in humans:
            humans.append(conn)
            conn.send(str(len(Sgeneration.cubes.list)).encode())
            for x in range(len(Sgeneration.cubes.list)):
                conn.send((str(x)+"|"+str(Sgeneration.cubes.list[x][2][0]) + ","  + str(Sgeneration.cubes.list[x][2][1]) + "," + str(Sgeneration.cubes.list[x][2][2])).encode())
                data = conn.recv(buff).decode("utf-8")
            start_new_thread(threaded_client,(conn,))
        Sgeneration.generate.draw(gameDisplay)
        pygame.display.update()
stuffs()
