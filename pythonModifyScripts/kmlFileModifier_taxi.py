import sys;

ID = []
taxi = []
taxi_gen = []
linecount = 0

colors = ['00800080','0a800080','14800080','1f800080','29800080','33800080','40800080','66800080','99800080','cc800080','ff800080']
#red['000000ff','1a0000ff','330000ff','4d0000ff','660000ff','800000ff','990000ff','b30000ff','cc0000ff','e60000ff','ff0000ff']
#red['000000ff','0a0000ff','140000ff','1f0000ff','290000ff','330000ff','400000ff','660000ff','990000ff','cc0000ff','ff0000ff']
#['000000ff','1a0000ff','330000ff','4d0000ff','660000ff','800000ff','990000ff','b30000ff','cc0000ff','e60000ff','ff0000ff']
#['01400FF','a1400FF','141400FF','1e1400FF','281400FF','321400FF','3c1400FF','461400FF','501400FF','5a1400FF','641400FF']
#['50FFFFFF','50CAC6FF','50B0AAFF','509F97FF','508D84FF','507C71FF','506B5EFF','50594BFF','503625FF','502512FF','501400FF']
#'50FFFFFF','50E4E2FF','46C2BCFB','46B0AAFA','46968DF8','46857AF7','467367F6','465042F3','462E1CF1','461400F0']

for line in sys.stdin:
    linecount +=1
    if linecount <=1:
        continue
    line = line.strip().split(',')
    ID.append(line[0])
    taxi_gen.append(line[-1])
    taxi.append(line[-2])

with open("nycounty_onlyIDModified.kml", 'r') as file:
    data = file.readlines()

count = 0
for i in range(len(ID)):
    for j in range(len(data)):
        if data[j].find("<name>%s</name>"%(ID[i])) != -1:
            try:
                taxiPerc = (float(taxi[i])) * 100
                taxi_gen[i] = int(taxi_gen[i])
            except ValueError:
                continue
            addString = '<description><![CDATA[<h2>Trip Increased Rate from 2009 to 2013</h2><p><i>%.2f%%</i></p>]]></description>'%(taxiPerc)
            data[j] = "  <name>%s</name>%s\n"%(ID[i],addString)
            data[j+1] = "  <Style><LineStyle><width>0.5</width><color>%s</color></LineStyle><PolyStyle><color>%s</color></PolyStyle></Style>\n"%(colors[taxi_gen[i]],colors[taxi_gen[i]])

with open("nycounty_taxiIncModified.kml", 'w') as file:
    file.writelines(data)
