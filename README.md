# ThreeBodyTB_python

by Kevin F. Garrity

This is a python wrapper for the
[ThreeBodyTB.jl](http://github.com/kfgarrity/ThreeBodyTB.jl) Julia
package, which runs two- and three-body tight-binding calculations for
materials.

Using the Julia version directly is the primary method for running the
code. However, I recognize many materials science codes are written in
python. Therefore, I have created this wrapper to help people with no
Julia knowledge run the code using the
[PyJulia](https://github.com/JuliaPy/pyjulia) interace.

## Installation

1) Clone this distribution.

    git clone https://github.com/kfgarrity/ThreeBodyTB_python.git

2) Run the installation

    python3 install.py

Note that this can take a while and may use sigifigant disk space. The code
will, if necessary, a) download & install Julia b) download & install
ThreeBodyTB.jl, and c) create a system image for fast loading.


3) Import TB3.py

Example usage :

    >>> import TB3
    >>> import numpy as np
    >>> A = np.eye(3) * 5.0
    >>> coords = np.zeros((1,3))
    >>> c = TB3.jl.makecrys(A, coords, ["Li"])
    >>> energy, tbc, flag = TB3.jl.scf_energy(c)


