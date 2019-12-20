# socket サーバを作成
import socket

#アドレス、ポートの設定
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('127.0.0.1', 50007))
soc.listen(1)

while True:
    #誰かがアクセスしてきたら、コネクションを確立
    conn, addr = soc.accept()
    while True:
        #データを受け取る
        data = conn.recv(1024)
        if not data:
            break
        print('data:{}\naddr:{}'.format(data, addr))
        #受け取れたら送信元に返す
        conn.sendall(b'Received ' + data)