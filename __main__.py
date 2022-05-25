import src.convert as convert
from src.get_path import getPath
from PIL import Image
import numpy
import os

path = getPath(__file__)
in_path = os.path.join(path, 'input')
in_path = os.path.abspath(os.path.realpath(in_path)) 
# print(in_path)

dir_list = os.listdir(in_path)
print(dir_list)

count = 0

# Usage:
print("Place input images in /inputs/")
print("Enter 2 characters for the Art: ")
char = ['.','i']
char[0] = input("Partial: ")
char[1] = input("Full: ")

for fin in dir_list:
    if(fin != 'grey'):
        #fin_path, fout and fin_grey:
        fin_path = os.path.join(in_path, fin)

        fout = fin.split('.')[0]
        fout += '.out'

        fin_grey = fin.split('.')[0]
        fin_grey += "_grey." 
        fin_grey += fin.split('.')[1]

        #counter
        count +=1 
        print(str(count) + '.')
        print(fout)

        #Creating a greyscale copy in /inputs/grey/
        img = Image.open(fin_path).convert('L')
        fin_grey_path = os.path.join(in_path,'grey',fin_grey)
        img.save(fin_grey_path)

        #Storing image data in a 2d Numpy array
        imgdata = numpy.asarray(img)
        print(imgdata.shape)

        # Very ineffecient v space heavy initial output
        f = open("imgdata.txt", "w")
        for i in imgdata:
            for j in i:
                # if j==255:
                #     print(' ', end=" ")
                # elif j<255:
                #     print(char[0], end=" ")
                # elif j<126:
                #     print(char[1], end=" ")
                # print(" ")
                
                f.write(str(j)+" ")
            
            f.write(" ")

                
        #checking if satisfied:
        flag = 'N'
        while flag != 'Y':
            flag = input("Enter Y to continue: ")

        #using C++ to process:
        

        #Deleting old file
        # os.remove("imgdata.txt")      





