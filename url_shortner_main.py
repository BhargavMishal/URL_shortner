import pyshorteners
import pyperclip
from tkinter import *

# making the main window
root = Tk()
root.geometry("500x300")
root.title("URL Shortner")
root.config(bg="#D2E0D3")

# defining variables
long_url = StringVar()
short_url = StringVar()

# shortening function
def shortner():
    url = long_url.get()
    shortner_obj = pyshorteners.Shortener()
    shortened_url = shortner_obj.tinyurl.short(url)
    short_url.set(shortened_url)

# copy to clipboard function
def copy_url():
    shortened_url = short_url.get()
    pyperclip.copy(shortened_url)

# UI components
Label(root, text="URL Shortner", font=("Lexend", 23, "bold"), bg="#D2E0D3").pack(pady=20)
Entry(root, textvariable=long_url, font=("Lexend", 14), width=40, bd=2).pack(pady=10)
Button(root, text="Generate short URL", font=("Lexend", 14), bg="#4CAF50", fg="white", command=shortner).pack(pady=10)
Entry(root, textvariable=short_url, font=("Lexend", 14), width=40, bd=2).pack(pady=10)
Button(root, text="Copy URL", font=("Lexend", 14), bg="#2196F3", fg="white", command=copy_url).pack(pady=10)

# running the main loop
root.mainloop()