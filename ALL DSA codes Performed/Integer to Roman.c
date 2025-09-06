#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * intToRoman(int num) {
	int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
	char *symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
	char *roman = malloc(20 * sizeof(char));
	roman[0] = '\0';

	for(int i = 0; i < 13;i++) {
		while(num >= values[i]){
			strcat(roman, symbols[i]);
			num -= values[i];
		}
	}
	return roman;
}

int main(int argc, char *argv[]) {
	int num = atoi(argv[1]);
	printf("%s\n", intToRoman(num));
	return 0;
}