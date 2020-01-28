from path import Path
import re

pattern = re.compile("^.+values(-[a-zA-Z]{1,3})+(\\+\\w{2,5})*\\\\.+$")
folders = {}
valueFolders = {}
for f in Path('../Projects').walkfiles():
	if pattern.match(f):
		valueFolder = f[0:(f.rfind('\\'))]
		resFolder = valueFolder[0:(valueFolder.rfind('\\'))]
		if valueFolder not in valueFolders:
			valueFolders[valueFolder] = 1
			if resFolder in folders:
				folders[resFolder] += 1
			else:
				folders[resFolder] = 1
		

f = open("result_properties_android.txt", "w")
for folder in folders:
	text = folder + " " + str(folders.get(folder))
	print(text)
	f.write(text + ";")

f.close()

		


