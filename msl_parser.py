from bs4 import BeautifulSoup
import urllib.request, re
import time

from classHelper import Helper
hp = Helper()

def parsePage (tid):
    with urllib.request.urlopen('https://igra.msl.ua/sportprognoz/uk/results?drawId=' + str(tid)) as response:
       html = response.read()
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    data.append(tid)
    for item in soup.findAll("div", {"class": "sp-r__total"}):
        item = str(item)
        print(item)
        match = re.search(r'\d', item) 
        #print(match[0] if match else 'Not found') 
        if match:
            data.append(int(match[0]))
    return data
#print(parsePage(t_id))

archive = []
#t_ids = [1,2,3,4]
t_ids = range(1,194)
for t_id in t_ids:
    time.sleep(1)
    line = parsePage(t_id)
    print(line)
    archive.append(line)
	
#archive = hp.Invert(archive, 4)
outputFile = 'sp-arhiv.txt'
hp.arr2txt_2(outputFile, archive)

def generateXXX():
    X1 = [1,1,1,1]
    X2 = [1,0,0,0]
    X3 = [1,2,2,2]
    X4 = [0,1,2,0]
    X5 = [0,0,1,2]
    X6 = [0,2,0,1]
    X7 = [2,1,0,2]
    X8 = [2,0,2,1]
    X9 = [2,2,1,0]
    XX = [X1,X2,X3,X4,X5,X6,X7,X8,X9]
    XXX = {
        1:X1,2:X2,3:X3,4:X4,5:X5,6:X6,7:X7,8:X8,9:X9,
        10:X1,11:X2,12:X3,13:X4,14:X5,15:X6,16:X7,17:X8,18:X9,
        19:X1,20:X2,21:X3,22:X4,23:X5,24:X6,25:X7,26:X8,27:X9
    }
    return XX
	
def code27SPdata(inp):
	#i = 0
	out = []
	Y1=[inp[1],inp[2],inp[3],inp[4]]
	Y2=[inp[5],inp[6],inp[7],inp[8]]
	Y3=[inp[9],inp[10],inp[11],inp[12]]
	#print inp[0]
	#print Y1
	#print Y2
	#print Y3

	XXX = generateXXX()
	#print XXX
	out_raw = []
	key=0
	for X in XXX:
		#out_raw.append(inp[0])
		#i=0
		i=j1=j2=j3=0
		key+=1
		#print X
		while i<4:
		   
			if X[i] == Y1[i]:
				j1+=1
			if X[i] == Y2[i]:
				j2+=1
			if X[i] == Y3[i]:
				j3+=1
			i+=1
		#print str(j1)+'-'+str(j2)+'-'+str(j3)
		if j1>=3:
			y1=key
		if j2>=3:
			y2=key+9
		if j3>=3:
			y3=key+18
	if inp[0] < 420:
		tirag = inp[0] + 1000
	else:
		tirag = inp[0]
	out = [tirag,y1,y2,y3]
	return out
		
def code36SPdata(inp):
    i = 1
    out = []
    if inp[0] < 420:
        tirag = inp[0] + 1000
    else:
        tirag = inp[0]
    out.append(tirag)
    for item in inp[1:13]:
        if item>3:
            k = item
        elif item==2:
            k = i*3
        else:
            k = i*3-item-1
        # print str(i)+'-'+str(item)+'-'+str(k)
        out.append(k)
        i += 1
    #print out
    return out
	
#print A
result = []
resultC = []
A = archive
for a in A:
    C=code36SPdata(a)
    B=code27SPdata(a)
    #print (a)
    #print C
    #print(B)

    result.append(B)
    resultC.append(C)

result = hp.Invert(result, 4)
resultC = hp.Invert(resultC, 4)

outputFile = 'sportprognoz-nocode.txt'
hp.arr2txt_2(outputFile, A)

outputFile = 'sportprognoz-code27.txt'
hp.arr2txt_2(outputFile, result)

outputFile = 'sportprognoz-code36.txt'
hp.arr2txt_2(outputFile, resultC)
