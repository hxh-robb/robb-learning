#include <stdio.h>

main(){
    // int fahr, celsius;
    float fahr, celsius; // P-12
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    fahr=lower;
    
    /* Exercise 1-3 */
    printf("%s\t%s\n","Fahrenheit","Celsius");
    
    while(fahr<=upper){
        // celsius = 5 * (fahr-32) / 9;
        celsius = 5.0 / 9.0 * (fahr-32); // P-12
 
        // printf("%d\t%d\n", fahr, celsius);
        // printf("%3d %6d\n", fahr, celsius); // P-11
        // printf("%3.0f %6.1f\n", fahr, celsius); // P-12
        
        printf("%10.0f\t%7.1f\n",fahr, celsius); // Exercise 1-3

        fahr += step;
    }
}
