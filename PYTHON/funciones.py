import smtplib
import ssl
import sys
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from re import search
import socket
import csv
from twilio.rest import Client
import requests
import time
import json
import pandas
import hashlib
import os
from configparser import ConfigParser
import subprocess
import nmap


def SocketInfo(hostname):
    print("=== Inicio de la aplicacion SocketInfo... ===\n")
    try:
        info = socket.gethostbyname_ex(hostname)
        print("Info del dominio: " + str(info))
        print("\nResultados de buscar este dominio en Google: ")
        query = info[0]
        for enlace in search(query, tld="com", num=10, stop=10, pause=2):
            print(enlace)
        print("\n=== Fin de la busqueda ===")
    except:
        traceback.print_exc(file=sys.stdout)
        print("\nLINK INVALIDO. No se pudo analizar ningun host.")

def correo(sender,reciever,passw,asunt,mens):

    print("Correo Remitente (GMAIL)")
    sender_email = sender
    print("Correo Destinatario (GMAIL)")
    receiver_email = reciever
    password = passw

    message = MIMEMultipart("alternative")
    print("asunto")
    message["Subject"] = asunt
    message["From"] = sender_email
    message["To"] = receiver_email
    # Create the plain-text and HTML version of your message
    text = mens
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def mensajetxt(sid,autht,number,destcell,msg1):
    accountSID = sid
    authToken = autht

    twilioCli = Client(accountSID, authToken)

    myTwilioNumber = number

    destCellPhone = destcell

    msg = msg1

    message = twilioCli.messages.create(to=destCellPhone, from_=myTwilioNumber, body=msg)

def scanweburls(filepath,apikey):
    print("links extraídos de archivo Excel")

    file_path = str(filepath)
    domain_CSV = pandas.read_csv((file_path))

    Urls = domain_CSV['Domain'].tolist()


    API_key = apikey
    url = 'https://www.virustotal.com/vtapi/v2/url/report'

    parameters = {'apikey': API_key, 'resource': Urls}

    response = requests.get(url=url, params=parameters)
    json_response = json.loads(response.text)

    for i in Urls:
        parameters = {'apikey': API_key, 'resource': i}

        response = requests.get(url=url, params=parameters)
        json_response = json.loads(response.text)

        if json_response['response_code'] <= 0:
            with open('not Found result.txt', 'a')  as notfound:
                notfound.write(i) and notfound.write("\tNOT found please Scan it manually\n")
        elif json_response['response_code'] >= 1:

            if json_response['positives'] <= 0:
                with open('Virustotal Clean result.txt', 'a')  as clean:
                    clean.write(i) and clean.write("\t NOT malicious \n")
            else:
                with open('Virustotal Malicious result.txt', 'a')  as malicious:
                    malicious.write(i) and malicious.write("\t Malicious") and malicious.write(
                        "\t this Domains Detectd by   " + str(json_response['positives']) + "  Solutions\n")

        time.sleep(15)



def valorhash():
    archivo = "config.ini"

    config = ConfigParser()
    config.read(archivo)

    def hash_file(filename):
           """"Esta Funcion regresa el valor hash md5 del path que se le pase por los parametros"""

           # crea el objeto hash
           h = hashlib.md5()
           archivo = "config.ini"

           config = ConfigParser()
           config.read(archivo)

           # abre el archivo para lectura en modo binario
           with open(filename,'rb') as file:

               # cicla hasta que termine el archivo
               chunk = 0
               while chunk != b'':
                   # Lee solo 1024 bytes
                   chunk = file.read(1024)
                   h.update(chunk)

            #d
           return h.hexdigest()

    message1 = hash_file(config.get('Rutas','ruta1'))
    message2 = hash_file(config.get('Rutas','ruta2'))
    message3 = hash_file(config.get('Rutas','ruta3'))
    message4 = hash_file(config.get('Rutas','ruta4'))
    message5 = hash_file(config.get('Rutas','ruta5'))

    filename1 = os.path.basename(config.get('Rutas','ruta1'))
    filename2 = os.path.basename(config.get('Rutas','ruta2'))
    filename3 = os.path.basename(config.get('Rutas','ruta3'))
    filename4 = os.path.basename(config.get('Rutas','ruta4'))
    filename5 = os.path.basename(config.get('Rutas','ruta5'))


    resultados = open("resultado.txt","w")
    resultados.write(filename1 +" "+" "+ message1)
    resultados.write("\n" + filename2 +" "+" "+ message2)
    resultados.write("\n" + filename3 +" "+" "+ message3)
    resultados.write("\n" + filename4 +" "+" "+ message4)
    resultados.write("\n" + filename5 +" "+" "+ message5)
    resultados.close()


def portscan():

    begin = 78
    end = 80

    target = '192.168.50.222'

    nm = nmap.PortScanner()

    for i in range(begin, end + 1):

        res = nm.scan(target, str(i))
        res = res['scan'][target]['tcp'][i]['state']

        print(f'port {i} is {res}.')

        for host in nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                lport = nm[host][proto].keys()

                for port in lport:
                    print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    host_data = []

    csv_file = open('scan.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_header = ['Protocol', 'Port', 'Service']
    csv_writer.writerow(csv_header)
    for port in lport:
        csv_writer.writerow(port)

    csv_file.close()


def verstatus():
    comando = "Ver-StatusPerfil"
    lineaPS = "powershell -Executionpolicy ByPass -Command " + comando
    runningProcesses = subprocess.check_output(lineaPS)
    print(runningProcesses.decode())


