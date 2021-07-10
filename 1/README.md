# DSA: Complexity Analysis and Basics Warm up

```
1. Your program is to use the brute-force approach in order to find the Answer to 
Life, the Universe, and Everything. More precisely… rewrite small numbers from input 
to output. Stop processing input after reading in the number 42. All numbers at input
are integers of one or two digits.

Sample Input

    1
    2
    88
    42
    99

Sample Output

    1
    2
    88
```
<br />

```
2. Given an Integer N, write a program to reverse it.

Input

    The first line contains an integer T, total number of testcases. 
    Then follow T lines, each line contains an integer N.

Output

    For each test case, display the reverse of the given number N, in a new line.

Constraints

    1 ≤ T ≤ 1000
    1 ≤ N ≤ 1000000

Sample Input

    4
    12345
    31203
    2123
    2300

Sample Output

    54321
    30213
    3212
    32
```
<br />

```
3. Lapindrome is defined as a string which when split in the middle, gives two 
halves having the same characters and same frequency of each character. If there 
are odd number of characters in the string, we ignore the middle character and 
check for lapindrome. For example gaga is a lapindrome, since the two halves ga and 
ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a 
few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves 
contain the same characters but their frequencies do not match. Your task is simple. 
Given a string, you need to tell if it is a lapindrome.

Input

    First line of input contains a single integer T, the number of test cases.
    Each test is a single line containing a string S composed of only lowercase 
    English alphabet.

Output

    For each test case, output on a separate line: "YES" if the string is a 
    lapindrome and "NO" if it is not.

Constraints

    1 ≤ T ≤ 100
    2 ≤ |S| ≤ 1000, where |S| denotes the length of S

Sample Input

    6
    gaga
    abcde
    rotor
    xyzxy
    abbaab
    ababc


Sample Output

    YES
    NO
    YES
    YES
    NO
    NO
```
<br />

```
4. Given three distinct integers A, B and C, print the second largest number among them.

Input:

    The input consists of three lines.
    The first line contains a single integer A
    The second line contains a single integer B
    The third line contains a single integer C

Output:

    Print the second largest number among A, B and C, in a separate line.

Constraints

    1≤A,B,C≤10^9

Sample Input 1:

    2
    7
    21

Sample Output 1:

    7

Sample Input 2:

    14
    28
    16

Sample Output 2:

    16

EXPLANATION:

    In the first example, 7 is the second largest number among the given three numbers.
    In the second example, 16 is the second largest number among the given three numbers.
```
<br />

```
5. You're given two numbers L and R. Print all odd numbers between L and R (both inclusive) in 
a single line separated by space, in ascending (increasing) order.

Input:

    First-line will contain two numbers L and R

Output:

    Print all odd numbers in a single line separated by space, in ascending (increasing) order.

Constraints

    1≤L<R≤10^6

Sample Input 1:

    2 9

Sample Output 1:

    3 5 7 9

Sample Input 2:

    3 4

Sample Output 2:

    3

EXPLANATION:

    In the first example, odd numbers between 2 and 9 are 3,5,7,9
    In the second example, the only odd number in the range is 3
```
<br />

```
6. Raju is planning to visit his favourite restaurant. He shall travel to it by bus. Only the buses 
whose numbers are divisible by 5 or by 6 shall take him to his destination. You are given a bus number N. 
Find if Raju can take the bus or not. Print YES if he can take the bus, otherwise print NO.

Input:

    The first and only line of the input shall contain an integer N, denoting the bus number.

Output:

    Print YES if Raju can take that bus, else print NO.

Constraints

    1≤N≤10^6

Sample Input 1:

    60

Sample Output 1:

    YES

Sample Input 2:

    16

Sample Output 2:

    NO

Sample Input 3:

    20

Sample Output 3:

    YES

EXPLANATION:

    In the first example, 60 is divisible by 5 and 6 both, so he can take the bus.
    In the second example, 16 is divisible by neither 5 nor 6, so he can't take the bus.
    In the third example, 20 is divisible by 5, so he can take the bus.
```
<br />

```
7. You are given a list of N integers and you need to reverse it and print the reversed list in a new line.

Input:

    First-line will contain the number N
    Second line will contain N space-separated integers.

Output:

    Print the reversed list in a single line.

Constraints

    1≤N,Ai≤10^5

Sample Input 1:

    4
    1 3 2 4

Sample Output 1:

    4 2 3 1

Sample Input 2:

    2
    9 8

Sample Output 2:

    8 9

EXPLANATION:

    In the first example, the reverse of the [1,3,2,4] is [4,2,3,1]
    In the second example, the reverse of [9,8] is [8,9].
```
<br />

```
8. You are given a list of N integers and a value K. Print 1 if K exists 
in the given list of N integers, otherwise print −1

Input:

    First-line will contain two numbers N and K
    Next line contains N space-separated numbers.

Output:

    Print the answer in a new line.

Constraints

    1≤N,K,Ai≤10^5

Sample Input 1:

    4 2
    1 2 3 4

Sample Output 1:

    1

Sample Input 2:

    4 4
    1 2 6 9

Sample Output 2:

    -1

EXPLANATION:

    In the first example, as 2 is present in the list.
    In the second example, 4 is not present in the list.
```
<br />

```
9. You're given the length of three sides a, b, and c respectively. Now check 
if these three sides can form a triangle or not. Print "YES"(without quotes) if 
it can form a valid triangle with an area greater than 0, otherwise print "NO" 
(without quotes).

Input:

    First-line will contain three numbers a, b, and c separated by space.

Output:

    Print "YES"(without quotes) if these sides can form a valid triangle, 
    otherwise print "NO" (without quotes).

Constraints

    1≤a,b,c≤10^6

Sample Input 1:

    2 4 3

Sample Output 1:

    YES

Sample Input 2:

    1 1 4

Sample Output 2:

    NO

EXPLANATION:

    In the first example, (2, 4, 3) can form a triangle with an area greater than 0.
    In the second example, (1, 1, 4) will never form a valid triangle.
```