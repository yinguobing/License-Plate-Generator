import os
import cv2

W = 43
H = 90

if __name__ == "__main__":
    img_dir = '/home/robin/developer/github/License-Plate-Generator/assets/tokens/condensed-1/digits'
    img_files = os.listdir(img_dir)

    for img_file in img_files:
        img = cv2.imread(os.path.join(img_dir, img_file))
        height, width, channel = img.shape

        scale = 1.0 * H / height
        scaled_width = int(width * scale)

        scaled_img = cv2.resize(img, (W, H))

        cv2.imwrite(os.path.join(img_dir, img_file), scaled_img)
        cv2.imshow('p', scaled_img)
        if cv2.waitKey(50) == 27:
            break
