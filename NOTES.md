```
omc -s Hello.mo
make -f Hello.makefile
./Hello -override startTime=0,stopTime=10 -s rungekutta
```

Output is in Hello_res.mat file.
