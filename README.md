# Isotope Mass Calculator #

The program computes the isotope pattern of a given molecular formula.

## Program use ##

```
python -m <name> --config-file=<file> C6H12O6
```

## File ##

mass  
neutron mass = 1.0001  
ratios = 90.0, 10.0

```
[
  {
    "name": "C",
    "alias": "carbon",
    "isotopes": [
      {
        "name": "C12",
        "mass": 12.0,
        "abundance": 98.93
      },
      {
        "name": "C13",
        "mass": 13.0,
        "abundance": 0.07
      }
    ]
  }
]

elements:
- name: C
  alias: carbon
  isotopes:
  - name: C12
    mass: 12.0
    abundance: 98.93
  - name:
- name:
```

```
[C]
C12 = 
13 = 13.0
[H]
0 = 1.00
1 = 2.00
2 = 3.00
[O]
16 = 1.00
```