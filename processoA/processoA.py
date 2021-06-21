import paho.mqtt.client as mqtt
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


listaA = " "
teste = []

## Novas variaveis ##
valores = []
teste2 = []
op = ""
valorAplicar = 0


def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe ("vetorA")
        client.subscribe ("operacaoA")
        client.publish ("novaOperacao", "start")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg): 
    # print(msg.topic+" >>> "+str(msg.payload))
    listaA = str(msg.payload)
    teste.append(listaA)

    if (len(teste) >= 2):
        client.disconnect()

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect ("172.17.0.1", 1883, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()


print("Array Recebido:")
print(teste)
print("_____________________")

arrayValores = teste[0]
operacoes = teste[1]

arrayValores = arrayValores.replace('b', '')
arrayValores = arrayValores.replace("'", '')
arrayValores = arrayValores.replace('[', '')
arrayValores = arrayValores.replace(']', '')
arrayValores = arrayValores.replace(',', '')

teste2 = arrayValores.split()

print("Array Limpo: ")
print("Tamanho do Array Limpo: ", len(teste2))
print(teste2)
print("_____________________")

operacoes = operacoes.replace('b', '')
operacoes = operacoes.replace("'", '')

print("Operação: ", operacoes)

if "/" in operacoes:
    op = "/"
    operacoes = operacoes.replace("/", '')
elif "+" in operacoes:
    op = "+"
    operacoes = operacoes.replace("+", '')
elif "*" in operacoes:
    op = "*"
    operacoes = operacoes.replace("*", '')
elif "-" in operacoes:
    op = "-"
    operacoes = operacoes.replace("-", '')
else:
    op = "^"
    operacoes = operacoes.replace("^", '')

valorAplicar = int(operacoes)

print("Valor aplicar: ", valorAplicar)
print("_______________________________")

for i in range(len(teste2)):
    teste2[i] = int(teste2[i])

if (op == "+"):
    for i in range(len(teste2)):
        teste2[i] += valorAplicar
elif (op == "-"):
    for i in range(len(teste2)):
        teste2[i] -= valorAplicar
elif (op == "*"):
    for i in range(len(teste2)):
        teste2[i] *= valorAplicar
elif (op == "/"):
    for i in range(len(teste2)):
        teste2[i] /= valorAplicar
else:
    for i in range(len(teste2)):
        teste2[i] = (teste2[i] ** valorAplicar)


print("Tamanh do Resultado final: ", len(teste2))
print("Resultado Final: ")
# teste2.append("break")
print(teste2)

for i in range(len(teste2)):
    teste2[i] = str(teste2[i])

while True:
    for i in range(len(teste2)):
        mensagem_envio = "x" + teste2[i]
        cliente.sendto(mensagem_envio.encode(), ("172.17.0.3", 33000))
        mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)

    break
