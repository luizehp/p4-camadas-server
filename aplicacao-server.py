#####################################################
# Camada Física da Computação
#Carareto
#11/08/2022
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
from funcao import *
import time
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                   # Windows(variacao de)


def main():
    try:
        print("Iniciou o main")
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.

        print("esperando 1 byte de sacrifício")
        rxBuffer, nRx = com1.getData(1)
        print("RECEBEU")
        
        com1.rx.clearBuffer()
        time.sleep(.05)
        

        #server = Server(serialName,1)
        
        erro=False
        n=1
        while True:
            msg=b""
            print("esperando pacote")
            rxBuffer, nRx = com1.getData(10)
            time.sleep(.05)
            print("=========HEAD=========")
            print(rxBuffer)
            msg+=rxBuffer
            int_list = [int(byte) for byte in rxBuffer]

            tamanho=int_list[5]
            if int_list[0]!=1:
                rxBuffer, nRx = com1.getData(tamanho)
                time.sleep(.05)
                print("=========PAYLOAD=========")
                print(rxBuffer)
                msg+=rxBuffer
            rxBuffer, nRx = com1.getData(4)
            time.sleep(.05)
            print("=========EOP=========")
            print(rxBuffer)
            msg+=rxBuffer
            resposta,recebeu=recebeDatagrama(msg,1,1,n,int_list[3])
            if recebeu:
                n+=1
            print("+++++ENVIA+++++")
            print(resposta)
            com1.sendData(resposta)
            time.sleep(.05)


        


        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
