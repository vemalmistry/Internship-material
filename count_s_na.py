f = open('count_s_na.dat', 'wa+')
xlist = []
with open('s_na.dat') as g:
	for line in g:
		if not line.startswith('con'):
			num = line.split()
			val = int(num[0])
			dis = int(float(num[1]))
			info = val, dis
			xlist.append(info)				
vallist = [item[0] for item in xlist]
dislist = [item[1] for item in xlist]			

for i in range(min(dislist), max(dislist)):
	each1 = [val for (val, dis) in xlist if dis == i]
	avg = float(sum(each1))/float(len(each1))
	print >> f, i, avg									

