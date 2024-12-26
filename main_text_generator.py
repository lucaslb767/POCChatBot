import  openai
client = openai.Client()
def text_generator(message:dict, model:str = 'gpt-4-turbo-2024-04-09', max_tokens:int = 1000, temperatura:float = 0) -> list:
    resposta = client.chat.completions.create(messages= message, model= model, max_tokens=max_tokens, temperature= temperatura)
    print(resposta.choices[0].message.content)
    message.append({'role': 'assistant', 'content': resposta.choices[0].message.content})
    return message