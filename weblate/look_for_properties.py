from path import Path
import re

pattern = re.compile("^.+_\\w{2}.properties$")

folders = {}
for f in Path('../Projects').walkfiles():
	if pattern.match(f):
		if f[0:(f.rfind('\\'))] in folders:
			folders[f[0:(f.rfind('\\'))]] += 1;
		else:
			folders[f[0:(f.rfind('\\'))]] = 1;

f = open("result_properties.txt", "w")
for folder in folders:
	text = folder + " " + str(folders.get(folder))
	print(text)
	f.write(text + ";")

f.close()

		


