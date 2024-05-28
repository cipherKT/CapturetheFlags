# start
Get the file given in challege 
```bash
curl -O https://artifacts.picoctf.net/c_titan/111/enc_flag
```
This will download the file [enc_flag](../15_interncdec/enc_flag)
try logging this file it gives this output 

`*YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==`

This seems like a base64 encoded now go to [cyberchef](https://cyberchef.org/)

And try running the magic option you will get something in base64
`b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='`
now after dropping the `b'` and `'` insert the remaining thing again in base64 this will give this as a output 
`wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}`
this seems like in flag format and after going through some encryption this is decoded by rot13 bruteforce in 19th iteration 

# boom!!!
```
picoCTF{caesar_d3cr9pt3d_890d2379}
```
