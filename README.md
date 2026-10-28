# Insertion Sort Algorithm

A Python implementation of insertion sort (sorts in decreasing order) with its own file reader. You can put any data in the format below, and the program will read it and sort it for you.

## Data format

The input file is plain text with numerical values separated by commas, all on a single line:

```
5,2,4,6,1,3
```

## Usage

Run `main.py` and type the path to the file you want to use:

```
python3 main.py
```

The program asks:

```
Specify the file to get data from: examples/large.txt
```

It then prints the input data and the data after sorting.

## Examples

The `examples` folder has four ready-made input files:

| File              | Numbers |
| ----------------- | ------- |
| `small.txt`       | 10      |
| `large.txt`       | 1,000   |
| `extra_large.txt` | 10,000  |
| `ginormous.txt`   | 100,000 |

Note: I made these to test how time-consuming the algorithm gets with different amounts of data. With the smaller files you won't notice anything, but with `ginormous.txt` you will really feel the difference. You can make the file even bigger, but make sure you have powerful enough hardware and be ready to wait, because even `ginormous.txt` takes a long time.
