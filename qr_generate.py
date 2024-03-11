import qrcode
#central
qr = qrcode.QRCode(
    version =15,
    box_size =10,
    border =5
)
central ="https://maps.app.goo.gl/YEpHUXnxSfUdcC5g6"
qr.add_data(central)
qr.make(fit =True)
img =qr.make_image(fill="black",back_color ="white")
img.save('central.png')

# Block A
qr = qrcode.QRCode(
    version =15,
    box_size =10,
    border =5
)
Block_A ="https://maps.app.goo.gl/4KHc2vZyUAX4yawg7"
qr.add_data(Block_A)
qr.make(fit =True)
img =qr.make_image(fill="black",back_color ="white")
img.save('Block_A.png')

#Block B
qr = qrcode.QRCode(
    version =15,
    box_size =10,
    border =5
)
Block_B ="https://maps.app.goo.gl/QoC7p9Nm7UbQKqR69"
qr.add_data(Block_B)
qr.make(fit =True)
img =qr.make_image(fill="black",back_color ="white")
img.save('Block_B.png')

#Block C
qr = qrcode.QRCode(
    version =15,
    box_size =10,
    border =5
)
Block_C ="https://maps.app.goo.gl/LqCaTHjCP42GTmJFA"
qr.add_data(Block_C)
qr.make(fit =True)
img =qr.make_image(fill="black",back_color ="white")
img.save('Block_C.png')

#Block D
qr = qrcode.QRCode(
    version =15,
    box_size =10,
    border =5
)
Block_D ="https://maps.app.goo.gl/eYZx7YAruj8VBdy68"
qr.add_data(Block_D)
qr.make(fit =True)
img =qr.make_image(fill="black",back_color ="white")
img.save('Block_D.png')

#siemens
qr = qrcode.QRCode(
    version =15,
    box_size =10,
    border =5
)
siemens ="https://maps.app.goo.gl/ohzcGtX7Le3SuR4W9"
qr.add_data(siemens)
qr.make(fit =True)
img =qr.make_image(fill="black",back_color ="white")
img.save('siemens.png')
