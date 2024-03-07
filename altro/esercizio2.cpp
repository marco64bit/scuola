#include <iostream>
using namespace std;

int main()
{
    const int dim = 5;
    int numeri[dim];
    for (int i = 0; i < dim; i++)
    {
        printf("inserisci numero ");
        scanf("%d", &numeri[i]);
    }
    int somma = 0;
    int min, max = -1;
    for (int i = 0; i < dim; i++)
    {
        somma = somma + numeri[i];
        if (i == 0)
        {
            min = numeri[i];
            max = numeri[i];
        }
        else
        {
            if (numeri[i] < min)
            {
                min = numeri[i];
            }
            if (numeri[i] > max)
            {
                max = numeri[i];
            }
        }
        printf("%i \n", numeri[i]);
    }
    printf("somma %d", somma);
    printf("\n");
    printf("media %d", somma / dim);
    printf("\n");
    printf("min %d", min);
    printf("\n");
    printf("max %d", max);

    printf("\n\nFine\n");
    return 0;
}
