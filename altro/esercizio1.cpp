#include <iostream>
using namespace std;

int main()
{
    string sesso;
    int eta;
    cout << "di che sesso sei? ";
    cin >> sesso;
    cout << "quanti anni hai? ";
    cin >> eta;
    if (sesso == "maschio")
    {
        cout << "è maschio ed ha " << eta;
    }
    else
    {
        eta = eta / 2;
        cout << "è femmina ma i gentiluomini ti danno " << eta << " anni";
    }
}