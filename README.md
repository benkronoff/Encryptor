# Encrypt / Decrypt

This is just a Python script I was messing around with, wasn't a serious project but nevertheless it works well and could easily be incorperated into an actual command etc. 
I don't normally code in Python so this is pretty simple, but I had a lot of fun learning by making this. 

## File notes:

### How it works:
 - chooses which array creation algorithm to use (two slight alternations)  
 - uses code to create randomly ordered number array with  
   no repeats  
 - iterates through dictionary, replacing every key (letter / char),  
   with an again randomly picked number, done by randomly selecting  
   an index in the array, making sure the number isn't assigned to another  
   char/used already, then assigning it to the approx. char in the dictionary.  
 - the users input is then iterated through, with each char being used  
   to call its specified key in the dictionary. this key now has that  
   absolutely randomly picked # value assigned to it, and thus that  
   is what is ultimately used in the message.  


## Update: 
Added decode, with commented walkthrough. The encryptor will return a message and key, and you will need to use these in the correctly output format to decrypt. Send this repo to a friend and have fun!

#### Where to find me:
- ben@flytlabs.dev
- benkronoff.com
- reddit.com/zxrooo
