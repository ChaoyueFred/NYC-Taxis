import sys;

ID = []
pov = []
pov_gen = []
linecount = 0

colors = ['000000ff','1a0000ff','330000ff','4d0000ff','660000ff','800000ff','990000ff','b30000ff','cc0000ff','e60000ff','ff0000ff']
#more distance on lower(0,30)
#more distance on higher(0,4,8,12,16,20,30,40,60,80,100)['000000ff','0a0000ff','140000ff','1f0000ff','290000ff','330000ff','4d0000ff','660000ff','990000ff','cc0000ff','ff0000ff']
#average(0:10:100)['000000ff','1a0000ff','330000ff','4d0000ff','660000ff','800000ff','990000ff','b30000ff','cc0000ff','e60000ff','ff0000ff']
#['01400FF','a1400FF','141400FF','1e1400FF','281400FF','321400FF','3c1400FF','461400FF','501400FF','5a1400FF','641400FF']
#['50FFFFFF','50CAC6FF','50B0AAFF','509F97FF','508D84FF','507C71FF','506B5EFF','50594BFF','503625FF','502512FF','501400FF']
#'50FFFFFF','50E4E2FF','46C2BCFB','46B0AAFA','46968DF8','46857AF7','467367F6','465042F3','462E1CF1','461400F0']

for line in sys.stdin:
    linecount +=1
    if linecount <=1:
        continue
    line = line.strip().split(',')
    ID.append(line[0])
    pov_gen.append(line[-5])
    pov.append(line[-6])

with open("nycounty_onlyIDModified.kml", 'r') as file:
    data = file.readlines()

count = 0
for i in range(len(ID)):
    for j in range(len(data)):
        if data[j].find("<name>%s</name>"%(ID[i])) != -1:
            try:
                povPerc = (float(pov[i])) * 100
                pov_gen[i] = int(pov_gen[i])
            except ValueError:
                continue
            addString = '<description><![CDATA[<h2>Poverty Proportion</h2><p><i>%.2f%%</i></p>]]></description>'%(povPerc)
            data[j] = "  <name>%s</name>%s\n"%(ID[i],addString)
            data[j+1] = "  <Style><LineStyle><width>0.5</width><color>%s</color></LineStyle><PolyStyle><color>%s</color></PolyStyle></Style>\n"%(colors[pov_gen[i]],colors[pov_gen[i]])

with open("nycounty_povertyModified.kml", 'w') as file:
    file.writelines(data)
