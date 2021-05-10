import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Star']

def get_file_ext(filename):
    return filename[filename.index('.') + 1:]

def roll_dice(num):
    return random.randint(1, num)







questionprompt =[
    "What color are Apples?\n(a) Red/Green\n(b) Purple \n(c) Orange\n\n",
    "What color are Banana?(a) Teal\n(b) Magenta \n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

print(questionprompt)