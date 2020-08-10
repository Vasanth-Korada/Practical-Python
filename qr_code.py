from PIL import Image
import qrcode
img = Image.new('RGB',(250,250),color = 'white')

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size =2.5,
    border = 0,
)

storage_id = input("Storage ID:")
location = input("Location:")
holder_1 = input("Holder 1:")
holder_2 = input("Holder 2:")
holder_3 = input("Holder 3:")
holder_4 = input("Holder 4:")

data = {
"storage_id":storage_id,
"location":location,
"Holder_1":holder_1,
"Holder_2":holder_2,
"Holder_3":holder_3,
"Holder_4":holder_4
}

qr.add_data(data)
qr.make(fit=True)
qrimg = qr.make_image()
img.paste(qrimg,(65,65))
img.show("qr_image.png")


