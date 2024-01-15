from tkinter import *
from tkinter import ttk


def average_cleanliness(list_of_feedback):
    """takes a list of integers - the feedback - and returns the average of that list."""
    total_feedback = sum(list_of_feedback)
    average_feedback = total_feedback / len(list_of_feedback)
    return average_feedback.__round__(2)


def show_average_cleanliness():
    """Changes the label to display the latest average."""
    display_average_cleanliness.configure(text=(average_cleanliness(feedback)))


# This list collects the data from the feedback GUI.
feedback = []

# Create the GUI window where the passengers will be able to give their feedback.
window = Tk()
window.title("CodeTown Public Transport Cleanliness Feedback System")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Create a label to ask the passengers to submit feedback.
rate_label = ttk.Label(window, text="Please rate the cleanliness of this bus on the below scale")
rate_label.grid(column=2, row=1, columnspan=5)
rate_label.configure(font=("Ariel", 10, "bold"))

# Visual representation on the feedback scale - red sad face for 1.
sad_face = PhotoImage(file='red_sad_face.gif')
sad_face_label = ttk.Label(window, image=sad_face)
sad_face_label.grid(column=1, row=2, sticky=E)

# Visual representation of the feedback scale - green smiley face for 5.
happy_face = PhotoImage(file='green_happy_face.gif')
happy_face_label = ttk.Label(window, image=happy_face)
happy_face_label.grid(column=7, row=2, sticky=W)

# Create the buttons that the passengers will press.
# Pushing a button will trigger the feedback to be appended to the list as well as triggering the function that will
# display the average cleanliness to the passenger.
one_button = ttk.Button(window, text='1', command=lambda: [feedback.append(int(1)), show_average_cleanliness()])
one_button.grid(column=2, row=2, sticky=(E, W))
two_button = ttk.Button(window, text='2', command=lambda: [feedback.append(int(2)), show_average_cleanliness()])
two_button.grid(column=3, row=2, sticky=(E, W))
three_button = ttk.Button(window, text='3', command=lambda: [feedback.append(int(3)), show_average_cleanliness()])
three_button.grid(column=4, row=2, sticky=(E, W))
four_button = ttk.Button(window, text='4', command=lambda: [feedback.append(int(4)), show_average_cleanliness()])
four_button.grid(column=5, row=2, sticky=(E, W))
five_button = ttk.Button(window, text='5', command=lambda: [feedback.append(int(5)), show_average_cleanliness()])
five_button.grid(column=6, row=2, sticky=(E, W))

# Create a label to tell the passenger what the average cleanliness of the bus is.
average_cleanliness_title = ttk.Label(window, text="The average cleanliness of this bus is:")
average_cleanliness_title.configure(font=("Ariel", 10))
average_cleanliness_title.grid(column=2, row=3, columnspan=5)

# Create a label where the average cleanliness number will be displayed.
display_average_cleanliness = ttk.Label(window, text=" ")
display_average_cleanliness.configure(font=("Ariel", 10))
display_average_cleanliness.grid(column=2, row=4, columnspan=5)

# Allow the window to be resized gracefully.
for child in window.winfo_children():
    child.grid_configure(padx=5, pady=5)

for i in range(1, 10):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

window.mainloop()
