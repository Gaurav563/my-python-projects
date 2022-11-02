import qrcode as qr
from PIL import Image

 #| ------------------ BASIC QR ---------------------------|
# img =  qr.make("PUT WHAT U WANT")
# img.save("ANthing.png")

 # || -----------------------------------------------------|
QR =  qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,border=4
)
#|============= CUSTOM QRCODE ================================ |
QR.add_data(" ANY THINGS")
QR.make(fit=True)
img =QR.make_image(fill_color ='red',back_color ='blue')
img.save("customized.png")
#|============================================================ |
