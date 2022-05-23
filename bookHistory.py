

import re
import string
import pandas as pd

import hashlib
m = hashlib.md5()


labels_dict = dict()
labels_dict["Achternaam"] = "familyName"
labels_dict["Beroep"] = "Occupation"
labels_dict["Datum Aanstelling"] = "dateEmplyment"
labels_dict["Datum huwelijk"] = "dateMariage"
labels_dict["Datum veiling"] = "dateAuction"
labels_dict["Doop_getuigen"] = "baptismWitness"
labels_dict["Eind_werkperiode"] = "endProfessionalActivity"
labels_dict["Einddatum"] = "nan"
labels_dict["Functie in het gilde"] = "guildFunction"
labels_dict["Functie werknemer"] = "function"
labels_dict["Geboortedatum"] = "birthDate"
labels_dict["Geboorteplaats"] = "birthPlace"
labels_dict["Geslacht"] = "gender"
labels_dict["Getuigen"] = "witness"
labels_dict["Geveilde collectie"] = "collectionAuction"
labels_dict["Gilde"] = "nan"
labels_dict["Gilde_InDienstVan"] = "guildEmployedBy"
labels_dict["Gilde_Literatuur"] = "nan"
labels_dict["Huwelijkspartner"] = "marriedTo"
labels_dict["Kind_doop"] = "nan"
labels_dict["Kind_naam"] = "hasChild"
labels_dict["Locatie"] = "location"
labels_dict["Locatie_startdatum"] = "location_start"
labels_dict["Misc"] = "note"
labels_dict["Naam werknemer"] = "nameEmployee"
labels_dict["Plaats van overlijden"] = "deathPlace"
labels_dict["Soort huwelijk"] = "marriageType"
labels_dict["Start_werkperiode"] = "startProfessionalActivity"
labels_dict["Startdatum"] = "startDate"
labels_dict["Sterfdatum"] = "deathDate"
labels_dict["Tweede naam"] = "secondName"
labels_dict["Voornaam"] = "givenName"
labels_dict["Naamsvariant"] = "variantName"
labels_dict["Bron"] = "source"
labels_dict["Literature"] = "Literature"
labels_dict["Doop kind"] = "BaptismChild"
labels_dict["Naam kind"] = "NameChild"
labels_dict["Religie"] = "religion"
labels_dict["Adres"] = "address"
labels_dict["Geboortedatum kind"] = "birthDateChild"
labels_dict["Locatie_einddatum"] = "locationEndDate"
labels_dict["Kinderen"] = "children"
labels_dict["Vader"] = "father"
labels_dict["Moeder"] = "mother"
labels_dict["STCN"] = "stcn"
labels_dict["Begraafplaats"] = "burialPlace"






def getText( label , line):
    text = re.sub( r'^' + label + ':\s?' , '' , line , re.IGNORECASE )
    text = text.strip()
    text = text.strip( string.punctuation )
    return text



def findNameParts( name ):

    name = re.sub( r'\(' , '' , name )
    name = re.sub( r'\)' , '' , name )
    name = re.sub( r'\-' , '' , name )

    parts = re.split( '\s+' , name )
    firstName = parts[0].strip()
    lastName = parts[-1].strip()

    name = re.sub( r'^{}'.format( parts[0] ) , '' , name )
    name = re.sub(  r'{}$'.format(parts[-1])  , '' , name )
    return ( firstName, lastName , name.strip() )




def createData2( lines ):

    data = dict()

    for line in lines:
        if re.search( '^Voornaam:' , line , re.IGNORECASE ):
            data["firstName"] = getText('Voornaam' , line )
            data["firstName"] = re.sub( '(\[)|(\])' , '' , data["firstName"] )
            #print( data["firstName"] )
        elif re.search( '^Tweede naam:' , line , re.IGNORECASE ):
            data["secondName"] = getText('Tweede naam' , line )
            data["secondName"] = re.sub( '(\[)|(\])' , '' , data["secondName"] )
        elif re.search( '^Achternaam:' , line , re.IGNORECASE ):
            data["lastName"] = getText('Achternaam' , line )
            data["lastName"] = re.sub( '(\[)|(\])' , '' , data["lastName"] )
        elif re.search( '^Geboortedatum:' , line , re.IGNORECASE ):
            data["dob"] = getText('Geboortedatum' , line )
        elif re.search( '^Sterfdatum:' , line , re.IGNORECASE ):
            data["dod"] = getText('Sterfdatum' , line )
        elif re.search( '^Geboorteplaats:' , line , re.IGNORECASE ):
            data['pob'] = getText('Geboorteplaats' , line )
            data['pob'] = data['pob'].lower()
        elif re.search( '^Plaats van overlijden:' , line , re.IGNORECASE ):
            data['pod'] = getText('Plaats van overlijden' , line )
            data['pod'] = data['pod'].lower()
        elif re.search( '^Geslacht:' , line , re.IGNORECASE ):
            data["sex"] = getText('Geslacht' , line )
        elif re.search( '^Start_werkperiode:' , line , re.IGNORECASE ):
            data["profStart"] = getText('Start_werkperiode' , line )
        elif re.search( '^Eind_werkperiode:' , line , re.IGNORECASE ):
            data["profEnd"] = getText('Eind_werkperiode' , line )
        elif re.search( '^Religie:' , line , re.IGNORECASE ):
            data["religion"] = getText('Religie' , line )
        elif re.search( '^Begraafplaats:' , line , re.IGNORECASE ):
            data["burialPlace"] = getText('Begraafplaats' , line )
        elif re.search( '^Datum doop:' , line , re.IGNORECASE ):
            data["dateBaptism"] = getText('Datum doop' , line )
        elif re.search( '^Album studiosorum:' , line , re.IGNORECASE ):
            data["education"] = getText('Album studiosorum' , line )
        elif re.search( '^Weeskamer:' , line , re.IGNORECASE ):
            data["orphanage"] = getText('Weeskamer' , line )

        elif re.search( '^STCN:' , line , re.IGNORECASE ):
            data["stcn"] = getText('STCN' , line )
        elif re.search( '^Vader:' , line , re.IGNORECASE ):
            data["father"] = getText('Vader' , line )
        elif re.search( '^Moeder:' , line , re.IGNORECASE ):
            data["mother"] = getText('Moeder' , line )

    return data



def createData( lines ):

    data = dict()

    for line in lines:
        if re.search( '^Voornaam:' , line , re.IGNORECASE ):
            data["firstName"] = getText('Voornaam' , line )
            data["firstName"] = re.sub( '(\[)|(\])' , '' , data["firstName"] )
            #print( data["firstName"] )
        elif re.search( '^Tweede naam:' , line , re.IGNORECASE ):
            data["secondName"] = getText('Tweede naam' , line )
            data["secondName"] = re.sub( '(\[)|(\])' , '' , data["secondName"] )
        elif re.search( '^Achternaam:' , line , re.IGNORECASE ):
            data["lastName"] = getText('Achternaam' , line )
            data["lastName"] = re.sub( '(\[)|(\])' , '' , data["lastName"] )
        elif re.search( '^Geboortedatum:' , line , re.IGNORECASE ):
            data["dob"] = getText('Geboortedatum' , line )
        elif re.search( '^Sterfdatum:' , line , re.IGNORECASE ):
            data["dod"] = getText('Sterfdatum' , line )
        elif re.search( '^Geboorteplaats:' , line , re.IGNORECASE ):
            data['pob'] = getText('Geboorteplaats' , line )
            data['pob'] = data['pob'].lower()
        elif re.search( '^Plaats van overlijden:' , line , re.IGNORECASE ):
            data['pod'] = getText('Plaats van overlijden' , line )
            data['pod'] = data['pod'].lower()
        elif re.search( '^Geslacht:' , line , re.IGNORECASE ):
            data["sex"] = getText('Geslacht' , line )
        elif re.search( '^Start_werkperiode:' , line , re.IGNORECASE ):
            data["profStart"] = getText('Start_werkperiode' , line )
        elif re.search( '^Eind_werkperiode:' , line , re.IGNORECASE ):
            data["profEnd"] = getText('Eind_werkperiode' , line )
        elif re.search( '^Religie:' , line , re.IGNORECASE ):
            data["religion"] = getText('Religie' , line )
        elif re.search( '^Begraafplaats:' , line , re.IGNORECASE ):
            data["burialPlace"] = getText('Begraafplaats' , line )
        elif re.search( '^Datum doop:' , line , re.IGNORECASE ):
            data["dateBaptism"] = getText('Datum doop' , line )
        elif re.search( '^Album studiosorum:' , line , re.IGNORECASE ):
            data["education"] = getText('Album studiosorum' , line )
        elif re.search( '^Weeskamer:' , line , re.IGNORECASE ):
            data["orphanage"] = getText('Weeskamer' , line )

        elif re.search( '^STCN:' , line , re.IGNORECASE ):
            data["stcn"] = getText('STCN' , line )
        elif re.search( '^Vader:' , line , re.IGNORECASE ):
            data["father"] = getText('Vader' , line )
        elif re.search( '^Moeder:' , line , re.IGNORECASE ):
            data["mother"] = getText('Moeder' , line )

    return data


def findFullName(data):
    fullName = data.get( 'firstName' , '' )
    fullName += ' ' + data.get( 'secondName' , '' )
    fullName += ' ' + data.get( 'lastName' , '' )
    fullName = re.sub( '\s+' , ' ' , fullName )
    return fullName.strip()

def standardiseName( text ):
    if re.search( ',' , text ):
        text = text[ 0 : text.index(',') ]
    if re.search( '\[' , text  ):
        text = text [ 0 : text.index('[') ]
    if re.search( r'\(' , text  ):
        text = text [ 0 : text.index('(') ]

    text = re.sub(  r'voor\s+\d+\s+jaar' , '' , text , re.IGNORECASE )
    return text.strip()


def analyseName( text ):

    data = dict()
    parts = re.split( '\s+' , text )
    data['firstName'] = parts[0].strip()
    data['lastName'] = parts[-1].strip()
    text = re.sub( r'^' + parts[0] , '' , text )
    text = re.sub( parts[-1] + '$', '' , text )
    data['secondName'] = text.strip()
    return data


def findAllNames( file ):

    allNames = dict()

    count = 0

    archive = open( file )
    recordLines = []

    for line in archive:
        #print(line)
        if not(re.search( '\w' , line.strip() ) ):
            if len(recordLines) > 0:
                count += 1
                data = createData( recordLines )
                fullName = findFullName( data )
                allNames[ fullName ] = allNames.get( fullName , 0 ) + 1
                if 'father' in data:
                    father = standardiseName( data['father'] )
                    allNames[ father ] = allNames.get( father , 0 ) + 1
                if 'mother' in data:
                    mother = standardiseName( data['mother'] )
                    allNames[ mother ] = allNames.get( mother , 0 ) + 1

                for line in recordLines:
                    if re.search( '^Gilde_InDienstVan:' , line , re.IGNORECASE ):
                        employer = getText('Gilde_InDienstVan' , line )
                        employer = standardiseName( employer )
                        if re.search( '\w' , employer ):
                            allNames[ employer ] = allNames.get( employer , 0 ) + 1
                    elif re.search( '^Huwelijkspartner:' , line , re.IGNORECASE ):
                        spouse = getText('Huwelijkspartner' , line )
                        spouse = standardiseName( spouse )
                        if re.search( '\w' , spouse ):
                            allNames[ spouse ] = allNames.get( spouse , 0 ) + 1
                    elif re.search( '^Naam werknemer:' , line , re.IGNORECASE ):
                        employee = getText('Naam werknemer' , line )
                        employee = standardiseName( employee )
                        #print(employee)
                        if re.search( '\w' , employee ):
                            allNames[ employee ] = allNames.get( employee , 0 ) + 1



                recordLines = []

        else:
            recordLines.append( line.strip() )

    if len(recordLines) > 0:

        data = createData( recordLines )
        fullName = findFullName( data )
        allNames[ fullName ] = allNames.get( fullName , 0 ) + 1
        if 'father' in data:
            father = standardiseName( data['father'] )
            allNames[ father ] = allNames.get( father , 0 ) + 1
        if 'mother' in data:
            mother = standardiseName( data['mother'] )
            allNames[ mother ] = allNames.get( mother , 0 ) + 1
        recordLines = []

    #print( count )
    return allNames


def findAllProfessions( file ):

    professions = dict()
    archive = open( file )

    recordLines = []

    for line in archive:
        #print(line)
        if not(re.search( '\w' , line.strip() ) ):
            if len(recordLines) > 0:
                for field in recordLines:
                    if re.search( '^Beroep:' , field , re.IGNORECASE ):
                        pr = getText('Beroep' , field )
                        if re.search( '\w' , pr ):
                            pr = pr.strip()
                            pr = pr.title()
                            professions[ pr ] = professions.get( pr , 0 ) + 1
                recordLines = []

        else:
            recordLines.append( line.strip() )

    if len(recordLines) > 0:

        for field in recordLines:
            if re.search( '^Beroep:' , field , re.IGNORECASE ):
                pr = getText('Beroep' , field )
                if re.search( '\w' , pr ):
                    pr = pr.strip()
                    pr = pr.title()
                    professions[ pr ] = professions.get( pr , 0 ) + 1
        recordLines = []

    return professions



def findAllCities( file ):

    cities = dict()
    archive = open( file )

    recordLines = []

    for line in archive:
        #print(line)
        if not(re.search( '\w' , line.strip() ) ):
            if len(recordLines) > 0:
                data = createData( recordLines )
                if 'pob' in data:
                    #print( data['pob']  )
                    cities[ data['pob'] ] = cities.get( data['pob'] , 0 ) + 1
                if 'pod' in data:
                    #print( data['pod']  )
                    cities[ data['pod'] ] = cities.get( data['pod'] , 0 ) + 1
                recordLines = []

        else:
            recordLines.append( line.strip() )

    if len(recordLines) > 0:

        data = createData( recordLines )
        if 'pob' in data:
            cities[ data['pob'] ] = cities.get( data['pob'] , 0 ) + 1
        if 'pod' in data:
            cities[ data['pod'] ] = cities.get( data['pod'] , 0 ) + 1
        recordLines = []

    return cities




def createPersonData( file ):

    columnString = '''firstName
    secondName
    lastName
    dob
    dod
    pob
    pod
    burialPlace
    sex
    religion
    profStart
    profEnd
    education
    father
    mother'''

    columnNames = re.split( '\s+' , columnString )

    df = pd.DataFrame( columns= columnNames )

    archive = open( file )
    recordLines = []

    for line in archive:
        #print(line)
        if not(re.search( '\w' , line.strip() ) ):
            if len(recordLines) > 0:

                data = createData( recordLines )
                newData = dict()
                for c in columnNames:
                    newData[c] = data.get( c , '' )
                if re.search( '\w' , data.get( 'lastName' , '' ) ):
                    df = df.append( newData , ignore_index=True)
                recordLines = []

        else:
            recordLines.append( line.strip() )

    if len(recordLines) > 0:

        data = createData( recordLines )
        newData = dict()
        for c in columnNames:
            newData[c] = data.get( c , '' )
        if re.search( '\w' , data.get( 'lastName' , '' ) ):
            df = df.append( newData , ignore_index=True)
        recordLines = []

    return df


def writeDfData( data , columns ):

    dfData = dict()

    for c in columns:
        dfData[c] = data.get( c , '' )

    return dfData


def writeGuildData( fullName , data , columns ):

    dfData = dict()

    for c in columns:
        dfData[c] = data.get( c , '' )

    dfData['fullName'] = fullName

    return dfData




def createTablePersonnel( file ):

    columnString = '''employee
    startDate
    function
    employedBy
    source'''
    columnNames = re.split( '\s+' , columnString )

    df = pd.DataFrame( columns= columnNames )

    archive = open( file )
    recordLines = []

    for line in archive:

        if not(re.search( '\w' , line.strip() ) ):
            if len(recordLines) > 0:

                personnel = dict()
                data = dict()

                for field in recordLines:
                    if re.search( '^Voornaam:' , field , re.IGNORECASE ):
                        data["firstName"] = getText('Voornaam' , field )
                        data["firstName"] = re.sub( '(\[)|(\])' , '' , data["firstName"] )
                    elif re.search( '^Tweede naam:' , field , re.IGNORECASE ):
                        data["secondName"] = getText('Tweede naam' , field )
                        data["secondName"] = re.sub( '(\[)|(\])' , '' , data["secondName"] )
                    elif re.search( '^Achternaam:' , field , re.IGNORECASE ):
                        data["lastName"] = getText('Achternaam' , field )
                        data["lastName"] = re.sub( '(\[)|(\])' , '' , data["lastName"] )

                personnel['employedBy'] = findFullName(data)

                for field in recordLines:
                    if re.search( '^Datum Aanstelling:' , field , re.IGNORECASE ):
                        column = 'startDate'
                        #print(column)
                        #if column in personnel:
                        #    personnelDf = writeDfData( personnel , columnNames )
                        #    df = df.append( personnelDf , ignore_index=True)
                        #    personnel = dict()
                        personnel['startDate'] = getText('Datum Aanstelling' , field )
                    elif re.search( '^Naam werknemer:' , field , re.IGNORECASE ):
                        personnel['employee'] = standardiseName( getText('Naam werknemer' , field ) )
                    elif re.search( '^Functie werknemer:' , field , re.IGNORECASE ):
                        personnel['function'] = getText('Functie werknemer' , field )
                    elif re.search( '^Personeel' , field , re.IGNORECASE ):
                        if len(personnel) > 1:
                            personnelDf = writeDfData( personnel , columnNames )
                            #print(personnel['employedBy'],personnel['employee'])
                            #for p in personnel:
                            #    print( p , personnel[p] )
                            #print('\n\n')
                            df = df.append( personnelDf , ignore_index=True)
                            personnel = dict()
                            personnel['employedBy'] = findFullName(data)


                if len(personnel) > 1:
                    personnelDf = writeDfData( personnel , columnNames )
                    df = df.append( personnelDf , ignore_index=True)
                    personnel = dict()

                recordLines = []
        else:
            recordLines.append( line.strip() )

    return df





def createTableGuild( file ):

    columnString = '''startDate
    function
    employer
    source'''
    columnNames = re.split( '\s+' , columnString )

    df = pd.DataFrame( columns= columnNames )

    archive = open( file )
    recordLines = []

    for line in archive:

        if not(re.search( '\w' , line.strip() ) ):
            if len(recordLines) > 0:

                guild = dict()
                data = dict()

                for field in recordLines:
                    if re.search( '^Voornaam:' , field , re.IGNORECASE ):
                        data["firstName"] = getText('Voornaam' , field )
                        data["firstName"] = re.sub( '(\[)|(\])' , '' , data["firstName"] )
                    elif re.search( '^Tweede naam:' , field , re.IGNORECASE ):
                        data["secondName"] = getText('Tweede naam' , field )
                        data["secondName"] = re.sub( '(\[)|(\])' , '' , data["secondName"] )
                    elif re.search( '^Achternaam:' , field , re.IGNORECASE ):
                        data["lastName"] = getText('Achternaam' , field )
                        data["lastName"] = re.sub( '(\[)|(\])' , '' , data["lastName"] )

                fullName = findFullName(data)

                for field in recordLines:
                    if re.search( '^Startdatum:' , field , re.IGNORECASE ):
                        column = 'startDate'
                        #print(column)
                        if column in guild:
                            guildDf = writeGuildData( fullName , guild , columnNames )
                            df = df.append( guildDf , ignore_index=True)
                            guild = dict()
                        guild[column] = getText('Startdatum' , field )
                    elif re.search( '^Functie in het gilde:' , field , re.IGNORECASE ):
                        column = 'function'
                        if column in guild:
                            guildDf = writeGuildData( fullName , guild , columnNames )
                            df = df.append( guildDf , ignore_index=True)
                            guild = dict()
                        guild[column] = getText('Functie in het gilde' , field )
                    elif re.search( '^Gilde_InDienstVan:' , field , re.IGNORECASE ):
                        column = 'employer'
                        if column in guild:
                            guildDf = writeGuildData( fullName , guild , columnNames )
                            df = df.append( guildDf , ignore_index=True)
                            guild = dict()
                        guild[column] = getText('Gilde_InDienstVan' , field )
                    elif re.search( '^Gilde_Literatuur:' , field , re.IGNORECASE ):
                        column = 'source'
                        if column in guild:
                            guildDf = writeGuildData( fullName , guild , columnNames )
                            df = df.append( guildDf , ignore_index=True)
                            guild = dict()
                        guild[column] = getText('Gilde_Literatuur' , field )

                if len(guild) > 0:
                    guildDf = writeGuildData( fullName , guild , columnNames )
                    df = df.append( guildDf , ignore_index=True)
                    guild = dict()

                recordLines = []
        else:
            recordLines.append( line.strip() )

    return df



def createTableEmployment( file ):

    columnString = '''person
    profession
    startDate'''

    columnNames = re.split( '\s+' , columnString )

    df = pd.DataFrame( columns= columnNames )

    archive = open( file )
    recordLines = []

    for line in archive:

        if not(re.search( '\w' , line.strip() ) ):
            if len(recordLines) > 0:

                empl = dict()
                data = dict()

                for field in recordLines:
                    if re.search( '^Voornaam:' , field , re.IGNORECASE ):
                        data["firstName"] = getText('Voornaam' , field )
                        data["firstName"] = re.sub( '(\[)|(\])' , '' , data["firstName"] )
                    elif re.search( '^Tweede naam:' , field , re.IGNORECASE ):
                        data["secondName"] = getText('Tweede naam' , field )
                        data["secondName"] = re.sub( '(\[)|(\])' , '' , data["secondName"] )
                    elif re.search( '^Achternaam:' , field , re.IGNORECASE ):
                        data["lastName"] = getText('Achternaam' , field )
                        data["lastName"] = re.sub( '(\[)|(\])' , '' , data["lastName"] )

                fullName = findFullName(data)

                for field in recordLines:
                    if re.search( '^Beroep:' , field , re.IGNORECASE ):
                        prof = getText('Beroep' , field )
                        df = df.append( {'fullName':fullName,'profession':prof,'startDate':''}, ignore_index=True)

                recordLines = []
        else:
            recordLines.append( line.strip() )

    return df






def createPID():
    new_pid = 1

    pids = []

    with open('pids.txt') as pids_file:
        for pid in pids_file:
            pids.append(pid)

    pids = sorted(pids)

    #print(len(pids))
    if len(pids) > 0:
        highest = int( pids[-1].strip("0") )
        #print('H' , highest)
        new_pid = highest + 1
        #print(new_pid)
    new_pid = str(new_pid).zfill(12)
    with open('pids.txt' , 'a' , encoding = 'utf-8' ) as pid_file:
        pid_file.write( f'{new_pid}\n' )
    return(new_pid )
