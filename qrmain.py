import qrcode
#central
qr = qrcode.QRCode(
    version =15,
    box_size =10,
    border =5
)
central ="https://priyankamaturi.github.io/majortest/"
qr.add_data(central)
qr.make(fit =True)
img =qr.make_image(fill="black",back_color ="white")
img.save('main.png')
