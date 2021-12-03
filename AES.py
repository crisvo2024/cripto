import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyaes


def main():
    name = input("Enter the name of the image: ")
    image = open(name, "rb")
    image_bytes = image.read()
    image.close()
    key = bytearray("qwertyuiopasdfghjklnzxcvbnmqwert", "ascii")
    encoder = pyaes.AESModeOfOperationCTR(key)
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
