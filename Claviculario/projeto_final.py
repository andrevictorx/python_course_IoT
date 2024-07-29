import paho.mqtt.client as mqtt
import time
import json
import mariadb
from email.mime.text import MIMEText
from datetime import datetime
import os
import smtplib

chaves = [26,28]

def enviar_email():
        smtpObj.sendmail("",'receiver@mail.com', '''Subject: Claviculario \n\n Retirada da chave {} \n\n Dia e Horario: {} \n\n Colaborador: {}, \n\n Favor verificar.'''.format((str(resp[0][1])), (str(resp[0][3])),(str(resp[0][0]))))
        print('Email enviado com sucesso!')

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Cliente conectado ao Broker!\n")
        try:
            client.subscribe("Treinamento/ets/Projeto", qos=0)
            print("Cliente inscrito no tópico!\n")
        except:
            print("Não foi possível inscrever o cliente no tópico\n")
    else:
        print("Cliente não conectado ao Broker.\n")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Cliente disconectado do Broker inesperadamente.\n")  


def on_message(client, userdata, msg):
    payload = str(msg.payload.decode('utf-8'))
    n = 53
    payload = payload.replace('\r\n',"")
    chunks = [payload[i:i+n] for i in range (0, len(payload), n)]
    print(chunks)
    print(len(chunks))
    for i in range(len(chunks)):
        payload=chunks[i]
        payload=payload.strip('\r\n')
        msgTopic = str(msg.topic)
        print(payload + "\n")

        # separa parâmetros do payload
        jsonPayload = json.loads(payload)
        
        
        id_arduino = jsonPayload['id_arduino']
        edv = jsonPayload['RFID']
        key= jsonPayload['key']
        state = jsonPayload['state']
        data_hora = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        global con
        con = mariadb.connect(user='root',
                              password='************',
                              host='localhost',
                              port=3306,
                              database='claviculario')
        cursor = con.cursor()
                   
        try:
            #INSERE DADOS NO BANCO DE DADOS
            cursor.execute(
            "INSERT INTO chaves (id_arduino, rfid, chave_usada, pega_devolvida, data_hora) VALUES (?, ?, ?, ? ,?)", 
            (id_arduino, edv, key, state, data_hora))
            con.commit()
            print("Dados inseridos no banco com sucesso!") 
                  
        except mariadb.Error as e: 
            print(f"Error: {e}")
               


broker_address='broker.hivemq.com'
broker_port=1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
print("Conectando ao Broker")
client.connect(broker_address, broker_port)
time.sleep(0.5)
while 8 <= datetime.now().hour <= 17:
    client.loop_start()
    if str(datetime.now().strftime("%H:%M:%S")) == "17:06:00":
        client.loop_stop()
        con = mariadb.connect(user='root',
        password='**********',
        host='localhost',
        port=3306,
        database='claviculario')
        #CONECTA NO EMAIL
        Senha= '**********'
        email="your_mail@mail.com"
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(email , Senha)
        for i in range (len(chaves)):
            query = "SELECT rfid, chave_usada, pega_devolvida, data_hora FROM chaves WHERE chave_usada = {} ORDER BY id DESC LIMIT 1".format(chaves[i])
            cursor = con.cursor()
            cursor.execute(query)
            resp = list(cursor)
            print(resp)
            if resp[0][2] == 0:
                enviar_email()
        smtpObj.quit()

