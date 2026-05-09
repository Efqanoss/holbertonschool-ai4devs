#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};
    
    // Xəta: Massiv sərhədini aşır (Buffer overflow ehtimalı)
    for (int i = 0; i <= 10; i++) {
        printf("Rəqəm: %d\n", numbers[i]);
    }

    // Xəta: Sıfıra bölmə
    int x = 10;
    int y = 0;
    int z = x / y;

    return 0;
}
