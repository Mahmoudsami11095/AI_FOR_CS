import os
import re
import glob

pathMaleware = "/home/azureuser/Downloads/Malware_Samples_After_Comments"
pathNormal = "/home/azureuser/Downloads/Benign_Samples_After_Comments"
dataMaleware = glob.glob(pathMaleware + '/*')
dataNormal = glob.glob(pathNormal + '/*')
#print(dataMaleware)
#print(dataNormal)

scriptsMaleware = []

MaxNumoflines=0
for i in range(len(dataMaleware)):
  try:
      fileScript = open(dataMaleware[i],encoding='ISO-8859-1') 
      fileTemp = open("/home/azureuser/Desktop/temp.txt", "r+")
      dataSetCSV = open("/home/azureuser/Desktop/dataSet.csv", "a")
      str = "1"
      lineNum = 0
      #f = re.findall("[\w']+", f.splitlines())
      #print((f.read()))
      for line in fileScript.read().splitlines():
        #print(line) 
        lineNum = lineNum + 1
        fileTemp.seek(0) 
        fileTemp.write(line)
        fileTemp.truncate()
        stream=os.popen('flarestrings /home/azureuser/Desktop/temp.txt | rank_strings --scores')
        out = stream.read()
        #print(out)
        str = str + ", " +(out.split(',')[0]) 
        #print(str)
        #scriptsMaleware.append(line)
      #print(str) 
      if(lineNum > MaxNumoflines):
        MaxNumoflines = lineNum
      dataSetCSV.write(str+"\n")
      print("Script NUM {} is Done".format(i))
  except:
    print("An exception occurred ==> "+str(i)+" ==> "+ dataMaleware[i])


for i in range(len(dataNormal)):
  try:
      fileScript = open(dataNormal[i],encoding='ISO-8859-1') 

      str = "0"
      lineNum = 0
      #f = re.findall("[\w']+", f.splitlines())
      #print((f.read()))
      for line in fileScript.read().splitlines():
        #print(line)
        lineNum = lineNum + 1 
        fileTemp.seek(0) 
        fileTemp.write(line)
        fileTemp.truncate()
        stream=os.popen('flarestrings /home/azureuser/Desktop/temp.txt | rank_strings --scores')
        out = stream.read()
        #print(out)
        str = str + ", " +(out.split(',')[0]) 
        #print(str)
        #scriptsMaleware.append(line)
      #print(str) 
      if(lineNum > MaxNumoflines):
        MaxNumoflines = lineNum
      dataSetCSV.write(str+"\n")
      print("Scrip Begnin Num {} Done " .format(i))
  except:
    print("An exception occurred ==> "+str(i)+" ==> "+ dataMaleware[i])

str="label"
print("MaxNumoflines " ,MaxNumoflines)
for col in range(MaxNumoflines):
        str = str + "," + "Wgt_Line_" + format(col)
dataSetCSV.write(str)

dataSetCSV.close()
fileTemp.close()
