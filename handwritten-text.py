# pip install pywhatkit #
import pywhatkit as kit

text = '''
It's not a lack of coffee, nor tequila.

It's my code, which doesn't compile!
'''

# Generates image with written text #
kit.text_to_handwriting(text, save_to='handwritten_text.png')
