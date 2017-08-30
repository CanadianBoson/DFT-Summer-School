#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define REPEAT 1

double matmul_ikj(int I, int J, int K, double *A, double *B, double *C)
{
    int i, j, k;

    for(i=0; i < I * J; i++) {
        C[i] = 0.0;
    }

    clock_t t1 = clock();
    int r;
    for(r=0; r < REPEAT; r++) {
    for(i=0; i < I; i++) {
        for(k=0; k < K; k++) {
            for(j=0; j < J; j++) {
                C[i * J + j] += A[i * K + k] * B[k * J + j];
            }
        }
    }
    }
    clock_t t2 = clock();
    return (double)(t2 - t1) / CLOCKS_PER_SEC;
}

double matmul_ijk(int I, int J, int K, double *A, double *B, double *C)
{
    int i, j, k;

    for(i=0; i < I * J; i++) {
        C[i] = 0.0;
    }

    clock_t t1 = clock();
    int r;
    for(r=0; r < REPEAT; r++) {
    for(i=0; i < I; i++) {
        for(j=0; j < J; j++) {
            for(k=0; k < K; k++) {
                C[i * J + j] += A[i * K + k] * B[k * J + j];
            }
        }
    }
    }
    clock_t t2 = clock();
    return (double)(t2 - t1) / CLOCKS_PER_SEC;
}
double matmul_jik(int I, int J, int K, double *A, double *B, double *C)
{
    int i, j, k;

    for(i=0; i < I * J; i++) {
        C[i] = 0.0;
    }

    clock_t t1 = clock();
    int r;
    for(r=0; r < REPEAT; r++) {
    for(j=0; j < J; j++) {
        for(i=0; i < I; i++) {
            for(k=0; k < K; k++) {
                C[i * J + j] += A[i * K + k] * B[k * J + j];
            }
        }
    }
    }
    clock_t t2 = clock();
    return (double)(t2 - t1) / CLOCKS_PER_SEC;
}

double matmul_jki(int I, int J, int K, double *A, double *B, double *C)
{
    int i, j, k;

    for(i=0; i < I * J; i++) {
        C[i] = 0.0;
    }

    clock_t t1 = clock();
    int r;
    for(r=0; r < REPEAT; r++) {
    for(j=0; j < J; j++) {
        for(k=0; k < K; k++) {
            for(i=0; i < I; i++) {
                C[i * J + j] += A[i * K + k] * B[k * J + j];
            }
        }
    }
    }
    clock_t t2 = clock();
    return (double)(t2 - t1) / CLOCKS_PER_SEC;
}

double matmul_kji(int I, int J, int K, double *A, double *B, double *C)
{
    int i, j, k;

    for(i=0; i < I * J; i++) {
        C[i] = 0.0;
    }

    clock_t t1 = clock();
    int r;
    for(r=0; r < REPEAT; r++) {
    for(k=0; k < K; k++) {
        for(j=0; j < J; j++) {
            for(i=0; i < I; i++) {
                C[i * J + j] += A[i * K + k] * B[k * J + j];
            }
        }
    }
    }
    clock_t t2 = clock();
    return (double)(t2 - t1) / CLOCKS_PER_SEC;
}

double matmul_kij(int I, int J, int K, double *A, double *B, double *C)
{
    int i, j, k;

    for(i=0; i < I * J; i++) {
        C[i] = 0.0;
    }

    clock_t t1 = clock();
    int r;
    for(r=0; r < REPEAT; r++) {
    for(k=0; k < K; k++) {
        for(i=0; i < I; i++) {
            for(j=0; j < J; j++) {
                C[i * J + j] += A[i * K + k] * B[k * J + j];
            }
        }
    }
    }
    clock_t t2 = clock();
    return (double)(t2 - t1) / CLOCKS_PER_SEC;
}

void test(int M)
{
    int I = M, J = M, K = M;
    int i;

    double *A = malloc(I * K * sizeof(double));
    double *B = malloc(K * J * sizeof(double));
    double *C = malloc(I * J * sizeof(double));

    // Initialize arrays to arbitrary values
    for(i=0; i < I * K; i++) {
        A[i] = i;
    }
    for(i=0; i < K * J; i++) {
        B[i] = i;
    }

    printf("ikj %e\n", matmul_ikj(I, J, K, A, B, C));
    printf("kij %e\n", matmul_kij(I, J, K, A, B, C));
    printf("ijk %e\n", matmul_ijk(I, J, K, A, B, C));
    printf("jik %e\n", matmul_jik(I, J, K, A, B, C));
    printf("jki %e\n", matmul_jki(I, J, K, A, B, C));
    printf("kji %e\n", matmul_kji(I, J, K, A, B, C));

    free(A);
    free(B);
    free(C);
}

int main(int argc, char **argv)
{
    test(1000);
    return 0;
}
