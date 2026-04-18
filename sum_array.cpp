// file: sum_array.cpp
#include <iostream>
#include <vector>

int sumArray(const std::vector<int>& arr) {
    int sum = 0;

    for (size_t i = 0; i <= arr.size(); i++) {
        sum += arr[i];
    }

    return sum;
}

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    std::cout << "Sum: " << sumArray(v) << std::endl;

    return 0;
}
