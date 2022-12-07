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
#Instantiating of some count variables
Index_count:int = 0
Miss_count: int = 0
Hit_count: int = 0

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
        if trace_line[2] == cache_line[0]: # Pointing towards the pointed set.

# ------------------- Command 0--------------------------------------------------------------------------------
            if trace_line[0] == 0:

      # ------------------- Checking whether the Tag Hit in the way1.--------------------------------------------------------------------------------
                if trace_line[1] == cache_line[2]:

         # ----------------------Check the state-------------------------------------------------------------------------------
                     if cache_line[1] != "I":
                         Hit_count = Hit_count + 1

                #------------------- Updating MESI State on Hit--------------------------------------------------------------------------------
                        if cache_line[1] == "I":
                            cache_line[1] = "E"
                        elif cache_line[1] == "S":
                            cache_line[1] == "S"
                        elif cache_line[1] == "E":
                            cache_line[1] == "E"
                        elif cache_line[1] == "M":
                            cache_line[1] == "M"

                #---------- Updating PLRU Bits--------------------------------------------------------------------------
                        cache_line[17] = 0
                        cache_line[18] = 0
                        cache_line[20] = 0

                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[1]))
                            print("PLRU = %d%d%d%d%d%d%d" %(cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))

                        break

      # ------------------- Checking whether the Tag Hit in the way2.--------------------------------------------------------------------------------
                    elif trace_line[1] == cache_line[4]:

# ----------------------Check the state-------------------------------------------------------------------------------
                      if cache_line[3] != "I":
                        Hit_count = Hit_count + 1

    # ------------------- Updating MESI State on Hit--------------------------------------------------------------------------------
                        if cache_line[3] == "I":
                            cache_line[3] = "E"
                        elif cache_line[3] == "S":
                            cache_line[3] == "S"
                        elif cache_line[3] == "E":
                            cache_line[3] == "E"
                        elif cache_line[3] == "M":
                            cache_line[3] == "M"

    # ---------- Updating PLRU Bits--------------------------------------------------------------------------
                        cache_line[17] = 0
                        cache_line[18] = 0
                        cache_line[20] = 1

                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[3]))
                            print("PLRU = %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))

                        break

      # ------------------- Checking whether the Tag Hit in the way3.--------------------------------------------------------------------------------
                    elif trace_line[1] == cache_line[6]:

        # ----------------------Check the state-------------------------------------------------------------------------------
                      if cache_line[5] != "I":
                        Hit_count = Hit_count + 1

# ------------------- Updating MESI State on Hit--------------------------------------------------------------------------------
                        if cache_line[5] == "I":
                            cache_line[5] = "E"
                        elif cache_line[5] == "S":
                            cache_line[5] == "S"
                        elif cache_line[5] == "E":
                            cache_line[5] == "E"
                        elif cache_line[5] == "M":
                            cache_line[5] == "M"

    # ---------- Updating PLRU Bits--------------------------------------------------------------------------
                        cache_line[17] = 0
                        cache_line[18] = 1
                        cache_line[21] = 0

                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[5]))
                            print("PLRU = %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))

                        break
    #---------------------- Checking whether the Tag Hit in the way4.--------------------------------------------------------------------------------
                    elif trace_line[1] == cache_line[8]:

     # ----------------------Check the state-------------------------------------------------------------------------------
                      if cache_line[7] != "I":
                        Hit_count = Hit_count + 1

#------------------- Updating MESI state.--------------------------------------------------------------------------------
                        if cache_line[7] == "I":
                            cache_line[7] = "E"
                        elif cache_line[7] == "S":
                            cache_line[7] == "S"
                        elif cache_line[7] == "E":
                            cache_line[7] == "E"
                        elif cache_line[7] == "M":
                            cache_line[7] == "M"

            #--------------Updating PLRU Bits------------------------------------------------------------------
                        cache_line[17] = 0
                        cache_line[18] = 1
                        cache_line[21] = 1


                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[7]))
                            print("PLRU = %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))

                        break


    #-------------------Checking Tag hit in the way5------------------------------------------------------------------------------
                    elif trace_line[1] == cache_line[10]:
        # ----------------------Check the state-------------------------------------------------------------------------------
                      if cache_line[9] != "I":
                        Hit_count = Hit_count + 1

#------------------Updating MESI State-----------------------------------------------------------------------------
                        if cache_line[9] == "I":
                            cache_line[9] = "E"
                        elif cache_line[9] == "S":
                            cache_line[9] == "S"
                        elif cache_line[9] == "E":
                            cache_line[9] == "E"
                        elif cache_line[9] == "M":
                            cache_line[9] == "M"

         #-------------------Updating PLRU bits--------------------------------------------------------------------------
                        cache_line[17] = 1
                        cache_line[19] = 0
                        cache_line[22] = 0


                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[9]))
                            print("PLRU = %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))

                        break

    #-------------Checking Tag hit in way6-------------------------------------------------------------------------------
                    elif trace_line[1] == cache_line[12]:
                      Hit_count = Hit_count + 1


# ----------------------Check the state-------------------------------------------------------------------------------
                      if cache_line[11] != "I":

        #--------------------Updating MESI state-----------------------------------------------------------------------
                        if cache_line[11] == "I":
                            cache_line[11] = "E"
                        elif cache_line[11] == "S":
                            cache_line[11] == "S"
                        elif cache_line[11] == "E":
                            cache_line[11] == "E"
                        elif cache_line[11] == "M":
                            cache_line[11] == "M"

            #-------------------Updating PLRU-----------------------------------------------------------------------------
                        cache_line[17] = 1
                        cache_line[19] = 0
                        cache_line[22] = 1

                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[11]))
                            print("PLRU = %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))

                        break

    #-----------------------Checking tag hit in the way7-----------------------------------------------------
                    elif trace_line[1] == cache_line[14]:

      # ----------------------Check the state-------------------------------------------------------------------------------
                      if cache_line[13] != "I":
                        Hit_count = Hit_count + 1


#---------------------------Updating MESI State-------------------------------------------------------------
                        if cache_line[13] == "I":
                            cache_line[13] = "E"
                        elif cache_line[13] == "S":
                            cache_line[13] == "S"
                        elif cache_line[13] == "E":
                            cache_line[13] == "E"
                        elif cache_line[13] == "M":
                            cache_line[13] == "M"

        #----------------Updating PLRU Bit---------------------------------------------------------------------------------------
                        cache_line[17] = 1
                        cache_line[19] = 1
                        cache_line[23] = 0


                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[13]))
                            print("PLRU = %d%d%d%d%d%d%d" % (cache_line[17], cache_line[18], cache_line[19], cache_line[20], cache_line[21], cache_line[22], cache_line[23]))

                        break

    #---------------------Checking Tag hit in the way8-----------------------------------------------------
                    elif trace_line[1] == cache_line[16]:
                      Hit_count = Hit_count + 1


# ----------------------Check the state-------------------------------------------------------------------------------
                      if cache_line[15] != "I":

        #----------------------Updating MESI State-------------------------------------------------------------------------
                        if cache_line[15] == "I":
                            cache_line[15] = "E"
                        elif cache_line[15] == "S":
                            cache_line[15] == "S"
                        elif cache_line[15] == "E":
                            cache_line[15] == "E"
                        elif cache_line[15] == "M":
                            cache_line[15] == "M"

            #--------------------Updating PLRU bits---------------------------------------------------------------------------
                        cache_line[17] = 1
                        cache_line[19] = 1
                        cache_line[23] = 1

                        if arg == "N":
                            print("Hit: Index = %d | Tag = %d | MESI State = %s" %(trace_line[2], trace_line[1], cache_line[15]))

                        break
    #------------Tag   Miss because every way is in INVALID state-----------------------------------------------------------------------------------------------
                      elif cache_line[15] == "I":
                          Miss_count = Miss_count + 1

                          #Cache Miss
        #---------Eviction of a line in this Index based on the PLRU replacement policy------------------------------------------------

            #-----Complimenting all the PLRU bits-----------------------------------------------------------------------------------------
                        if cache_line[17] == 0:
                            cache_line[17] = 1
                        elif cache_line[17] == 1:
                            cache_line[17] = 0

                        if cache_line[18] == 0:
                            cache_line[18] = 1
                        elif cache_line[18] == 1:
                            cache_line[18] = 0

                        if cache_line[19] == 0:
                            cache_line[19] = 1
                        elif cache_line[19] == 1:
                            cache_line[19] = 0

                        if cache_line[20] == 0:
                            cache_line[20] = 1
                        elif cache_line[20] == 1:
                            cache_line[20] = 0

                        if cache_line[21] == 0:
                            cache_line[21] = 1
                        elif cache_line[21] == 1:
                            cache_line[21] = 0

                        if cache_line[22] == 0:
                            cache_line[22] = 1
                        elif cache_line[22] == 1:
                            cache_line[22] = 0

                        if cache_line[23] == 0:
                            cache_line[23] = 1
                        elif cache_line[23] == 1:
                            cache_line[23] = 0

            #------Bracnch of PLRU bits replacing the PLRU way with the Address --------------------------------------------------------------------------------------------------
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



      #------------Cahe Miss because failed to find any equal tag----------------------------------------------------
                    elif trace_line[1] != cache_line[16]:
                        Miss_count = Miss_count + 1


#---------Eviction of a line in this Index based on the PLRU replacement policy------------------------------------------------

            #-----Complimenting all the PLRU bits-----------------------------------------------------------------------------------------
                        if cache_line[17] == 0:
                            cache_line[17] = 1
                        elif cache_line[17] == 1:
                            cache_line[17] = 0

                        if cache_line[18] == 0:
                            cache_line[18] = 1
                        elif cache_line[18] == 1:
                            cache_line[18] = 0

                        if cache_line[19] == 0:
                            cache_line[19] = 1
                        elif cache_line[19] == 1:
                            cache_line[19] = 0

                        if cache_line[20] == 0:
                            cache_line[20] = 1
                        elif cache_line[20] == 1:
                            cache_line[20] = 0

                        if cache_line[21] == 0:
                            cache_line[21] = 1
                        elif cache_line[21] == 1:
                            cache_line[21] = 0

                        if cache_line[22] == 0:
                            cache_line[22] = 1
                        elif cache_line[22] == 1:
                            cache_line[22] = 0

                        if cache_line[23] == 0:
                            cache_line[23] = 1
                        elif cache_line[23] == 1:
                            cache_line[23] = 0

            #------Bracnch of PLRU bits replacing the the PLRU way with the Address --------------------------------------------------------------------------------------------------
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







# Calculation of Hit ratio and miss ratio--------------------
Miss_count_ratio: float = Miss_count/(Hit_count + Miss_count)
Hit_count_ratio: float = Hit_count/(Hit_count + Miss_count)
