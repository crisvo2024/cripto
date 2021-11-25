import base64
import pyDes
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    name = input("Enter the name of the image: ")
    image = open(name, "rb")
    image_bytes = image.read()
    image.close()
    key = b'\xd8\xbb\xd9\xb6\xc1\xcb8X'
    encoder = pyDes.des(key, padmode=pyDes.PAD_PKCS5)
    des_encoded = encoder.encrypt(image_bytes)
    encoded = base64.b64encode(des_encoded)
    print(encoded)
    decoded64 = base64.b64decode(encoded)
    decoded = encoder.decrypt(decoded64)
    new_name = "new_image."+name.split(".")[-1]
    new_image = open(new_name, "wb")
    new_image.write(decoded)
    new_image.close()
    plt.imshow(mpimg.imread(new_name))
    plt.show()


if __name__ == '__main__':
    main()
