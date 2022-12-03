import sys
import math

# Info of the cache
scale = 32
addrs_bits = 32
memory_size = (2**20)*2**4
cache_line_size = 2**6
asso = 8
cache_lines = memory_size/cache_line_size
sets = cache_lines/asso
offset_bits_no = int(math.log2(cache_line_size))
index_bits_no = int(math.log2(sets))
tag_bits_no = int(addrs_bits - (offset_bits_no + index_bits_no))

# Arguments
fileinput = sys.argv[1]
arg = sys.argv[2]

# Initialization of the list and dictionary variables
trace_line_lst = list()

if arg =="N":
    with open(fileinput, 'r') as f:
        trace_line_str = f.read() # Here 'linetrace' represents every line of the trace file
        trace_line_lst = trace_line_str.rstrip().split('\n') # Removes the whitespace from strings and converts them to list

# Following is the list() containing that will contain all the tag arrays in hex
    for i in range(len(trace_line_lst)):
        trace_line_tag_array = trace_line_lst[i][2:]
        trace_line_tag_array_bin = bin(int(trace_line_tag_array, 16))[2:].zfill(32)
        offset_bits_bin = trace_line_tag_array_bin[tag_bits_no + index_bits_no:]
        index_bits_bin = trace_line_tag_array_bin[tag_bits_no: tag_bits_no + index_bits_no]
        tag_bits_bin = trace_line_tag_array_bin[0:tag_bits_no]
        n_bit = trace_line_lst[i][0:1]
        way1 = {'MESI': 00, 'Valid Bit': 0, 'Tag': tag_bits_bin, 'Index': index_bits_bin, 'Offset Bit': offset_bits_bin}
        print(way1)




    print("The process has been completed in Normal Mode")

elif arg =="S":
    print("The process has been completed in Silent Mode")
else:
    print("Please select a Valid mode")
