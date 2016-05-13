import sys;

ID = []
unemp = []
unemp_gen = []
linecount = 0

colors = ['000000ff','1a0000ff','330000ff','4d0000ff','660000ff','800000ff','990000ff','b30000ff','cc0000ff','e60000ff','ff0000ff']

for line in sys.stdin:
    linecount +=1
    if linecount <=1:
        continue
    line = line.strip().split(',')
    ID.append(line[0])
    unemp_gen.append(line[-9])
    unemp.append(line[-10])

with open("nycounty_onlyIDModified.kml", 'r') as file:
    data = file.readlines()

count = 0
for i in range(len(ID)):
    for j in range(len(data)):
        if data[j].find("<name>%s</name>"%(ID[i])) != -1:
            try:
                unempPerc = (float(unemp[i])) * 100
                unemp_gen[i] = int(unemp_gen[i])
            except ValueError:
                continue
            addString = '<description><![CDATA[<h2>Unemployment rate</h2><p><i>%.2f%%</i></p>]]></description>'%(unempPerc)
            data[j] = "  <name>%s</name>%s\n"%(ID[i],addString)
            data[j+1] = "  <Style><LineStyle><width>0.5</width><color>%s</color></LineStyle><PolyStyle><color>%s</color></PolyStyle></Style>\n"%(colors[unemp_gen[i]],colors[unemp_gen[i]])

with open("nycounty_unemploymentModified.kml", 'w') as file:
    file.writelines(data)
