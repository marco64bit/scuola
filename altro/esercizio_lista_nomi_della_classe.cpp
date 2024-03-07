#include <iostream>
using namespace std;

// esercizio:
// chiedere il numero di alunni all'utente
// inserire i nomi degli alunni in una lista di string
// stamapre a schermo i nomi inseriti nella lista

// PREMESSA:
/**
 * la scrittura cout << "a"; equivale a scrivere printf("a");
 * la scrittura cin >> x; equivale a srivere scanf("%d", &x);
 *
 * da ora in poi useremo cin e cout al posto di printf e scanf in quanto ci consentono di lavorare con le liste
 */

void bubbleSort(int listSize, string classe[]) {
  int i, j;
  string temp;

  // ordino gli elementi
  for (j = 0; j < listSize - 1; j++)
  {

    for (i = 0; i < listSize - 1; i++)
    {
      if (classe[i] > classe[i + 1])
      {
        temp = classe[i];
        classe[i] = classe[i + 1];
        classe[i + 1] = temp;
      }
    }
  }

  cout << "Array ordinato con bubble sort:\n\n";

  for (i = 0; i < listSize; i++)
  {
    cout << "\t - " << classe[i] << "\n";
  }
}

int main() {

  // creo la variabile numeroAlunni di tipo intero
  int numeroAlunni;

  // stampo a schermo
  cout << "Quanti alunni ci sono in classe? ";

  // traserisco l'input da tastiera dell'utente nella variabile numeroAlunni
  cin >> numeroAlunni;

  // stampo a schermo il valore appena inserito
  cout << "La classe avrà " << numeroAlunni << " alunni\n";

  // creo la variabile di lista di string con dimensione massima = numeroAlunni (scritto tra parentesi quadre)
  string classe[numeroAlunni];

  // faccio un ciclo da 0 a numeroAlunni -1
  for (int posizione = 0; posizione < numeroAlunni; posizione += 1)
  {
    cout << "inserisci nome alunno: ";
    // trasferisco l'input da tastiera nella lista di string alla posizione "posizione"
    cin >> classe[posizione];
    cout << "- Alunno inserito\n";
  }

  cout << "\n\n";
  cout << "riepilogo alunni in classe:\n";

  for (int i = 0; i < numeroAlunni; i += 1)
  {
    // stampo la lista di tuttli gli alunni
    cout << "\t - " << classe[i] << "\n";
  }

  // Note:
  // \n manda a capo la linea
  // \t è la tabulazione, indenta la scritta

  bubbleSort(numeroAlunni, classe);

  return 0;
}