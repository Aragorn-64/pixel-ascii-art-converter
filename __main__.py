from sys import meta_path
import src.convert as convert
from src.get_path import getPath
from PIL import Image
import numpy
import os
import subprocess

path = getPath(__file__)
in_path = os.path.join(path, 'input')
in_path = os.path.abspath(os.path.realpath(in_path)) 
src_path = os.path.join(path, 'src')
# print(src_path)

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

        #Creating a greyscale copy in /inputs/grey

        img = Image.open(fin_path).convert('L')
        fin_grey_path = os.path.join(in_path,'grey',fin_grey)
        img.save(fin_grey_path)

        #Storing image data in a 2d Numpy array

        imgdata = numpy.asarray(img)
        # print(imgdata.shape)
        m = imgdata.shape[0]
        n = imgdata.shape[1]

        #storing meta data in .path/img_metadata.txt

        metadata_path =  os.path.join(path, "metadata.txt")
        metafile = open(metadata_path, "w")
        metafile.write(fout + "\n")
        metafile.write(str(m) +" "+ str(n)+ "\n")
        metafile.close()


        # Very ineffecient v space heavy initial output

        imagedata_path = os.path.join(path, "converted" ,'imgdata.txt')
        
        # f = open(imagedata_path, "w")
        # f.write(str(m) +" "+ str(n)+ "\n")
        
        # alternative methods to write to txt file:
        numpy.savetxt(imagedata_path, imgdata, fmt="%d") 
        # with open(imagedata_path, "w+") as file:
        #     img_content = str(imgdata)
        #     file.write(img_content)


        #calling C++ to process:

        san_cpp_path = os.path.join(src_path, 'sanitize.exe')
        gen_cpp_path = os.path.join(src_path, 'generate.exe')
        # sanitized_path = os.path.join(path, "converted" , 'imgdata_san.txt')
        # sanitize_comm = san_cpp_path + ' < ' + imagedata_path + ' > ' + sanitized_path
        generated_path = os.path.join(path, "converted" , 'imgdata_san.txt')
        final_output_path = os.path.join(path, 'output', fout)
        generate_comm = gen_cpp_path + ' < ' + imagedata_path + ' > ' + final_output_path
        # print(sanitize_comm)
        # os.system(sanitize_comm)
        os.system(generate_comm)


        #checking if satisfied:

        flag = 'N'
        while flag != 'Y':
            flag = input("Enter Y to continue: ")
            print("done")
        
        #Deleting old file

        # os.remove(imagedata_path)
        # os.remove(sanitized_path)

         
    





#trying to process in python:
        # for row in imgdata:
        #     for i in row:
        # empty = numpy.where(imgdata == 255)
        # partial = numpy.where(imgdata == 0)