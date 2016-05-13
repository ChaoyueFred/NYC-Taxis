import sys;

ID = []
rentInc = []
rentInc_gen = []
linecount = 0

colors = ['000000ff','0a0000ff','140000ff','1f0000ff','290000ff','330000ff','4d0000ff','660000ff','990000ff','cc0000ff','ff0000ff']

for line in sys.stdin:
    linecount +=1
    if linecount <=1:
        continue
    line = line.strip().split(',')
    ID.append(line[0])
    rentInc_gen.append(line[-3])
    rentInc.append(line[-4])

with open("nycounty_onlyIDModified.kml", 'r') as file:
    data = file.readlines()

count = 0
for i in range(len(ID)):
    for j in range(len(data)):
        if data[j].find("<name>%s</name>"%(ID[i])) != -1:
            try:
                rentIncPerc = (float(rentInc[i])) * 100
                rentInc_gen[i] = int(rentInc_gen[i])
            except ValueError:
                continue
            addString = '<description><![CDATA[<h2>Rent Increased Rate from 2000 to 2010</h2><p><i>%.2f%%</i></p>]]></description>'%(rentIncPerc)
            data[j] = "  <name>%s</name>%s\n"%(ID[i],addString)
            data[j+1] = "  <Style><LineStyle><width>0.5</width><color>%s</color></LineStyle><PolyStyle><color>%s</color></PolyStyle></Style>\n"%(colors[rentInc_gen[i]],colors[rentInc_gen[i]])

with open("nycounty_rentIncModified.kml", 'w') as file:
    file.writelines(data)
