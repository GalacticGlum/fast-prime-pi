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
#include <cmath>
#include <chrono>
#include <primecount.hpp>
#include <algorithm>

int main(const int argc, char** argv)
{
    if (argc < 2)
    {
        std::cout << "Missing required positional argument.\n";
        return -1;
    }

    // Initialize output file handle
    const uint64_t x = std::strtoull(argv[1], argv + argc, 10);
    const std::string outputFilepath = "ppiccg_" + std::to_string(x) + ".out.csv";
    
    std::ofstream outputFile(outputFilepath);
    if (!outputFile.is_open())
    {
        std::cout << "Could not create output file (\"" << outputFilepath << "\").\n";
        return -1;
    }

    // Set the buffer size to 64 kB
    const unsigned int bufferSize = 65536;
    char buffer[bufferSize];
    outputFile.rdbuf()->pubsetbuf(buffer, bufferSize);

    const std::chrono::steady_clock::time_point startTime = std::chrono::steady_clock::now();

    // Generate graph data on the domain [1, x].
    uint64_t sampleInterval = 1;
    uint64_t nextIntervalMark = 100;
    for (uint64_t n = 1; n <= x; n += sampleInterval)
    {
        // The density of the sample points decreases as x gets larger
        // for performance reasons. This is okay since precision becomes
        // less necessary for larger values of x.
        if (n > nextIntervalMark)
        {
            sampleInterval *= std::pow(10, std::max(1.0, std::log10(n) - 8));
            nextIntervalMark *= 10;
        }

        const int64_t pi = primecount::pi(n);
        const double ratio = pi * std::log(n) / n;
        outputFile << std::to_string(n) << "," << std::to_string(ratio) << "\n";
    }

    const std::chrono::steady_clock::time_point endTime = std::chrono::steady_clock::now();
    const double elapsed = std::lround(std::chrono::duration_cast<std::chrono::seconds>(endTime - startTime).count() * 100 + 0.5) / 100.0;
    std::cout << "Operation took " << elapsed << " seconds.\n";

    return 0;
}
