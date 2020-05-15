
#                                      [] SCRIPT START []
########################################################################################################

##################################################
####                     [] TEXT DECRYPTION SCRIPT
##################################################

#####################
####         [] ABOUT
#####################




########################################################################
#### contact for business / requests / help / questions / collaborations
########################################################################
####                                                                ####
####                        ben@flytlabs.dev                        ####
####                                                                ####
########################################################################
### |01101001|01110110|01100001|01101110|00001101 was here.




def msg(x):
    if x == "longMsg":
        print("#######################################")
        print("#######################################")
        print("#######################################")
        print("#######################################")
    if x == "gap":
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()


def decrypt(x, y):
    strIn = str(x)
    keyIn = str(y)

    # set the msg array, split it up by '-'
    decryptmsg = strIn.split("-")

    # set the key array, split it up by ' '
    keylist = keyIn.split(" ")

    # prepare output variables
    msg_Str = str()
    msg_Array = [0]

    dictt = {'a': 1, 'b': 2,'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
            'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,'z': 26, '-': 27,
            ',': 28, ' ': 29, '.': 30, '?': 31, '!': 32, '|': 33, '@': 34, '#': 35, '$': 36, '%': 37, '^': 38, '&': 39, '*': 40,
             '(': 41, ')': 42, '_': 43, '=': 44, '+': 45, '[': 46, ']': 47, '{': 48, '}': 49, '"': 50, "'": 51, '<': 52, '>': 53,
             '/': 54, '~': 55, '1': 56, '2': 57, '3': 58, '4': 59, '5': 60, '6': 61, '7': 62, '8': 63, '9': 64, '0': 65}

    tmpkey = [0]

    key_dict = {'NUL__': 0}

    # find each keys value, as it + 1 will be the index of its
    # value in the encrypted message in the key list.
    for key in dictt:

        index = int(dictt[key] + 1)
        index = int(index)
        index = index - 1

        # we found the index via the value, now go look in keylist and get it
        passchar = keylist[index]

        # create a new dictionary so we can just call each value in the message and assign
        # it to its value in the dictionary, pretty much opposite of encryption
        key_dict[passchar] = str(key)

    # now we have the new dictionary set
    # loop through our user message
    for elem in decryptmsg:

        # get the current character
        passchar = key_dict[elem]

        # set it appropriately
        if msg_Str == str():
            msg_Str = passchar
            msg_Array = [passchar]
        else:
            msg_Str = msg_Str + passchar
            msg_Array.append(passchar)


    return msg_Str, msg_Array


######################################################################
# main runtime

x = input("'1-27-3-42' MSG.LIST: | ")
y = str(input("'0 186 60 4' KEY.LIST: | "))

msgs = decrypt(x, y)

msg_Str = msgs[0]
msg_Array = msgs[1]

msg("longMsg")
msg("gap")

print("    ...  message decoded")
print()
msg("longMsg")
print()
print("OUTPUT: ")
print("#########")
print(msg_Str)
print("#########")
print()
print()
print()
print(msg_Array)
print()
msg("longMsg")
