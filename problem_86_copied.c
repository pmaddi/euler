// Copied from answers... amazed how much faster c is 
// than python
#include <stdio.h>
#include <math.h>

int main() {
    int say = 0;
    for (int i = 1;; i++) {
        for (int j = 1; j <= i; j++) {
            for (int k = 1; k <= j; k++) {
                int x = (i * i)+(k + j)*(k + j);
                if ((float) sqrt(x) == sqrt(x))
                    say++;
                if (say > 1000000) {
                    printf("%d", i);
                    return 0;
                }
            }
        }
    }
}
