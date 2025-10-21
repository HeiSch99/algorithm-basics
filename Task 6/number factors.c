#include <stdio.h>

// Defining the number factors calculation as a function
void factors(int n) {
    printf("Factors of %d: ", n);
    for (int i = 1; i <= n; i++) {      // For loop with utility integer i
        if (n % i == 0) {
            printf("%d ", i);           // Prints calcualted factor numbers
        }
    }
    printf("\n");
}

// Main loop
int main() {
    int n;                              // Integer n is declared
    printf("Enter a number: ");
    scanf("%d", &n);                    // Writes input into n
    
    factors(n);                         // Function call

    // Keeps program open until the further input so it does not close immediately
    printf("Press Enter to exit...");
    getchar();
    getchar();
    
    return 0;
}

