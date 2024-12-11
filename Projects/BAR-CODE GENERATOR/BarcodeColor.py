import qrcode as qr
from PIL import Image

Qr=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=4,)

fg=input("Enter Foreground Color:")
bg=input("Enter Backgound Color:")
nm=input("Enter Filename:")
url=input("Enter url :")

# Qr.add_data("https://github.com/Shikher-jain/SJ_MAIN")
Qr.add_data(url)
Qr.make(fit=True)

img=Qr.make_image(fill_color=fg, back_color=bg)
img.save(f"Advance-Python-SJ/Projects/BAR-CODE GENERATOR/{nm}.png")