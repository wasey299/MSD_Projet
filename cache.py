import sys
import math

# Info of the cache
Address_size = 32
Memory_size = (2**20)*2**4
Cache_line_size = 2**6
Ways = 8
Cache_lines = Memory_size/Cache_line_size
Sets = Cache_lines/Ways
Offset_bits = int(math.log2(Cache_line_size))
Index_bits = int(math.log2(Sets))
Tag_bits = int(Address_size - (Offset_bits + Index_bits))

# Arguments
fileinput = sys.argv[1]
arg = sys.argv[2]

# Initialization of the list variables
Trace_line_list = list()
Trace_line_list_2d = list()
Trace_line_dict_2d = dict()
Trace_line_list_2d_hex = list()
Trace_line_list_2d_hex_ext = [""]*int(Sets)
Sets_list = [""]*int(Sets)
Cache_structure = list()
Tests_list = list()
n_bit_list = list()
Tag_list = list()
Index_list = list()
Offset_list = list()
n_bit_list_ext = list()
Tag_list_ext = list()
Index_list_ext = list()
Offset_list_ext = list()
Trace_line_list_2d_ext = [""]*int(Sets)
Trace_line_dict_list = list()
#Some Variable
Index_count:int = 0

#if arg =="N":
with open(fileinput, 'r') as f:
    Trace_line_string = f.read() # Here 'linetrace' represents every line of the trace file
    Trace_line_list = Trace_line_string.rstrip().split('\n') # Removes the whitespace from strings and converts them to list

# Following is the list() containing that will contain all the tag arrays in hex
for i in range(len(Trace_line_list)):
    n_bit = int(Trace_line_list[i][0:1])
    n_bit_list.append(n_bit)
    Trace_line_tag_array = Trace_line_list[i][2:]
    Trace_line_tag_array_bin = bin(int(Trace_line_tag_array, 16))[2:].zfill(32)
    Offset_bin = Trace_line_tag_array_bin[Tag_bits + Index_bits:]
    Index_bin = Trace_line_tag_array_bin[Tag_bits: Tag_bits + Index_bits]
    Tag_bin = Trace_line_tag_array_bin[0:Tag_bits]
    Offset = int(Offset_bin, 2)
    Offset_list.append(Offset)
    Offset_hex = hex(int(Offset_bin, 2))[2:]
    Index = int(Index_bin, 2)
    Index_list.append(Index)
    Index_hex = hex(int(Index_bin, 2))[2:]
    Tag = int(Tag_bin, 2)
    Tag_list.append(Tag)
    Tag_hex = hex(int(Tag_bin, 2))[2:]
    Trace_line_list_2d.append([n_bit, Tag, Index, Offset])
    Trace_line_list_2d_hex.append([n_bit, Tag_hex, Index_hex, Offset_hex])


# Cache Structure

for index_count in range(len(Sets_list)):
    #Cache_structure.append([index_count, "LRU", "Way1", "Way2", "Way3", "Way4", "Way5", "Way6", "Way7", "Way8"])
    Cache_structure.append([index_count, 0])


for trace_line in Trace_line_list_2d:
    for cache_line in Cache_structure:
        if trace_line[2] == cache_line[0]:
            if trace_line[0] == 0:
                    if trace_line[1] == cache_line[2]:
                        if cache_line[1] == "I":
                            cache_line[1] = "E"
                        elif cache_line[1] == "S":
                            cache_line[1] == "S"
                        elif cache_line[1] == "E":
                            cache_line[1] == "E"
                        elif cache_line[1] == "M":
                            cache_line[1] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[1]))
                        break

                    if trace_line[1] == cache_line[4]:
                        if cache_line[3] == "I":
                            cache_line[3] = "E"
                        elif cache_line[3] == "S":
                            cache_line[3] == "S"
                        elif cache_line[3] == "E":
                            cache_line[3] == "E"
                        elif cache_line[3] == "M":
                            cache_line[3] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[3]))
                        break

                    if trace_line[1] == cache_line[6]:
                        if cache_line[5] == "I":
                            cache_line[5] = "E"
                        elif cache_line[5] == "S":
                            cache_line[5] == "S"
                        elif cache_line[5] == "E":
                            cache_line[5] == "E"
                        elif cache_line[5] == "M":
                            cache_line[5] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[5]))
                        break

                    if trace_line[1] == cache_line[8]:
                        if cache_line[7] == "I":
                            cache_line[7] = "E"
                        elif cache_line[7] == "S":
                            cache_line[7] == "S"
                        elif cache_line[7] == "E":
                            cache_line[7] == "E"
                        elif cache_line[7] == "M":
                            cache_line[7] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[7]))
                        break

                    if trace_line[1] == cache_line[10]:
                        if cache_line[9] == "I":
                            cache_line[9] = "E"
                        elif cache_line[9] == "S":
                            cache_line[9] == "S"
                        elif cache_line[9] == "E":
                            cache_line[9] == "E"
                        elif cache_line[9] == "M":
                            cache_line[9] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[9]))
                        break

                    if trace_line[1] == cache_line[12]:
                        if cache_line[11] == "I":
                            cache_line[11] = "E"
                        elif cache_line[11] == "S":
                            cache_line[11] == "S"
                        elif cache_line[11] == "E":
                            cache_line[11] == "E"
                        elif cache_line[11] == "M":
                            cache_line[11] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[11]))
                        break

                    if trace_line[1] == cache_line[14]:
                        if cache_line[13] == "I":
                            cache_line[13] = "E"
                        elif cache_line[13] == "S":
                            cache_line[13] == "S"
                        elif cache_line[13] == "E":
                            cache_line[13] == "E"
                        elif cache_line[13] == "M":
                            cache_line[13] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[13]))
                        break

                    if trace_line[1] == cache_line[16]:
                        if cache_line[15] == "I":
                            cache_line[15] = "E"
                        elif cache_line[15] == "S":
                            cache_line[15] == "S"
                        elif cache_line[15] == "E":
                            cache_line[15] == "E"
                        elif cache_line[15] == "M":
                            cache_line[15] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[15]))
                        break

            if trace_line[0] == 1:
                    if trace_line[1] == cache_line[2]:
                        if cache_line[1] == "I":
                            cache_line[1] = "E"
                        elif cache_line[1] == "S":
                            cache_line[1] == "S"
                        elif cache_line[1] == "E":
                            cache_line[1] == "E"
                        elif cache_line[1] == "M":
                            cache_line[1] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[1]))
                        break

                    if trace_line[1] == cache_line[4]:
                        if cache_line[3] == "I":
                            cache_line[3] = "E"
                        elif cache_line[3] == "S":
                            cache_line[3] == "S"
                        elif cache_line[3] == "E":
                            cache_line[3] == "E"
                        elif cache_line[3] == "M":
                            cache_line[3] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[3]))
                        break

                    if trace_line[1] == cache_line[6]:
                        if cache_line[5] == "I":
                            cache_line[5] = "E"
                        elif cache_line[5] == "S":
                            cache_line[5] == "S"
                        elif cache_line[5] == "E":
                            cache_line[5] == "E"
                        elif cache_line[5] == "M":
                            cache_line[5] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[5]))
                        break

                    if trace_line[1] == cache_line[8]:
                        if cache_line[7] == "I":
                            cache_line[7] = "E"
                        elif cache_line[7] == "S":
                            cache_line[7] == "S"
                        elif cache_line[7] == "E":
                            cache_line[7] == "E"
                        elif cache_line[7] == "M":
                            cache_line[7] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[7]))
                        break

                    if trace_line[1] == cache_line[10]:
                        if cache_line[9] == "I":
                            cache_line[9] = "E"
                        elif cache_line[9] == "S":
                            cache_line[9] == "S"
                        elif cache_line[9] == "E":
                            cache_line[9] == "E"
                        elif cache_line[9] == "M":
                            cache_line[9] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[9]))
                        break

                    if trace_line[1] == cache_line[12]:
                        if cache_line[11] == "I":
                            cache_line[11] = "E"
                        elif cache_line[11] == "S":
                            cache_line[11] == "S"
                        elif cache_line[11] == "E":
                            cache_line[11] == "E"
                        elif cache_line[11] == "M":
                            cache_line[11] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[11]))
                        break

                    if trace_line[1] == cache_line[14]:
                        if cache_line[13] == "I":
                            cache_line[13] = "E"
                        elif cache_line[13] == "S":
                            cache_line[13] == "S"
                        elif cache_line[13] == "E":
                            cache_line[13] == "E"
                        elif cache_line[13] == "M":
                            cache_line[13] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[13]))
                        break

                    if trace_line[1] == cache_line[16]:
                        if cache_line[15] == "I":
                            cache_line[15] = "E"
                        elif cache_line[15] == "S":
                            cache_line[15] == "S"
                        elif cache_line[15] == "E":
                            cache_line[15] == "E"
                        elif cache_line[15] == "M":
                            cache_line[15] == "M"
                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[15]))
                        break


if arg == "N":
    print(Cache_structure[609])

