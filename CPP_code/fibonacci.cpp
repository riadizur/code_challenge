#include <iostream>

auto fibonacci = [](auto& self, int n) -> int {
    if(n < 2){
        return n;
    }
    return self(self, n-1) + self(self, n-2);
};

int main() {
    int x = 100;
    for(int n=0;n<x; n++){
        std::cout << "Fibonacci(" << n << ") = " << fibonacci(fibonacci, n) << std::endl;
    }
    return 0;
}