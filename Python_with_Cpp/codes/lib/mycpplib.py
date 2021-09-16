# ===========================================================================

import ctypes as ct

# ===========================================================================
# Initialization
# ===========================================================================

# Note that we have to use the path reltive to the master / top script,
# not relative to this module file (the .so file is in this same directory).
libmy = ct.cdll.LoadLibrary("lib/libmycpp.so")

# ===========================================================================
# Call to a simple implementation of check_overlaps() function with
# preallocated python arrays.
# ===========================================================================


def check_overlaps(conf):
    n = len(conf.atoms)

    # Set the input and return types for our C++ function
    # according to the design.
    libmy.overlaps.restype = ct.c_int
    libmy.overlaps.argtypes = [ct.POINTER(ct.c_double),
                               ct.POINTER(ct.c_double),
                               ct.POINTER(ct.c_double),
                               ct.POINTER(ct.c_double),
                               ct.c_int,
                               ct.c_int,
                               ct.POINTER(ct.c_int),
                               ct.POINTER(ct.c_int),
                               ct.POINTER(ct.c_double)]

    # Use a euristic, make the buffer twice the number of atoms.
    max_nolaps = 2 * n

    # Prepare the input arrays.
    xx = (ct.c_double * n)()
    yy = (ct.c_double * n)()
    zz = (ct.c_double * n)()
    rr = (ct.c_double * n)()

    for i in range(n):
        xx[i] = conf.atoms[i].x
        yy[i] = conf.atoms[i].y
        zz[i] = conf.atoms[i].z
        rr[i] = conf.atoms[i].radius

    while True:
        ii = (ct.c_int * max_nolaps)()
        jj = (ct.c_int * max_nolaps)()
        dd = (ct.c_double * max_nolaps)()

        nolaps = libmy.overlaps(xx, yy, zz, rr, n,
                                max_nolaps, ii, jj, dd)

        # If the number of overlaps is less than max_nolaps then we are done.
        if nolaps <= max_nolaps:
            break

        # Repeat the search with increased buffers.
        max_nolaps = nolaps

    # Repackage the output into expected format.
    overlaps = [(ii[k], jj[k], dd[k]) for k in range(nolaps)]

    return overlaps

# ===========================================================================
# Call to a complex implementation of check_overlaps() function
# with internal memory allocation.
# ===========================================================================


def check_overlaps_mem(conf):
    n = len(conf.atoms)

    # Set the input and return types for our C++ function
    # according to the design.
    libmy.overlaps_mem.restype = ct.c_int
    libmy.overlaps_mem.argtypes = [ct.POINTER(ct.c_double),
                                   ct.POINTER(ct.c_double),
                                   ct.POINTER(ct.c_double),
                                   ct.POINTER(ct.c_double),
                                   ct.c_int,
                                   ct.POINTER(ct.POINTER(ct.c_int)),
                                   ct.POINTER(ct.POINTER(ct.c_int)),
                                   ct.POINTER(ct.POINTER(ct.c_double))]

    # Prepare the input arrays.
    xx = (ct.c_double * n)()
    yy = (ct.c_double * n)()
    zz = (ct.c_double * n)()
    rr = (ct.c_double * n)()

    for i in range(n):
        xx[i] = conf.atoms[i].x
        yy[i] = conf.atoms[i].y
        zz[i] = conf.atoms[i].z
        rr[i] = conf.atoms[i].radius

    # Arrays of pointers for output buffers, size = 1;
    # Trick to to overcome C argument-by-value passing.
    pii = (ct.POINTER(ct.c_int) * 1)()
    pjj = (ct.POINTER(ct.c_int) * 1)()
    pdd = (ct.POINTER(ct.c_double) * 1)()

    nolaps = libmy.overlaps_mem(xx, yy, zz, rr, n, pii, pjj, pdd)

    # Read the pointers to the arrays allocaed during the search.
    pi = pii[0]
    pj = pjj[0]
    pd = pdd[0]

    # Repackage the output into expected format.
    overlaps = [(pi[k], pj[k], pd[k]) for k in range(nolaps)]

    # Release the allocated memory using our C++ funciton.
    libmy.free_mem(pi, pj, pd)
    return overlaps

# ===========================================================================
