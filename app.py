#I believe mental health is one of the most important elements to a humans life On my mental health journey i am currently learning to focus on the things in life that i can control and to not let 
#the things that i can't control, control me!
#
#Thus far this has been one of the most rewarding journeys I have been on and has started
#to mold me and my outlook on life in a very positive way!
#
#Please enjoy and share and i will continue to make these :) suggestions more than welcome!!!
#
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



#Window Configuration
root = ttk.Window(themename="vapor")
root.title("Trick Buttons")
HEIGHT = 300
WIDTH = 600
root.geometry(f"{WIDTH}x{HEIGHT}")

#Create Tk label that will present on the screen :)
label = ttk.Label(root,text="Is today going to be a good day?",font=('Times', 76))
label.pack(padx=20, pady=20)
label0 = ttk.Label(root, text="Select your choice?")
label0.pack()

#logic for the submit button 
def handle_submit():
    if selected_option.get() == "yes":
        print("Good! Control what you can and accept what you can't!")
        label2 = ttk.Label(root, text="Good! Control what you can and accept what you can't!")
        label2.pack()
    elif selected_option.get() == "no":     
        #this is the part that makes this a trick ;) 
        label3 = ttk.Label(root, text="It's a choice for a reason! Check your answer now! ;)")
        label3.pack()
        selected_option.set("yes")
        submit_button.invoke()

#placement for other buttons
selected_option = tk.StringVar()
selected_option.set("")

yes_radio = ttk.Radiobutton(root, text="Yes", variable=selected_option, value="yes")
yes_radio.pack(padx=5, pady=5)

no_radio = ttk.Radiobutton(root, text="No", variable=selected_option, value="no")
no_radio.pack(padx=5, pady=5)

submit_button = tk.Button(root, text="Submit", command=handle_submit)
submit_button.pack(padx=10, pady=10)

root.mainloop()
