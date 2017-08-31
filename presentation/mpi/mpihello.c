#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm comm = MPI_COMM_WORLD;

    MPI_Comm_rank(comm, &rank); // Ranks enumerate processes
    MPI_Comm_size(comm, &size);
    printf("hello world from process %d/%d\n", rank, size);
    MPI_Barrier(comm);  // Wait for all processes to print

    int ranksum;
    MPI_Allreduce(&rank, &ranksum, 1, MPI_INTEGER, MPI_SUM, comm);
    printf("rank %d: I got %d\n", rank, ranksum);
    MPI_Finalize();
    return 0;
}
