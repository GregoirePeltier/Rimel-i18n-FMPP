import json

from path import Path
import re

patternForJsp = re.compile("^.+\\.jsp$")
patternForJava = re.compile("^.+\\.java$")
patternForProperties = re.compile("^.+\\.properties$")
patternForKey = re.compile("key='.+'")
patternForUnity = re.compile("msg\\.getMessage")
patternForAndroidReference = re.compile("getString\\(R\\.string\\.")
patternForFreePlane = re.compile("TextUtils\\.getText")
patternForRouteConverter = re.compile("(getBundle\\(\\)|bundle)\\.getString")

androidProjects = [
	"../Projects/andors-trail",
	"../Projects/android-app",
	"../Projects/Android-IMSI-Catcher-Detector",
	"../Projects/Android-Open-Radio",
	"../Projects/AndroidApp",
	"../Projects/apple-flinger",
	"../Projects/apps-android-commons",
	"../Projects/AsteroidOSSync",
	"../Projects/Blurify",
	"../Projects/boilr",
	"../Projects/chibe",
	"../Projects/DietDiaryApp",
	"../Projects/FeedTV",
	"../Projects/gdroidclient",
	"../Projects/getback_gps",
	"../Projects/ghini.pocket",
	"../Projects/ghini.tour",
	"../Projects/haven",
	"../Projects/KISS",
	"../Projects/lexica",
	"../Projects/locationprivacy",
	"../Projects/Logfly",
	"../Projects/loyalty-card-locker",
	"../Projects/Markdown-Notes",
	"../Projects/min-cal-widget",
	"../Projects/mtmods4android",
	"../Projects/NewPipe",
	"../Projects/obscuracam",
	"../Projects/OpenBikeSharing",
	"../Projects/OpenCircle",
	"../Projects/OpenRefine",
	"../Projects/openScale",
	"../Projects/Osmand",
	"../Projects/peertube-android",
	"../Projects/PixelKnot",
	"../Projects/RedReader",
	"../Projects/ripple",
	"../Projects/SkyTube",
	"../Projects/StarkeVerben",
	"../Projects/tasks",
	"../Projects/Tok-Android",
	"../Projects/TrebleShot",
	"../Projects/World-Weather",
	"../Projects/your-local-weather"
]

keyInFile = {}
listOfFile = []
for f in Path('../Projects/unity').walkfiles():
	if patternForJava.match(f):
		# print(f)
		file = open(f, "r")
		for line in file:
			if patternForUnity.search(line):
				listOfFile.append(f)
				# if len(listOfFile) == 0:
				# 	listOfFile.append({f: 0})
				# else:
				# 	alreadyExist = False
				# 	for item in listOfFile:
				# 		if item[f] is not None:
				# 			item[f] = item[f] + 1
				# 			alreadyExist = True
				# 			break
				# 	else:
				# 		listOfFile.append({f: 1})
				print(f)

keyInFile['../Projects/unity'] = listOfFile.copy()

listOfFile.clear()

for f in Path('../Projects/airsonic').walkfiles():
	if patternForJsp.match(f):
		# print(f)
		file = open(f, "r")
		for line in file:
			if patternForKey.search(line):
				listOfFile.append(f)
				print(f)

keyInFile['../Projects/airsonic'] = listOfFile.copy()

listOfFile.clear()

for f in Path('../Projects/freeplane').walkfiles():
	if patternForJava.match(f):
		# print(f)
		file = open(f, "r")
		for line in file:
			if patternForFreePlane.search(line):
				listOfFile.append(f)
				print(f)

keyInFile['../Projects/freeplane'] = listOfFile.copy()

listOfFile.clear()


for f in Path('../Projects/RouteConverter').walkfiles():
	if patternForJava.match(f):
		# print(f)
		file = open(f, "r")
		for line in file:
			if patternForRouteConverter.search(line):
				listOfFile.append(f)
				print(f)

keyInFile['../Projects/RouteConverter'] = listOfFile.copy()

listOfFile.clear()

for s in androidProjects:
	for f in Path(s).walkfiles():
		if patternForJava.match(f):
			# print(f)
			file = open(f, "r", encoding="utf8")
			for line in file:
				if patternForAndroidReference.search(line):
					listOfFile.append(f)
					print(f)
	keyInFile[s] = listOfFile.copy()
	listOfFile.clear()


f = open("result_key_in_java.json", "w")
# for folder in keyInFile:
# 	text = folder + " " + str(keyInFile.get(folder))
result = json.dumps(keyInFile, indent=4, sort_keys=True)
print(result)
f.write(result + "\n")

# f.close()
#
# x = len(keyInFile)
# y = [i for i in x]
# y_2 = [i**2 for i in x]
# y_3 = [i**3 for i in x]
#
# print(x)
#
# plt.plot(x, y, label='linear')
# plt.plot(x, y_2, label='quadratic')
# plt.plot(x, y_3, label='cubic')
#
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.show()