def Compliment(bit):
    if bit == 0:
        return 1
    elif bit == 1:
        return 0

cache_line = ["index_count", "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "I", 0, "x", "x", "x", "x", "x", "x", "x"]
#                                                                                             L1   L2   L3   L4   L5   L6   L7
#                   0         1    2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21   22    23
#                            way1    way2    way3    way4    way5     way6    way7    way8


#---way 1 referenced--------------------------------------------------------------------------------
cache_line[2] = 1
# ---Updating PLRU bits--------------------------------------------------------------------------
cache_line[17] = 0
cache_line[18] = 0
cache_line[20] = 0
print([cache_line])

#---way 2 referenced--------------------------------------------------------------------------------
cache_line[4] = 1
# ---Updating PLRU bits--------------------------------------------------------------------------
cache_line[17] = 0
cache_line[18] = 0
cache_line[20] = 1
print([cache_line])

#---way 3 referenced--------------------------------------------------------------------------------
cache_line[6] = 1
# ---Updating PLRU bits--------------------------------------------------------------------------
cache_line[17] = 0
cache_line[18] = 1
cache_line[21] = 0
print([cache_line])

#---way 4 referenced--------------------------------------------------------------------------------
cache_line[8] = 1
# ---Updating PLRU bits--------------------------------------------------------------------------
cache_line[17] = 0
cache_line[18] = 1
cache_line[21] = 1
print([cache_line])

#---way 5 referenced--------------------------------------------------------------------------------
cache_line[10] = 1
# ---Updating PLRU bits--------------------------------------------------------------------------
cache_line[17] = 1
cache_line[19] = 0
cache_line[22] = 0
print([cache_line])

#---way 6 referenced--------------------------------------------------------------------------------
cache_line[12] = 1
# ---Updating PLRU bits--------------------------------------------------------------------------
cache_line[17] = 1
cache_line[19] = 0
cache_line[22] = 1
print([cache_line])

#---way 7 referenced--------------------------------------------------------------------------------
cache_line[14] = 1
# ---Updating PLRU bits--------------------------------------------------------------------------
cache_line[17] = 1
cache_line[18] = 1
cache_line[23] = 0
print([cache_line])

#---way 8 referenced--------------------------------------------------------------------------------
cache_line[16] = 1
# ---Updating PLRU bits--------------------------------------------------------------------------
cache_line[17] = 1
cache_line[18] = 1
cache_line[23] = 1
print([cache_line])

# ---Eviction Using PLRU policy------------------------------------------------------------------
# ---Complimenting PLRU Bits---------------------------------------------------------------------
cache_line[17] = Compliment(cache_line[17])
cache_line[18] = Compliment(cache_line[18])
cache_line[19] = Compliment(cache_line[19])
cache_line[20] = Compliment(cache_line[20])
cache_line[21] = Compliment(cache_line[21])
cache_line[22] = Compliment(cache_line[22])
cache_line[23] = Compliment(cache_line[23])

# ---Eviction to add 2 by the means of the PLRU branch------------------------------------------------------------------------------------
if cache_line[17] == 0:
    if cache_line[18] == 0:
        if cache_line[20] == 0:
            cache_line[2] = 2
        elif cache_line[20] == 1:
            cache_line[4] = 2
    elif cache_line[18] == 1:
        if cache_line[21] == 0:
            cache_line[6] = 2
        elif cache_line[21] == 1:
            cache_line[8] = 2

elif cache_line[17] == 1:
    if cache_line[19] == 0:
        if cache_line[22] == 0:
            cache_line[10] = 2
        if cache_line[22] == 1:
            cache_line[12] = 2
    elif cache_line[19] == 1:
        if cache_line[23] == 0:
            cache_line[14] = 2
        elif cache_line[23] == 1:
            cache_line[16] == 2


print([cache_line])

