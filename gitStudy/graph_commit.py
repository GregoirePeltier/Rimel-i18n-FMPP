# Example adapté de https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
import numpy as np
from matplotlib import pyplot as plt

f = open("output/output.txt", "r")

data = {}
for line in f:
	commitValues = (line[(line.rfind('='))+1:]).replace(" ","");
	name = (line[:(line.rfind('='))]).replace(" ","");
	commitLoc = float(commitValues[:commitValues.rfind('/')]);
	commit = float(commitValues[commitValues.rfind('/')+1:]);
	if(commitLoc != 0 and commit != 0):
		sub = (commitLoc/commit)*100;
		data[name] = sub;


f.close();

names = list(data.keys())
values = list(data.values())

plt.bar(names, values);
plt.show();
