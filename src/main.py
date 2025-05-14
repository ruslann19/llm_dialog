from OpenRouterChat import OpenRouterChat

with open("OPENROUTER_API_KEY.txt", "r") as f:
    API_KEY = f.readline()

scammer_prompt = """
    Ты телефонный мошенник, но ты тщательно это скрываешь

    Тебе нужно узнать у меня код от моей бакнковской карты
    Придумай какую-нибудь историю, чтобы ты смог получить мои данные

    Пиши не очень длинные сообщения
"""

scammer = OpenRouterChat(
    api_key=API_KEY,
    model="meta-llama/llama-3-8b-instruct",
    system_prompt=scammer_prompt,
)

defencer_prompt = """
    Тебе позвонили, но ты подозреваешь, что это мошенник

    Постарайся вывести его на чистую воду
    Придумай, что ты будешь отвечать собеседнику, чтобы его раскусить

    Пиши не очень длинные сообщения
"""

defencer = OpenRouterChat(
    api_key=API_KEY,
    model="meta-llama/llama-3-8b-instruct",
    system_prompt=defencer_prompt,
)

defencer_response = "Алло? Кто это?"
print(f"defencer: {defencer_response}")

for _ in range(5):
    scammer_response = scammer.ask(defencer_response)
    print("-------------------------------")
    print(f"scammer: {scammer_response}")

    defencer_response = defencer.ask(scammer_response)
    print("-------------------------------")
    print(f"defencer: {defencer_response}")
