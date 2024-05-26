# start
If we observe the images it is clearly visible that this is cipher encoded flag.
Now our job is to find the formula used for encoding.
Since there is fixed pattern followed in every pico ctf challenge, clearly first letter is p so ascii value of p is 112, similarly for i ascii value is 105 and for c it is 99 
Clear from the pattern 
every char is converted into ascii value and 96 is subtracted from it 
So lets write a code that will convert this number in string

Code is in solve.cpp

# Boom!!!

After running it through the code we get the flag
```
picoCTF{thenumbersmason}
```
