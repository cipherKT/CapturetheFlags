# start
Start by downloading the zip file in desired directory<br> 
```
curl -O https://artifacts.picoctf.net/c_titan/75/challenge.zip
```

unzip this file using the command<br>

```
unzip challenge.zip
```

Now there is one directory [drop-in](../14_commitment_issues/drop-in/) in that directory there is a txt file message.txt file <br>
try logging that in terminal <br>

```
cat message.txt
```
Nothing happens<br>
Now while uzipping the file we have notices git files so try getting git commit history<br>

```
git reflog 
```
we can see a commit where there is commit message create flag so checkout that commit and get the flag<br>

```
git checkout 6603cb4
```

this code can differ so make sure to use your key of the commit where flag is created <br>


# boom!!! got the flag 
```
picoCTF{s@n1t1z3_9539be6b}
```
