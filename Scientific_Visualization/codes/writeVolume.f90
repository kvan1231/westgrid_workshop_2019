program writeVolume

  implicit none
  integer*8 :: i, j, k
  integer*8, parameter :: n = 30
  real*4:: x, y, z, f, r
  real*4, parameter :: r0 = 0.4
  character*90, parameter :: filename = 'cylinder.vtk'
  character(4) :: dimLine
  character(10) :: spacingLine, ntotLine

  write(dimLine,fmt="(i4)") n
  write(spacingLine,fmt="(f10.6)") 1./float(n)
  write(ntotLine,fmt="(i8)") n**3

  open(unit=101,file=trim(filename),action='write',status='replace')
  write(101,'(a)') '# vtk DataFile Version 3.0'
  write(101,'(a)') 'Volume example'
  write(101,'(a)') 'ASCII'
  write(101,'(a)') 'DATASET STRUCTURED_POINTS'
  write(101,'(a)') 'DIMENSIONS'//dimLine//dimLine//dimLine
  write(101,'(a)') 'SPACING'//spacingLine//spacingLine//spacingLine
  write(101,'(a)') 'ORIGIN 0 0 0'
  write(101,'(a)') 'POINT_DATA '//trim(ntotLine)
  write(101,'(a)') 'SCALARS density float 1'
  write(101,'(a)') 'LOOKUP_TABLE default'
  close(101)

  open(unit=102,file=trim(filename),action='write',access='append',form='formatted')
  do i = 1, n
     x = (float(i)-0.5)/float(n)
     do j = 1, n
        y = (float(j)-0.5)/float(n)
        do k = 1, n
           z = (float(k)-0.5)/float(n)
           r = sqrt((x-0.5)**2+(y-0.5)**2)
           f = exp(-abs(r-r0))
           write(102,*) f
        enddo
     enddo
  enddo
  close(102)
  stop

end program writeVolume
