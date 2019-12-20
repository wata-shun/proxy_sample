import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#プロキシサーバ(127.0.0.1:50008)とコネクション確立
soc.connect(('127.0.0.1', 50008))
while True:
    message = input("入力メッセージ:")
    #プロキシサーバへのメッセージ
    soc.sendall(message.encode('utf-8'))

    data = soc.recv(1024)
    print(repr(data))
