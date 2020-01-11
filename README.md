# Tupper's Self-Referential Formula plotter

This Python package plots Tupper's Self-Referential Formula for *(0 ≤ x < 106, k ≤ y < k + 17)*.

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

The plot of that number will draw Tupper's Self-Referential Formula itself,
which is **super cool**.

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

There's an awesome video about the formula here:
https://www.youtube.com/watch?v=_s5RFgd59ao

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

## Test data

The **test_data** directory contains CSV files for testing the calculation.

Each file contains three columns:

1. The `x` coordinate.
2. The `y` coordinate.
3. The expected `true`/`false` solution.
