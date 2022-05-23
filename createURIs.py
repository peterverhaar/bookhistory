
import bookHistory as b
import os
from os.path import isfile, join , isdir
import re


dataDir = 'Data'

allNames = dict()
personId = dict()

with open("pids.txt",'w') as f:
    pass




unique = dict()

for file in os.listdir( dataDir ):
    if file.endswith(".txt"):
        #print(file)
        names = b.findAllNames( join( dataDir , file ))
        for n in names:
            if re.search( '\w' , n ):
                allNames[n] = allNames.get( n , 0 ) + 1


#Find solution for name variants
#182458705189,IJsbrand Buys
#236736417201,IJsbrant Buijs


for n in allNames:
    personId[n] = b.createPID()

out = open( 'persons.csv' , 'w' )

for n in sorted( allNames ):
    np = re.sub( ',' , '' , n )
    out.write( f'{personId[n]},{np}\n' )

out.close()

cities = open( 'city.txt' )
out = open( 'cities.csv' , 'w' )

for c in cities:
    out.write( f'{ c.strip() },C{ b.createPID() }\n' )

out.close()
