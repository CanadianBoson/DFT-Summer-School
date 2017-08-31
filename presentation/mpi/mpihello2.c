#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm comm = MPI_COMM_WORLD;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    double mynumber;
    MPI_Status status;
    if(rank == 0) {
        mynumber = 42.0;  // Pass number around to each process
        printf("rank 0 sends to %f to rank 1\n", mynumber);
        MPI_Send(&mynumber, 1, MPI_DOUBLE, 1, 0, comm);
        MPI_Recv(&mynumber, 1, MPI_DOUBLE, size - 1, 0, comm, &status);
        printf("rank 0 finally received %f\n", mynumber);
    } else {
        MPI_Recv(&mynumber, 1, MPI_DOUBLE, rank - 1, 0, comm, &status);
        printf("rank %d received %f from %d, sends to %d\n",
               rank, mynumber, rank - 1, (rank + 1) % size);
        MPI_Send(&mynumber, 1, MPI_DOUBLE, (rank + 1) % size, 0, comm);
    }
    MPI_Finalize();
    return 0;
}
