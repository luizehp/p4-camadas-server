from funcao import *
from enlace import *
import numpy as np
import time

""" class Server:

    def __init__(self, porta: str, id:int) -> None:
        self.porta= porta
        self.id=id
        self.qnt_payloads=0
        self.n=0

        """ """ try:
            self.com = enlace(self.porta)
            self.com.enable()
            #self.recebeByteSacrificio()
            #self.enviaByteSacrificio()
        except Exception as erro:
            print("ops! :-\\")
            print(erro)
            self.com.disable() """ """ """
        



def recebeDatagrama( msg: bytearray, id_arquivo:int, id:int, n:int, qnt_payloads:int):
    int_list = [int(byte) for byte in msg]
    head = int_list[0:10]
    payload = int_list[10:125]
    eop = int_list[-4:]
    recebeu=False
    rsp=b""
    if head[0] == 1 and head[1] == id and head[5]==id_arquivo and n==0:
        print("*******Início handshake*******")
        rsp=[0]*10
        rsp[0]=2
        resp=bytes(resp)
        resp+=b'\xAA\xBB\xCC\xDD'
        qnt_payloads=head[3]
        recebeu=True
    elif head[0]==3 :
        if eop == [170,187,204,221]:
            if head[3]==qnt_payloads:
                if n==head[4]:
                    if head[5]==len(payload):
                        rsp=[0]*10
                        rsp[0]=4
                        rsp[7]=n
                        resp=bytes(resp)
                        resp+=b'\xAA\xBB\xCC\xDD'   
                        recebeu=True              
    return rsp,recebeu


            
       

    """ def enviaByteSacrificio(self) -> None:
        print('Enviando byte de sacrificio')
        self.com.sendData(np.asarray(b'x00'))    #enviar byte de lixo
        time.sleep(.05)
        self.com.rx.clearBuffer()

    
    def recebeByteSacrificio(self) -> None:
        print("Esperando byte de sacrifício")
        rxBuffer, nRx = self.com.getData(1)
        print("RECEBEU")
        time.sleep(.05)
        self.com.rx.clearBuffer() """

    """ def clearbuffer(self):
        self.com.rx.clearBuffer()
    def sendata(self,array):
        self.com.sendData(array)
    def getdata(self,tamanho):
        rxBuffer, nRx=self.com.getData(tamanho)
        return rxBuffer, nRx """

   # def enviaDatagrama(self, id_arquivo: int):
        
    """ def getFeedback(self, n: int):
        rxBuffer, nRx, check = self.com.getData_teste(n)
        return rxBuffer, nRx, check """
            


#   h0 – Tipo de mensagem.
#   h1 – Se tipo for 1: número do servidor. Qualquer outro tipo: livre
#   h2 – Livre.
#   h3 – Número total de pacotes do arquivo.
#   h4 – Número do pacote sendo enviado.
#   h5 – Se tipo for handshake: id do arquivo (crie um para cada arquivo). Se tipo for dados: tamanho do payload.
#   h6 – Pacote solicitado para recomeço quando a erro no envio.
#   h7 – Ùltimo pacote recebido com sucesso.
#   h8 – h9 – CRC (Por ora deixe em branco. Fará parte do projeto 5).
#   PAYLOAD – variável entre 0 e 114 bytes. Reservado à transmissão dos arquivos.
#   EOP – 4 bytes: 0xAA 0xBB 0xCC 0xDD.


#cria_pacotes_4(b'\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef'*10)
