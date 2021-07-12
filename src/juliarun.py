# routines to run the code with Julia
import os
import subprocess

mypath = os.path.dirname(os.path.realpath(__file__))




# check the system image
sysimage = os.environ["HOME"]+"/.julia/sysimages/sys_threebodytb.so"
if not os.path.isfile(sysimage):
    print("No ThreeBodyTB.jl system image found, this may take some time")
    sysimage = None

try: # create the executable
    from julia.api import Julia
    jlsession = Julia(runtime=julia_cmd, compiled_modules=False, sysimage=sysimage)
#    jlsession = Julia(compiled_modules=False,
#                      sysimage=sysimage) # start the Julia session
    jlsession.eval("using Suppressor") # suppress output
except:
    print("Julia cannot be executed")
    

#def run(self):
#    """Execute the Julia program"""
#    import contextlib
#    c = "@suppress_out include(\""+mypath+"/mpsjulia/mpsjulia.jl\");"
#    self.execute(lambda: jlsession.eval(c)) # evaluate Julia



def install(julia=None):
    """Install Julia and TB"""
    if julia is None:
        julia = "julia" # julia command
    print("install ", julia)
#    os.system(julia+" --eval "+"\"import Pkg; Pkg.add(url=\\\"https://github.com/kfgarrity/ThreeBodyTB.jl\\\")\"")

    os.system(julia+" --eval "+"\"import Pkg; Pkg.add(\\\"ThreeBodyTB\\\")\"")
    os.system(julia+" --eval "+"\"import Pkg; Pkg.add(\\\"PyCall\\\")\"")
    os.system(julia+" --eval "+"\"import Pkg; Pkg.add(\\\"Plots\\\")\"")
    os.system(julia+" --eval "+"\"import Pkg; Pkg.add(\\\"Suppressor\\\")\"")
    precompile(julia)


def precompile(julia=None):
    """Precompile Julia"""
    print("precompile")
    if julia is None:
        julia = "julia" # julia command
#    os.system(julia+" --eval  \"using TightlyBound; TightlyBound.compile()\"")
    os.system(julia+" --eval  \"using ThreeBodyTB; using Plots; ThreeBodyTB.compile()\"") 
