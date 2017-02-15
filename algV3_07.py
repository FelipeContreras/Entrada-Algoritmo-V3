"""
Implementacion del Algoritmo de Daniel Nieto v3

Salida para el ejemplo:
Escherichia coli is able to use trehalose [O-U-D-glucosyl-a-D-glucoside] as a
carbon source when grown in high-osmolarity medium.

Escherichia coli is able to can also synthesize trehalose as an osmoprotectant when
grown in high-osmolarity medium.

Escherichia coli is able to can also accumulate trehalose as an osmoprotectant when
grown in high-osmolarity medium.
"""

import copy
import sys


class Simp(object):
  TYPE=""
  TEXT=""
#  COMP=["","",""]
  COMP=[]

class Frase(object):
  TYPE=""
  TEXT=""
  POS=""
  TREE=""
#  SIMP=[Simp(),Simp()]
  SIMP=[]

class Sentence(object):
  TEXT=""
  TREE=""
  SIMP=[]
  
MEMORIAB=[]
sentencepru=Frase()

#----lectura de datos desde archivo
arch=(sys.argv[1])
f = open(arch)
dato = f.read().splitlines()
f.close
#print "len",len(dato),"\n","dato",dato
numSimp=-1
#numCOMP=-1
for i in range(len(dato)):
  if 'TYPE: ' in dato[i][0:6]:
    sentencepru.TYPE=copy.deepcopy(dato[i][6:])
  elif 'TEXT: ' in dato[i][0:6]:
    sentencepru.TEXT=copy.deepcopy(dato[i][6:])
  elif 'POS : ' in dato[i][0:6]:
    sentencepru.POS=copy.deepcopy(dato[i][6:])
  elif 'TREE: ' in dato[i][0:6]:
    sentencepru.TREE=copy.deepcopy(dato[i][6:])
  elif 'SIMP:' in dato[i]:
    sentencepru.SIMP.append(Simp())
    numSimp = numSimp+1
    numCOMP=-1
  elif '  TYPE: ' in dato[i][0:8]:
    sentencepru.SIMP[numSimp].TYPE=copy.deepcopy(dato[i][8:])
#    print "SIMP.TYPE",sentencepru.SIMP[numSimp].TYPE
  elif '  TEXT: ' in dato[i][0:8]:
    sentencepru.SIMP[numSimp].TEXT=copy.deepcopy(dato[i][8:])
#    print "SIMP.TEXT",sentencepru.SIMP[numSimp].TEXT
  elif '  COMP: ' in dato[i][0:8]:  
    sentencepru.SIMP[numSimp].COMP.append('')
    numCOMP=numCOMP+1
    sentencepru.SIMP[numSimp].COMP[numCOMP]=copy.deepcopy(dato[i][8:])
    
    print "numSimp",numSimp
    print "COMP[",numSimp,"]",sentencepru.SIMP[numSimp].COMP
    
    


print "TYPE= ",sentencepru.TYPE
print "TEXT= ",sentencepru.TEXT
print "POS = ",sentencepru.POS
print "TREE= ",sentencepru.TREE
print "SIMP[0].TYPE= ",sentencepru.SIMP[0].TYPE
print "SIMP[0].TEXT= ",sentencepru.SIMP[0].TEXT
print "SIMP[0].COMP[0]= ",sentencepru.SIMP[0].COMP[0]
print "SIMP[0].COMP[1]= ",sentencepru.SIMP[0].COMP[1]
print "SIMP[0].COMP[2]= ",sentencepru.SIMP[0].COMP[2]
print "SIMP[1].TYPE= ",sentencepru.SIMP[1].TYPE
print "SIMP[1].TEXT= ",sentencepru.SIMP[1].TEXT
print "SIMP[1].COMP[0]= ",sentencepru.SIMP[1].COMP[0]
print "SIMP[1].COMP[1]= ",sentencepru.SIMP[1].COMP[1]
print "SIMP[1].COMP[2]= ",sentencepru.SIMP[1].COMP[2]
print "SIMP[1].COMP[2]= ",sentencepru.SIMP[1].COMP[3]




#-----------parte para poner los datos desde archivo

