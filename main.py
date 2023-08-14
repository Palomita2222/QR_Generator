import qrcode
from tkinter import *
from PIL import Image, ImageTk
import os

def generate_qr(data):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code to the current directory
    img.save("qrcode.png")

    return img

def display_qr(img):
    # Start the tkinter window
    root = Tk()
    root.title("QR Code")

    # Convert the QR code image for tkinter
    img = ImageTk.PhotoImage(img)
    label = Label(root, image=img)
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    data = input("Enter the data for the QR code: ")
    img = generate_qr(data)
    display_qr(img)
