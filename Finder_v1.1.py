import os
import csv

def fWITH_SPECIAL_CHAR(vDIRETORIO, vDELIMITER, vSEARCH, vCONTADOR):
    for root, dirs, files in os.walk(vDIRETORIO):
        for name in files:
            if name[-4:] == '.csv':
                vCONTADOR += 1
                vCSV = root + '\\' + name
                with open(vCSV, 'r') as vARQUIVO:
                    vLER = csv.reader(vARQUIVO, delimiter=vDELIMITER)

                    for vLINHA in vLER:
                        for i in range(len(vLINHA)):
                            vINFO = vLINHA[i]
                            if vINFO.strip().upper() == vSEARCH.strip().upper():
                                print('{} | {}'.format(vCSV, vINFO))
    return vCONTADOR

def fWITHOUT_SPECIAL_CHAR(vDIRETORIO, vDELIMITER, vSEARCH, vCONTADOR):
    for root, dirs, files in os.walk(vDIRETORIO):
        for name in files:
            if name[-4:] == '.csv':
                vCONTADOR += 1
                vCSV = root + '\\' + name
                with open(vCSV, 'r') as vARQUIVO:
                    vLER = csv.reader(vARQUIVO, delimiter=vDELIMITER)

                    for vLINHA in vLER:
                        for i in range(len(vLINHA)):
                            vINFO = vLINHA[i]
                            vINFO = vINFO.strip().upper()
                            if vINFO == vSEARCH:
                                print('{} | {}'.format(vCSV, vINFO))
    return vCONTADOR

def fFORMAT_STRING(vSTRING):
    vSTRING = vSTRING.strip().upper().translate({ord(c): '' for c in '!@#$%^&*()[]{};:,./<>?\|`~-=_+"'})
    return vSTRING


vDIRETORIO = str(input('Path: '))
vDELIMITER = str(input('Delimiter: '))
vSEARCH = str(input('Text: '))
while True:
    vSPECIAL_CHAR = str(input('Special char [Y/N]: ')).upper()
    if (vSPECIAL_CHAR == 'Y' or vSPECIAL_CHAR == 'N'):
        break

vCONTADOR = 0

if vSPECIAL_CHAR == 'Y':
    print('\nSEARCHING FOR: {}\n'.format(vSEARCH))
    vCONTADOR = fWITH_SPECIAL_CHAR(vDIRETORIO, vDELIMITER, vSEARCH, vCONTADOR)
elif vSPECIAL_CHAR == 'N':
    vSEARCH = fFORMAT_STRING(vSEARCH)
    print('\nSEARCHING FOR: {}\n'.format(vSEARCH))
    vCONTADOR = fWITHOUT_SPECIAL_CHAR(vDIRETORIO, vDELIMITER, vSEARCH, vCONTADOR)
    

print('\nSearched for "{}" in {} files'.format(vSEARCH, vCONTADOR))

