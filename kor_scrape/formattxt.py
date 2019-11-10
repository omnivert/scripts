import re, csv, io
fname = 'tmpkor'
csvfname = 'tmpkor.csv'

#TODO modify for utf8
with io.open(fname, 'r', encoding='utf-8') as f:
    text = f.read()

#strip newlines
text = text.replace('\n',' ')
#strange unicode
text = text.replace('\xa0', '')
text = text.replace('\xc2', '')
#tabs and whitespace replaced w 1 space
text = re.sub('\t|  *', ' ', text)
#split on number. assumes input is lines of phrases
#[phrase no. in XX. format] [korean phrase] [english translation] [optional note or explanation]
#omits phrase number in result
lines = re.split('[0-9][0-9]*\.', text)

tocsv = []
for line in lines:
    #we don't care about blank entries
    if line != '':
        #any nonzero repetition of non-alphanum characters
        #catches kor chars, punctuation, whitespace
        tmp = re.split('(^[^0-9a-zA-Z]+)', line)
        #get rid of extra empty results that re.split() generates
        tmp = list(filter(lambda a: a != '', tmp))
        # if optional 3rd field exists, we want it, otherwise 3rd field is empty
        if 'Explanation' in tmp[1] or 'Note:' in tmp[1]:
            tmp2 = re.split(r'(Explanation:.*$|Note:.*$)', tmp[1])
            tmp2 = list(filter(lambda a: a != '', tmp2))
            tmp = [tmp[0]] + tmp2
        else:
            tmp += ['']
        
        #line = re.split('(^ +[\u3131-\ucb4c ]+)', line)
        tocsv.append(tmp)


with io.open(csvfname, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(tocsv)
