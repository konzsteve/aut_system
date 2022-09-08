import numpy as np
from PIL import Image

def generate_shares(data, filename, share=2):
    filename_1 = "media/image_otp/otp/%s1.png" % filename
    filename_2 = "media/image_otp/otp/%s2.png" % filename

    data = np.array(data, dtype='u1')

    # Generate image of same size
    img1 = np.zeros(data.shape).astype("u1")
    img2 = np.zeros(data.shape).astype("u1")

    # Set random factor
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                n = int(np.random.randint(data[i, j, k] + 1))
                img1[i, j, k] = n
                img2[i, j, k] = data[i, j, k] - n

    # Saving shares
    img1 = Image.fromarray(img1)
    img2 = Image.fromarray(img2)

    img1.save(filename_1, "PNG")
    img2.save(filename_2, "PNG")

def compress_shares(img1, img2):
    # Read images
    img1 = np.asarray(Image.open(img1)).astype('int16')
    img2 = np.asarray(Image.open(img2)).astype('int16')

    img = np.zeros(img1.shape)

    # Fit to range
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                img[i, j, k] = img1[i, j, k] + img2[i, j, k]

    # Save compressed image
    img = img.astype(np.dtype('u1'))

    img = Image.fromarray(img)
    img.save("media/image_otp/compress.png", "PNG")


