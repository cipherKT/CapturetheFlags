# start
start by running the source file download it and give it permission to execute and run that file you can follow series of commands to do it
```
curl -O https://mercury.picoctf.net/static/bd84b0d8b57e043a028c36381910d0b7/source
chmod +x source
./source
```
Now after running file interact with it, after entering some inputs coins are getting reduced in multiples of 10 whatever the price is 
And there is a option to buy a flag so try entering the negative value for item to buy 
I entered -100 and it worked 
Now try to buy fruit it gives error that flag.txt doesnot exist 
Now do the nc command and do the same thing 
```
nc mercury.picoctf.net 11371
```
Do the same thing buy negative items and get the coins to buy the flag after running this file we get an array of numbers it seems this are ascii values convert them into text 
```
python solve.py
```
this will return the flag 

# Boom !!!
```
picoCTF{b4d_brogrammer_b8d7271f}
```
