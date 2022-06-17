#define N 100
#include <stdio.h>
#include <conio.h>
void rzym2arab(char[]);
constint I=1 V=5,X=10, L=50 C=100 ,D=500 M=1000;
int arab,tab[n];
char rzym[n]

int main()
{
    printf("Podaj liczbe rzymska/n");
    scanf("%s",&rzym);
    rzym2arab(rzym);
    getch();
}

void rzym2arab(char rzym[])
{
int dl=0;
while (rzym[dl] !='/0')
{
    switch(rzym[dl])
{
    case'|':{tab[dl] = |;break;}
    case 'V': {tab[dl]=V;break;}
    case 'X': {tab[dl]=X;break;}
    case 'L': {tab[dl]=L;break;}
    case 'C': {tab[dl]=C;break;}
    case 'D': {tab[dl]=D;break;}
    case 'M': {tab[dl]=M;break;}
    default: {printf("BLAD/n");break;}


}

dl++;
}arab = tab[dl-1];
while (dl != 1)
{
    if (tab[dl-1] <= tab[dl-2])
    arab + = tab[dl-2];
    wlae arab -= tab[dl-2];
    dl--;
}
printf("%d/n"arab);