# TOTP 2FA Authentication Demo

## Overview

This project demonstrates a simple implementation of Time-Based One-Time Password (TOTP) authentication using Python and the `pyotp` library.

The goal is to illustrate how TOTP works internally, how a shared secret generates time-based codes, and how Google Authenticator compatibility is achieved via provisioning URIs and QR codes.

---

## Implementation

The demo script performs the following:

1. Defines a shared secret key.
2. Generates the current 6-digit OTP.
3. Verifies a token using `totp.verify()`.
4. Generates an `otpauth://` provisioning URI.
5. Creates a QR code compatible with Google Authenticator.

---

## Demo Script

File: `totp_demo.py`

```python
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
```

---

## QR Provisioning

The generated QR code can be scanned using Google Authenticator.

<img width="886" height="184" alt="image" src="https://github.com/user-attachments/assets/8893366b-6a5e-4e46-9cab-e1adfb799843" />

<img width="545" height="474" alt="image" src="https://github.com/user-attachments/assets/92366ce2-94c6-48e4-a868-79a9e5d287b9" />


---

## Google Authenticator Registration

After scanning the QR, a rotating 6-digit code is generated every 30 seconds.

<img width="437" height="412" alt="image" src="https://github.com/user-attachments/assets/c25f5e54-9f22-4d93-93e6-055d69c6b4a9" />


---

## Token Verification Example

The generated code can be verified using:

```python
totp.verify(code)
```

If the code is valid within the current time window, the function returns:

```
True
```

Successful verification confirms that both sides share the same secret and time reference.

<img width="572" height="158" alt="image" src="https://github.com/user-attachments/assets/6863ad91-70b7-4421-b9c9-0ec8aede91d2" />


---

## Security Concepts Demonstrated

- Time-Based One-Time Password (TOTP)
- Shared secret authentication
- HMAC-based token generation
- 30-second validity window
- Google Authenticator compatibility

---

## Notes

- The secret key is static for demonstration purposes.
- In production systems, secrets must be securely generated and stored.
- Time synchronization between client and server is essential.
