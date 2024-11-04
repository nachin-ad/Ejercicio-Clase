import psutil

def listar_procesos(palabra_clave):
    # Lista para almacenar los procesos filtrados
    procesos_encontrados = []

    # Iteramos sobre todos los procesos en ejecución
    for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_info']):
        try:
            # Accedemos a los atributos del proceso
            pid = proc.info['pid']
            nombre = proc.info['name']
            memoria = proc.info['memory_info'].rss  # Uso de memoria en bytes

            # Filtramos por la palabra clave
            if palabra_clave.lower() in nombre.lower():
                procesos_encontrados.append((nombre, pid, memoria))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Manejo de excepciones: proceso no encontrado o acceso denegado
            continue

    # Mostramos los resultados
    if procesos_encontrados:
        print(f"Procesos que contienen '{palabra_clave}':")
        for nombre, pid, memoria in procesos_encontrados:
            print(f"Nombre: {nombre}, PID: {pid}, Uso de memoria: {memoria / (1024 ** 2):.2f} MB")
    else:
        print(f"No se encontraron procesos que contengan '{palabra_clave}'.")

def main():
    palabra_clave = input("Introduce la palabra clave para filtrar procesos: ")
    listar_procesos(palabra_clave)

if __name__ == "__main__":
    main()