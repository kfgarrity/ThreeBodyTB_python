import subprocess
import os


mpath = os.path.dirname(os.path.realpath(__file__)) 

try:
    out,err = subprocess.Popen(['julia', '--version'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT).communicate()
except: out = ""

#check if Julia has the correct version
hasjulia = ( ("julia version 1.6" in str(out)) or
             ("julia version 1.5" in str(out)) or
             ("julia version 1.7" in str(out)) or
             ("julia version 1.8" in str(out)) or
             ("julia version 1.9" in str(out)))

if not hasjulia:
    julia_cmd = mpath+"/src/julia/julia-1.6.1/bin/julia" # path for julia
    if not os.path.exists(julia_cmd):
        raise Exception("no julia, you must run install.py first")
        print()
else:
    julia_cmd = "julia"


sysimage = os.environ["HOME"]+"/.julia/sysimages/sys_threebodytb.so"

if not os.path.exists(sysimage):
    raise Exception("missing sysimage, you can run without it but loading may be slow, try running install.py")

    
from julia.api import Julia
jlsession = Julia(runtime=julia_cmd, compiled_modules=False, sysimage=sysimage)
jlsession.eval("using Suppressor") # suppress output

from julia import ThreeBodyTB as jl

if not os.path.exists("intro_message.txt"):
    print("one time intro message")
    print("success, loaded ThreeBodyTB from julia")
    print("example usage:")
    print()
    print("import numpy as np")
    print("A = np.eye(3) * 5.0")
    print("coords = np.zeros((1,3))")
    print('c = TB3.jl.makecrys(A, coords, ["Li"])')
    print('energy, tbc, flag = TB3.jl.scf_energy(c)')
    print()

    f = open("intro_message.txt", "w")
    f.write("success, loaded ThreeBodyTB from julia\n")
    f.write("example usage:\n")
    f.write("\n")
    f.write("import numpy as np\n")
    f.write("A = np.eye(3) * 5.0\n")
    f.write("coords = np.zeros((1,3))\n")
    f.write('c = TB3.jl.makecrys(A, coords, ["Li\n"])\n')
    f.write('energy, tbc, flag = TB3.jl.scf_energy(c)\n')
    f.write("\n")
    f.close()

    
    
#print("to run in repl\n")
#print("exec(open(\"quickstart.py\").read())")


