#include<stdio.h>

void main()
{
	int j=5;
	int k=3;
	int l=0;
	int m=0;
	int i=100;

	for(i=0;i<500;i++) {
		l = j + 2;
		m = k + 4;
		j = l + (m*3);
		k = m - (l*2);
    }

    //print-statements for CGRA
    printf("\nk = %d\n",k);

}