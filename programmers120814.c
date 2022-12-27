// Code Submmited
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    if(n >= 1 && n <= 100) {
        answer = n / 7;
        if(n % 7 != 0)  answer++;
    }
    return answer;
}

// Better Code
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    answer = n / 7 + ((n % 7 == 0) ? 0 : 1);
    return answer;
}
