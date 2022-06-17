#include<iostream>
using namespace std;

int main()
{
    int tab[1001], i = 0, szukana;
    
    //wczytanie elementów tablicy, ostatnim elementem jaki wczytamy jest wartownik = -1
    do{
        cin>>tab[i];
    }while(tab[i++]!=-1);
    
    //podanie liczby do wyszukania
    cin>>szukana;
    
    i = 0;
    //przeszukanie tablicy
    while(tab[i]!=szukana && tab[i]!=-1) ++i;
    //koniec szukania
    //jeśli zatrzymaliśmy się na wartowniku, to oznacza, 
   //że szukana liczba nie występuje w zbiorze    
    if(tab[i] == -1) 
       cout<<"Szukany element nie występuje w tablicy"<<endl;
    else
       cout<<"Liczba "<<szukana<<" znajduje się na pozycji "<<i+1<<endl;
    
    return 0;
}