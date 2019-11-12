#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################
# PROBLEM 3.                                                   #
# There are N books and two readers, A and B, wanting to       #
# read these books. Nonnegative integers A[I] and B[I] are     #
# given such as reader A (or B) needs A[I] (or B[I],           #
# respectively) hours to read book I, 1<=I<=N. Both the        #
# readers begin reading at time 0. At any time each reader     #
# is allowed to read at most one book and both readers         #
# cannot read the same book.                                   #
# Integer K, 2<=K<=N, is given and the books are supposed      #
# to be numbered in such a way that no reader can start        #
# reading book J, 2<=J<=K, until book J-1 is read by both      #
# the readers.                                                 #
# The order of reading the other books is immaterial for       #
# each reader and may be arbitrary.                            #
# Preemptions are allowed in the process of reading any        #
# book by any reader. It means that this process may be        #
# interrupted at any integer time and be resumed lately        #
# starting from the point of interruption. In between          #
# interruption and resumption of the process of reading the    #
# book a reader may read any other book he has not             #
# completed and has the right to read it.                      #
# IT IS NECESSARY:                                             # 
# 1. To organize inputting the data in the form:               #
# < ENTER N --> >                                              #
# < ENTER K --> >                                              #
# < ENTER: >                                                   #
# < A[1] --> > < B[1] --> >                                    #
# < A[2] --> > < B[2] --> >                                    #
# ..........................                                   #
# < A[N] --> > < B[N] --> >                                    #
# 2. To find the largest possible time T before which all      #
# the books cannot be read by both the readers; to output      # 
# calculated value of T.                                       #
# 3. To build a schedule of reading the books by each          #
# reader which meets all the restrictions listed above and     #
# under which the process of reading all the books             #
# terminates at time T. The schedule for each reader is to     #
# be written in the form.                                      #
# < SCHEDULE FOR READER A ( or B ) >                           #
# < Book > < Start > < Finish >                                #
#   .....    .....     .....                                   #
#   .....    .....     .....                                   #
# In the tables of the above form all the time intervals       # 
# within which reader A (or B) is reading a book and the       #
# number of this book should be mentioned.                     #
# 4. Output the number of preemptions of each reader. Try      #
# to reduce the number of preemptions for each reader.         #
################################################################
# I've decided this time to write the program as a script, ____#
# so more or less everything is just a global stuff.        |1 #
#######################^#######################################^
k = 2                  #                                       #
a, b = 0, 1            #########################################
reader = ([4,5,4,6,9,7,5],                                          
          [3,2,3,7,5,8,7])                                          
pas = 0                #########################################
verbose = True         #`#####################################\#
###############################^###############################^
lock = [r[:k] for r in reader] # split books to locked: < k,   #
free = [r[k:] for r in reader] # and free: >= k per reader     #
def baz(): #########^^#########=###############################=
    baz.s = '#'* 64 ##                                         #
    print(baz.s)    ##                                         #
####################==##############^##########################^
if verbose:                         #                          #
    baz() ##########################+###########################
    print("reader[a] =", reader[a]) #                          #
    print("reader[b] =", reader[b]) #                          #
    baz() ######################^###=##########################^
    print("lock[a] =", lock[a]) #                              #
    print("lock[b] =", lock[b]) #                              #
    print("free[a] =", free[a]) #                              # 
    print("free[b] =", free[b]) #                              #
################################=##############################=
# We can think of a reading time as a seq of book numbers per  #  
# hour, for example [3, 2, 1] can be represented as:        ___#
# 1, 1, 1, 2, 2, 3. Let's call this process expanding.       |2# 
################################################################
#   e}   x:   p|   a~   n!   d/    _   l!   o,   c<   k#   e:
#   d,    .   b~   o*   o.   k@   s)    +   b$   y?    _   i:
#   n#   s(   e%   r<   t-   i$   n)   g>    _   e:   x,   p`
#   a:   n'   d`   e^   d,    _   p*   a:   s!   s!   e:   s!
#   f;   o.   r"    _   t*   h;   e@    ,   o:   p:   p_   o~
#   s,   i`   t:   e!    =   r+   e,   a^   d;   e_   r!
def expand_lock(): #############################################
    """#########################################################
    example: lock = [[2, 3], [3, 4]]
    expand_lock() -> [[1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0, 0, 0, 2, 2, 2, 2]]
    """#################################^#######################
    ls = [[], []]                       # At  the position of ze
    locksiz = k                         # pases  (zeroes),  free
    for j in range(locksiz):            # book  numbers  can  be 
        ls[a].extend([j+1]* lock[a][j]) # placed. If  the sum of
        ls[b].extend([pas]* lock[a][j]) # free  reading  time is
        ls[a].extend([pas]* lock[b][j]) # <=  number  of  zeroes
        ls[b].extend([j+1]* lock[b][j]) #____ for   one  of  the
    return ls                           # 3| readers we are don!              
################################################################
#   k!   e,   e'   p:    ?   s!   e;   p.   a*   r!   a+   t:
#   e-    +   b(   o_   o_   k,   s+    ,   i=   n%    -   l~
#   i:   s<   t,   s&
def expand_free(): #############################################
    """#########################################################
    example: free = [[1, 4], [3, 2]], k = 2
    expand_free() -> [[3],[4,4,4,4]],
                     [[3,3,3],[4,4]]
    """#########################################################
    ls = [[], []]                              # We   keep  book
    for i in (a, b):                           # numbers  intact
        free1 = enumerate(free[i])             # cause   of  the
        ls[i] = [[k+j+1]* t for j, t in free1] #____ Reduction()
    return ls                                  # 4|
#################################^##########################^^^^
# Okay let's refer 1 hour reading time az a book, and let's take
# reader A who has sum(lock[B]) slots to fill with free books. #
# As mentioned if the number of free books is less than this ###
# number than we are don! I don't know how to call the differ- #
# ence sum(free[r]) - sum(lock[not r]), but this is the number #
# of remaining free books reader r has to read. So let's pick ##___
# some original name as remb (remaining books:)                  5
remb = [sum(free[r]) - sum(lock[not r]) for r in (a, b)]    #######
cross = min(remb)                #                          ####
# Now that is a lie... actually this is the overlap between ####
# readers A and B remaining free books and it's the essence of #
# the problem I guess, cause we have2 figure such arangements ##___
# of books so that at least in the crossection there are no #### 6
# book repetitions.              ############_#####################
free[:] = expand_free()          #   _ KAINE        .. WTF? ####
lock[:] = expand_lock()          #= 7  BEVIGLUNG!   4       #### 
##################################=#############################
if verbose:                      #=                         ####
    baz() ######################################################
    print("xp lock:", *lock, sep = '\n') #######################
    print("xp free:", *free, sep = '\n') #######################
    print("cross =", cross) ####################################
################################################################
def flat(ls): return [i for j in ls for i in j] # ha-ha        #
###f###z###e###q###g###3###x###g###3###g###z### ###q###4###3###3
#  f   i   l   l       p   a   s       s   l   o   t   s       w
#  i   t   h       d   a   t   a   _   _   _   _   _   _   _   _
def fill_lock(data): ################## ########################
    for r in (a, b): ###################### ####################
        for j in range(len(lock[r])): ######### ################ 
            if lock[r][j] is pas: ################# ############   
                if data[r]: lock[r][j] = data[r].pop()  ########               
############################################^############## ####
if cross <= 0:                              # Here we are! At <-
    free[a][:] = flat(free[a])              # point  one  of the
    free[b][:] = flat(free[b])              # reader  free  list
    fill_lock(free)                         # <- should be empty
    for r in (a, b):                        # Add  waiting  time
        siz = len(free[not r])              # and  append  it to
        free[r].extend([pas]* siz)          # ze lock list which
    for r in (a, b):                        # will represend the
        lock[r].extend(free[r])             # actual  shedule in
    print("shedule:", *lock, sep = '\n')    #____          hours.
    exit()                                  # 7|
################################################################
# Ok I have a picture here but let's try to give an example    #
# here as well. The general idea is to arrange free book such  #
# that there is a minimum repetitions at a given time, zen we  #
# can chop off cross of them and distribute the others at lock #
# pas positions defined earlier. Because we have repeating     #
# objects the best way seems to be to use permutations from a  #
# multiset but the algorithm seems complex to me, so here we   #
# use the available python permutations but first we reduce    #
# the number of variations by a process called Reduction():    # __ SILENCE
# free[a]: ???******@@@@--                                      8
# free[b]: ??****@@@---                                        ####
# 1). First we put b's head books at ze end:                   #
#     ****@@@---??                                             #
# 2). Zen add passess to the corespondingg smaller group       #
#     ???0******@@@@--                                         #
#     ****@@@000---0??                                         #
# 3). Split into two groups:                                   #
#     ???***@@@--      0***@                                   #
#     ***@@@---??, and *0000                                   #
# Second group is called crossbar = [[***@],[*]] zen we use    #
# permutations on zhat group to find maximum matches, that is  #
# minimum repetitions                                          #
################################################################
def Reduction():                   #                           #        
    free[b].append(free[b].pop(0)) # rotate first and last     #
    ############################################################
    for i in range(len(free[a])):              # add passes    #
        d = len(free[a][i]) - len(free[b][i])  #               #
        if d > 0: free[b][i].extend( d *[pas]) # Next:         #
        else:     free[a][i].extend(-d *[pas]) # cmnt, flat()  #
    ############################################################
    free[a][:] = flat(free[a]) #                               #
    free[b][:] = flat(free[b]) #                               #
    ############################################################
    goal = [[],[]]     #                                       #
    crossbar = [[],[]] #                                       # 
    ############################################################
    for j in range(len(free[a])):                      #       #
        for r in (a, b):                               #       #
            if free[r][j] == pas:                      #       #
                crossbar[not r].append(free[not r][j]) #########
                break        # Next: Get_MaxSpeed()            #
        else:                #                                 #
            for r in (a, b): #                                 #
                goal[r].append(free[r][j]) #####################
    return goal, crossbar #                                    #
################################################################
goal, crossbar = Reduction() #                                 #
################################################################
if verbose: ## - Tos kBagpaT Bukgam <u ro TaM??             ####  
    baz()   ## - He!?                                       ####
    print("goal:", *goal, sep = '\n') ##########################
    print("crossbar:", *crossbar, sep = '\n') ##            ####
################################################################
from itertools import permutations as permutat #               #
################################################################
def Get_Speed(more, less, p):    # - TBa e nogurpaBKa c Hac... #
    speed = [[], []]             # - u3nt<HeH ctM ctc rHsB!!!  #
    for j, i in enumerate(p):    #                             #
        if crossbar[more][i] != crossbar[less][j]: #########c/:D
            speed[more].append(i) #                            # 
            speed[less].append(j) #                            #
    return speed                  #                            #
#########################################=##########*#####^##<##
def Get_MaxSpeed(more, less):            #          #     #  ### 
    n = len(crossbar[more])              #          #     #  ###
    k = len(crossbar[less])              #          #     #    #
    maxspeed = [[], []]                  #          #     ######
    maxlen = 0                           #          #          #
    for p in permutat(range(n), k):      #          #          #
        speed = Get_Speed(more, less, p) #          ############
        if len(speed[0]) > maxlen:       #                     #
            maxspeed = speed             #                     #
            maxlen = len(maxspeed)       #                     #
    return maxspeed                      #                     #
########################################^######################^
if len(crossbar[b]) > len(crossbar[a]): #       o o      wow!  # 
    more, less = b, a                   #    . .         what  #
else:                                   #   ''           is    #
    more, less = a, b                   #     "          this? #
####################################=##########################+
maxspeed = Get_MaxSpeed(more, less) # maxspeed hold crossbar   #---$
if verbose:                         # indexes which will         9 |
    baz()                           # maximize reading speed:) ######
    print("maxspeed =", maxspeed)   #                          #
###########################################+###################-
for r in (a, b):                           # Next: Test Infut, #  
    for j in maxspeed[r]:                  # and Heroes III    #
        goal[r].append(crossbar[r][j])     # Yeah! I think     #
for r in (a, b):                           # dhis is the 3-rd  #
    for j in range(len(crossbar[r])):      # program in a row  #
        if j not in maxspeed[r]:           # showing how not 2 #...,
            goal[r].append(crossbar[r][j]) # write programs.     a :
###########################################=####################```'
fill_lock(goal)                        #####                   #
for r in (a, b):                       ####>-------------------<
    lock[r].extend(goal[r])            ####>-------------------<
siz = [len(lock[a]), len(lock[b])]     ####>-------------------<
m = max(siz)                           ####>-------------------<
for r in (a, b):                       ####>-------------------<
    siz[r] = m - siz[r]                ####>-------------------<
for r in (a, b):                       ####>-------------------<
    lock[r].extend([pas]* siz[r])      ####>-------------------<
print("shedule:", *lock, sep = '\n')   ####>-------------------<
baz()                                  #####                   #
########################################################### log:
