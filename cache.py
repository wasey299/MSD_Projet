#---Libarary imports----------------------------------------------------------------------------------------------------
import sys
import math

#---Info of the cache---------------------------------------------------------------------------------------------------
Address_size = 32
Memory_size = (2**20)*2**4
Cache_line_size = 2**6
Ways = 8
Cache_lines = Memory_size/Cache_line_size
Sets = Cache_lines/Ways
Offset_bits = int(math.log2(Cache_line_size))
Index_bits = int(math.log2(Sets))
Tag_bits = int(Address_size - (Offset_bits + Index_bits))

#---Arguments-----------------------------------------------------------------------------------------------------------
fileinput = sys.argv[1]
arg = sys.argv[2]

#---Initialization of the list variables--------------------------------------------------------------------------------
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

#---Instantiating of some count variables-------------------------------------------------------------------------------
Index_count: int = 0
Miss_count: int = 0
Hit_count: int = 0
Index_referenced_count: int = 0
Index_not_referenced_count: int = 0
debug1: int = 0

#---Reading Trace File--------------------------------------------------------------------------------------------------
with open(fileinput, 'r') as f:
    Trace_line_string = f.read() # Here 'linetrace' represents every line of the trace file
    Trace_line_list = Trace_line_string.rstrip().split('\n') # Removes the whitespace from strings and converts them to list

#---Storing the trace file inside a list--------------------------------------------------------------------------------
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
    Trace_line_list_2d_hex.append({"Command":n_bit, "Tag": Tag_hex, "Index":Index_hex, "Byte Offset": Offset_hex})
if arg == "N":
    print("///////////Trace File Seperated//////////")
    for i in range(len(Trace_line_list_2d_hex)):
        print(Trace_line_list_2d_hex[i])
    print("////////Trace File has %d lines//////////"%(i+1))

#---MESI State Class----------------------------------------------------------------------------------------------------
def MESI(Command, State):
    if Command == 0 or 2:
        if State == "M":
            return "M"
        elif State == "E":
            return "E"
        elif State == "S":
            return "S"
        elif State == "I":
            return "E"

    if Command == 1:
        if State == "M":
            return "M"
        elif State == "E":
            return "M"
        elif State == "S":
            return "M"
        elif State == "I":
            return "M"

#---Snooping class------------------------------------------------------------------------------------------------------
def Snooping(Command, State, Index, Tag, way, Address):
    trc: str

    trace_line1 = bin(int(Address[1], 10))[2:].zfill(11)
    trace_line2 = bin(int(Address[2], 10))[2:].zfill(15)
    trace_line3 = bin(int(Address[3], 10))[2:].zfill(6)
    trace_line3_2 = int(trace_line3[4:], 2)

    if trace_line3_2 == 0:
        trc == "HIT"
    if trace_line3_2 == 1:
        trc == "HITM"
    if trace_line3_2 == 2 or 3:
        trc == "NOHIT"
    trace_line_main = str(trace_line1) + str(trace_line2) + str("000000")


    if Command == 4:
        if State == "M":
            print("===================SNOOP RESULT===================")
            print("HITM at Set: %h, Tag: %h, and Way: %s" % (hex(Index), hex(Tag), way))
            print("GETLINE: %s" % (str(hex(Index)))+way)
            print("WRITE %s, %s" %(trace_line_main+trc))
            print("Message to L2 cache")
            print("INVALIDATE Set: %h and Way: %s"%(hex(Index), way))
            return "S"

        elif State == "E":
            print("===================SNOOP RESULT===================")
            print("HIT at Set: %d, Tag: %h, and Way: %s" % (Index, hex(Tag), way))
            return "S"

        elif State == "S":
            print("===================SNOOP RESULT===================")
            print("HIT at Set: %d, Tag: %h, and Way: %s" % (Index, hex(Tag), way))
            return "S"

    elif Command == 3:
        if State == "S":
            print("===================SNOOP RESULT===================")
            print("INVALIDATE Set: %h and Way: %s"%(hex(Index), way))
            print("HIT at Set: %d, Tag: %h, and Way: %s" % (Index, hex(Tag), way))
            return "I"

    elif Command == 6:
        if State == "M":
            print("===================SNOOP RESULT===================")
            print("INVALIDATE Set: %h and Way: %s"%(hex(Index), way))
            print("INVALIDATE Set: %h and Way: %s" % (hex(Index), way))
            print("WRITE %s, %s" % (trace_line_main + trc))
            return "I"
        elif State == "E":
            print("===================SNOOP RESULT===================")
            print("INVALIDATE Set: %h and Way: %s"%(hex(Index), way))
            return "I"
        if State == "S":
            print("===================SNOOP RESULT===================")
            print("INVALIDATE Set: %h and Way: %s"%(hex(Index), way))
            pass

#---Compliment Class----------------------------------------------------------------------------------------------------
def Compliment(bit):
    if bit == 0:
        return 1
    elif bit == 1:
        return 0

#---Cache Structure-----------------------------------------------------------------------------------------------------
for index_count in range(int(Sets)):
    Cache_structure.append([index_count, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, 0, 0, 0, 0, 0, 0, 0])
#                                                                                                         L1   L2   L3   L4   L5   L6   L7
#                                 0       1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21   22    23
#                                         way1    way2    way3    way4    way5     way6    way7    way8

#if arg == "N":
#    for i in Cache_structure:
#        print(i)


#---Operations----------------------------------------------------------------------------------------------------------
for trace_line in Trace_line_list_2d:
    for cache_line in Cache_structure:
    #    debug1 = debug1 + 1

    #---Finding the index-----------------------------------------------------------------------------------------------
         #---Checing Index match------------------------------------------------------------------------
        if cache_line[0] == trace_line[2]:
            Index_referenced_count = Index_referenced_count + 1
            #---Checking whether the line is in Valid state for the way-----------------------------------------------------------------------
            if cache_line[1] != "I":
                if cache_line[2] == trace_line[1]:
                    Hit_count = Hit_count + 1
                    #---Updating MESI State on hit------------------------------------------------------------------
                    cache_line[1] = MESI(trace_line[0], cache_line[1])
                    #---Bus Snoop-----------------------------------------------------------------------------------
                    Snooping(trace_line[0], cache_line[1], cache_line[0], trace_line[1], "Way1", Address)
                    #---Updating PLRU bits--------------------------------------------------------------------------
                    cache_line[17] = 0
                    cache_line[18] = 0
                    cache_line[20] = 0
                    break
            elif cache_line[3] != "I":                
                if cache_line[4] == trace_line[1]:
                    Hit_count = Hit_count + 1
                    #---Updating MESI State on hit------------------------------------------------------------------
                    cache_line[3] = MESI(trace_line[0], cache_line[3])
                    #---Updating PLRU bits--------------------------------------------------------------------------
                    cache_line[17] = 0
                    cache_line[18] = 0
                    cache_line[20] = 1
                    break
            elif cache_line[5] != "I":                
                if cache_line[6] == trace_line[1]:
                    Hit_count = Hit_count + 1
                    #---Updating MESI State on hit------------------------------------------------------------------
                    cache_line[5] = MESI(trace_line[0], cache_line[5])
                    #---Updating PLRU bits--------------------------------------------------------------------------
                    cache_line[17] = 0
                    cache_line[18] = 1
                    cache_line[21] = 0
                    break
            elif cache_line[7] != "I":                
                if cache_line[8] == trace_line[1]:
                    Hit_count = Hit_count + 1
                    #---Updating MESI State on hit------------------------------------------------------------------
                    cache_line[7] = MESI(trace_line[0], cache_line[7])
                    #---Updating PLRU bits--------------------------------------------------------------------------
                    cache_line[17] = 0
                    cache_line[18] = 1
                    cache_line[21] = 1
                    break
            elif cache_line[9] != "I":                                
                if cache_line[10] == trace_line[1]:
                    Hit_count = Hit_count + 1
                    #---Updating MESI State on hit------------------------------------------------------------------
                    cache_line[9] = MESI(trace_line[0], cache_line[9])
                    #---Updating PLRU bits--------------------------------------------------------------------------
                    cache_line[17] = 1
                    cache_line[19] = 0
                    cache_line[22] = 0
                    break
            elif cache_line[11] != "I":                
                if cache_line[12] == trace_line[1]:
                    Hit_count = Hit_count + 1
                    #---Updating MESI State on hit------------------------------------------------------------------
                    cache_line[11] = MESI(trace_line[0], cache_line[11])
                    #---Updating PLRU bits--------------------------------------------------------------------------
                    cache_line[17] = 1
                    cache_line[19] = 0
                    cache_line[22] = 1
                    break
            elif cache_line[13] != "I":                                
                if cache_line[14] == trace_line[1]:
                    Hit_count = Hit_count + 1
                    #---Updating MESI State on hit------------------------------------------------------------------
                    cache_line[13] = MESI(trace_line[0], cache_line[13])
                    #---Updating PLRU bits--------------------------------------------------------------------------
                    cache_line[17] = 1
                    cache_line[18] = 1
                    cache_line[23] = 0
                    break
            elif cache_line[15] != "I":                                
                if cache_line[16] == trace_line[1]:
                    Hit_count = Hit_count + 1
                    #---Updating MESI State on hit------------------------------------------------------------------
                    cache_line[15] = MESI(trace_line[0], cache_line[15])
                    #---Updating PLRU bits--------------------------------------------------------------------------
                    cache_line[17] = 1
                    cache_line[18] = 1
                    cache_line[23] = 1
                    break
            else:
                Miss_count = Miss_count + 1
                if cache_line[17] and cache_line[18] and cache_line[19] and cache_line[20] and cache_line[21] and cache_line[22] and cache_line[23] == 0:
                    cache_line[2] = trace_line[1]
                    break
                elif cache_line[17] == 0:
                    cache_line[17] = 1
                    if cache_line[19] == 0:
                        cache_line[19] = 1
                        if cache_line[23] == 0:
                            cache_line[23] = 1
                            cache_line[16] = trace_line[1]
                            cache_line[15] = MESI(trace_line[0], cache_line[15])
                            break
                        elif cache_line[23] == 1:
                            cache_line[23] = 0
                            cache_line[14] = trace_line[1]
                            cache_line[13] = MESI(trace_line[0], cache_line[13])
                            break
                    elif cache_line[19] == 1:
                        cache_line[19] = 0
                        if cache_line[22] == 0:
                            cache_line[22] = 1
                            cache_line[12] = trace_line[1]
                            cache_line[11] = MESI(trace_line[0], cache_line[11])
                            break
                        elif cache_line[22] == 1:
                            cache_line[22] = 0
                            cache_line[10] = trace_line[1]
                            cache_line[9] = MESI(trace_line[0], cache_line[9])
                            break
                                    
                elif cache_line[17] == 1:
                    cache_line[17] = 0
                    if cache_line[18] == 0:
                        cache_line[18] = 1
                        if cache_line[21] == 0:
                            cache_line[21] =1
                            cache_line[8] = trace_line[1]
                            cache_line[7] = MESI(trace_line[0], cache_line[7])
                            break
                        elif cache_line[21] == 1:
                            cache_line[21] = 0
                            cache_line[6] = trace_line[1]
                            cache_line[5] = MESI(trace_line[0], cache_line[5])
                            break
                    elif cache_line[18] == 1:
                        cache_line[18] = 0
                        if cache_line[20] == 0:
                            cache_line[20] = 1
                            cache_line[4] = trace_line[1]
                            cache_line[3] = MESI(trace_line[0], cache_line[3])
                            break
                        elif cache_line[20] == 1:
                            cache_line[20] = 0
                            cache_line[2] = trace_line[1]
                            cache_line[1] = MESI(trace_line[0], cache_line[1])
                            break

        else:
            Index_not_referenced_count = Index_not_referenced_count + 1
            continue
            

if arg == "D":
    print(Index_referenced_count)
    print(Index_not_referenced_count)
    print(debug1)
    print(Cache_structure[2])
    print(Cache_structure[4])
    print(Cache_structure[6])
    print(Cache_structure[31])
    print(Cache_structure[2])

    
if arg == "S":
    print(Hit_count)
    print(Miss_count)
