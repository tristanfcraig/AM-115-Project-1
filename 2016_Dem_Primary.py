import sys
import csv
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
	if len(sys.argv[1]) == 2:
		states = [sys.argv[1]]
else:
	states = ['AK','AR','AZ','CA','CO','CT','FL','GA','IA','IL','KY','LA','MD','MI','MN','MO','NC','NH','NJ','NV','NY','OH','OK','PA','TN','TX','UT','VA','WI']
# start_date = 
# end_date = 

for state in states:
	
	in_file = 'Data/' + state + '.csv'

	try:
	    df = pd.read_csv(in_file, sep=',')
	except IOError:
	    exit("No Data :(")


	df = df[df['Sanders'].astype(str).str.contains('-')==False]
	df = df[df['Clinton'].astype(str).str.contains('-')==False]
	
	clinton = df['Clinton'].tolist()
	sanders = df['Sanders'].tolist()
	t = []
	
	spread = []

	for i in range(0,len(clinton)):
		spread.append(float(clinton[i]) - float(sanders[i]))
		t.append(i)

	spread = spread[::-1]

	plt.figure()
	plt.plot(t,spread)
	out_file = 'Output/' + state + '.png'
	plt.savefig(out_file)

	