# Galino_Gonzales_P-system-simulator

This simulator is a Python implementation of the Single Cell P-system
proposed by **Radu Nicolescu** in [Parallel Thinning With Complex Objects and
Actors](https://link.springer.com/chapter/10.1007/978-3-319-14370-5_21 "*Parallel Thinning With
Complex Objects and Actors") in 2014. This model is one of three proposed membrane computing models
of the Guo-Hall Skeletonization

Algorithm in the same paper.

The program primarily consists of three files:  
1. `SCP System G_H Implementation.py` - Primary Implementation File
2. `neighbor_gen_module.py` - Calculates the coordinates of the neighbors of a specified cell
3. `rule_module.py` - Implementation of Rules described in Nicolescu 2014

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

## Usage

To run the project, just run `SCP_System-G_H-Implementation.py`. It requires several arguments.
```python
python SCP_System-G_H-Implementation.py <path> -t <threshold> <-n>
```
- `path` - Path to the image to be skeletonized. Required
- `-t <threshold>` - The threshold for binarization. Must be from 0 to 255. Optional, defauts to 127
- `-n` - Add this flag if the inverse of the image will be skeletonized. Optional.

## How to setup experiments
- Test Case 3
Get the image at https://drive.google.com/file/d/1FI0KbZYQwI6UBn-FpoeVZPv64TipWNzX/view?usp=sharing.
You can run the skeletonization using the following command.
```python
python SCP_System-G_H-Implementation.py <path to image> -t 100 # for normal
python SCP_System-G_H-Implementation.py <path to image> -t 100 -n # for inversed
```

## Multiprocessed Version
The multiprocess version of the project can be found at the `multiProc4Segment` branch
of the repository.

## Authors

- [@jhgalino](https://github.com/jhgalino)
- [@Koniiro](https://github.com/Koniiro)

## References
- Nicolescu, R. (2014). Parallel Thinning with Complex Objects and Actors. In: Gheorghe, M., Rozenberg, G., Salomaa, A., Sosík, P., Zandron, C. (eds) Membrane Computing. CMC 2014. Lecture Notes in Computer Science(), vol 8961. Springer, Cham. https://doi.org/10.1007/978-3-319-14370-5_21
