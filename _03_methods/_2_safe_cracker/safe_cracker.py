import random
import sys
from tkinter import messagebox, Tk

wekncrzpasfdkjhcfjse= random.randint(0,3)
print(wekncrzpasfdkjhcfjse)
def crack_the_safe():
    #pass
    try_code(guess=wekncrzpasfdkjhcfjse)
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations



# ====================== DO NOT EDIT THE CODE BELOW =========================




def try_code(guess):
    print("trying " + str(guess))

    secret_code = random.randint(0,100)

    if guess == secret_code:
        messagebox.showinfo(None, "Congratulations! You cracked the safe with " + str(guess))
        play_the_sound_of_success()
        sys.exit(0)


def play_the_sound_of_success():
    play_the_sound_of_success('me-gusta.wav')


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    crack_the_safe()
