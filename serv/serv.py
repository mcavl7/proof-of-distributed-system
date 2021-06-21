import paho.mqtt.client as mqtt
import socket
from requests import get

meuip = get("https://api.ipify.org").text
meuhost = socket.gethostname()
meuipinterno = socket.gethostbyname(meuhost)
print(meuip)
print(meuhost)
print(meuipinterno)

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("", 33000))

client = mqtt.Client()
client.connect("172.17.0.1", 1883, 60)

lista = []
listaA = []
listaB = []

while True:
    mensagem_bytes, endereco_ip_cliente = servidor.recvfrom(2048)

    mensagem_resposta = mensagem_bytes.decode()

    servidor.sendto(mensagem_resposta.encode(), endereco_ip_cliente)

    msg = mensagem_resposta
    
    if (msg == "break"):
        break
    else:
        lista.append(msg)


print("Sai do loop")
for i in range(len(lista)):
    if "x" in lista[i]:
        v = lista[i].replace('x', '')
        listaA.append(v)
    else:
        listaB.append(lista[i])


resultadoA = []
resultadoB = []

for i in range(len(listaA)):
    soma = int(listaA[i]) + int(listaB[i])
    resultadoA.append(soma)


for i in range(len(listaB)):
    dif = int(listaA[i]) - int(listaB[i])
    resultadoB.append(dif)


strResultadoA = str(resultadoA)
strResultadoB = str(resultadoB)


client.publish("soma", strResultadoA)
client.publish("diferenca", strResultadoB)
