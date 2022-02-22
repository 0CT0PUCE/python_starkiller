from googletrans import Translator
import random
from time import sleep
translator = Translator()
data="The two presidents spoke by phone on July 25."
result = translator.translate(data, dest='fr').text
result=str(result)
print(result)
for character in result:
    print(character)
    wait=random.randrange(4, 0, -1)
    wait=wait*0.1
    sleep(wait)
