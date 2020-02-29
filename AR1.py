import random

# states = []
# start_date = 
# end_date = 

phi = .8
c = .5 * (1 - phi)


noiseeffect = .05 ## Noise will be (-noiseeffect, noiseeffect)

numpolls = 8

finals = []

for k in range(100):
  X = 0.58
  for i in range(numpolls):
    random.seed()
    r = random.random()
    noise = (r - 0.5) * (noiseeffect / 2)

    X = c + (phi * X) + noise

  finals.append(X)

print(sum(finals) / len(finals))


