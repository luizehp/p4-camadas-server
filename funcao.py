from enlace import *
import numpy as np
import time
from crc import Calculator, Crc16
import crcmod




def recebeDatagrama( msg: bytearray, id_arquivo:int, id:int, n:int, qnt_payloads:int, timeout):
    resp=b""
    #calculator = Calculator(Crc16.CCITT)
    crc16 = crcmod.predefined.Crc('crc-16')
    if timeout:
        resp=[0]*10
        resp[0]=4
        resp=bytes(resp)
        resp+=b'\xAA\xBB\xCC\xDD'
        return resp

    int_list = [int(byte) for byte in msg]
    head = int_list[0:10]
    

    eop = int_list[-4:]
    ocioso=True
    recebeu=False
    erro=False

    if head[0] == 1 and head[1] == id and head[5]==id_arquivo and n==1:
        print("*******Início handshake*******")
        resp=[0]*10
        resp[0]=2
        resp=bytes(resp)
        resp+=b'\xAA\xBB\xCC\xDD'
        qnt_payloads=head[3]
        ocioso=False
        return resp,ocioso,recebeu,erro
    
    payload = msg[10:]
    payload = payload[:-4]

    """ crc16.update(bytes(payload))
    crc_value = crc16.crcValue
    print("CRC",crc_value)
    byte_array = int.to_bytes(crc_value, 2, byteorder='big') """
    #print("PAYLOAD=",payload)
    byte_array= __criaCRC (payload)
    int_crc = [int(byte) for byte in byte_array]
    #print(byte_array, int_crc, head[8],head[9])

    if (head[0]!=3) or (eop != [170,187,204,221]) or (head[3]!=qnt_payloads) or (n!=head[4]) or (int_crc[0]!=head[8]) or (int_crc[1]!=head[9]):
        print("PACOTE ERRO")
        resp=[0]*10
        resp[0]=6
        resp[6]=n
        resp=bytes(resp)
        resp+=b'\xAA\xBB\xCC\xDD'   
        #recebeu=True 
        erro=True
    else:
        print("PACOTE OK")
        """ print("CALCULO",bytes(calculator.checksum(bytes(payload))))
        expected=bytes([head[8],head[9]])
        #if expected == calculator.checksum(bytes(payload)):
            #print("CRC OK") """
        resp=[0]*10
        resp[0]=4
        resp[7]=n
        resp=bytes(resp)
        resp+=b'\xAA\xBB\xCC\xDD'   
        recebeu=True  
    
    return resp,ocioso,recebeu,erro

            

def __criaCRC(payload: bytearray):
        crc16 = crcmod.predefined.Crc('crc-16') 
        crc16.update(bytes(payload))
        crc_value = crc16.crcValue
        byte_array = int.to_bytes(crc_value, 2, byteorder='big')
        return byte_array
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
