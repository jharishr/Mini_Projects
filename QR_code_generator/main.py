import qrcode

url = input("Enter URL: ").strip()
file_path = "E:\\PROJECTS\\QR_code_generator\\qr_code.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)