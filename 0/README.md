# DSA: Easy Problems to Get Started

```
1. Chef went to a shop and buys a pens and b pencils. Each pen costs x units and each 
pencil costs y units. Now find what is the total amount Chef will spend to buy 
a pens and b pencils.

Input:

    First-line will contain 4 space separated integers a, b, x and y respectively.

Output:

    Print the answer in a new line.

Constraints

    1≤a,b,x,y≤10^3

Sample Input 1:

    2 4 4 5

Sample Output 1:

    28

Sample Input 2:

    1 1 4 8

Sample Output 2:

    12

EXPLANATION:

    In the first example, total cost is (2 * 4 + 4 * 5) = 28.
    In the second example, total cost is (1 * 4 + 1 * 8) = 12.
```
<br />

```
2. You're given a number N. If N is divisible by 5 or 11 but not both then print "ONE"(without quotes). If N is divisible by both 
5 and 11 then print "BOTH"(without quotes). If N is not divisible by 5 or 11 then print "NONE"(without quotes).

Input:

    First-line will contain the number N

Output:

    Print the answer in a newline.

Constraints

    1≤N≤10^3

Sample Input 1:

    50

Sample Output 1:

    ONE

Sample Input 2:

    110

Sample Output 2:

    BOTH

Sample Input 2:

    16

Sample Output 2:

    NONE

EXPLANATION:

    In the first example, 50 is divisible by 5, but not 11.
    In the second example, 110 is divisible by both 5 and 11.
    In the third example, 16 is not divisible by 5 or 11.
```
<br />

```
3. You are given a number N and find all the distinct factors of N

Input:

    First-line will contain the number N

Output:

    In the first line print number of distinct factors of N
    In the second line print all distinct factors in ascending order separated by space.

Constraints

    1≤N≤10^6

Sample Input 1:

    4

Sample Output 1:

    3
    1 2 4

Sample Input 2:

    6

Sample Output 2:

    4
    1 2 3 6

EXPLANATION:

    In the first example, all factors of 4 are 1, 2, 4.
    In the second example, all factors of 6 are 1, 2, 3, 6.
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
<br />

```
10. You're given a number N. Print the first N lines of the below-given pattern.

    *
   **
  ***
 ****
*****

Input:

    First-line will contain the number N

Output:

    Print the first N lines of the given pattern.
    
Constraints

    1≤N≤200

Sample Input 1:

    4

Sample Output 1:

       *
      **
     ***
    ****

Sample Input 2:

    2

Sample Output 2:

     *
    **

EXPLANATION:

    In the first example, we'll print the first 4 lines of the given pattern.
    In the second example, we'll print the first 2 lines of the given pattern
```
<br />

```
11. You are given a number N. Find the sum of all numbers from 1 to N

Input:

    First-line will contain the number N

Output:

    Print the answer in a single line.

Constraints

    1≤N≤10^9

Sample Input 1:

    4

Sample Output 1:

    10

Sample Input 2:

    8

Sample Output 2:

    36

EXPLANATION:

    In the first example, (1 + 2 + 3 + 4) = 10.
    In the second example, (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8) = 36.
```
<br />

```
12. You are given a number N and find the sum of the first N odd and even 
numbers in a line separated by space. All even and odd numbers should be 
greater than 0

Input:

    First-line will contain the number N

Output:

    Print the sum of the first N odd and even numbers in a 
    line separated by space.

Constraints

    1≤N≤10^6

Sample Input 1:

    4

Sample Output 1:

    16 20

Sample Input 2:

    1

Sample Output 2:

    1 2

EXPLANATION:

    In the first example, (1 + 3 + 5 + 7) = 16 and (2 + 4 + 6 + 8) = 20.
    In the second example, only one odd that is 1 and only one even that is 2.
```
<br />

```
13. You're given the three angles a, b, and c respectively. Now check if these three 
angles can form a valid triangle with an area greater than 0 or not. Print "YES"
(without quotes) if it can form a valid triangle with an area greater than 0, otherwise print "NO" (without quotes).

Input:

    First-line will contain three numbers a, b, and c separated by space.

Output:

    Print "YES"(without quotes) if these sides can form a valid triangle, 
    otherwise print "NO" (without quotes).

Constraints

    0≤a,b,c≤180

Sample Input 1:

    20 40 120

Sample Output 1:

    YES

Sample Input 2:

    100 18 42

Sample Output 2:

    NO

EXPLANATION:

    In the first example, angles set (20, 40, 120) can form a triangle with 
    an area greater than 0.
    In the second example, angles set (100, 18, 42) will never form a valid triangle.
```
<br />

```
14. You're given the length of three sides a, b, and c respectively. Now If these 
three sides can form an Equilateral Triangle then print 1, if these three sides can 
form an Isosceles Triangle then print 2, if these three sides can form a Scalene 
Triangle then print 3, otherwise print −1

Input:

    First-line will contain three numbers a, b, and c separated by space.

Output:

    Print the answer in a new line.

Constraints

    1≤a,b,c≤10^3

Sample Input 1:

    2 4 3

Sample Output 1:

    3

Sample Input 2:

    4 4 4

Sample Output 2:

    1

Sample Input 3:

    4 4 9

Sample Output 3:

    -1

EXPLANATION:

    In the first example, (2, 4, 3) will form a Scalene Triangle.
    In the second example, (4, 4, 4) will form an Equilateral Triangle.
    In the third example, (4, 4, 9) will not form a triangle.
```
<br />

```
15. You're given a number N. Print the first N lines of the below-given pattern.

    1 2 3 4 5
    10 9 8 7 6
    11 12 13 14 15
    20 19 18 17 16
    21 22 23 24 25
    30 29 28 27 26

Input:

    First-line will contain the number N

Output:

    Print the first N lines of the given pattern.

Constraints

    1≤N≤200

Sample Input 1:

    4

Sample Output 1:

    1 2 3 4 5
    10 9 8 7 6
    11 12 13 14 15
    20 19 18 17 16

Sample Input 2:

    2

Sample Output 2:

    1 2 3 4 5
    10 9 8 7 6

EXPLANATION:

    In the first example, we'll print the first 4 lines of the given pattern.
    In the second example, we'll print the first 2 lines of the given pattern.
```