program writeNetCDF

  ! this program writes data in NetCDF

  use netcdf
  implicit none
  integer, parameter :: nx = 100, ny = nx, nz = nx
  character*90, parameter :: filename = 'volume.nc'
  integer :: ncid, varid, dimids(3), x_dimid, y_dimid, z_dimid, i, j, k
  real*4:: x, y, z, r
  real*4, parameter :: r0 = 0.4
  real*4, dimension(:,:,:), allocatable :: data

  allocate(data(nx,ny,nz))

  do i = 1, nx
     x = (float(i)-0.5)/float(nx)
     do j = 1, ny
        y = (float(j)-0.5)/float(ny)
        do k = 1, nz
           z = (float(k)-0.5)/float(nz)
           r = sqrt((x-0.5)**2+(y-0.5)**2)
           data(i,j,k) = exp(-((z-0.5)**2+(r-r0)**2)**0.5)
        enddo
     enddo
  enddo

  call check(nf90_create(trim(filename), NF90_CLOBBER, ncid))
  call check(nf90_def_dim(ncid, "z", nz, z_dimid))
  call check(nf90_def_dim(ncid, "y", ny, y_dimid))
  call check(nf90_def_dim(ncid, "x", nx, x_dimid))
  dimids =  (/ x_dimid, y_dimid, z_dimid /)
  call check(nf90_def_var(ncid, "density", NF90_FLOAT, dimids, varid))
  call check(nf90_enddef(ncid))
  call check(nf90_put_var(ncid, varid, data))
  call check(nf90_close(ncid))

contains

  subroutine check(status)

    integer, intent (in) :: status
    
    if (status.ne.nf90_noerr) then 
      print *, trim(nf90_strerror(status))
      stop 2
    end if

  end subroutine check

end program writeNetCDF
