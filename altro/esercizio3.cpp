#include <iostream>
using namespace std;

int main()
{

    srand(time(0)); // Initialize random number generator.

    int c1 = 0, c2 = 0, c3 = 0, c4 = 0, c5 = 0, c6 = 0, c7 = 0, c8 = 0, c9 = 0, c10 = 0;
    int dim = 100000000;
    printf("%d numeri casuali da 1 a 10\n", dim);
    for (int i = 0; i < dim; i++)
    {
        int num = (rand() % 10) + 1;
        if (num == 1)
        {
            c1++;
        }
        else if (num == 2)
        {
            c2++;
        }
        else if (num == 3)
        {
            c3++;
        }
        else if (num == 4)
        {
            c4++;
        }
        else if (num == 5)
        {
            c5++;
        }
        else if (num == 6)
        {
            c6++;
        }
        else if (num == 7)
        {
            c7++;
        }
        else if (num == 8)
        {
            c8++;
        }
        else if (num == 9)
        {
            c9++;
        }
        else if (num == 10)
        {
            c10++;
        }
    }
    printf("\nc1=%i, c2=%i, c3=%i, c4=%d, c5=%i, c6=%i, c7=%i, c8=%i, c9=%i, c10=%i", c1, c2, c3, c4, c5, c6, c7, c8, c9, c10);
    return 0;
}