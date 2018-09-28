c ... lammps2pdb.f:
c ... reads dump atom output from lammps and a bond list and constructs a pdb file.

      implicit none
      integer nsize,maxmolec
      parameter (nsize = 180000,maxmolec=60000)

      integer natoms,inum,itype,ntype,ione
      integer edge,izero,i,j,oldtimestep
      integer ntimestep
      integer nx,ny,nz,iconfig,jconfig,nconfig
   

      double precision xmin,xmax,ymin,ymax,zmin,zmax,xdim,ydim,zdim
      double precision xi,yi,zi,coords,fzero,fone,maxz,minz

      character*3 atomtype
      character*4 restype
      character*5 stepchar
      character*16 filename
      character*80 fname
      dimension coords(nsize,3),ntype(nsize),edge(nsize,3)

c      open(2,file="all_atoms.out")
      open(20,file='in.a2m')
      open(30,file='log.atoms2movie.out')

      izero = 0
      ione = 1
      fzero = 0.0d0
      fone = 1.0d0
      
      do i = 1,nsize
         ntype(i) = 0
         do j = 1,3
            coords(i,j) = 0.0d0
         enddo
         do j = 1,3
            edge(i,j) = 0
         enddo
      enddo

      read(20,*) 
      read(20,*) nconfig
      read(20,*)
      read(20,*) fname
      open(2,file=fname)
      close(20)


      oldtimestep = -100
      jconfig = 0
      do iconfig = 1,nconfig
         read(2,*)
         read(2,*) ntimestep
         read(2,*)
         read(2,*) natoms
         if (natoms .gt. nsize) then
            write(30,*) '*** natoms > nsize ***'
            write(30,*) '*** must increase nsize to ',natoms + 1,' ***'
            stop
         endif
         read(2,*)
         read(2,*) xmin,xmax
         read(2,*) ymin,ymax
         read(2,*) zmin,zmax
         read(2,*)
         xdim = xmax - xmin
         ydim = ymax - ymin 
         zdim = zmax - zmin
         maxz = zmin
         minz = zmax
         write(30,*) "Dimension x,y,z: ",xdim,ydim,zdim
         write(30,*) "Min x,y,z: ",xmin,ymin,zmin
         write(30,*) "Max x,y,z: ",xmax,ymax,zmax
         do i = 1,natoms
            read(2,*) inum,itype,xi,yi,zi,nx,ny,nz
c            read(2,*) inum,itype,xi,yi,zi
            coords(inum,1) = ((xdim)*xi)
            coords(inum,2) = ((ydim)*yi)
            coords(inum,3) = ((zdim)*zi)
c            coords(inum,1) = xi - xmin
c            coords(inum,2) = yi - ymin
c            coords(inum,3) = zi - zmin
            ntype(inum) = itype
         enddo
         if (ntimestep .gt. oldtimestep) then
            jconfig = jconfig + 1
            write(stepchar,'(i5.5)') jconfig
            filename = 'config_'//stepchar//'.pdb'
            open(10,file=filename)
            do i = 1,natoms
               if (ntype(i) .eq. 1) then
                  atomtype = 'H1 '
                  restype = 'SDS '
               else if (ntype(i) .eq. 2) then
                  atomtype = 'H2'
                  restype = 'SDS '
               else if (ntype(i) .eq. 3) then
                  atomtype = 'C1 '
                  restype = 'SDS '
               else if (ntype(i) .eq. 4) then
                  atomtype = 'C2 '
                  restype = 'SDS '
               else if (ntype(i) .eq. 5) then
                  atomtype = 'O1 '
                  restype = 'SDS '
               else if (ntype(i) .eq. 6) then
                  atomtype = 'O2 '
                  restype = 'SDS '
               else if (ntype(i) .eq. 7) then
                  atomtype = 'S1 '
                  restype = 'SDS '
               else if (ntype(i) .eq. 8) then
                  atomtype = 'OW '
                  restype = 'H2O '
               else if (ntype(i) .eq. 9) then
                  atomtype = 'HW '
                  restype = 'H2O '
               else if (ntype(i) .eq. 10) then
                  atomtype = 'Na+'
                  restype = 'SOD '
               else if (ntype(i) .eq. 11) then
                  atomtype = 'Br-'
                  restype = 'BRO '
               endif
               write (10,5) "ATOM",i,atomtype,restype,ione,
     &            coords(i,1),coords(i,2),coords(i,3),fone,fzero 
c               write (10,5) "ATOM",i,atomtype,"NONE",izero,coords(i,1),
c     &               coords(i,2),coords(i,3),fone,fzero 
            enddo
            oldtimestep = ntimestep
            write(10,*) "END"   
            close(10)
         end if
      enddo
      close(2)

    5 format(a4,i7,2x,a3,1x,a4,i5,3x,f8.3,f8.3,f8.3,2x,f4.2,2x,f4.2) 
                  
      end

