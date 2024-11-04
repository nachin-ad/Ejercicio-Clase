import subprocess
import time
import asyncio

def ejecutar_sincrono():
    start_time = time.time()
    print("Ejecutando Notepad.exe de manera síncrona...")
    subprocess.run(["notepad.exe"])
    end_time = time.time()
    print(f"Tiempo de ejecución síncrono: {end_time - start_time:.2f} segundos")

async def ejecutar_asincrono():
    start_time = time.time()
    print("Ejecutando Notepad.exe de manera asíncrona...")
    process = await asyncio.create_subprocess_exec("notepad.exe")
    await process.wait()
    end_time = time.time()
    print(f"Tiempo de ejecución asíncrono: {end_time - start_time:.2f} segundos")

def main():
    print("Elija el modo de ejecución:")
    print("1. Synchronous")
    print("2. Asynchronous")
    option = input("Ingress 1 o 2: ")

    if option == '1':
        ejecutar_sincrono()
    elif option == '2':
        asyncio.run(ejecutar_asincrono())
    else:
        print("Opción no válida. Por favor, elija 1 o 2.")

if __name__ == "__main__":
    main()
