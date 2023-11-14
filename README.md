# fisher-exact-test-mcmc

A command line tool that calculate p value of Fisher's exact test using MCMC.
Each sample is determined by Markov basis.

This tool only supports 2x2 contingency table.

## Requirements

- Python >= 3.9
- Libraries that are listed in requirements.txt

## Usage

To visualize MCMC samples:

```
python3 main.py visualize 3 4 5 6 --sample 10
```

To calculate p value:

```
python3 main.py p-value 3 4 5 6 --burn-in 0 --sample 1000
```
