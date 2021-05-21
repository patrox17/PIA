import funciones
from funciones import *
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, filename='main.log')


def menuFiltrado():

    while (True):
        opcion = input(
            "1.-Valor Hash \n2.-Ver Status powershell\n3.-Salir\n")

        if opcion == '1':
            valorhash()


        elif opcion == '2':
            verstatus()

        elif opcion == '3':
            break


        else:
            print("opcion invalida")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Herramientas de ciberseguridad')

    parser.add_argument('--hostname', dest='hostname',
                        help='URL Del Dominio".')

    # Argumentos para el envío de correo.
    parser.add_argument("--sender", "-s",
                        dest="sender",
                        type=str,
                        help="Correo del remitente GMAIL")

    parser.add_argument("--pswd", "-p",
                        dest="pswd",
                        type=str,
                        help="Contraseña del remitente")

    parser.add_argument("--receiver", "-r",
                        dest="receiver",
                        type=str,
                        help="Correo del destinatario")

    parser.add_argument("--asunto", "-a",
                        dest="asunto",
                        type=str,
                        help="Asunto del Correo")

    parser.add_argument("--msg", "-m",
                        dest="msg",
                        type=str,
                        help="Mensaje del Correo")

    # Argumentos para mensaje de texto.
    parser.add_argument("--SID", "-si",
                        dest="SID",
                        type=str,
                        help="ACCOUNT SID de Twilio")

    parser.add_argument("--autht", "-at",
                        dest="autht",
                        type=str,
                        help="AUTH TOKEN de Twilio")

    parser.add_argument("--num1", "-n1",
                        dest="num1",
                        type=str,
                        help="Numero Remitente (Twilio)")

    parser.add_argument("--dest1", "-d1",
                        dest="dest1",
                        type=str,
                        help="Numero Destinatario (Agrega el +52)")

    parser.add_argument("--dest1", "-t",
                        dest="text",
                        type=str,
                        help="Mensaje de texto")

    # Argumentos para Total Virus
    parser.add_argument("--filepath", "-fp",
                        dest="filepath",
                        type=str,
                        help="File Path al archivo excel con los link")

    parser.add_argument("--apikey", "-ak",
                        dest="apikey",
                        type=str,
                        help="Api Key de Total Virus")

    params = parser.parse_args()

    if params.filepath:
        scanweburls(params.filepath, params.apikey)

    if params.hostname:
        SocketInfo(params.hostn)

    if params.receiver:
        correo(params.sender, params.receiver, params.pswd, params.asunto, params.msg)

    if params.SID:
        mensajetxt(params.SID, params.autht, params.num1, params.dest1, params.text)

    else:
        menuFiltrado()
