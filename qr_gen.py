from pathlib import Path
import sys

url = "https://ibtikar-2.onrender.com/"
size = 512
out = Path(r"c:\Users\Fawaz Nasser\Desktop\project\qr-ibtikar.png")

try:
    import qrcode
except Exception:
    print("MISSING_QRCODE_LIB")
    sys.exit(2)

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
img = img.resize((size, size))
img.save(out)
print(str(out))
