import cv2
from region import Region
from config import image_path, color, thickness, output_path

img = cv2.imread(image_path)

regions = []

x_space = img.shape[1]/10
y_space = img.shape[0]/10

for i in range(0, 10):
    for j in range(0, 10):
        regions.append(
                Region(
                    (int(x_space * i), int(y_space * j)),
                    (int(x_space * i + x_space), int(y_space * j + y_space))
                    )
                )

for i,reg in enumerate(regions):
    cv2.rectangle(img, reg.top_left, reg.bottom_right, color, thickness)

    region_img = img[reg.top_left[1]:int(reg.top_left[1] + y_space),reg.top_left[0]:int(reg.top_left[0] + x_space)]
    print(region_img)

    cv2.imwrite(f"{output_path}/region{i}.png", region_img) 


cv2.imwrite("all_regions.png", img)
cv2.imshow("test image", img)
cv2.waitKey(0)

