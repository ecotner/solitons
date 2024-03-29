# Solitons

A lot of my PhD work involved working with solitons of various types, such as Q-balls, oscillons, boson stars, axion miniclusters, etc.
I think they are pretty cool and often don't get the attention they deserve.
This repo will serve as a place for me to "collect" solitons of varying types.
I think for each type, I will have like a little theory section that explains the math behind them, and then I will do some actual numerical computation of some kind to illustrate them.
Depending on the kind of soliton, dimensionality, number of parameters, perhaps it will be an animation, snapshot, visualization of some parameter space?

## Numerical calculations
Recent advances in scientific computing have led to a variety of easy-to-use tools for performing numerical computations.
Within the python environment, `numpy`, `scipy` and `numba` can take advantage of JIT compilation, vectorization, multithreading/multiprocess speedups... even GPU acceleration with custom kernels!
So I don't feel any need to use a language other than python for now.

## Conventions
In most places, I will be using natural units (unless specifically noted otherwise). This means that:
* $c = \hbar = k_B = \varepsilon_0 = \mu_0 = 1$
* energy, mass, temperature, all are measured in units of energy (eV, MeV, GeV, ...)
* length, time, etc. are measured in units of inverse energy (1/eV, ...)
* angular momentum, electric charge, etc. are dimensionless
* Newton's gravitational constant can be rewritten as $G = 1/M_p^2$, where $M_p \approx 1.22\times 10^{19}$ GeV is the Planck mass

I prefer to use the "mostly minus" spacetime metric, so that $ds^2 = dt^2 - dx^2$, $ds < 0$ denotes a timelike interval, $ds > 0$ a spacelike interval, and $ds = 0$ a lightlike interval.

## Simulation list:
Click the ✅ to go to the notebook for that scenario.

| status | field content | kinetic term | potential | gravity | \# dim. | time dep. |
| --- | --- | --- | --- | --- | --- | --- |
| [✅](./simulations/01_nonlinear_schrodinger_1d_stationary.ipynb) | single scalar | Schrodinger | $\alpha (\|\psi\|^2-\bar{\psi}^2)^2$ | no | 1D | no |
| [✅](./simulations/02_nonlinear_schrodinger_1d_collisions.ipynb) | single scalar | Schrodinger | $\alpha (\|\psi\|^2-\bar{\psi}^2)^2$ | no | 1D | yes - binary collisions |
| ❌ | single scalar | Klein-Gordon | $\alpha\cos(\phi/M)$ | no | 1D | no |
| ❌ | two scalars | Schrodinger | $\alpha(\chi^2 - \bar{\chi}^2)^2 + \beta \chi^2 \|\psi\|^2$ | no | 1D | no |
| ❌ | single scalar | Schrodinger | $\alpha (\|\psi\|^2-\bar{\psi}^2)^2$ | no | 3D | no |
| ❌ | single scalar | Schrodinger | $\alpha (\|\psi\|^2-\bar{\psi}^2)^2$ | no | 3D | binary collisions |
| ❌ | single scalar | Schrodinger | $\alpha (\|\psi\|^2-\bar{\psi}^2)^2$ | Newtonian | 3D | no |
| ❌ | single scalar | Schrodinger | $\alpha (\|\psi\|^2-\bar{\psi}^2)^2$ | Newtonian | 3D | binary collisions |
| ❌ | single scalar + $U(1)$ gauge field | Schrodinger | $\alpha (\|\psi\|^2-\bar{\psi}^2)^2$ | no | 3D | no |
| ❌ | single scalar | Klein-Gordon | $\alpha (\|\phi\|^2-\bar{\phi}^2)^2$ | no | 1D | no |
| ❌ | single scalar | Klein-Gordon | $\alpha (\|\phi\|^2-\bar{\phi}^2)^2$ | no | 1D | binary collisions |
| ❌ | single scalar | Klein-Gordon | $\alpha (\|\phi\|^2-\bar{\phi}^2)^2$ | no | 1D | condensate fragmentation |
