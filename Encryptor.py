import time
import numpy

from numpy.random.mtrand import randint


#                                      [] SCRIPT START []
########################################################################################################

##################################################
####                     [] TEXT ENCRYPTION SCRIPT
##################################################

#####################
####         [] ABOUT
#####################

# text encryption script by Ben Kronoff
#                           benkronoff.com
# how it works:
# - chooses array code to use (two slight alternations)
# - uses code to create randomly ordered number array with
#   no repeats
# - iterates through dictionary, replacing every key (letter / char),
#   with an again randomly picked number, done by randomly selecting
#   an index in the array, making sure the number isn't assigned to another
#   char/used already, then assigning it to the approp. char in the dictionary.
# - the users input is then itterated through, with each char being used
#   to call its specified key in the dictionary. this key now has that
#   absolutely randomly picked # value assigned to it, and thus that
#   is what is ultimately used in the message.
# - decode part soon; itterating back through key to assign appropriate letters.
#   if you are looking for this now it is easily done - look up 'parsing string
#   into a dictionary' i.e, then itterate through your message assigning each char
#   to its original value in that dictionary. you may have to switch the keys/values
#   rather than trying to reference in reverse, but i don't know enough about
#   python to know which is possible/most effecient. (you can test keys and values
#   with a for loop right?)
#   if not then parse from string but backwards, keys > vals etc
#
# comments are placed at various sections to explain what the program is doing.
# if you appreciate my efforts, kindly view my website for more by me.
#
# i am NOT a python coder generally. i am currently learning c# however, and
# started with scripting languages like bash batch etc. this was just a fun
# project that i though others may find some value in using this to learn or
# expand, etc. thus, please ignore redundant code etc, changes were made,
# i may have forgotten to delete some redunant vars etc, and i definitely
# don't have enough experience to make this even 1/2 as effecient as it could
# be in this language.
#
# hour total: 9pm-4pm = 16 total / ~12 hours after sleep (not good lol)
#   .. this script was originally much longer and as it is now could
#   have easily been written in fractions of the time. but, i'm learning.
#   and that was the point!
#
# stay safe, and enjoy.

########################################################################
#### contact for business / requests / help / questions / collaborations
########################################################################
####                                                                ####
####                        ben@flytlabs.dev                        ####
####                                                                ####
########################################################################
### |01101001|01110110|01100001|01101110|00001101 was here.








# random number function used throughout script

def rando(n):
    range_start = int(10**(n-1))
    range_end = int((10**n)-1)
    return randint(range_start, range_end)


done = []

'''figure out which array code we should use using the most redundantly
random way possible
this was implemented different before, and was too lazy too take out
after redesign, don't really need this anymore but ads to randomness
and could be extended to choose from more equations that determine
the array used'''

def find_array():
    print("[] 10k Calculations now...")
    print("")
    print("#######################")
    num = 0
    for x in range (10000):
        num =+ 1
        rand1 = int(rando(2) - rando(2))
        rand = int(rand1 / 2)
        if rand <= 2:
            if rand > 0:
                print("       [] CAUGHT // RANDOM #: " + str(rand) + " //    [] from    '" + str(rand1) + " / 2'")
                choice = str(rand)
                choice = int(rand)
        else:
            count = 0
    return choice


def len_print(input):
    return len(input)







# set the array  ################################################
# sets to a bunch of non repeating numbers which are randomly
# picked from

def set_array(choice):
    # let's create a random list of numbers, non repeating
    # probably not the best way of doing this but this will works.
    # define used dict:
    choice = int(choice)
    used_val = ['']
    a = []

    # random code choice 1 ###########
    if choice == int(1):
        print("[] USING KEY #1")
        print("   [] This may take a few seconds... (3 x (100 - 999k calculations!))")
        for x in range(int(10000 + rando(5) / rando(1))):
            val = rando(2)

            # we already used this value!
            if int(val) in used_val:
                val = int(rando(2))
            else:
                used_val.append(int(val))
                a.append(int(val))

    # random code choice 2 ###########
    if choice == int(2):
        print("[] USING KEY #2")
        print("    [] This may take a few seconds... (3 x (100 - 999k calculations!))")
        for x in range(int(10000 + rando(5) + rando(3))):
            val = rando(2)

            # we already used this value!
            if int(val) in used_val:
                val = int(rando(2))
            else:
                used_val.append(int(val))
                a.append(int(val))



    num1 = int(rando(1)) + int(rando(1) * 2)
    # the array generated is, pretty long, so a random slice is taken from it,
    # and used to assign to chars.
    num2 = num1 + 150
    a = a[num1:num2]
    print(str())
    print(str())
    print("#######################################################################################")
    print ("ARRAY_[" + str(a) + "]")
    print("#######################################################################################")
    print(str())
    return a


'''
in_range - passed from argument
 defining how many encryptions of the same msg we want it to return.
 can be useful for distributing the message to others without compromising a single key.
 '''





# parse numbers to dictionary keys (the chars expected in the msg) #######################################

def parse(a):

    in_range = a
    if in_range == str():
        in_range = int(1)

    range_count = 0
    coded_array = []
    for y in range(in_range):

        range_count =+ 1
        elem_count = 0
        char_count = 0
        print("[" + str(range_count) + "] OUTPUT[S] REQUESTED ###################################")
        coded_str = str()
        nope = ['']
        time.sleep(3)


        # define dictionary keys will looped from
        # this method is effecient as new characters can
        # be supported by simply adding them as a key
        # here.
        dictt = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13,
                 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22,
                 'y': 25, 'x': 24, 'z': 26, '-': 27, ',': 28, ' ': 29, '.': 30, '?': 31, '!': 32, '|': 33}

        for key in dictt:
            elem_count =+ 1
            print("        [] PASSING CHAR:              [" + str(key) + "]")
            selection = int(rando(3) / rando(1))

            while selection in done:
                print("        [] PASSED AS                  -[" + str(selection) + "] - error_already_used")
                selection = int(rando(3) / rando(1)) - int(rando(1) + rando(1))

            if coded_str == str():
                done.append(int(selection))
                dictt[key] = int(selection)
            else:
                dictt[key] = int(selection)
                done.append(int(selection))
            print("        [] PASSED AS                  -[" + str(selection) + "]")

    return dictt



# encrypt #######################################
def encrypt(in_str, key):

    coded_str = str()

    print("[JOB: ENCRYPT MESSAGE] ##############################################")
    print("[MESSAGE: " + in_str + "]")

    # loop through chars in user input
    for char in in_str:
        parse = key[char]
        # first letter
        if coded_str == str():
            coded_str = str(parse)
            coded_array = [int(parse)]
        # not the first letter
        else:
            coded_str = coded_str + "-" + str(parse)
            coded_array.append(int(parse))

    # user messages
    elem_count = len(in_str)
    print(" [] ALL [" + str(elem_count) + "] CHARS SUCCESSFULLY PARSED.")
    print(str())
    print("########### .... OUTPUT []")
    print("## STRING.MSG: ##      '" + str(coded_str) + "'")
    print("## ARRAY.MSG: ##      '" + str(coded_array) + "'")
    print("##################################################################")
    print(str())
    print("# KEY.MSG: " + str(key) + "###")
    print("###########")
    print(str())
    print("20 SECONDS []")
    print("###############################")
    time.sleep(20)

    return str(coded_str)






# main program runtime #######################################

# choice between array code (1st or 2nd)
# choice will = script being used, 1 or 2
choice = find_array()

print("   [] Done! 10k tries // random: " + str(choice))
print("   [] Acting accordingly...")

time.sleep(3)
# create array using previously chosen command
a = set_array(choice)

print("[] ARRAY SET #####")
print(str())

# get the message to encrypt
user_in = str(input("MESSAGE FOR ENCRYPTION | "))

print(str())

# parse the array ontop of the dictionary values randomly

#       param can be used to assign them multiple times. it

#       was a more useful feature in orig design, however i

#       suppose it could be used for increased randomness still.
key = parse(1)


# using these randomly assigned numbers to chars, substitute in

# users msg as appropriate.
msg = encrypt(user_in, key)

# presentational
print(str())
print(msg)
print("")
print("##################################################################")
print("Job complete.")

# done!
# this section is pretty simple eh? love python.
#########################################################################################################
