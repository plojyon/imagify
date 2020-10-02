# required python 3.8 or alter byte-writing condition
input = input("name of imagified file:");
output = input.split(".");
output.pop();
output[-2] += "_deimagified";
output = ".".join(output);

import math;
from PIL import Image;

def bitstring2bytearr(s):
	ba = bytearray();
	print("output filesize: "+str(int(len(s)/8))+" bytes");
	for i in range(0, len(s), 8):
		if (i % 2000000 == 0): print("transforming "+str(int((i/int(len(s)))*100))+" % done");
		sbyte = s[i:i+8];
		ibyte = int(sbyte, 2);
		ba.append(ibyte);
	return ba;

img = Image.open(input);
size = img.size[0];
print("image size: "+str(size)+"x"+str(size)+" pixels");
bits = [];
print("decoding ...");
pixels = img.load(); # create the pixel map
try:
	for row in range(size):
		if (row % 100 == 0): print("decoding "+str(int(100*row/size))+" % done");
		for col in range(size):
			if (pixels[col, row][0]-pixels[col, row][1] > 100): # hit red pixel
				raise IndexError; # break out of nested for loop
			if (pixels[col, row][0] < 127):
				bits.append("0");
			else:
				bits.append("1");
except IndexError:
	pass;

print("done decoding");
print("transforming ...");

byte_array = bitstring2bytearr("".join(bits));

print("done transforming");
print("writing to disk ...");
with open(output, "wb") as f:
	f.write(byte_array);
print("done writing");
print("done.");
