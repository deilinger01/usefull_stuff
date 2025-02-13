import qrcode

def generate_qr_code(data, output_file):
    qr = qrcode.make(data)
    qr.save(output_file)
    print(f"QR Code saved as {output_file}")

# Example usage
# generate_qr_code("https://www.google.com/", "qrcode.png")
