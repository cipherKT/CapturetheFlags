# start
start by netcatting the server try playing with code you will notice that you can manipulate data by your own and the data that you can manipulate and data that is fixed secure_var are at differnt addresses and for me the data that can be manipulated is at `0x56b4607952b0` and fixed data is at `0x56b4607952d0` so this is 32 bit difference so what i did enter the value at buffer which is greater than `32bits`you can enter an integer larger thatn 2.1 billion ig that works but i entered just bunch of 9s for a long period of time and got the flag 
# Boom !!!
```
picoCTF{my_first_heap_overflow_c3935a08}
```
