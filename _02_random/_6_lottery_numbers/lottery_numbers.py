import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    ticket_number_one = random.randint(1,9)
    ticket_number_two = random.randint(1,9)
    ticket_number_three = random.randint(1,9)
    ticket_number_four = random. randint(1,9)
    ticket_number_five = random.randint(1,9)
    ticket_number_six = random.randint(1,9)
    ticket = str(ticket_number_one) + " " +str(ticket_number_two) + " "  +str(ticket_number_three)+ " "   +str( ticket_number_four)+ " "  +str(ticket_number_five)+ " " +str(ticket_number_six)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title='hi',message= 'You won the lottery with your ticket of'+ ' ' +str(ticket))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
