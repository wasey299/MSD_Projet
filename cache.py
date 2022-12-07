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
    if Command == 0:
        if State == "M":
            return "M"
        if State == "E":
            return "E"
        if State == "S":
            return "S"
        if State == "I":
            return "E"

#---Compliment Class----------------------------------------------------------------------------------------------------
def Compliment(bit):
    if bit == 0:
        return 1
    elif bit == 1:
        return 0

#---Cache Structure-----------------------------------------------------------------------------------------------------
for index_count in range(int(Sets)):
    Cache_structure.append([index_count, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "x", "x", "x", "x", "x", "x", "x"])
#                                                                                                         L1   L2   L3   L4   L5   L6   L7
#                                 0       1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21   22    23
#                                         way1    way2    way3    way4    way5     way6    way7    way8

#---Operations----------------------------------------------------------------------------------------------------------
for trace_line in Trace_line_list_2d:
    for cache_line in Cache_structure:
    #---Finding the index-----------------------------------------------------------------------------------------------
            #---Command 0-----------------------------------------------------------------------------------------------
                #---Checking the Tag hit in way1------------------------------------------------------------------------
                if trace_line[2] == cache_line[0] and trace_line[1] == cache_line[2] and trace_line[0] == 0:
                    #---Checking if the line is in a Valid State--------------------------------------------------------
                    if cache_line[1] != "I":
                        Hit_count = Hit_count + 1
                        #---Updating MESI State on hit------------------------------------------------------------------
                        cache_line[1] = MESI(trace_line[0], cache_line[1])
                        #---Updating PLRU bits--------------------------------------------------------------------------
                        cache_line[17] = 0
                        cache_line[18] = 0
                        cache_line[20] = 0
                        #---Print if Normal Mode------------------------------------------------------------------------
                        if arg == "N":
                            print("/////////////////////////////////////////////////////////////////////////////")
                            print("Tag: %h Hit at %h index and way 1" %(hex(trace_line[1]), hex(cache_line[0])))
                            print("MESI State: %s" %(cache_line[1]))
                            print("LRU bits: %d%d%d%d%d%d%d" %(cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                            break
                        break
                    break

                # ---Checking the Tag hit in way2-----------------------------------------------------------------------
                elif trace_line[2] == cache_line[0] and trace_line[1] == cache_line[4] and trace_line[0] == 0:
                    # ---Checking if the line is in a Valid State-------------------------------------------------------
                    if cache_line[3] != "I":
                        #---Incrementing Hit Counter--------------------------------------------------------------------
                        Hit_count = Hit_count + 1
                        # ---Updating MESI State on hit-----------------------------------------------------------------
                        cache_line[3] = MESI(trace_line[0], cache_line[3])
                        # ---Updating PLRU bits-------------------------------------------------------------------------
                        cache_line[17] = 0
                        cache_line[18] = 0
                        cache_line[20] = 1
                        # ---Print if Normal Mode-----------------------------------------------------------------------
                        if arg == "N":
                            print("/////////////////////////////////////////////////////////////////////////////")
                            print("Tag: %h Hit at %h index and way 2" % (hex(trace_line[1]), hex(cache_line[0])))
                            print("MESI State: %s" % (cache_line[3]))
                            print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                            break
                        break
                    break

                # ---Checking the Tag hit in way3-----------------------------------------------------------------------
                elif trace_line[2] == cache_line[0] and trace_line[1] == cache_line[6] and trace_line[0] == 0:
                    # ---Checking if the line is in a Valid State-------------------------------------------------------
                    if cache_line[5] != "I":
                        #---Incrementing Hit Counter--------------------------------------------------------------------
                        Hit_count = Hit_count + 1
                        # ---Updating MESI State on hit-----------------------------------------------------------------
                        cache_line[5] = MESI(trace_line[0], cache_line[5])
                        # ---Updating PLRU bits-------------------------------------------------------------------------
                        cache_line[17] = 0
                        cache_line[18] = 1
                        cache_line[21] = 0
                        # ---Print if Normal Mode-----------------------------------------------------------------------
                        if arg == "N":
                            print("/////////////////////////////////////////////////////////////////////////////")
                            print("Tag: %h Hit at %h index and way 3" % (hex(trace_line[1]), hex(cache_line[0])))
                            print("MESI State: %s" % (cache_line[5]))
                            print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                            break
                        break
                    break

                # ---Checking the Tag hit in way4-----------------------------------------------------------------------
                elif trace_line[2] == cache_line[0] and trace_line[1] == cache_line[8] and trace_line[0] == 0:
                    # ---Checking if the line is in a Valid State-------------------------------------------------------
                    if cache_line[7] != "I":
                        #---Incrementing Hit Counter--------------------------------------------------------------------
                        Hit_count = Hit_count + 1
                        # ---Updating MESI State on hit-----------------------------------------------------------------
                        cache_line[7] = MESI(trace_line[0], cache_line[7])
                        # ---Updating PLRU bits-------------------------------------------------------------------------
                        cache_line[17] = 0
                        cache_line[18] = 1
                        cache_line[21] = 1
                        # ---Print if Normal Mode-----------------------------------------------------------------------
                        if arg == "N":
                            print("/////////////////////////////////////////////////////////////////////////////")
                            print("Tag: %h Hit at %h index and way 4" % (hex(trace_line[1]), hex(cache_line[0])))
                            print("MESI State: %s" % (cache_line[7]))
                            print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                            break
                        break
                    break

                # ---Checking the Tag hit in way5-----------------------------------------------------------------------
                elif trace_line[2] == cache_line[0] and trace_line[1] == cache_line[10] and trace_line[0] == 0:
                    # ---Checking if the line is in a Valid State-------------------------------------------------------
                    if cache_line[9] != "I":
                        #---Incrementing Hit Counter--------------------------------------------------------------------
                        Hit_count = Hit_count + 1
                        # ---Updating MESI State on hit-----------------------------------------------------------------
                        cache_line[9] = MESI(trace_line[0], cache_line[9])
                        # ---Updating PLRU bits-------------------------------------------------------------------------
                        cache_line[17] = 1
                        cache_line[19] = 0
                        cache_line[22] = 0
                        # ---Print if Normal Mode-----------------------------------------------------------------------
                        if arg == "N":
                            print("/////////////////////////////////////////////////////////////////////////////")
                            print("Tag: %h Hit at %h index and way 5" % (hex(trace_line[1]), hex(cache_line[0])))
                            print("MESI State: %s" % (cache_line[9]))
                            print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                            break
                        break
                    break

                # ---Checking the Tag hit in way6-----------------------------------------------------------------------
                elif trace_line[2] == cache_line[0] and trace_line[1] == cache_line[12] and trace_line[0] == 0:
                    # ---Checking if the line is in a Valid State-------------------------------------------------------
                    if cache_line[11] != "I":
                        #---Incrementing Hit Counter--------------------------------------------------------------------
                        Hit_count = Hit_count + 1
                        # ---Updating MESI State on hit-----------------------------------------------------------------
                        cache_line[11] = MESI(trace_line[0], cache_line[11])
                        # ---Updating PLRU bits-------------------------------------------------------------------------
                        cache_line[17] = 1
                        cache_line[19] = 0
                        cache_line[22] = 1
                        # ---Print if Normal Mode-----------------------------------------------------------------------
                        if arg == "N":
                            print("/////////////////////////////////////////////////////////////////////////////")
                            print("Tag: %h Hit at %h index and way 6" % (hex(trace_line[1]), hex(cache_line[0])))
                            print("MESI State: %s" % (cache_line[11]))
                            print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                            break
                        break
                    break

                # ---Checking the Tag hit in way7-----------------------------------------------------------------------
                elif trace_line[2] == cache_line[0] and trace_line[1] == cache_line[14] and trace_line[0] == 0:
                    # ---Checking if the line is in a Valid State-------------------------------------------------------
                    if cache_line[13] != "I":
                        #---Incrementing Hit Counter--------------------------------------------------------------------
                        Hit_count = Hit_count + 1
                        # ---Updating MESI State on hit-----------------------------------------------------------------
                        cache_line[13] = MESI(trace_line[0], cache_line[13])
                        # ---Updating PLRU bits-------------------------------------------------------------------------
                        cache_line[17] = 1
                        cache_line[19] = 1
                        cache_line[23] = 0
                        # ---Print if Normal Mode-----------------------------------------------------------------------
                        if arg == "N":
                            print("/////////////////////////////////////////////////////////////////////////////")
                            print("Tag: %h Hit at %h index and way 1" % (hex(trace_line[1]), hex(cache_line[0])))
                            print("MESI State: %s" % (cache_line[13]))
                            print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                            break
                        break
                    break

                # ---Checking the Tag hit in way8-----------------------------------------------------------------------
                elif trace_line[2] == cache_line[0] and trace_line[1] == cache_line[16] and trace_line[0] == 0:
                    # ---Checking if the line is in a Valid State-------------------------------------------------------
                    if cache_line[15] != "I":
                        #---Incrementing Hit Counter--------------------------------------------------------------------
                        Hit_count = Hit_count + 1
                        # ---Updating MESI State on hit-----------------------------------------------------------------
                        cache_line[15] = MESI(trace_line[0], cache_line[15])
                        # ---Updating PLRU bits-------------------------------------------------------------------------
                        cache_line[17] = 1
                        cache_line[19] = 1
                        cache_line[23] = 1
                        # ---Print if Normal Mode-----------------------------------------------------------------------
                        if arg == "N":
                            print("/////////////////////////////////////////////////////////////////////////////")
                            print("Tag: %h Hit at %h index and way 1" % (hex(trace_line[1]), hex(cache_line[0])))
                            print("MESI State: %s" % (cache_line[15]))
                            print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                            break
                        break


                    #---Tag miss because all the ways are invalid-------------------------------------------------------
                    elif cache_line[15] == "I":
                    #Incrementing miss counter--------------------------------------------------------------------------
                        Miss_count = Miss_count + 1
                        #---Eviction Using PLRU policy------------------------------------------------------------------
                        #---Complimenting PLRU Bits---------------------------------------------------------------------
                        cache_line[17] = Compliment(cache_line[17])
                        cache_line[18] = Compliment(cache_line[18])
                        cache_line[19] = Compliment(cache_line[19])
                        cache_line[20] = Compliment(cache_line[20])
                        cache_line[21] = Compliment(cache_line[21])
                        cache_line[22] = Compliment(cache_line[22])
                        cache_line[23] = Compliment(cache_line[23])
                        #---Eviction------------------------------------------------------------------------------------
                        if cache_line[17] == 0:
                            if cache_line[18] == 0:
                                if cache_line[20] == 0:
                                    cache_line[2] = trace_line[1]
                                elif cache_line[20] == 1:
                                    cache_line[4] = trace_line[1]
                            elif cache_line[18] == 1:
                                if cache_line[21] == 0:
                                    cache_line[6] = trace_line[1]
                                elif cache_line[21] == 1:
                                    cache_line[8] = trace_line[1]

                        elif cache_line[17] == 1:
                            if cache_line[19] == 0:
                                if cache_line[22] == 0:
                                    cache_line[10] = trace_line[1]
                                if cache_line[22] == 1:
                                    cache_line[12] = trace_line[1]
                            elif cache_line[19] == 1:
                                if cache_line[23] == 0:
                                    cache_line[14] = trace_line[1]
                                elif cache_line[23] == 1:
                                    cache_line[16] == trace_line[1]
                            #---Print Evicted Way if Normal Mode--------------------------------------------------------
                            if arg == "N":
                                print("/////////////////////////////////////////////////////////////////////////////")
                                print("EVICTION")
                                print("Tag: %h Index: %h" % (hex(trace_line[1]), hex(cache_line[0])))
                                print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                                break
                            break
                        break
                elif trace_line[2] == cache_line[0] and trace_line[1] == cache_line[16] and trace_line[0] != 0:
                    #Incrementing miss counter--------------------------------------------------------------------------
                        Miss_count = Miss_count + 1
                        #---Eviction Using PLRU policy------------------------------------------------------------------
                        #---Complimenting PLRU Bits---------------------------------------------------------------------
                        cache_line[17] = Compliment(cache_line[17])
                        cache_line[18] = Compliment(cache_line[18])
                        cache_line[19] = Compliment(cache_line[19])
                        cache_line[20] = Compliment(cache_line[20])
                        cache_line[21] = Compliment(cache_line[21])
                        cache_line[22] = Compliment(cache_line[22])
                        cache_line[23] = Compliment(cache_line[23])
                        #---Eviction------------------------------------------------------------------------------------
                        if cache_line[17] == 0:
                            if cache_line[18] == 0:
                                if cache_line[20] == 0:
                                    cache_line[2] = trace_line[1]
                                elif cache_line[20] == 1:
                                    cache_line[4] = trace_line[1]
                            elif cache_line[18] == 1:
                                if cache_line[21] == 0:
                                    cache_line[6] = trace_line[1]
                                elif cache_line[21] == 1:
                                    cache_line[8] = trace_line[1]

                        elif cache_line[17] == 1:
                            if cache_line[19] == 0:
                                if cache_line[22] == 0:
                                    cache_line[10] = trace_line[1]
                                if cache_line[22] == 1:
                                    cache_line[12] = trace_line[1]
                            elif cache_line[19] == 1:
                                if cache_line[23] == 0:
                                    cache_line[14] = trace_line[1]
                                elif cache_line[23] == 1:
                                    cache_line[16] == trace_line[1]
                            #---Print Evicted Way if Normal Mode--------------------------------------------------------
                            if arg == "N":
                                print("/////////////////////////////////////////////////////////////////////////////")
                                print("EVICTION")
                                print("Tag: %h Index: %h" % (hex(trace_line[1]), hex(cache_line[0])))
                                print("LRU bits: %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))
                                break
                            break
                        break












