#! /usr/bin/env python
# ====================================================================================================
import time
import sys
import random
import math

sys.path.append("lib")

# ====================================================================================================
# Clases.
# ====================================================================================================


class timing_type:

        def __init__(self):
            self.t0 = 0.0       # Base time at the beggining.
            self.t10 = 0.0      # Time after reading input.
            self.t20 = 0.0      # Time after system generation.
            self.t100 = 0.0     # End time at the very end.

        def report(self):
            sep = "=" * 60

            print(sep)
            print(" Timings")
            print(sep)
            print("    Input parsing: %.3f sec" % (self.t10 - self.t0))
            print("System generation: %.3f sec" % (self.t20 - self.t10))
            print("   Overlap search: %.3f sec" % (self.t100 - self.t20))
            print(sep)
            print("       Total time: %.3f sec" % (self.t100 - self.t0))
            print

# ====================================================================================================


class params_type:

    def __init__(self):
            self.num = 0
            self.box = 10.0
            self.randomseed = 0

    def report(self):
        print("Input parameters:")
        print
        print("\tNumber of atoms: %d" % self.num)
        print("\t       Box size: %.2f x %.2f x %.2f (Ang3)" %
              (self.box, self.box, self.box))
        print("\t    Random Seed: %s" % self.randomseed)
        print

# ====================================================================================================


class atom_type:

        def __init__(self, name, radius, x, y, z):
            self.name = name
            self.radius = radius
            self.x = x
            self.y = y
            self.z = z

# ====================================================================================================


class config_type:

        def __init__(self):
            self.box = 0.0
            self.atoms = []

        def report(self):
            print("Configuraion of %d atoms in %.2f Ang cubic box." %
                  (len(self.atoms), self.box))
            print

# ====================================================================================================
# Functions.
# ====================================================================================================


def get_input():
    p = params_type()

    # Read in 2 command line parameters here: box size (Ang), number_of_atoms.
    if len(sys.argv) < 3:
        print("At least 2 parameters are expected: box_size, number_of_atoms,\
              [random_seed]")
        print("Aborting.")
        sys.exit()

    p.box = float(sys.argv[1])
    p.num = int(sys.argv[2])

    p.randomseed = int(time.time() * 1000)
    if len(sys.argv) >= 4:
        p.randomseed = int(sys.argv[3])

    return p

# ====================================================================================================


def gen_config(params):
    cfg = config_type()
    cfg.box = params.box

    random.seed(params.randomseed)

    aname = "Ar"
    aradius = 3.4 / 2.      # Atomics radius in Ang.
    natoms = params.num

    for i in range(natoms):
        x = random.uniform(0, cfg.box)
        y = random.uniform(0, cfg.box)
        z = random.uniform(0, cfg.box)

        cfg.atoms.append(atom_type(aname, aradius, x, y, z))

    return cfg

# ====================================================================================================


def check_overlaps(conf):
    overlaps = []

    n = len(conf.atoms)

    for i in range(n):
        for j in range(i + 1, n):
            # for j in range(n):
            # This would be (n + 2 * clashes),
            # self clashes ii + double counted ij and ji
            ai = conf.atoms[i]
            aj = conf.atoms[j]

            r = ai.radius + aj.radius
            r2 = r * r

            dx = aj.x - ai.x
            dy = aj.y - ai.y
            dz = aj.z - ai.z

            d2 = (dx**2 + dy**2 + dz**2)

            if d2 < r2:
                d = math.sqrt(d2)
                overlaps.append((i, j, d))

    return overlaps

# ====================================================================================================
# The code starts here.
# ====================================================================================================
# Read input parameters.


timings = timing_type()
timings.t0 = time.time()

params = get_input()
params.report()

# ----------------------------------------------------------------------------------------------------
# Generate a configuration of a Number of Ag atoms.


timings.t10 = time.time()

conf = gen_config(params)
print("Generated:")
conf.report()

# ----------------------------------------------------------------------------------------------------
# Check the generated configuration for atomic clashes (overlaps).


timings.t20 = time.time()

overlaps = check_overlaps(conf)

print("Found %d atomics clashes." % len(overlaps))
print
for i in range(len(overlaps)):
    if i > 7:
        break
    print(overlaps[i])
print("...")
print

timings.t100 = time.time()
# ====================================================================================================
timings.report()
