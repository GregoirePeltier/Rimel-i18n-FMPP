import json
from collections import Counter

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
totalNbFile = 0
totalNbFileWithKey = 0
javaFileNb = 0
cnt = Counter()
for f in Path('../Projects/unity').walkfiles():
	if patternForJava.match(f):
		# print(f)
		javaFileNb += 1
		file = open(f, "r")
		for line in file:
			if patternForUnity.search(line):
				cnt[f] += 1
				print(f)

keyInFile['../Projects/unity'] = {
	"totalNbFile": javaFileNb,
	"listOfFileWithKey": cnt.copy(),
	"totalNbFileWithKey": len(cnt),
	"average": (len(cnt) / javaFileNb) * 100
}

totalNbFile += javaFileNb
totalNbFileWithKey += len(cnt)
jspFileNb = 0
cnt = Counter()

for f in Path('../Projects/airsonic').walkfiles():
	if patternForJsp.match(f):
		# print(f)
		jspFileNb += 1
		file = open(f, "r")
		for line in file:
			if patternForKey.search(line):
				cnt[f] += 1
				print(f)

keyInFile['../Projects/airsonic'] = {
	"totalNbFile": jspFileNb,
	"listOfFileWithKey": cnt.copy(),
	"totalNbFileWithKey": len(cnt),
	"average": (len(cnt) / jspFileNb) * 100
}

totalNbFile += javaFileNb
totalNbFileWithKey += len(cnt)
javaFileNb = 0
cnt = Counter()
for f in Path('../Projects/freeplane').walkfiles():
	if patternForJava.match(f):
		javaFileNb += 1
		# print(f)
		file = open(f, "r")
		for line in file:
			if patternForFreePlane.search(line):
				cnt[f] += 1
				print(f)

keyInFile['../Projects/freeplane'] = {
	"totalNbFile": javaFileNb,
	"listOfFileWithKey": cnt.copy(),
	"totalNbFileWithKey": len(cnt),
	"average": (len(cnt) / javaFileNb) * 100
}

totalNbFile += javaFileNb
totalNbFileWithKey += len(cnt)
javaFileNb = 0
cnt = Counter()
for f in Path('../Projects/RouteConverter').walkfiles():
	if patternForJava.match(f):
		javaFileNb += 1
		# print(f)
		file = open(f, "r")
		for line in file:
			if patternForRouteConverter.search(line):
				cnt[f] += 1
				print(f)

keyInFile['../Projects/RouteConverter'] = {
	"totalNbFile": javaFileNb,
	"listOfFileWithKey": cnt.copy(),
	"totalNbFileWithKey": len(cnt),
	"average": (len(cnt) / javaFileNb) * 100
}



totalNbFile += javaFileNb
totalNbFileWithKey += len(cnt)

keyInFile["Java stat"] = {
	"totalNbFile": totalNbFile,
	"totalNbFileWithKey": totalNbFileWithKey,
	"average": (totalNbFileWithKey / totalNbFile) * 100
}

javaFileNb = 0
cnt = Counter()
totalNbFile = 0
totalNbFileWithKey = 0
for s in androidProjects:
	for f in Path(s).walkfiles():
		if patternForJava.match(f):
			javaFileNb += 1
			# print(f)
			file = open(f, "r", encoding="utf8")
			for line in file:
				if patternForAndroidReference.search(line):
					cnt[f] += 1
					print(f)
	keyInFile[s] = {
		"totalNbFile": javaFileNb,
		"listOfFileWithKey": cnt.copy(),
		"totalNbFileWithKey": len(cnt),
		"average": (len(cnt) / javaFileNb) * 100
	}
	totalNbFile += javaFileNb
	totalNbFileWithKey += len(cnt)
	javaFileNb = 0
	cnt.clear()
keyInFile["Android stat"] = {
	"totalNbFile": totalNbFile,
	"totalNbFileWithKey": totalNbFileWithKey,
	"average": (totalNbFileWithKey / totalNbFile) * 100
}

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