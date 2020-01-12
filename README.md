# Tupper's Self-Referential Formula plotter

This Python package calculates and plots Tupper's Self-Referential Formula.

I've written about the formula and this project at [Tupper’s Self-Referential Formula in Python](https://cariad.io/tupper/).

The video that influenced this whole thing is here: https://www.youtube.com/watch?v=_s5RFgd59ao

```text
        █                   █                █ ██ █     █                █  █ █     █    █ ██ █      █   █
        █                   █ █      █       █  █ █     █                █  █ █     █    █  █ █      █   █
██      █                  █  █      █    ██ █  █ █ █ █ █ ██ ████  ███ ███ █  █ █ █ █    █  █  █      █  █
 █      █                  █  █  █ █ █       █ █  █  █  █    █ █ █ █ █ █ █ █  █ █ █ █    █ █   █      █  █
 █      █                  █  █  █ █ █       █ █  █ █ █ █    █ █ █ ███ ███ █  █  █  █    █ █   █      █  █
 █      █               █ █   █   █  █  ██        █     █                  █  █ █   █  █       █   ██  █ █
███   █ █               █ █   █  █   █ █  █       █     █                   █ █     █  █      █   █  █ █ █
     █  █ ██ █   ██   ███ █   █      █   █        ███ ███                   █ ███ ███ █       █     █  █ █
███ █   █ █ █ █ █  █ █  █ █   █ ████ █  █                                                          █   █ █
     █  █ █ █ █ █  █ █  █ █   █      █ █                                                          █    █ █
██    █ █ █ █ █  ██   ███ █   █ █ ██ █ ████                                                       ████ █ █
  █     █                 █   █ █  █ █                                                          █      █ █
 █      █                  █  █ █  █ █                                                          █     █  █
█       █                  █  █ █ █  █                                                         █      █  █
███     █                  █  █ █ █  █                                                                █  █
        █                   █ █      █                                                               █   █
        ███                 █ ███  ███                                                               █ ███
```

## Requirements

- Python 3

## Installation

```shell
pip3 install tupper
```

## Console usage

```shell
python3 -m tupper
```

Optional arguments:

- `--help` -- show usage instructions.
- `--k <number>` -- the value of *k* to plot.
- `--true <string>` -- the string to print for *truthy* points.
- `--false <string>` -- the string to print for *falsy* points.
- `--export <filename>` -- export the (x, y) coordinates and their truthy solution to a CSV file.

If you don't specify *k* then *k* =

```text
9609393799189588849716729621278527547150043396601293066515055192717028023952664
2468964284217435071812126715378277062335599323728087414430789132596394133772348
7857735749823926629715517173716995165232890538221612403238855866184013235585136
0488286933379024914542292886670810961844960917051834540678277315517054053816273
8096760256562501698148208341878316384911559022561000365235137034387446184837873
7238198224849863465033159410054974700593138339226497249461751545728366702369745
461014655997933798537483143786841806593422227898388722980000748404719
```

## Code usage

### `Solver` class

To solve ad-hoc *(x, y)* points, import the `Solver` class and call the `solve(x, y)` function:

```python
from tupper import Solver
# ...
s = Solver()
b = s.solve(x, y)
```

`x()` and `y()` functions are provided for yielding the coordinates of a graph:

```python
from tupper import Solver
# ...
s = Solver()
k = 960939379918958...
for y in s.y(k):
    for x in s.x():
        b = s.solve(x, y)
```

### `StringPlotter` class

`StringPlotter` exposes two functions for rendering graphs as text.

`row()` yields the characters for any given row:

```python
from tupper import StringPlotter
# ...
sp = StringPlotter(true_mark="x", false_mark=" ")
k = 960939379918958...
for c in sp.row(k):
    print(c, end="")
```

`graph()` yields the characters for the entire graph, including newlines at the end of each row:

```python
from tupper import StringPlotter
# ...
sp = StringPlotter(true_mark="x", false_mark=" ")
k = 960939379918958...
for c in sp.graph(k):
    print(c, end="")
```

## Test data

The **test_data** directory contains CSV files for testing the calculation.

Each file contains three columns:

1. The `x` coordinate.
2. The `y` coordinate.
3. The expected `true`/`false` solution.
