#!/usr/bin/python3
import os
import sys
import subprocess


mpath = os.path.dirname(os.path.realpath(__file__)) 


# main path
try:
    out,err = subprocess.Popen(['julia', '--version'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT).communicate()
except: out = ""
#check if JUlia has the correct version
hasjulia = ( ("julia version 1.6" in str(out)) or ("julia version 1.5" in str(out)) or ("julia version 1.7" in str(out)) or ("julia version 1.8" in str(out)))

             
#print(hasjulia) ; exit()

print("hasjulia: ", hasjulia)
             
if not hasjulia: # if the correct Julia version is not present
    julia_cmd = mpath+"/src/julia/julia-1.6.1/bin/julia" # path for julia
    if not os.path.exists(julia_cmd):
        print("Julia not present in path, downloading")
        os.system("mkdir "+mpath+"/src/julia") # create a subfodler for julia
        os.chdir(mpath+"/src/julia") # go to the subfolder
        ## download julia
        juliafile = "julia-1.6.1-linux-x86_64.tar.gz" # julia file
        os.system("wget https://julialang-s3.julialang.org/bin/linux/x64/1.6/"+juliafile)
        os.system("tar -xvf "+juliafile) # untar the file
        os.system("rm "+juliafile) # rm the file
    else:
        print("We already downloaded to ",mpath+"/src/julia/julia-1.6.1/bin/julia")
             
    julia_cmd = mpath+"/src/julia/julia-1.6.1/bin/julia" # path for julia
    os.chdir(mpath) # go back

else: 
    julia_cmd = "julia"
    print("Correct Julia version found in path")


print("julia command : ", julia_cmd)

# install python dependences
os.system("python3 -m pip install --user julia")

#using julia
#import julia
#julia.install()


#os.system("pip install pmdarima")


# install 
sysimage = os.environ["HOME"]+"/.julia/sysimages/sys_threebodytb.so"
if not os.path.isfile(sysimage):
    import src.juliarun as juliarun
    juliarun.install(julia_cmd) # install Julia dependences


from julia.api import Julia
jlsession = Julia(runtime=julia_cmd, compiled_modules=False, sysimage=sysimage)
jlsession.eval("using Suppressor") # suppress output

from julia import ThreeBodyTB

c = ThreeBodyTB.makecrys( [[5.0,0,0],[0,5.0,0],[0,0,5.0]] , [[0, 0, 0]], ["Li"])

print()
print("result of makecrys")
print(c)
print()
print("the end")
print()
