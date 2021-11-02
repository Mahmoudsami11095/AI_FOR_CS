import os
import re
import glob

pathMaleware = "/home/azureuser/Downloads/Malware_Samples_After_Comments"
pathNormal = "/home/azureuser/Downloads/Benign_Samples_After_Comments"
dataMaleware = glob.glob(pathMaleware + '/*')
dataNormal = glob.glob(pathNormal + '/*')
print(dataMaleware)
print(dataNormal)

scriptsMaleware = []

for i in range(len(dataMaleware)):
  try:
      fileScript = open(dataMaleware[i],encoding='ISO-8859-1') 
      fileTemp = open("/home/azureuser/Desktop/temp.txt", "r+")
      dataSetCSV = open("/home/azureuser/Desktop/dataSet.csv", "a")

      #f = re.findall("[\w']+", f.splitlines())
      #print((f.read()))
      for line in fileScript.read().splitlines():
        fileTemp.seek(0) 
        fileTemp.write(str)
        fileTemp.truncate()
        stream=os.popen('flarestrings socket | rank_strings --scores')
        out = stream.read()
        print(out)
        str = str +(line.split(',')[0]) + "," 

        #scriptsMaleware.append(line)
      print(str) 
      dataSetCSV.write(str+"\n")
      print(scriptsMaleware)
  except:
    print("An exception occurred ==> "+str(i)+" ==> "+ dataMaleware[i])

dataSetCSV.close()
fileTemp.close()
