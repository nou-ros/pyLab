# install qrcode & Pillow
import qrcode
'''
# simple 
img = qrcode.make("Hello world! this is ynouros")
img.save("code.png")
'''

'''
# moderate
qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=2)

# added data in the qrcode
qr.add_data("https://github.com/nou-ros")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="yellow")
img.save("yn.png")
'''

# advance - svg for website

import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make('https://github.com/nou-ros', image_factory=factory)
svg_img.save('yn.svg')
