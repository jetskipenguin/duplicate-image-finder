from PIL import Image, ImageStat
import os
import shutil
'''
This program opens images in pillow and stores a calculated mean value
It then iterates through the directory comparing mean values
Any images with matching mean values are stored in dupes list
It then moves duplicates into a duplicate folder.

'''
import time
# times the main function
def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took:", time.time() - before, "seconds")
    
    return wrapper

@timer
def main():
    file_extensions = ['png', 'jpg', 'gif', 'jpeg']
    files = []
    file_names = []
    print("Loading Images..")
    for file in os.listdir():
        for ending in file_extensions:
            if file.endswith(ending):
                file_names.append(file)
                files.append(ImageStat.Stat(Image.open(file)).mean)

    dupes = []
    if 'duplicates' not in os.listdir(): os.mkdir('duplicates')
    # only loops through first half
    for i in range(len(files)):
        # starts at current i and searches till end of files
        for y in range(len(files)-1, i, -1):
            print("Comparing {} and {}".format(file_names[i], file_names[y]))
            if files[i] == files[y]:
                print("Image A: {} Image B: {}\n".format(file_names[i], file_names[y]))
                if file_names[i] not in dupes:
                    dupes.append(file_names[i])

    
    for i in dupes:
        shutil.move(i, 'duplicates')
    
if __name__ == "__main__":
    main()
