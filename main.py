import requests
import argparse

banner = """ __          __     ______ ______ _      ______      _____ _____ 
 \ \        / /\   |  ____|  ____| |    |  ____|    / ____/ ____|
  \ \  /\  / /  \  | |__  | |__  | |    | |__ _____| (___| (___  
   \ \/  \/ / /\ \ |  __| |  __| | |    |  __|______\___ \\___ \ 
    \  /\  / ____ \| |    | |    | |____| |____     ____) |___) |
     \/  \/_/    \_\_|    |_|    |______|______|   |_____/_____/  

Waffle-SS is another tool to search for subdomains using a public API.                                                                                                                             
"""
api = "https://api.subdomain.center/?domain=" 

def buscar_subdominios(u):
    r = requests.get(api + u, headers={'Accept': 'application/json'})
    lista = list(r.json())
    print(f"Los subdominios del dominio {u} son: ")
    for i in lista:
        print(i)
    guardar_subdominios(u, lista)


def guardar_subdominios(u, lista):
    respuesta = input("¿Deseas guardar los subdominios en un archivo? (Ingrese Y/N): ")
    if respuesta.lower() == "y":
        with open(u+".txt","w") as f:
          for i in lista:
               f.write(i+"\n")
    elif respuesta.lower() == "n":
        pass
    else:
        print("La opción que ingresaste no es valida :c\n")
        guardar_subdominios(u, lista)

print(banner.rstrip(), "\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Ingresa el dominio que deseas escanear (ejemplo.com)")
    parser.add_argument("-f", "--file", help="Ingresa la ruta del archivo con los dominios a escanear")
    args = parser.parse_args()

    if args.url:
        buscar_subdominios(args.url)
    elif args.file:
        with open(args.file, "r") as f:
            data = f.readlines()
            for i in data:
                buscar_subdominios(i.strip())
                if i != data[-1]:
                    print("\n" + "*"*50)
                
    else:
        parser.print_help()
        exit()

main()