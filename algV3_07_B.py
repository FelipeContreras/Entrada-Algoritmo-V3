
import copy
import sys


class Simp(object):
  def __init__(self):
    self.TYPE=""
    self.TEXT=""
    self.COMP=[]

  def agregarTYPE(self,Type):
    self.TYPE=Type

  def agregarTEXT(self,text):
    self.TEXT=text

  def agregarCOMP(self,comp):
    self.COMP.append(comp)

class Frase(object):
  def __init__(self):
    self.TYPE=""
    self.TEXT=""
    self.POS=""
    self.TREE=""
    self.SIMP=[]

  def agregarTYPE(self,Type):
    self.TYPE=Type

  def agregarTEXT(self,text):
    self.TEXT=text

  def agregarPOS(self,Pos):
    self.POS=Pos

  def agregarTREE(self,Tree):
    self.TREE=Tree

  def agregarSIMP(self):
    self.SIMP.append(Simp())

class Sentence(object):
  def __init__(self):
    self.TEXT=""
    self.TREE=""
    self.SIMP=[]

  def agregarTEXT(self,text):
    self.TEXT=text

  def agregarTREE(self,Tree):
    self.TREE=Tree

  def agregarSIMP(self):
    self.SIMP.append(Simp())
  
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
    sentencepru.agregarTYPE(dato[i][6:])
  elif 'TEXT: ' in dato[i][0:6]:
    sentencepru.agregarTEXT(dato[i][6:])
  elif 'POS : ' in dato[i][0:6]:
    sentencepru.agregarPOS(dato[i][6:])
  elif 'TREE: ' in dato[i][0:6]:
    sentencepru.agregarTREE(dato[i][6:])
  elif 'SIMP:' in dato[i]:
    sentencepru.agregarSIMP()
    #numSimp = numSimp+1
  elif '  TYPE: ' in dato[i][0:8]:
#    sentencepru.SIMP[numSimp].agregarTYPE(dato[i][8:])
    sentencepru.SIMP[-1].agregarTYPE(dato[i][8:])
  elif '  TEXT: ' in dato[i][0:8]:
#    sentencepru.SIMP[numSimp].agregarTEXT(dato[i][8:])
    sentencepru.SIMP[-1].agregarTEXT(dato[i][8:])
  elif '  COMP: ' in dato[i]:
    sentencepru.SIMP[-1].agregarCOMP(dato[i][8:])

#Salidas para verificar que lo haga correctamente
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

print "SIMP[0].COMP= ",sentencepru.SIMP[0].COMP
print "SIMP[1].COMP= ",sentencepru.SIMP[1].COMP







