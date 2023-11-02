import cv2

def image_to_pencil_sketch(image_path: str):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    negative_image = cv2.bitwise_not(grayscale_image)
    blurred_image = cv2.GaussianBlur(negative_image, (21, 21), 0)
    sketch_image = cv2.divide(grayscale_image, 255 - blurred_image, scale=256.0)
    cv2.imshow('Image To Pencil Sketch', sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image_to_pencil_sketch('datasets/dog.jpg')