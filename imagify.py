# required python 3.8 or alter byte-reading condition
from PIL import Image;
import math;
import os;

def get_size(bits_left):
	size = int(math.ceil(math.sqrt(bits_left)));
	# ^ must be betwen 256 and 4 000 (16 MP limit)
	if (size < 256):
		size = 256;
	elif (size > 4000):
		size = 4000;
	return size;
	#if (size > 4000):
		#print("pp too big");
		#exit();

input_file = input("enter filename to imagify:"); #song.mp3
filesize = os.path.getsize(input_file);
print("filesize: "+str(filesize)+" B = "+str(filesize*8)+" b");

if (input("this will produce "+str(math.ceil(filesize / (2*(10**6))))+" images. Proceed? (y/n): ").upper() != "Y"):
	print("Aborted.");
	exit();

# read file by byte
with open(input_file, "rb") as f:
	bytes_read = 0;
	bits_read = 0;
	row = 0;
	col = 0;
	img_index = 0;
	size = get_size(filesize*8);
	img = Image.new('RGB', (size, size), color = 'red');
	pixels = img.load(); # create the pixel map
	while (byte := f.read(1)):
		if (bytes_read % 100000 == 0): print(str(int(100*bytes_read / filesize))+" % done");
		bits = ''.join(format(ord(byte), '08b'));
		for b in range(8):
			if (bits[b] == "1"):
				color = (255,255,255);
			else:
				color = (0,0,0);
			pixels[col, row] = color;

			bits_read += 1;
			col += 1;
			col %= size;
			if (col == 0): row += 1;
			row %= size;
			if ((row == 0 and col == 0) or bits_read == filesize*8):
				print("saving image "+str(img_index)+"/"+str(file_count)+" ...");
				img.save(input_file+"."+str(img_index)+".png");
				size = get_size(filesize*8 - bits_read);
				img = Image.new('RGB', (size, size), color = 'red');
				pixels = img.load(); # create the pixel map

				img_index += 1;
				row = 0;
				col = 0;
		bytes_read += 1;

f.close();

print("all done!");
print("Thank you for using imagify");
