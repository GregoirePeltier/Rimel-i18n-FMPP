import numpy as np
from matplotlib import pyplot as plt

f = open("../output/output.txt", "r")
allLines = f.read();
f.close();


commitsLoc = [];
commits = [];
names = [];
allLinesClean = allLines[:(allLines.rfind(';'))]
for line in allLinesClean.split('\n'):
	nameProject = line[:(line.find('='))].replace(" ","")
	names.append(nameProject)

	commitLoc = (line[(line.find('='))+1:line.find('/')]).replace(" ","")
	commit = (line[(line.find('/'))+1:]).replace(" ","")
	pourcentageLoc = (float(commitLoc) / float(commit)) * 100


	print(pourcentageLoc);
	commitsLoc.append(int(pourcentageLoc))

	

	commits.append(int(commit))


ind = np.arange(len(names))
width = 0.50
p1 = plt.bar(ind, tuple(commits), width)
p2 = plt.bar(ind, tuple(commitsLoc), width, bottom=tuple(commits))

plt.ylabel('Nombre de commits liés à la localisation par rapport au nombre de commits sur la branche master')
plt.title('')
plt.xticks(ind, tuple(names), rotation='vertical')
plt.legend((p1[0], p2[0]), ('Nb commits', 'Commits localisation'))

plt.show()