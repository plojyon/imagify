# required python 3.8 or alter byte-writing condition
input = input("name of imagified file (without .i.png):");
output = input.split(".");
output = ".".join(output);

import math;
from PIL import Image;
import os;

def bitstring2bytearr(s):
	ba = bytearray();
	for i in range(0, len(s), 8):
		sbyte = s[i:i+8];
		ibyte = int(sbyte, 2);
		ba.append(ibyte);
	return ba;

file_count = 0;
while (os.path.isfile(input+'.'+str(file_count)+'.png')):
	file_count += 1;
if (file_count == 0):
	print("No files detected. Aborted.");
	exit();

with open(output, "wb") as f:
	for file in range(file_count):
		img = Image.open(input+'.'+str(file)+'.png');
		size = img.size[0];
		print("processing image "+str(file+1)+"/"+str(file_count)+" ...");
		bits = [];
		pixels = img.load(); # create the pixel map
		size2 = size*size
		for px in range(size2):
			if (px % 500000 == 0): print(str(int(100*px/size2))+" % done");
			row = math.floor(px / size);
			col = px % size;
			if (pixels[col, row][0]-pixels[col, row][1] > 100): # hit red pixel
				break;
			if (pixels[col, row][0] < 127):
				bits.append("0");
			else:
				bits.append("1");
		byte_array = bitstring2bytearr("".join(bits));
		f.write(byte_array);

f.close();

print("all done!");
print("Thank you for using imagify");
