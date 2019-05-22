import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters 
from skimage.transform import rescale, resize, swirl
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour

image = io.imread('/home/wot1mtp/Pictures/shark.png')

def resize_image(image, newImagePath, width):
    # Resizes the image to the specified width in pixels, keeping the height/width ratio intact
    heightToWidthRatio = image.shape[0] / image.shape[1]
    print("Image shape 1: " + str(image.shape[0]))
    print("Image shape 2: " + str(image.shape[1]))
    image_resized = resize(image, (int(width * heightToWidthRatio), width), anti_aliasing=True)
    io.imsave(newImagePath, image_resized)

def reduce_pixel_density(image, newImagePath, scale):
    # Reduces the pixel density to the specified percentage (e.g. scale=0.25)
    image_rescaled = rescale(image, scale, anti_aliasing=True)
    image_resized = resize(image_rescaled, (image.shape[0], image.shape[1]), anti_aliasing=True)
    io.imsave(newImagePath, image_resized)

def make_image_grayscale(image, newImagePath):
    # self explanatory 
    grayscaleImage = rgb2gray(image)
    io.imsave(newImagePath, grayscaleImage)

def swirl_transformation(image, newImagePath):
    # o_O 
    swirled = swirl(image, rotation=0, strength=3, radius=3000)
    io.imsave(newImagePath, swirled)

resize_image(image, '/home/wot1mtp/Pictures/sharkresized500.png', 500)
resize_image(image, '/home/wot1mtp/Pictures/sharkresized1000.png', 1000)
reduce_pixel_density(image, '/home/wot1mtp/Pictures/sharkreducesPPI.png', 1.0/4.0)
# make_image_grayscale(image, '/home/wot1mtp/Pictures/tigergrayscale.bmp')
swirl_transformation(image, '/home/wot1mtp/Pictures/sharkswirl.png')