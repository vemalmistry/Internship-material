f = open('br_oxy.dat', 'wa+')
import numpy, math, glob
config = 0
files = glob.glob('d.sds_0_2M.prod.*')
for g in files:
	data = numpy.loadtxt(g, delimiter = ' ', skiprows = 9)
	print >> f, "configuration number", config  
	config += 5000
	type = data[:,1]
	x = data[:,2]
	y = data[:,3]
	z = data[:,4]
	list1 = []
	list2 = []
	list3 = []
	nearwater = 0
	dx = []
	dy = []        
	dz = []
	sdx = []
	sdy = []
	sdz = []
	suldx = []
	suldy = []
	suldz = []
	dislist = []
	biglist = []
	suldislist = []
	minsuldislist = []
	for i in range(0, 40476):         	        #Number of atoms
	        k = type[i]
	        if k == 11:		  	        #Type of ion	
	                list1.append(x[i])
			list2.append(y[i])
			list3.append(z[i])
		
		if k == 7:		  	        #Type for measuring sds/dtab distance
			sdx.append(x[i])
			sdy.append(y[i])				
			sdz.append(z[i])

	for i in range(0, 40476):	  	        #Number of atoms
		k = type[i]
		for j in range(0, 38):   	        #Number of ions 
		        sodx = list1[j]
		        sody = list2[j]
			sodz = list3[j]
			if k == 8:	  	        #Type of surrounding the ion		
				deltax = abs(x[i] - sodx)
		                if deltax >= 0.5:
			                deltax -= 0.5
				deltax *= 173.331
	        		dx.append(deltax) 
	                			
				deltay = abs(y[i] - sody)
	                        if deltay >= 0.5:
	                                deltay -= 0.5
				deltay *= 173.331
	                        dy.append(deltay)

	                        deltaz = abs(z[i] - sodz)
        	                if deltaz >= 0.5:
        	                        deltaz -= 0.5
				deltaz *= 173.331
        	                dz.append(deltaz)
					
	               	else: 
				dx = []
				dy = []
				dz = []

		if len(dx) > 1:
			for q in range(0, 38):		#Number of ions
				xval = dx[q]
				yval = dy[q]
				zval = dz[q]
				dis = math.sqrt(xval**2 + yval**2 + zval**2)		
				dislist.append(dis)
				if len(dislist) == 38: #Number of ions
					biglist.append(dislist)				
					dislist = []
		
	for i in range(0, 40476):			#Number of atoms
		k = type[i]
		for l in range(0, 200):			#Number of sds/dtab
			sulx = sdx[l]
			suly = sdy[l]
			sulz = sdz[l]
			if k == 11:			#Type of ion
				nearsulx = abs(x[i] - sulx)
				if nearsulx >= 0.5:
					nearsulx -= 0.5
				nearsulx *= 173.331
				suldx.append(nearsulx) 
				
				nearsuly = abs(y[i] - suly)
        	                if nearsuly >= 0.5:
        	                        nearsuly -= 0.5
                                nearsuly *= 173.331
                                suldy.append(nearsuly)
				
				nearsulz = abs(z[i] - sulz)
	                        if nearsulz >= 0.5:
        	                        nearsulz -= 0.5
                                nearsulz *= 173.331
                                suldz.append(nearsulz)
			
			else:
				suldx = []
				suldy = []
				suldz = []
						
			if len(suldz) == 200:		#Number of sds/dtab
				for m in range(0, 200): #Number of sds/dtab
					sulx = suldx[m]
					suly = suldy[m]
					sulz = suldz[m]
					suldis = math.sqrt(sulx**2 + suly**2 + sulz**2)
					suldislist.append(suldis)
				minsuldis = min(suldislist)
				minsuldislist.append(minsuldis)	
				suldislist = []
				suldx = []				
				suldy = []		
				suldz = []													 
	for r in range(0, 38): 			#Number of ions
		smin = minsuldislist[r]
		listval = [item[r] for item in biglist]
		for s in range(0, 10600):		#Number of surrounding of ion
			disval = listval[s]
			if disval <= 4.05:		#Mindis (see excel table)
				nearwater += 1
		print >> f, nearwater, smin
		nearwater = 0		
				
	

