"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/16/2020
This program creates a random number game using a built-in GUI
from tkinter
"""

import tkinter as tk
from tkinter import messagebox
import random
from class_definitions.NumberGuesser import add_num

window = tk.Tk()  # Creates a window
scrollbar = tk.Scrollbar(window)  # Creates a scrollbar
scrollbar.pack(side="right", fill="y")

frame_a = tk.Frame()  # Creates a frame for layout purposes
frame_b = tk.Frame()  # Creates a frame for layout purposes
frame_c = tk.Frame()  # Creates a frame for layout purposes

lbl_greeting = tk.Label(master=frame_a, text="\n===================================================="
                                             "\n\n///// Welcome to the Number Guessing Game /////\n\n"
                                             "Please click on the number you'd like to guess below...\n",
                        height=5,
                        bg="blue",
                        fg="yellow",
                        )
lbl_greeting.pack(fill=tk.BOTH, expand=True)  # Prints the greeting, fills the blue portion as wide as needed
x = 0


def onButtonClick(button_id):
    """
    This function creates a random number and outputs an answer based on
    what the user clicks on
    :param button_id:
    :return:
    """
    answer = random.randint(1, 10)  # assign a random number

    add_num.add_guess(button_id)  # adds picked numbers to a list

    if button_id == answer:
        # Prints the random number

        messagebox.showinfo("That's Right!", "================================\n" +
                            "... and the random answer is... " + str(answer) +
                            "\nYou guessed the correct number!\n "
                            "\n*************** Congrats *************** \n\n"
                            "Feel free to try as many times as you want!\n"
                            "================================\n"
                            )

    else:
        messagebox.showinfo("Nope!", "================================\n" +
                            "... and the random answer is... " + str(answer) +
                            "\nYou guessed the incorrect number!\n "
                            "Feel free to try as many times as you want!\n"
                            "================================\n"
                            )


button1 = tk.Button(master=frame_b, text="ONE", command=lambda: onButtonClick(1))
button1.pack(fill=tk.Y, side=tk.LEFT)
button2 = tk.Button(master=frame_b, text="TWO", command=lambda: onButtonClick(2))
button2.pack(fill=tk.Y, side=tk.LEFT)
button3 = tk.Button(master=frame_b, text="THREE", command=lambda: onButtonClick(3))
button3.pack(fill=tk.Y, side=tk.LEFT)
button4 = tk.Button(master=frame_b, text="FOUR", command=lambda: onButtonClick(4))
button4.pack(fill=tk.Y, side=tk.LEFT)
button5 = tk.Button(master=frame_b, text="FIVE", command=lambda: onButtonClick(5))
button5.pack(fill=tk.Y, side=tk.LEFT)
button6 = tk.Button(master=frame_b, text="SIX", command=lambda: onButtonClick(6))
button6.pack(fill=tk.Y, side=tk.LEFT)
button7 = tk.Button(master=frame_b, text="SEVEN", command=lambda: onButtonClick(7))
button7.pack(fill=tk.Y, side=tk.LEFT)
button8 = tk.Button(master=frame_b, text="EIGHT", command=lambda: onButtonClick(8))
button8.pack(fill=tk.Y, side=tk.LEFT)
button9 = tk.Button(master=frame_b, text="NINE", command=lambda: onButtonClick(9))
button9.pack(fill=tk.Y, side=tk.LEFT)
button10 = tk.Button(master=frame_b, text="TEN", command=lambda: onButtonClick(10))
button10.pack(fill=tk.Y, side=tk.LEFT)

frame_a.pack()  # unpacks the frames in order
frame_b.pack()
frame_c.pack()




tk.mainloop()

window.mainloop()
