import os
import csv

vDIRETORIO = str(input('Path: '))
vDELIMITER = str(input('Delimiter: '))
vPROCURA = str(input('Text: '))
vCONTADOR = 0

for root, dirs, files in os.walk(vDIRETORIO):
    for name in files:
        if name[-4:] == '.csv':
            print('=' * len(name))
            print(name)
            vCONTADOR += 1
            vCSV = root + '\\' + name
            with open(vCSV, 'r') as vARQUIVO:
                vLER = csv.reader(vARQUIVO, delimiter=vDELIMITER)

                for vLINHA in vLER:
                    for i in range(len(vLINHA)):
                        vINFO = vLINHA[i]
                        if vINFO.strip() == vPROCURA.strip():
                            print('{} | {}'.format(vCSV, vINFO))
                
print('\nProcurado em {} arquivos'.format(vCONTADOR))
print('FIM\n')