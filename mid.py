import socket
#プロキシサーバ
soc_mid_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc_mid_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#clientに対してサーバとして振る舞う
soc_mid_client.bind(('127.0.0.1', 50008))
soc_mid_client.listen(1)

#server (127.0.0.1:50007)とコネクション確立
soc_mid_server.connect(('127.0.0.1', 50007))

while True:
    #mid client間のコネクション
    conn_mid_client, addr_client = soc_mid_client.accept()
    while True:
        #clientからのデータ
        data_mid_client = conn_mid_client.recv(1024)
        if not data_mid_client:
            break
        print('data:{}\naddr:{}'.format(data_mid_client, addr_client))
        #clientからのデータをserverに送り返す
        soc_mid_server.sendall(data_mid_client)
        #データを受け取れたことをclientに返す
        conn_mid_client.sendall(b'Received im mid')
        
        #サーバからのデータを受け取る
        data_mid_server = soc_mid_server.recv(1024)
        print(repr(data_mid_server))