import numpy, collections

data = numpy.genfromtxt('d.sds_0_2M.prod.0', delimiter = ' ')

type = data[:,1]
x = data[:,2]
y = data[:,3]
z = data[:,4]


dx = []
list1 = []

for i in range(0, 40476):
	k = type[i]
	if k == 7:
		list1.append(x[i])
#print list1

for i in range(0, 50005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000500050005000):
        k = type[i]
	for j in range(0, 200):
		sul = list1[j]
        	if k != 7:
			deltax = abs(x[i] - list1[j])
			if deltax >= 0.5:
				deltax -= 0.5
			dx.append(deltax)
	xmin = min(dx)
	print xmin
	dx = []


#xmin = 1
#for xval in range(0, 200):
#	x_range = dx[xval]
#	if dx[val] <= xmin:
		




#rposition = data[:,4]
#z_cord = (173.331*rposition)
#bin = (z_cord//1)+1

#ds = 0
#h2o = 0
#sod = 0
#bro = 0
#bin_num = input("Type bin number ")
#bin_num = 0
#while bin_num <= 174:
#        for iatom in range(0, 40476):
#                k = bin[iatom]
#                if k == bin_num:
#                        if (type[iatom] <= 7):
#                                ds += 1
#                        elif (type[iatom] <= 9):
#                                h2o += 1
#                        elif (type[iatom] == 10):
#                                sod += 1
#                        else:
#                                (type[iatom] == 11)
#                                bro += 1
#        p_ds = ds/((72.8**2)*42)
#        p_h2o = h2o/((72.8**2)*3)
#        p_sod = sod/(72.8**2)
#        p_bro = bro/(72.8**2)
#        p = "bin", bin_num, "DS", p_ds, "H2O", p_h2o, "Na", p_sod, "Br", p_bro
#        print p
        
#        bin_num += 1
#        ds = 0
#        h2o = 0
#        sod = 0
#        bro = 0

