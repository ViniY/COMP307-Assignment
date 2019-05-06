 gcc -g -O -o nntrain nntrain.c backprop.c globals.c network.c patterns.c weights.c -lm -lc
gcc -g -O -o nntest nntest.c backprop.c globals.c network.c patterns.c weights.c -lm -lc
./nntrain iris.net iris.pat
./nntest iris.net iris.pat weights.dat
