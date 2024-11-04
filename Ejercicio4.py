import ftplib
import pyperclip
import time
import subprocess
import os



def descargar_archivo():
    try:
        # Conectar al servidor FTP
        ftp = ftplib.FTP(FTP_SERVER)
        ftp.login(FTP_USER, FTP_PASS)
        print(f"Conectado a {FTP_SERVER}")

        # Descargar el archivo
        with open(FILE_TO_DOWNLOAD, 'wb') as f:
            ftp.retrbinary(f'RETR {FILE_TO_DOWNLOAD}', f.write)
        print(f"Archivo {FILE_TO_DOWNLOAD} descargado.")

        # Cerrar la conexión FTP
        ftp.quit()
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")


def copiar_al_portapapeles():
    try:
        with open(FILE_TO_DOWNLOAD, 'r') as f:
            contenido = f.read()
            pyperclip.copy(contenido)
            print("Contenido copiado al portapapeles.")
    except Exception as e:
        print(f"Error al copiar al portapapeles: {e}")


def verificar_portapapeles(contenido_anterior):
    while True:
        time.sleep(2)  # Esperar 2 segundos antes de verificar
        contenido_actual = pyperclip.paste()
        if contenido_actual != contenido_anterior:
            print("¡El contenido del portapapeles ha cambiado!")
            contenido_anterior = contenido_actual
    return contenido_anterior


def main():
    descargar_archivo()
    copiar_al_portapapeles()

    # Obtener el contenido inicial del portapapeles
    contenido_inicial = pyperclip.paste()
    print("Esperando cambios en el portapapeles...")

    # Iniciar la verificación del portapapeles
    verificar_portapapeles(contenido_inicial)


if __name__ == "__main__":
    main()
