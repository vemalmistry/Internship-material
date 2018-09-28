f = open('fluid1.dat', 'wa+')
import numpy, math, glob
files = glob.glob('d.sds_0_2M.prod.*')
for g in files:
    data = numpy.loadtxt(g, delimiter = ' ', skiprows = 9)

type = data[:,1]
x = data[:,2]
y = data[:,3]
z = data[:,4]
 
list1 = []
list2 = []
list3 = []
binlist = []
dx = []
dy = []
dz = []
for i in range(0, 40476):
        k = type[i]
        if k == 7:
                list1.append(x[i])
		list2.append(y[i])
		list3.append(z[i])

for i in range(0, 40476):		
	k = type[i]
	for j in range(0, 200):    
	        sulx = list1[j]
	        suly = list2[j]
		sulz = list3[j]
		if k != 7:
			
		        deltax = abs(x[i] - list1[j])
	                if deltax >= 0.5:
		                deltax -= 0.5
			deltax *= 173.331
                        dx.append(deltax)

                        deltay = abs(y[i] - list2[j])
                        if deltay >= 0.5:
                                deltay -= 0.5
			deltay *= 173.331
                        dy.append(deltay)

                        deltaz = abs(z[i] - list3[j])
                        if deltaz >= 0.5:
                                deltaz -= 0.5
			deltaz *= 173.331
                        dz.append(deltaz)
		else: 
			dx = [0]
			dy = [0]
			dz = [0]

	xmin = min(dx)
	ymin = min(dy)
	zmin = min(dz)
	dis = math.sqrt(xmin**2 + ymin**2 + zmin**2)
	
	tempbin = ((dis*2)//1)/2
	binlist.append(tempbin)	
	dx = []
	dy = []
	dz = []

ds = 0
h2o = 0
sod = 0
bro = 0
bin_num = 2

for bin_num in [float(l)/1 for l in range(2, 35, 1)]:
	for i in range(0, 40476):
		k = binlist[i]
		if k == bin_num:	
		       	if (type[i] <= 7):
		        	       	ds += 1
                	elif (type[i] <= 9):
                	        h2o += 1
	                elif (type[i] == 10):
	                        sod += 1
	                else:
	                        (type[i] == 11)
	                        bro += 1
	p_ds = ds/((72.8**2)*42)
	p_h2o = h2o/((72.8**2)*3)
	p_sod = sod/(72.8**2)
	p_bro = bro/(72.8**2)
	p = "bin", bin_num + 52, "DS", p_ds, "H2O", p_h2o, "Na", p_sod, "Br", p_bro
	print >> f, p 
	bin_num += 0.5
	ds = 0
	h2o = 0
	sod = 0
	bro = 0

