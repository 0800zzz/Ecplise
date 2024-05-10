#!/usr/bin/python3
import sys
import socket
from datetime import datetime

print("""
░▒▓████████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░ ░▒▓█▓▒░       ░▒▓█▓▒░ ░▒▓███████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░        
░▒▓██████▓▒░ ░▒▓█▓▒░       ░▒▓███████▓▒░ ░▒▓█▓▒░       ░▒▓█▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░   
░▒▓█▓▒░      ░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░       ░▒▓█▓▒░░▒▓█▓▒░        
░▒▓████████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░       ░▒▓████████▓▒░░▒▓█▓▒░░▒▓███████▓▒░ ░▒▓████████▓▒░ 
by 0800 (Use is under your responsibility. made for educational purposes)
""")

def escanear_puertos(host):
    try:
        puertos_abiertos = []
        total_puertos = 0

        print("*" * 50)
        print("Analizando el Objetivo: " + host)
        print("Análisis iniciado :" + str(datetime.now()))
        print("*" * 50)

        start_time = datetime.now()

        for port in range(1, 100):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                puertos_abiertos.append(port)
            total_puertos += 1
            s.close()

        print("\nResumen del escaneo:")
        print("Número total de puertos escaneados:", total_puertos)
        print("Puertos abiertos:", ", ".join(map(str, puertos_abiertos)) if puertos_abiertos else "No se encontraron puertos abiertos.")
        print("Duración del escaneo:", datetime.now() - start_time)

    except KeyboardInterrupt:
        print("\n Cerrando el Programa !!!")
        sys.exit()
    except socket.gaierror:
        print("\n El Nombre del host no puede ser resuelto!!!")
        sys.exit()
    except socket.error:
        print('\n Host No Responde!!!')
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        target = sys.argv[1]
    elif len(sys.argv) < 2:
        target = input("Introduce la IP del objetivo: ")
    else:
        print("Demasiados argumentos proporcionados. Por favor, solo proporcione la IP del objetivo.")
        exit()

    escanear_puertos(target)
