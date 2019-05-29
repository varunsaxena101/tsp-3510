# Traveling Salesman - Simulated Annealing with Timer

## Made By
Varun Saxena
Ahan Shah
April 19th, 2019

## Files
- mat-test.txt: Given test data (Node ID, x coordinate, y coordinate)
- mat-solution.txt: created log file that states distance of tour and sequence of nodes traversed
- proof.txt: log file of smallest path length and sequence found
- tsp-3510.py: traveling salesman implementation using simulated annealing with timer

## Running Program
Run the program by opening terminal and navigating to folder containing files. Then run the following command:

`python3 tsp-3510.py <input-coordinates.txt> <output-tour.txt> <time>`  

Sample command:  
`python3 tsp-3510.py mat-test.txt mat-solution.txt 120`

## Known Bugs and Limitations
- Always uses the first node provided in the input file as the start and end node
- Always reserves 0.5 seconds to write to output file
- Temperature is based on input time
