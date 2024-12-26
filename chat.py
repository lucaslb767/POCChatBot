from main_text_generator import *
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


messages = []
while True:
    question = input('\nUser: ')
    if question == '':
        break
    messages.append({'role':'user', 'content': question})
    messages = text_generator(messages)


