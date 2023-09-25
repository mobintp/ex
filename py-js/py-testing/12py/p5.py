import random
import requests
import string

# getting lists's API
lists_url = 'https://www.randomlists.com/data/words.json'
response = requests.get(lists_url)
data = response.json()
words = data['data']

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
        
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()