
pen('out.dat', 'wa+')

import numpy, collections

data = numpy.genfromtxt('d.sds_0_2M.prod.0', delimiter = ' ')

type = data[:,1]

s = sum(type <= 7)
#print("Number of DS molecules is: ",s)

t1 = sum(type == 8)
t2 = sum(type == 9)
t = t1 + t2
#print("Number of water molecules is: ",t)

u = sum(type == 10)
#print("Number of Na molecules is: ",u)

v = sum(type == 11)
#print("Number of Br molecules is: ",v)


rposition = data[:,4]
z = (173.331*rposition)
bin = (z//1)+1

ds = 0
h2o = 0
sod = 0
bro = 0
#bin_num = input("Type bin number ")
bin_num = 0
while bin_num <= 174:
        for iatom in range(0, 40476):
                k = bin[iatom]
                if k == bin_num:
                        if (type[iatom] <= 7):
                                ds += 1
                        elif (type[iatom] <= 9):
                                h2o += 1
                        elif (type[iatom] == 10):
                                sod += 1
                        else:
                                (type[iatom] == 11)
                                bro += 1
        p_ds = ds/((72.8**2)*42)
        p_h2o = h2o/((72.8**2)*3)
        p_sod = sod/(72.8**2)
        p_bro = bro/(72.8**2)
        p = "bin", bin_num, "DS", p_ds, "H2O", p_h2o, "Na", p_sod, "Br", p_bro
        print p
        print >> f, p
        bin_num += 1
        ds = 0
        h2o = 0
        sod = 0
        bro = 0


