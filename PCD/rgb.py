import numpy as np
import imageio.v3 as img

image_path = "C:\\Users\\JARKOM 18\\Documents\\PCD\\kakgem.jpg"

image = img.imread(image_path)

if len(image.shape) < 3 or image.shape[2] !=3:
    print("format gambar harus RGB")
    exit()

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]
gray = red * 0.299 + green * 0.587  + blue * 0.114

image_red = np.zeros_like(image)
image_red[:,:,0] = red
img.imwrite("source.jpg", image_red)

image_green = np.zeros_like(image)
image_green[:,:,1] = green
img.imwrite("sourcegreen.jpg", image_green)

image_blue = np.zeros_like(image)
image_blue[:,:,2] = blue
img.imwrite("sourceblue.jpg", image_blue)


image_gray = np.zeros_like(image)

image_gray[:,:,0] = gray
image_gray[:,:,1] = gray
image_gray[:,:,2] = gray
img.imwrite("gray_image.jpg", image_gray)

threshold = 100
binary_image = np.where(gray > threshold, 255, 0 ).astype(np.uint8)
binary_rgb = np.zeros_like(image)
binary_rgb[:,:,0] = binary_image
binary_rgb[:,:,1] = binary_image
binary_rgb[:,:,2] = binary_image
img.imwrite("Black&white.jpg", binary_rgb )
print("proses berhasil")