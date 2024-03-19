#pip install pyqrcode
#pip install pypng

import pyqrcode
import png

write = "https://linktr.ee/aryan_residency"
url = pyqrcode.create(write)

# Generate QR code with PNG format and specified colors
url.png('final_qr.png', scale=5, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xff])
