import base64
def converBase64ToBin(base64_image):
    _, data = base64_image.split(',')

    # Giải mã base64 thành dữ liệu nhị phân
    binary_data = base64.b64decode(data)
    return binary_data

def converImageToBase64(image_path):
    if image_path:
        with open(image_path, "rb") as image_file:
            # Read the binary data of the image
            image_binary = image_file.read()

            # Encode the binary data as Base64
            image_base64 = base64.b64encode(image_binary).decode('utf-8')

        return f"data:image/png;base64,{image_base64}"