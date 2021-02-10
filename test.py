import socket
import sys
import datetime

import select
''' IP to Verisign Server, I currently don't have access
     to the Shared Registry System so the following 
    will be pseudocode until I get access.
    99.41.162.30
'''
#.com Server
server = "192.5.6.30"

#IP4 & TCP Connection
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()
try:
    x = input("Please enter in domain name: ")
    ip_x = socket.gethostbyname(x)
    print(ip_x)
    #Username and password for server.
    user = input("Please input username: ")
    passw = intput("Please input Password: ")
    #key for accessing root server.
    key = "superman2"
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
s.connect((server, 80))
s.setblocking(False)
res = s.recv(2048)
print(res.decode())
s.sendall(user.encode("utf-8"))
res_user = s.recv(2048)
print(res_u.decode())
s.sendall(passw.encode("utf-8"))
res_pass = users.recv(2048)
print(res_pass.decode())
s.sendall(key.encode())
recv_key = s.recv(2048)
print(recv_key.decode())

# go to page with the download file.
fileloc = "https://www.iana.org/domains/root/db/com.html"
send = "GET / HTTP/1.1\r\n Host:%s\r\n\r\n" % fileloc
s.senddall(send.encode())
with open('res_file', 'wb') as f:
    print("file opened")
    while True:
        print("receiving data...")
        data = s.recv(1024)
        if not data:
            break
        # write data to a file
        f.write(data)
#Parse data from file by finding expire.
searchfile = open("resfile", "r")
l = []
for line in searchfile:
    if ip_x in line:
        l = line

for x, i in enumerate(l):
    if x == "expire":
        p=str(l[x+1]))
        obj_time = datetime.datetime.strptime(p,"%Y-%m-%d %H:%M:%S.%f")
        print(obj_time)
searchfile.close()

s.close()
