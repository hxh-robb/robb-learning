/* Exercise 1-4 */
#include <stdio.h>

int main(){
    float fahr, celsius;
    int lower, upper, step;

    lower = -20;
    upper = 100;
    step = 3; 

    celsius = lower;

    printf("%s\t%s\n", "Celsius", "Fahrenheit");

    while(celsius <= upper){
        fahr = celsius * 9.0 / 5.0 + 32;
        printf("%7.0f\t%10.0f\n", celsius, fahr);
        celsius += step;
    }

}
