# start
start by going to the given link -> [here](http://titan.picoctf.net:64533/)
navigate and look around the website and when you go to about page it says inspect the page then go and inspect the page 
In this page there is something suspicios a tag named section and an attribute named notify_true have some wierd value so try checking if it is a flag or not the value is `cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMjgzZTYyZmV9` This looks like some encrypted flag so go to [cyberchef](https://cyberchef.org/) and run a magic on this text you will get the flag in `base64` decoded version 
# Boom !!!
```
picoCTF{web_succ3ssfully_d3c0ded_283e62fe}
```

