#!/usr/bin/env python3
import sys
import math

def borwein_function(x, n):
    if x == 0:
        return 1.0
    result = 1.0
    for k in range(n + 1):
        denominator = 2 * k + 1
        argument = x / denominator
        if argument == 0:
            term = 1.0
        else:
            term = math.sin(argument) / argument
        result *= term
    return result

def midpoint_rule(n, a, b, num_intervals):
    h = (b - a) / num_intervals
    total = 0.0
    for i in range(num_intervals):
        x_mid = a + (i + 0.5) * h
        total += borwein_function(x_mid, n)
    return total * h

def trapezoidal_rule(n, a, b, num_intervals):
    h = (b - a) / num_intervals
    total = 0.0
    total += borwein_function(a, n) / 2
    total += borwein_function(b, n) / 2
    for i in range(1, num_intervals):
        x = a + i * h
        total += borwein_function(x, n)
    
    return total * h

def simpson_rule(n, a, b, num_intervals):
    h = (b - a) / num_intervals
    total = 0.0
    total += borwein_function(a, n)
    total += borwein_function(b, n)
    for i in range(1, num_intervals):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * borwein_function(x, n)
        else:
            total += 4 * borwein_function(x, n)
    
    return total * h / 3

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("USAGE")
        print("    ./110borwein n")
        print()
        print("DESCRIPTION")
        print("    n constant defining the integral to be computed")
        return 0
    if len(sys.argv) != 2:
        print("Error: invalid number of arguments", file=sys.stderr)
        return 84
    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Error: n must be a positive integer", file=sys.stderr)
            return 84
    except ValueError:
        print("Error: n must be an integer", file=sys.stderr)
        return 84
    a = 0
    b = 5000
    num_intervals = 10000
    pi_over_2 = math.pi / 2
    midpoint_result = midpoint_rule(n, a, b, num_intervals)
    trapezoidal_result = trapezoidal_rule(n, a, b, num_intervals)
    simpson_result = simpson_rule(n, a, b, num_intervals)
    print("Midpoint:")
    print(f"I{n} = {midpoint_result:.10f}")
    print(f"diff = {abs(midpoint_result - pi_over_2):.10f}")
    print()
    print("Trapezoidal:")
    print(f"I{n} = {trapezoidal_result:.10f}")
    print(f"diff = {abs(trapezoidal_result - pi_over_2):.10f}")
    print()
    print("Simpson:")
    print(f"I{n} = {simpson_result:.10f}")
    print(f"diff = {abs(simpson_result - pi_over_2):.10f}")
    return 0
if __name__ == "__main__":
    sys.exit(main())