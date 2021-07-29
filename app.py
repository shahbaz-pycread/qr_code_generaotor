import qrcode

# Provide a string to be embedded in qr code

img = qrcode.make("shahbazalamdotin.wordpress.com")
img.save("website.jpg")