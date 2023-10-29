import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title='hi',prompt='Ask a question')
    # Make a variable and initialize it to a random number between 0 and 3
    eight_ball = random.randint(0,3)
    if eight_ball == 0:
        messagebox.showinfo(title='hi',message='yes')
    # If the random number is 0
    if eight_ball == 1:
        messagebox.showinfo(title='hi',message='No')
    if eight_ball == 2:
        messagebox.showinfo(title='hi',message='Maybe you ask google?')
    if eight_ball == 3:
        messagebox.showinfo(title='hi',message='ERROR')

     # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
