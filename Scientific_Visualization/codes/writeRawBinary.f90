program writeRawBinary

  implicit none
  integer, parameter :: n = 16
  integer :: i, j, k
  real*4, parameter :: pi = 3.141592654
  real*4 :: x, y, z
  real*4, dimension(n,n,n) :: a

  do i = 1, n
     x = (float(i)-0.5)/float(n)
     do j = 1, n
        y = (float(j)-0.5)/float(n)
        do k = 1, n
           z = (float(k)-0.5)/float(n)
           a(i,j,k) = (1.-z)*((1.-y)*sin(pi*x)+y*sin(2.*pi*x)**2) + &
                z*((1.-x)*sin(pi*y)+x*sin(2.*pi*y)**2)
        enddo
     enddo
  enddo

  ! the direct access mode below is necessary to avoid writing extra headers and making sure the file is
  ! actually 16*16*16*4=16384 bytes in size
  open(15,file='simpleData.raw',status='new',form='unformatted',access='direct',recl=n*n*n*4)
  write(15,rec=1) a

  close(15)

end program writeRawBinary
