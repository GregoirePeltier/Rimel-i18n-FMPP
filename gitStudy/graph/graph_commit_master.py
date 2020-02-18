import numpy as np
from matplotlib import pyplot as plt

f = open("../output/output.txt", "r")
allLines = f.read();
f.close();

filesImpacted = [];
allLinesClean = allLines[:(allLines.rfind(';'))]
for line in allLinesClean.split('\n'):
	nameProject = line[:(line.find('='))].replace(" ","")
	nbFilesLoc = (line[(line.find('='))+1:]).replace(" ","").split(";")
	sumAllFile = 0
	for nbFileLoc in nbFilesLoc:
		sumAllFile += int(nbFileLoc);

	pourcentage = (sumAllFile / len(nbFileLoc)) * 100
	filesImpacted.append(pourcentage);


fig1, ax1 = plt.subplots()
ax1.set_title('Nombre de fichiers modifiés lors d\'un commit lié à la i10n')
ax1.boxplot(filesImpacted)