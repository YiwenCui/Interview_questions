#include <iostream> 
#include <string>
using namespace std;
void common_factor(int a, int b);
int i;

int main(){
    common_factor(100,50);
    
    return 0;
}

void common_factor(int a , int b){
    int counter =1;
    for (i=std::min(a,b);i>=1;i--){
        if((a%i ==0)&&(b%i ==0)){
            printf("common factor %d is %d\n", counter++, i);
        }
    }

}