# Galino_Gonzales_P-system-simulator

This simulator is a Python implementation of the Single Celled P-system proposed by **Radu Nicolescu** in [Parallel Thinning With Complex Objects and Actors](https://link.springer.com/chapter/10.1007/978-3-319-14370-5_21 "*Parallel Thinning With Complex Objects and Actors") in 2014. This model is one of three proposed membrane computing models of the Guo-Hall Skeletonization Algorithm in the same paper.

The program primarily consists of three files:  
1. `SCP System G_H Implementation.py` - Primary Implementation File
2. `neighbor_gen_module.py` - Calculates the coordinates of the neighbors of a specified cell
3. `rule_module.py` - Implementation of Rules described in Nicolescu 2014

## Usage

### Input
The primary input of the simulator  is the nested-array *nodes*, structured as a 3x3 grid following the format used in Nicolescu (2014). This array consists of three sub-arrays, each containing three additional sub-arrays, effectively forming a 3x3 structure. These cells store the initial configuration of the grid for processing.


<figure style="text-align: center;">
	<figcaption><em>Figure 1: A sample initial configuration of the image below can be found in Code Block 1 </em></figcaption>
  <p align="center"><img src="https://github.com/Koniiro/Galino_Gonzales_P-system-simulator/blob/main/Images/Initial%20State.png" alt="Sample Initial Configuration"></p>
  
</figure>


#### Code Block 1
```python
#Sample Initial Configuration of  3x3 Grid
nodes=[
		[["pb","s0"],["pb","s0"],["pb","s0"]],
		[["pw","s0"],["pb","s0"],["pw","s0"]],
		[["pw","s0"],["pw","s0"],["pw","s0"]]
    ]
```
### Runtime
During runtime, the simulator processes each rule by attempting to apply it to the cells in the grid. If a cell meets the rule's conditions, the rule is applied. The simulator will display the rule being applied and print the contents of each cell after the application attempt. The cells are printed in order: (0,0), (0,1),(0,2),(1,0), ..., (2,2).

#### Code Block 2
```python
Executing rule_01:
['pb', 's0']
['pb', 's0']
['pb', 's0']
['pw', 's1']
['pb', 's0']
['pw', 's1']
['pw', 's1']
['pw', 's1']
['pw', 's1']
```

<figure style="text-align: center;">
	<figcaption><em>Figure 2: State of grid following application of Rule 1 </em></figcaption>
  <p align="center"><img src="https://github.com/Koniiro/Galino_Gonzales_P-system-simulator/blob/main/Images/R1State.png" alt="State of grid after Rule 1"></p>
  
</figure>
<figure style="text-align: center;">
	<figcaption><em>Figure 3: Rule 1 as described in Nicolescu (2014) </em></figcaption>
  <p align="center"><img src="https://github.com/Koniiro/Galino_Gonzales_P-system-simulator/blob/main/Images/rule1.png" alt="Rule 1 Nicolescu (2014)"></p>
</figure>


After attempting to apply each implemented rule, the simulator will check the value of the variable `checksum`. This value is used to determine how many times rule 11 has been successfully applied.

In other words, if a cell was changed from black to white as part of the skeletonization process, it means rule 11 was applied. If rule 11 has been applied at least once, the simulator will conduct another round of applying each rule.

<figure style="text-align: center;">
	<figcaption><em>Figure 4: Rule 11 as described in Nicolescu (2014) </em></figcaption>
  <p align="center"><img src="https://github.com/Koniiro/Galino_Gonzales_P-system-simulator/blob/main/Images/r11.png" alt="Rule 11 Nicolescu (2014)"></p>
</figure>


This process will continue until rule 11 can no longer be applied.
###Output
If no further rounds are to be conducted, the simulator will print out the final configuration of the 3x3 grid as well as indicate how many rounds were taken to reach this result.

#### Code Block 3
```python
=====Finished=====
Final Configuration
Rounds Taken: 2
[['s2', 'h1', 'pw'], ['pb', 's12', 'h1'], ['s2', 'h1', 'pw']]
[['pw', 's2'], ['s2', 'h1', 'pw'], ['pw', 's2']]
[['pw', 's2'], ['pw', 's2'], ['pw', 's2']]
```

<figure style="text-align: center;">
	<figcaption><em>Figure 5: Final state of grid following skeletonization </em></figcaption>
<p align="center"><img src="https://github.com/Koniiro/Galino_Gonzales_P-system-simulator/blob/main/Images/Final%20State.png" alt="Sample Final Configuration"></p>
  
</figure>


 
## Authors

- [@jhgalino](https://github.com/jhgalino)
- [@Koniiro](https://github.com/Koniiro)

## References
- Nicolescu, R. (2014). Parallel Thinning with Complex Objects and Actors. In: Gheorghe, M., Rozenberg, G., Salomaa, A., Sosík, P., Zandron, C. (eds) Membrane Computing. CMC 2014. Lecture Notes in Computer Science(), vol 8961. Springer, Cham. https://doi.org/10.1007/978-3-319-14370-5_21
