import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3

# Create the main window
root = tk.Tk()
root.title("User Dashboard")

# Set the window size and background image
root.geometry("800x600")
image = Image.open("assets\\image_1.png")
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create the database connection and cursor
conn = sqlite3.connect('Database\\AccountSystem.db')
cursor = conn.cursor()


# Create a function to get the user data and display it
def display_users():
    # Clear the previous data
    for widget in frame_display.winfo_children():
        widget.destroy()

    # Get the user data from the database
    cursor.execute("SELECT * FROM AccountDB")
    rows = cursor.fetchall()

    # Display the number of registered users
    num_users = tk.Label(frame_display, text=f"Number of registered users: {len(rows)}")
    num_users.pack()

    # Create a canvas to hold the user data and a scrollbar to navigate it
    canvas = tk.Canvas(frame_display)
    scrollbar = ttk.Scrollbar(frame_display, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for row in rows:
        user_info = tk.Label(scrollable_frame, text=f"Username: {row[1]}\nEmail: {row[3]}\nPassword: {row[4]}")
        user_info.pack(side="top", fill="both", expand=True)

        delete_button = tk.Button(scrollable_frame, text="Delete", command=lambda id=row[0]: delete_user(id))
        delete_button.pack()

    # Add the scrollbar to the frame
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)


# Create a function to delete a user record
def delete_user(ID):
    cursor.execute("DELETE FROM AccountDB WHERE ID=?", (ID,))
    conn.commit()
    display_users()


# Create a frame to display the user data
frame_display = tk.Frame(root, bg="#ffffff", bd=5)
frame_display.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor="n")

# Display the initial user data
display_users()

# Run the main loop
root.mainloop()

# Close the database connection
conn.close()
