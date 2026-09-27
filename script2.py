import qrcode
import customtkinter as ctk

root = ctk.CTk()
root.title("QR Code Generator")


root.geometry("400x400")

label = ctk.CTkLabel(root, text="Enter data for website: ", font=("Helvetica", 14))
label.pack(pady=10)
entry = ctk.CTkEntry(root, width=150, font=("Helvetica", 14))
entry.pack(pady=10)

def generate_qr_code():
    qrcode_data = entry.get()

    if not qrcode_data.startswith("http://") and not qrcode_data.startswith("https://"):
        qrcode_data = "https://www." + qrcode_data
        qrcode_data = qrcode_data.endswith(".com") and qrcode_data or qrcode_data + ".com"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qrcode_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

button = ctk.CTkButton(root, text="Generate QR Code", command=generate_qr_code)
button.pack(pady=10)

root.mainloop()
