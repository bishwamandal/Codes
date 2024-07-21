#include <stdio.h>
#include <string.h>

/**
 * This program concatenates two strings entered by the user.
 * It takes two strings as input and stores the concatenated string in a third string.
 * The concatenated string is then displayed as output.
 */

int main() {
    char s1[10], s2[10], s3[20];
    int i, j;

    printf("Enter first string: ");
    gets(s1);
    printf("Enter second string: ");
    gets(s2);

    for (i = 0; s1[i] != '\0'; i++) {
        s3[i] = s1[i];
    }

    for (j = 0; s2[j] != '\0'; j++) {
        s3[i] = s2[j];
        i++;
    }
    s3[i] = '\0';

    printf("Concatenated string is: %s", s3);
    return 0;
}