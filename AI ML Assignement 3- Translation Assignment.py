#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
from googletrans import Translator

def translate_to_hinglish(input_text):
    # Split the input text into words.
    words = input_text.split()

    # Translate each word to Hindi.
    hindi_translations = []
    translator = Translator()
    for word in words:
        hindi_translation = translator.translate(word, src='en', dest='hi').text
        hindi_translations.append(hindi_translation)

    # Combine the Hindi and English translations into Hinglish.
    hinglish_words = []
    for i in range(len(words)):
        if random.random() > 0.3:
            hinglish_words.append(hindi_translations[i])
        else:
            hinglish_words.append(words[i])

    # Shuffle the words in the Hinglish text.
#     random.shuffle(hinglish_words)

    # Join the translated words back into a text.
    hinglish_output = ' '.join(hinglish_words)

    return hinglish_output

if __name__ == "__main__":
    input_text = input("Enter the text in English: ")
    hinglish_output = translate_to_hinglish(input_text)

    print("Hinglish Output:", hinglish_output)


# In[21]:


import random
from googletrans import Translator

def translate_to_hinglish(input_text):
    # Split the input text into words.
    words = input_text.split()

    # Translate each word to Hindi.
    hindi_translations = []
    translator = Translator()
    for word in words:
        hindi_translation = translator.translate(word, src='en', dest='hi').text
        hindi_translations.append(hindi_translation)

    # Combine the Hindi and English translations into Hinglish.
    hinglish_words = []
    for i in range(len(words)):
        if random.random() > 0.3:
            hinglish_words.append(hindi_translations[i])
        else:
            hinglish_words.append(words[i])

    # Shuffle the words in the Hinglish text.
    random.shuffle(hinglish_words)

    # Join the translated words back into a text.
    hinglish_output = ' '.join(hinglish_words)

    return hinglish_output

if __name__ == "__main__":
    input_text = input("Enter the text in English: ")
    hinglish_output = translate_to_hinglish(input_text)

    print("Hinglish Output:", hinglish_output)


# In[31]:


import random
from googletrans import Translator

def translate_to_hinglish(input_text):
    # Split the input text into words.
    words = input_text.split()

    # Translate each word to Hindi.
    hindi_translations = []
    translator = Translator()
    for word in words:
        hindi_translation = translator.translate(word, src='en', dest='hi').text
        hindi_translations.append(hindi_translation)

    # Combine the Hindi and English translations into Hinglish.
    hinglish_words = []
    for i in range(len(words)):
        if random.random() > 0.5:
            hinglish_words.append(hindi_translations[i])
        else:
            hinglish_words.append(words[i])

    # Shuffle the words in the Hinglish text.
#     random.shuffle(hinglish_words)

    # Join the translated words back into a text.
    hinglish_output = ' '.join(hinglish_words)

    return hinglish_output

if __name__ == "__main__":
    input_text = input("Enter the text in English: ")
    hinglish_output = translate_to_hinglish(input_text)

    print("Hinglish Output:", hinglish_output)


# In[32]:


import random
from googletrans import Translator

def translate_to_hinglish(input_text):
    # Split the input text into words.
    words = input_text.split()

    # Translate each word to Hindi.
    hindi_translations = []
    translator = Translator()
    for word in words:
        hindi_translation = translator.translate(word, src='en', dest='hi').text
        hindi_translations.append(hindi_translation)

    # Combine the Hindi and English translations into Hinglish.
    hinglish_words = []
    for i in range(len(words)):
        if random.random() > 0.5:
            hinglish_words.append(hindi_translations[i])
        else:
            hinglish_words.append(words[i])

    # Shuffle the words in the Hinglish text.
#     random.shuffle(hinglish_words)

    # Join the translated words back into a text.
    hinglish_output = ' '.join(hinglish_words)

    return hinglish_output

if __name__ == "__main__":
    input_text = input("Enter the text in English: ")
    hinglish_output = translate_to_hinglish(input_text)

    print("Hinglish Output:", hinglish_output)


# In[ ]:


"""i can print same code with differnt shuffle  and different random parameter for output
list of all different parameter output you can also try it""" 

