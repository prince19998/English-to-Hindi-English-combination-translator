Title: Hinglish Text Translator

Description:

This Python script allows you to convert English text into Hinglish, a blend of Hindi and English. It utilizes the Google Translate API to translate individual English words into Hindi and then combines them randomly with the original English words to create a Hinglish output.

Usage:

1. Import the required libraries, `random` for randomness and `googletrans` for translation.
2. Define the `translate_to_hinglish` function, which takes an English text input and returns a Hinglish translation.
3. Split the input text into words.
4. Translate each English word to Hindi using the Google Translate API.
5. Combine the Hindi and English translations into Hinglish with a random mix.
6. Shuffle the words in the Hinglish text for added randomness.
7. Join the translated words back into a text.
8. Finally, the script prompts the user to enter English text and displays the corresponding Hinglish translation.

Dependencies:

- random: Python's built-in library for generating random numbers.
- googletrans: A library for Google Translate, which can be installed using `pip install googletrans==4.0.0-rc1`.



Note:

Ensure that you have the `googletrans` library installed and that you have an active internet connection for this script to work properly.
its fully dependent on internet connectivity


