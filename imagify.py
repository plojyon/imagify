# required python 3.8 or alter byte-reading condition
input = input("enter filename to imagify:"); #song.mp3
output = input+".png";

from PIL import Image;
import math;
import os;

def tobits(s):
	result = []
	for c in s:
		bits = bin(ord(c))[2:]
		bits = '00000000'[len(bits):] + bits
		result.extend([int(b) for b in bits])
	return result

# read file to bit string
bits = [];
with open(input, "rb") as f:
	while (byte := f.read(1)):
		bits.append(''.join(format(ord(byte), '08b')));
bits = ''.join(bits);
f.close()

filesize = os.path.getsize(input);
size = int(math.ceil(math.sqrt(filesize*8)));
# must be betwen 256 and 4 000 (16 MP limit)
if (size < 256): size = 256;
if (size > 4000):
	print("pp too big");
	exit();

img = Image.new('RGB', (size, size), color = 'red');
pixels = img.load(); # create the pixel map
try:
	for row in range(size):
		for col in range(size):
			pos = col + row*size;
			if (bits[pos] == "1"):
				color = (255,255,255);
			else:
				color = (0,0,0);
			pixels[col, row] = color;
except IndexError:
	pass;

print("saving image..");
img.save(output);
