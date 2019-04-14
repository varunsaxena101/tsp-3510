## Varun Saxena and Ahan Shah

import sys

#print(sys.argv)
args = sys.argv

# process inputs
input_coords_file = args[1]
output_file = args[2]
time_allowed = args[3]


my_dict = {}
# read in coordinates
input_file = open(input_coords_file, "r")

line = input_file.readline()
while(line is not ''):
    a = line.split(" ")
    my_dict[int(float(a[0]))] = (int(float(a[1])), int(float(a[2])))
    line = input_file.readline()

print(my_dict)
# write to output file

path_length = 4
path_sequence = ['1', '2', '3', '4']

f = open(output_file, "w")
string1 = str(path_length)
separator = " "
seq = separator.join(path_sequence)
f.write(string1 + '\n' + seq)