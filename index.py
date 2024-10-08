import os
from PIL import Image

folder_path = input()
sizes_list = []

for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg')): 
        file_path = os.path.join(folder_path, filename)
        with Image.open(file_path) as img:
            imgSize = str(img.size)
            if (imgSize not in sizes_list):
                os.makedirs(folder_path+"/"+imgSize, exist_ok=True)
                sizes_list.append(imgSize)
        os.rename(file_path, folder_path+"\\"+imgSize+"\\"+filename)