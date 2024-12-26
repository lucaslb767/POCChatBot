from main_text_generator import *
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())



while True:
    question = input('What do you want to know? Leave empty to quit\n')
    if question == '':
        break
    messages =[{'role':'user', 'content': question}]
    text_generator(messages)


