# Galino_Gonzales_P-system-simulator

This simulator is a Python implementation of the Single Cell P-system
proposed by **Radu Nicolescu** in [Parallel Thinning With Complex Objects and
Actors](https://link.springer.com/chapter/10.1007/978-3-319-14370-5_21 "*Parallel Thinning With
Complex Objects and Actors") in 2014. This model is one of three proposed membrane computing models
of the Guo-Hall Skeletonization

Algorithm in the same paper.

The Program has 3 Versions:
1. `Single Process Simulator (SPS)` - Baseline simulator with each rule being applied across an image using one process
2. `Multiprocess Simulator (MPS)` - Improved to make use of multiprocessing
3. `Multiprocess Simulator with NumPy (MPS_NP)` - Optimized version which uses Numpy to optimize the loops that occur.

## Installation
It is recommended to use a virtual environment for installing dependencies. You can create a virtual
environment using the following command.
```python
python -m venv .venv
source .venv/bin/activate
```
This project needs numpy and pillow. You may install them using the following command:
```python
pip install numpy pillow
```

## Authors

- [@jhgalino](https://github.com/jhgalino)
- [@Koniiro](https://github.com/Koniiro)

## References
- Nicolescu, R. (2014). Parallel Thinning with Complex Objects and Actors. In: Gheorghe, M., Rozenberg, G., Salomaa, A., Sosík, P., Zandron, C. (eds) Membrane Computing. CMC 2014. Lecture Notes in Computer Science(), vol 8961. Springer, Cham. https://doi.org/10.1007/978-3-319-14370-5_21
