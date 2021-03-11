import os 

url = "https://www.epey.com/bisiklet/"

shFile = open("downloadEpey.sh","w")

writeString = "#!/bin/bash\n"
for i in range(73):
    writeString += "\nwget -O epey"+ str(i+1) +".html https://www.epey.com/bisiklet/"+str(i+1)+" &"

shFile.write(writeString)