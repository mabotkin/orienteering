# Orienteering Round Generator
This is a program to generate an Orienteering Round.  The program should output a series of room assignments for easy setup of the paths of each team.  The program also outputs a direction for each team to map its answer to the next room number (very basic mapping, only uses four basic operations).  Designed for TJIMO 2016.

## Configuration

In the file "rooms.txt", list all room numbers to be used in the generation.  This can be sequential or out of order - they will be in order before scrambling.

In the file "ans.txt", list the answers to questions in correct order so the program can generate mappings between answers and room numbers.

To run the program, type:

```bash
$ python gen.py
```

The output should be produced in a file named "out.txt".

This program is designed for Python 2 but aside from print statements should be compatible with Python 3 as well.
