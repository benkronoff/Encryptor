import time


import numpy
from numpy.random.mtrand import randint


dict = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dictt = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26, '-': 27, ',': 28, ' ': 29, '.': 30}
done = []


def rando(n):
    range_start = int(10**(n-1))
    range_end = int((10**n)-1)
    return randint(range_start, range_end)


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


def set_array(choice):
    # lets create a random list of numbers, 1-30, non repeating, in a list
    # probably not the best way of doing it but this will work.
    # define used dict:
    choice = int(choice)
    used_val = ['']
    a = []
    len = 0
    a_old = 0
    if choice == int(1):
        print("[] USING KEY #1")
        print("   [] This may take a few seconds... (3 x (100 - 999k calculations!))")
        for x in range(int(rando(6))):
            val = rando(2)
            while val > 90:
                val = int(rando(2))
            else:
                if int(val) in used_val:
                    val = int(rando(2))
                else:
                    used_val.append(int(val))
                    a.append(int(val))

        # a = [1, 13, 24, 4, 5, 6, 29, 8, 9, 17, 11, 12, 2, 14, 26, 16, 10, 18, 19, 20, 21, 22, 23, 3, 25, 15, 27, 28, 7, 30]
    if choice == int(2):
        print("[] USING KEY #2")
        print("    [] This may take a few seconds... (3 x (100 - 999k calculations!))")
        for x in range(int(rando(6))):
            val = rando(2)
            while val > 90:
                val = int(rando(2))
            else:
                if int(val) in used_val:
                    val = int(rando(2))
                else:
                    used_val.append(int(val))
                    a.append(int(val))

    num1 = int(rando(1)) + int(rando(1) * 2)
    # the array generated is > 64 chars long, so a random slice is taken from it, and used to assign to chars.
    num2 = num1 + 64
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
def main(in_range, in_str):

    print("[JOB: ENCRYPT MESSAGE] ##############################################")
    print("[MESSAGE: " + in_str + "]")
    range_count = 0
    in_range = int(in_range)

    for y in range(in_range):

        range_count =+ 1
        elem_count = 0
        char_count = 0
        print("[" + str(range_count) + "] OUTPUT[s] REQUESTED ###################################")
        coded_str = str()
        nope = ['']
        time.sleep(3)

        char_count = len(in_str)
        print("[] Counted " + str(char_count) + " total chars.")

        for elem in in_str:
            elem_count =+ 1
            print("   [] PASSING CHAR: #[" + str(elem_count) + "]:    " + elem + " ### []")
            if str(elem) in done:
                # pull the existing element value from dictionary
                print(str(elem) + " is in " + str(done))
                elemnnew = dictt[str(elem)]
                coded_str = coded_str + "-" + str(elemnew)
                coded_array.append(int(elemnew))
                continue
            else:
                # ALL OF THIS IS TO GET THE NEW ELEM VALUE (THE CHAR IN THE STR)
                selection = int(33)

                while selection > 81:
                    math = 60 - selection
                    math2 = math + rando(1)
                    randchar = int(rando(2))
                    while randchar < math:
                        randchar = int(rando(2))
                    selection = int(randchar - math)
                    print("   [] TRYING x1 | " + str(selection))

                #    check again
                if elem in done:
                    print (str(elem) + " is in " + str(done))
                    elemnnew = dictt[str(elem)]
                    coded_str = coded_str + "-" + str(elemnew)
                    coded_array.append(int(elemnew))
                    break

                    # check our array size
                if int(0) <= int(selection) <= int(len(a)):
                    elemnew = a[selection]
                    elemnew = int(elemnew)
                else:
                    failsafe = int(rando(1) * 4)
                    selection = int(failsafe / rando(1))
                    print("   [] TRYING x2 | " + str(selection))
                    elemnew = a[int(selection)]

                    # have we used this elem we just came up with, before?
                if int(elemnew) in nope:
                    print("Already used x1: " + str(elem) + " | Trying: " + str(selection))
                    selection = selection - 3
                    elemnew = a[selection]
                    if int(elemnew) in nope:
                        print("Already used x2: " + str(elem) + " | Trying: " + str(selection))
                        selection =- int(rando(1))
                        elemnew = a[selection]
                        if int(elemnew) in nope:
                            print("Already used x3: " + str(elem) + " | Trying: " + str(selection))
                            print("Oh boy // you may want to restart the program...")
                            selection = selection - 3
                            elemnew = a[selection]
                            if int(elemnew) in nope:
                                print("Extremely unlucky or a bug. Please restart.")
                                quit()
                # ALL OF THIS IS TO GET THE NEW ELEM VALUE (THE CHAR IN THE STR)


                # we now have a value in place for our character
                # lets pass it to the appropriate places, log the character we used
                # for the letter (the last line), etc
                if coded_str == str():
                    # str is empty, this is first char
                    coded_str = str(elemnew)
                    coded_array = [int(elemnew)]
                    nope.append(int(elemnew))
                    done.append(str(elem))
                    dictt[str(elem)] = int(elemnew)
                else:
                    # str is not empty, append as necessary
                    coded_str = coded_str + "-" + str(elemnew)
                    coded_array.append(int(elemnew))
                    nope.append(int(elemnew))
                    done.append(str(elem))
                    dictt[str(elem)] = int(elemnew)


        # user messags
        print(" [] ALL [" + str(elem_count) + "] CHARS SUCCESSFULLY PARSED.")
        print(str())
        print("########### .... OUTPUT []")
        print("## STRING.MSG: ##      '" + coded_str + "'")
        print("## ARRAY.MSG: ##      '" + str(coded_array) + "'")
        print("##################################################################")
        print(str())
        print("###########")
        print("# KEY.MSG: " + str(dictt) + "###")
        print("###########")
        print("20 SECONDS []")
        print("###############################")
        time.sleep(20)
        return str(coded_str)


def done_msg():
    print("")
    print("##################################################################")
    print("Job complete.")




choice = find_array()
print("   [] Done! 10k tries // random: " + str(choice))
print("   [] Acting accordingly...")
a = set_array(choice)
print("[] ARRAY SET #####")
print(str())
user_in = str(input("MESSAGE FOR ENCRYPTION | "))
print(str())
msg = main(1, user_in)
print(str())
print (msg)
done_msg()