import threading

class SesionUsuario:
    def __init__(self):
        self.nombre_usuario = None

    def iniciar_sesion(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def mostrar_sesion(self):
        print(f"Sesión iniciada para el usuario: {self.nombre_usuario}")

datos_sesion = threading.local()

def gestionar_sesion(nombre_usuario):
    datos_sesion.sesion = SesionUsuario()
    datos_sesion.sesion.iniciar_sesion(nombre_usuario)
    datos_sesion.sesion.mostrar_sesion()

def ejecutar_hilo(nombre_usuario):
    gestionar_sesion(nombre_usuario)

nombres_usuarios = ["Ana", "Carlos", "Beatriz", "David", "Elena"]

hilos = []
for nombre_usuario in nombres_usuarios:
    hilo = threading.Thread(target=ejecutar_hilo, args=(nombre_usuario,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()