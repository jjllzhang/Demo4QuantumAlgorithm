# Demo4QuantumAlgorithm
A demo repo used to simulate quantum algorithm based on Cirq implementation and compare it to classical algorithm.

## Installation

Note: 

* I would prefer to recommend you to install the dependencies in another virtual environment for safety and simplicity. However, it is also OK if you install the dependencies just in the current working environment.

* Make sure you have python 3.7.0 or greater.

### Use requirements.txt

run the command below in the terminal:

```bash
pip install -r requirments.txt
```

### Install step by step

Here I referred to the [official document of Cirq](https://quantumai.google/cirq/start/install). If there is any ambiguity, please refer to it.

#### Linux

* Use `pip` to install [`cirq`](https://quantumai.google/reference/python/cirq):

```bash
  python -m pip install --upgrade pip
  python -m pip install cirq
```

* (Optional) install other dependencies. Install dependencies of features in [`cirq.contrib`](https://quantumai.google/reference/python/cirq/contrib).

```bash
python -m pip install cirq-core[contrib]
```

* Install system dependencies that pip can't handle. Without `texlive-latex-base` and `latexmk`, pdf writing functionality will not work.

```bash
sudo apt-get install texlive-latex-base latexmk
```

* Check that it works!

```bash
python -c 'import cirq_google; print(cirq_google.Sycamore)'
# should print:
#                                              (0, 5)───(0, 6)
#                                              │        │
#                                              │        │
#                                     (1, 4)───(1, 5)───(1, 6)───(1, 7)
#                                     │        │        │        │
#                                     │        │        │        │
#                            (2, 3)───(2, 4)───(2, 5)───(2, 6)───(2, 7)───(2, 8)
#                            │        │        │        │        │        │
#                            │        │        │        │        │        │
#                   (3, 2)───(3, 3)───(3, 4)───(3, 5)───(3, 6)───(3, 7)───(3, 8)───(3, 9)
#                   │        │        │        │        │        │        │        │
#                   │        │        │        │        │        │        │        │
#          (4, 1)───(4, 2)───(4, 3)───(4, 4)───(4, 5)───(4, 6)───(4, 7)───(4, 8)───(4, 9)
#          │        │        │        │        │        │        │        │
#          │        │        │        │        │        │        │        │
# (5, 0)───(5, 1)───(5, 2)───(5, 3)───(5, 4)───(5, 5)───(5, 6)───(5, 7)───(5, 8)
#          │        │        │        │        │        │        │
#          │        │        │        │        │        │        │
#          (6, 1)───(6, 2)───(6, 3)───(6, 4)───(6, 5)───(6, 6)───(6, 7)
#                   │        │        │        │        │
#                   │        │        │        │        │
#                   (7, 2)───(7, 3)───(7, 4)───(7, 5)───(7, 6)
#                            │        │        │
#                            │        │        │
#                            (8, 3)───(8, 4)───(8, 5)
#                                     │
#                                     │
#                                     (9, 4)
```

#### Mac OS X

* Use `pip` to install [`cirq`](https://quantumai.google/reference/python/cirq):

```bash
python -m pip install --upgrade pip
python -m pip install cirq
```

* (Optional) install dependencies of features in [`cirq.contrib`](https://quantumai.google/reference/python/cirq/contrib).

```bash
python -m pip install cirq-core[contrib]
```

* Install system dependencies that pip can't handle. Without `mactex`, pdf writing functionality will not work.

```bash
brew cask install mactex
```

* Check that it works!
```bash
python -c 'import cirq_google; print(cirq_google.Sycamore)'
# should print:
#                                              (0, 5)───(0, 6)
#                                              │        │
#                                              │        │
#                                     (1, 4)───(1, 5)───(1, 6)───(1, 7)
#                                     │        │        │        │
#                                     │        │        │        │
#                            (2, 3)───(2, 4)───(2, 5)───(2, 6)───(2, 7)───(2, 8)
#                            │        │        │        │        │        │
#                            │        │        │        │        │        │
#                   (3, 2)───(3, 3)───(3, 4)───(3, 5)───(3, 6)───(3, 7)───(3, 8)───(3, 9)
#                   │        │        │        │        │        │        │        │
#                   │        │        │        │        │        │        │        │
#          (4, 1)───(4, 2)───(4, 3)───(4, 4)───(4, 5)───(4, 6)───(4, 7)───(4, 8)───(4, 9)
#          │        │        │        │        │        │        │        │
#          │        │        │        │        │        │        │        │
# (5, 0)───(5, 1)───(5, 2)───(5, 3)───(5, 4)───(5, 5)───(5, 6)───(5, 7)───(5, 8)
#          │        │        │        │        │        │        │
#          │        │        │        │        │        │        │
#          (6, 1)───(6, 2)───(6, 3)───(6, 4)───(6, 5)───(6, 6)───(6, 7)
#                   │        │        │        │        │
#                   │        │        │        │        │
#                   (7, 2)───(7, 3)───(7, 4)───(7, 5)───(7, 6)
#                            │        │        │
#                            │        │        │
#                            (8, 3)───(8, 4)───(8, 5)
#                                     │
#                                     │
#                                     (9, 4)
```

#### Windows

* Use `pip` to install [`cirq`](https://quantumai.google/reference/python/cirq):

```bash
python -m pip install --upgrade pip
python -m pip install cirq
```

* (Optional) install dependencies of features in [`cirq.contrib`](https://quantumai.google/reference/python/cirq/contrib).

```bash
python -m pip install cirq-core[contrib]
```

* Check that it works!

```bash
python -c "import cirq_google; print(cirq_google.Sycamore)"
# should print:
#                                              (0, 5)───(0, 6)
#                                              │        │
#                                              │        │
#                                     (1, 4)───(1, 5)───(1, 6)───(1, 7)
#                                     │        │        │        │
#                                     │        │        │        │
#                            (2, 3)───(2, 4)───(2, 5)───(2, 6)───(2, 7)───(2, 8)
#                            │        │        │        │        │        │
#                            │        │        │        │        │        │
#                   (3, 2)───(3, 3)───(3, 4)───(3, 5)───(3, 6)───(3, 7)───(3, 8)───(3, 9)
#                   │        │        │        │        │        │        │        │
#                   │        │        │        │        │        │        │        │
#          (4, 1)───(4, 2)───(4, 3)───(4, 4)───(4, 5)───(4, 6)───(4, 7)───(4, 8)───(4, 9)
#          │        │        │        │        │        │        │        │
#          │        │        │        │        │        │        │        │
# (5, 0)───(5, 1)───(5, 2)───(5, 3)───(5, 4)───(5, 5)───(5, 6)───(5, 7)───(5, 8)
#          │        │        │        │        │        │        │
#          │        │        │        │        │        │        │
#          (6, 1)───(6, 2)───(6, 3)───(6, 4)───(6, 5)───(6, 6)───(6, 7)
#                   │        │        │        │        │
#                   │        │        │        │        │
#                   (7, 2)───(7, 3)───(7, 4)───(7, 5)───(7, 6)
#                            │        │        │
#                            │        │        │
#                            (8, 3)───(8, 4)───(8, 5)
#                                     │
#                                     │
#                                     (9, 4)
```

## Usage

### General Usage

cd into the `./examples` and run the command like `python grover.py` to see the simulated results. Also use commands like  `python shor.py -h`  to seek for help.

### Demo.py

Run the command `python demo.py -h` to see the detailed instructions. 

Demo.py is a script used to measure the running time of different algorithm.

Here is an example used to measure the average running time of shors.py in different mode by running 5 times:

```bash
python demo.py shor.py --arguments "--order_finder naive 3871" "--order_finder quantum 3871" --runs 5
```

## Flaw

When performing the simulation of the Shor’s algorithm, please be careful not to choose too large a number to avoid errors (because this is after all a classical computer simulation of quantum computing). After many experiments, it is best not to exceed 7500 (a rather strange number) in the Shor’s algorithm.

## Citation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7465577.svg)](https://doi.org/10.5281/zenodo.7465577)
