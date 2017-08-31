matmul: matmul.c
	gcc matmul.c -o matmul -Wall -O2

unroll: matmul_unroll.c
	gcc matmul_unroll.c -o matmul_unroll -Wall -O3 -funroll-loops

clean:
	rm -f matmul
