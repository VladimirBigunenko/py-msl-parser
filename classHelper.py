class Helper:

    def arr2txt_2(self, file, arr):
        # file = 'output/' + filename
        f = open(file, 'w')
        data = ''
        for val in arr:
            for v in val:
                if v < 10:
                # if v!=val[0] and v < 10:
                    v = str(0) + str(v)
                data = data + ' ' + str(v)
            data = data + '\n'
        f.write(data)
        f.close()
        
    def arr2txt_3(self, filename, arr):
        file = '' + filename
        f = open(file, 'w')
        data = ''
        for val in arr:
            for v in val:
                if v < 10:
                    v = str(0) + str(v)
                data = data + ' ' + str(v)
            data = data + '\n'
        f.write(data)
        f.close()
    
    def txt2arr(self, filename):
        #file = 'input/input.txt'
        keys = []
        file = open(filename, 'r')
        for line in file:
            line = line.strip()
            line = line.replace('   ', ' ')
            line = line.replace('  ', ' ')
            line = line.replace('	 ', '	')
            line = line.replace(' 	', '	')
            line = line.replace(' ', '	')
            line = line.split('	')
            #print line
            for j in range(len(line)):
                #print line[j]
                line[j] = int(line[j])

            keys.append(line)
        #print keys
        #print len(keys)
        return keys

    def Invert(self, A, N):
        return A[::-1]
    
    def pods4et_to4nyh_sovpadenij(self,list_1,list_2):
        n=0
        if len(list_1) == len(list_2):
            i=0
            while i<len(list_1):

                if list_1[i]==list_2[i]:
                    n=n+1

                i=i+1
        return n