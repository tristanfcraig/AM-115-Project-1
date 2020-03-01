import csv
import numpy as np
import pandas as pd
import random

states = ['IA','NH','TX']
# start_date = 
# end_date = 

data = pd.read_csv('Data/IA.csv', sep=',')
rows = data.shape[0]

clinton = data['Clinton']
sanders = data['Sanders']
#spread = clinton - sanders

for poll in range(0,rows):

	#if (is_number(clinton[poll])) and (is_number(sanders[poll])): 
	#	spread = clinton[poll] - spread[poll]
	
	print(sanders[poll])
	#spread.append()


	


#phi = .8
#c = .5 * (1 - phi)


#noiseeffect = .05 ## Noise will be (-noiseeffect, noiseeffect)

#numpolls = 8

#finals = []

#for k in range(100):
#  X = 0.58
#  for i in range(numpolls):
#    random.seed()
#    r = random.random()
#    noise = (r - 0.5) * (noiseeffect / 2)

    #X = c + (phi * X) + noise

  #finals.append(X)

#print(sum(finals) / len(finals))


