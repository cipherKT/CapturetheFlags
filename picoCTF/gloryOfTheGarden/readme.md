# start
Since this a jpg file first thing you need to do is check if weather Is is actually jpg file? 
Run the below command
```
file garden.jpg
```

Since this is actually a jpg now there are two possibilities
1. Change/modifiction in metadataa 
2. Hidden file/directory inside the image
Lets go with the option 1: 
Try runnig it throug the exiv2 tool it check for any commnets if any
```
exiv2 pr garden.jpg
```
It says no exif data try runnig exiftool:
```
exiftool garden.jpg
```
try looking for comments or any unsual data you think that is suspicious opps nothing found 
Now we can run it through the strings command this was the last option because gives too big output and it gets tedious to find the flag using this But we can mix it up with the grep Since every flag of picoCTf is wrapped around picoCTF{} we can use the command below to check if there is any flag of this format
```
strings garden.jpg | grep pico
```
This command will look for specific strings containing pico in it
# Boom !!!
final command got us the flag
```
picoCTF{more_than_m33ts_the_3y3eBdBd2cc}
```
