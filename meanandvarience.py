import csv 
from collections import defaultdict 
 
 
#for opening and reading a csv file 
col = defaultdict(list) 

seq = [] 
with open('feddback.csv') as file: 
    reader = csv.reader(file) 
    for row in reader: 
        seq.append(row)
       # print row
		
        for (k,v) in enumerate(row): 
            col[k].append(v)

			
mean=[]
varience=[]

for i in range(0,6):
	sum=0
	sum1=0
	for j in range(1,len(col[i])):
		sum+=int(col[i][j]) 
		sum1+=int(col[i][j])**2
	mean.append(sum/(len(col[0])-1.0))
	varience.append(sum1/(len(col[0])-1.0))

print mean
print varience
