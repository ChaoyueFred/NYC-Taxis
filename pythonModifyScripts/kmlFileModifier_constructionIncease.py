import sys;

ID = []
construct = []
construct_gen = []
linecount = 0

colors = ['000000ff','1a0000ff','330000ff','4d0000ff','660000ff','800000ff','990000ff','b30000ff','cc0000ff','e60000ff','ff0000ff']

for line in sys.stdin:
    linecount +=1
    if linecount <=1:
        continue
    line = line.strip().split(',')
    ID.append(line[0])
    construct_gen.append(line[-1])
    construct.append(line[-2])

with open("nycounty_onlyIDModified.kml", 'r') as file:
    data = file.readlines()

count = 0
for i in range(len(ID)):
    for j in range(len(data)):
        if data[j].find("<name>%s</name>"%(ID[i])) != -1:
            try:
                constructPerc = (float(construct[i])) * 100
                construct_gen[i] = int(construct_gen[i])
            except ValueError:
                continue
            addString = '<description><![CDATA[<h2>Construction activity increased from 2005 to 2013</h2><p><i>%.2f%%</i></p>]]></description>'%(constructPerc)
            data[j] = "  <name>%s</name>%s\n"%(ID[i],addString)
            data[j+1] = "  <Style><LineStyle><width>0.5</width><color>%s</color></LineStyle><PolyStyle><color>%s</color></PolyStyle></Style>\n"%(colors[construct_gen[i]],colors[construct_gen[i]])

with open("nycounty_constructionIncModified.kml", 'w') as file:
    file.writelines(data)
