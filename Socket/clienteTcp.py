import socket
ip = '127.0.0.1'
porta = 12001
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketCliente.connect((ip,porta))
mensagem = raw_input("Digite uma mensagem: ")
socketCliente.send(mensagem)
resposta = socketCliente.recv(2048)
print resposta
socketCliente.close()