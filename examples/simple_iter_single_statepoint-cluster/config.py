# Configured for seamless run on LLNL-LC (Quartz)

################################
##### General options
################################

EMAIL_ADD = "blaubach@umich.edu"

ATOM_TYPES     = ["C", "N"]
NO_CASES       = 3

DRIVER_DIR     = "/p/lustre2/laubach2/al_driver-myLLfork"
WORKING_DIR    = "/p/lustre2/laubach2/al_driver-myLLfork/examples/simple_iter_single_statepoint-cluster/"
CHIMES_SRCDIR  = "/p/lustre2/laubach2/chimes_lsq-myLLfork/src/"
HPC_ACCOUNT    = "iap"

################################
##### ChIMES LSQ
################################

ALC0_FILES    = WORKING_DIR + "ALL_BASE_FILES/ALC-0_BASEFILES/"
CHIMES_LSQ    = CHIMES_SRCDIR + "../build/chimes_lsq"
CHIMES_SOLVER = CHIMES_SRCDIR + "../build/chimes_lsq.py"
CHIMES_POSTPRC= CHIMES_SRCDIR + "../build/post_proc_chimes_lsq.py"

# Generic weight settings

WEIGHTS_FORCE =   1.0

REGRESS_ALG   = "dlasso"
REGRESS_VAR   = "1.0E-5"
REGRESS_NRM   = True

# Job submitting settings (avoid defaults because they will lead to long queue times)

CHIMES_BUILD_NODES = 2
CHIMES_BUILD_QUEUE = "pdebug"
CHIMES_BUILD_TIME  = "01:00:00"

CHIMES_SOLVE_NODES = 2
CHIMES_SOLVE_QUEUE = "pdebug"
CHIMES_SOLVE_TIME  = "01:00:00"

################################
##### Cluster Parameters
################################

DO_CLUSTER    = True
MAX_CLUATM    = 100 # Maximum number of atoms to allow in a cluster
TIGHT_CRIT    = WORKING_DIR + "ALL_BASE_FILES/CLUSTER_BASEFILES/tight_bond_crit.dat"
LOOSE_CRIT    = WORKING_DIR + "ALL_BASE_FILES/CLUSTER_BASEFILES/loose_bond_crit.dat"
# CLU_CODE      = DRIVER_DIR  + "/utilities/new_ts_clu.cpp"
CLU_CODE      = DRIVER_DIR  + "/examples/ts_debug/new_ts_clu.cpp"

################################
##### Molecular Dynamics
################################

MD_STYLE        = "CHIMES"
CHIMES_MD_MPI   = CHIMES_SRCDIR + "../build/chimes_md"

MOLANAL         = CHIMES_SRCDIR + "../contrib/molanal/src/"
MOLANAL_SPECIES = ["C1"]

################################
##### Single-Point QM
################################

QM_FILES = WORKING_DIR + "ALL_BASE_FILES/QM_BASEFILES"
VASP_EXE = "/usr/gapps/emc-vasp/vasp.5.4.4/build/gam/vasp"
VASP_TIME    = "01:00:00"
VASP_NODES   = 2
VASP_PPN     = 36
VASP_MODULES = "mkl intel/18.0.1 impi/2018.0"
