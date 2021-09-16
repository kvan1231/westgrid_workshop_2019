VTKDIR = $(HOME)/Documents/local/vtk
NETCDFDIR = /usr/local
SGrid: SGrid.cpp
	g++ $^ -o $@ -I$(VTKDIR)/include/vtk-6.1 -L$(VTKDIR)/lib \
	-lvtkIOXML-6.1.1 -lvtkCommonDataModel-6.1.1 -lvtkCommonCore-6.1.1
writeVolume: writeVolume.cpp
	g++ $^ -o $@
# writeVolume: writeVolume.f90
# 	gfortran $^ -o $@
writeNetCDF: writeNetCDF.cpp
	g++ $^ -o $@ -I$(NETCDFDIR)/include -L$(NETCDFDIR)/lib -lnetcdf_c++4 -lnetcdf
#writeNetCDF: writeNetCDF.f90
#	gfortran $^ -o $@ -I$(NETCDFDIR)/include -L$(NETCDFDIR)/lib -lnetcdff -lnetcdf
optimization: optimization.c
	gcc $^ -o $@ -I$(NETCDFDIR)/include -L$(NETCDFDIR)/lib -lnetcdf
writeRawBinary: writeRawBinary.f90
	gfortran $^ -o $@     # with Intel compiler use -assume byterecl
clean:
	@/bin/rm -rf *.o *.mod *~ cylinder.vtk volume.nc stvol.nc 111* halfCylinder.vts
	@find . -type f -perm +111 | xargs /bin/rm -rf
