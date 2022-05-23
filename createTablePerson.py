
import bookHistory as b
import os
from os.path import isfile, join , isdir
import re

names = dict()
cities = dict()
gender = dict()




personsFile = open( 'persons.csv' )
for p in personsFile:
    col = re.split( ',' , p.strip())
    names[ col[1] ] = col[0]
    #print(col[1])
personsFile.close()


citiesFile = open( 'cities.csv' )
for c in citiesFile:
    col = re.split( ',' , c.strip())
    cities[ col[0] ] = col[1]
    #print(col[1])
citiesFile.close()

import pandas as pd

dataDir = 'Data'

personDf = pd.DataFrame()

def addDataFrame( df1 , df2 ):
    if df1.empty:
        df1 = df2.copy()
    else:
        df1 = pd.concat( [ df1 , df2 ] , sort=False )
        #personDf.append( df, ignore_index = True)
    return df1


for file in os.listdir( dataDir ):
    if file.endswith(".txt"):
        print(file)
        df = b.createPersonData( join( dataDir , file ) )
        personDf = addDataFrame( personDf , df )

        for row, column in personDf.iterrows():
                if re.search( '\w' , column['mother'] ):
                    gender[ column['mother'] ] = 'F'
                if re.search( '\w' , column['father'] ):
                    gender[ column['father'] ] = 'F'
        print( personDf.shape )



columns = list( personDf.columns  )

out = open( 'sql.csv' , 'w' )

out.write( 'INSERT INTO `PERSON` (`PID`, `firstName`, `secondName`, `lastName`, `dob`, `dod`, `pob`, `pod`, `burialPlace`, `sex`, `religion`, `profStart`, `profEnd`, `education`, `father`, `mother`) VALUES \n')




count = 0
for row, column in personDf.iterrows():
    count += 1

    fullName = b.findFullName(column)
    fullName = re.sub( ',' , '' , fullName )
    pid = names[ fullName ]

    if fullName in gender:
        column['sex'] = gender[fullName]

    if re.search( '\w' , column['father'] ):
        column['father'] = re.sub( ',' , '' , column['father'] )
        if column['father'].strip() in names:
            column['father'] = names[ column['father'].strip() ]
        else:
            print( column['father'] )
    if re.search( '\w' , column['mother'] ):
        column['mother'] = re.sub( ',' , '' , column['mother'] )
        if column['mother'].strip() in names:
            column['mother'] = names[ column['mother'].strip() ]
        else:
            print( column['mother'] )
    if column['pob'] in cities:
        column['pob'] = cities[ column['pob'] ]
    if column['pod'] in cities:
        column['pod'] = cities[ column['pod'] ]

    column['lastName'] = re.sub( r'Willemsz \(edinburgh' , 'Willemsz' , column['lastName'] )

    out.write( f'( ' )
    out.write(  f"'{pid}', " )
    for i , c in enumerate( columns ):
        if not( re.search( '\w' , column[c] ) ):
            out.write( ' NULL ' )
        else:
            out.write( f"'{ column[c] }'")
        if i != len(columns) -1:
            out.write(',')
    out.write( ' ) ')

    if count != len(personDf.index):
        out.write( ',' )
    out.write(' \n' )


out.close()
