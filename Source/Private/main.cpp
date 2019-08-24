/**
 * Author: Shon Verch
 * File Name: main.cpp
 * Project Name: PPiCCG
 * Creation Date: 08/24/19
 * Modified Date: 08/24/19
 * Description: Generates the a CSV representing the graph
 *              of the prime counting (pi) function to its approximation.
 *              This graph helps visualize the limit of the quotient of the
 *              two functions (i.e. how the approximation converges eventually).
 *              
 *              The output of this program is a CSV file with two rows: the value of n
 *              and the ratio of the value of the prime counting (pi) function to its
 *              approximation at n (i.e. y = pi(n) / ~pi(n) where ~pi(n) denotes a
 *              function that approximates pi(n)).
 */
   
#include <iostream>
#include <fstream>
#include <string>
#include <primecount.hpp>

int main(const int argc, char** argv)
{
    if (argc <= 2)
    {
        std::cout << "Missing required positional argument.\n";
        return -1;
    }

    // Initialize output file handle
    const int64_t x = std::strtoll(argv[1], argv + argc, 10);
    const std::string outputFilepath = "ppiccg_" + std::to_string(x) + ".out.csv";
    const std::ofstream outputFile(outputFilepath);
    if (!outputFile.is_open())
    {
        std::cout << "Could not create output file (\"" << outputFilepath << "\").\n";
        return -1;
    }

    return 0;
}