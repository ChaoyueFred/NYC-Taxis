import sys;

geoIDList = []

for line in sys.stdin:
    geoIDList.append(line.strip())

with open("nycounty.kml", 'r') as file:
    data = file.readlines()

count = 0
for i in range(len(data)):
    if data[i].find("<Placemark>") != -1:
        data[i] = "  <Placemark>\n    <name>%s</name>\n"%(geoIDList[count])
        count+=1

with open("nycounty.kml", 'w') as file:
    file.writelines(data)
