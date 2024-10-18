import tkinter as tk
import time

def update_time():
    # Get the current local time
    current_time = time.strftime('%H:%M:%S %p')
    # Update the label with the current time
    label.config(text=current_time)
    # Call the update_time function again after 1000 milliseconds (1 second)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the update_time function to display the time
update_time()

# Start the GUI event loop
root.mainloop()
