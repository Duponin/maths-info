#!/usr/bin/python

autodestruction = 0.99964
populationOriginale = pow(10, 7)
population = populationOriginale
jourDemieVie=0

while population >= (populationOriginale / 2):
    population = population * autodestruction
    jourDemieVie += 1

print(jourDemieVie)
