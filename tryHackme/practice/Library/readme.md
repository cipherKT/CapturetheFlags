done with the nmap scan found port 80 and 22 open<br>
ran gobuster and found two interesting pages<br>
1. robots.txt
2. images (directory)

found one username meliodas and ran hydra on it to find password
`iloveyou1`

check for sudo permissions, user had sudo permission to run python files so make a python file for spawning a root terminal 
```python
#! /usr/bin/env python
import pty;pty.spwan("/bin/bash")
```
this will spawn a root terminal and then navigate to root directory to get the flag.
