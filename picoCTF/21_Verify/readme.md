# start
start by downloading the `challenge.zip` file then try to explore the directories, there is a file decrypt.sh and it demands a file from the directory files and checksum.txt contains the hash to match for the file which is complete so run the command to checksum the all files and match it with the checksum given in checksum.txt file that file contains the flag 
This is the logic that I had in mind so I started with this 
ran the command 
```bash
sha256sum files/*
```
This printed the checksum of all the files now it is hard to find exact matching hash so dumped this data in txt file 
```bash
sha256sum files/* > out.txt
```
This file contains all the checksum in it 
then I ran this two command to find the correct file 
```bash
cat out.txt| grep 3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4
```
this gave the file which is `e018b574` then I tried running the decrypt.sh file and it returned nothing then i did ssh to the server and ran the same command there
```bash
./decrypt.sh files/e018b574
```
It worked and gave the answer 
# Boom !!!
```
picoCTF{trust_but_verify_e018b574}
```
