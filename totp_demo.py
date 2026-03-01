import pyotp
import qrcode

key = "EstaEsMiKeySecreta"

totp = pyotp.TOTP(key)

current_code = totp.now()
print("Current OTP:", current_code)

totp.verify("327057")

url = totp.provisioning_uri(
    name="albertprueba@google",
    issuer_name="albertPrueba"
)

print("Provisioning URI:", url)

qr = qrcode.make(url)
qr.save("qrcode.png")
