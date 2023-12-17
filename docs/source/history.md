# History

## Creation of `hapsira`, by Sebastian M. Ernst

`hapsira` began as a fork of the then unmaintained and archived `poliastro` in October 2023. Its aim is the continuation of `poliastro`'s development with an emphasis on speed and package structure.

## Creation of `poliastro`, by Juan Luis Cano Rodríguez

I started `poliastro` as a wrapper of some MATLAB and Fortran algorithms that I needed for a University project: having good performance was a must, so pure Python was not an option. As a three language project, it was only known to work in my computer, and I had to fight against [oct2py](https://pypi.org/project/oct2py/) and [f2py](https://numpy.org/doc/stable/f2py/) for long hours.

Later on, I enhanced the plotting capabilities of `poliastro` to serve me in additional university tasks. I removed the MATLAB (Octave) code and kept only the Fortran algorithms. Finally, when numba was mature enough, I implemented everything in pure Python and `poliastro` 0.3 was born.

I am Juan Luis Cano Rodríguez (two names and two surnames, it\'s the Spanish way!), an Aerospace Engineer with a passion for Astrodynamics and the Open Source world. Before hapsira started to be a truly community project, I started it when I was an Erasmus student at Politecnico di Milano, an important technical university in Italy which deeply influenced my life and ambitions and gave name to the library itself. It is and always will be my tiny tribute to a country that will always be in my heart and to people that never ceased to inspire me. *Grazie mille!*

## Future ideas

`hapsira`/`poliastro` has been historically focused on interplanetary applications, so we would like to improve its Earth-specific capabilities in the future, for example:

- High order gravitational model for the Earth
- Input/output of TLE and other GP data format
- Attitude & dynamics

And in general, we would like to stabilize the API and release a 1.0 version at some point!
