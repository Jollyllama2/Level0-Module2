import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)


    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range (10):
        random_number = random.randint(1, 5)
        if random_number == 1 :
            messagebox.showinfo(title='Mr. Lee', message=' you are funny')
        if random_number == 2:
            messagebox.showinfo(title='Mr. Lee', message=' you are a SPECIAL person ')
        if random_number == 3:
            messagebox.showinfo(title='Mr. Lee', message=' you are a great person ')
        if random_number == 4:
            messagebox.showinfo(title='Mr. Lee', message=' you make other people smile')
        if random_number == 5:
            messagebox.showinfo(title='Mr. Lee', message=' grrrrrrrrr you meany ')

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
