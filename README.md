# Codechef: Data Structures and Algorithms - Warm up and Complexity Analysis

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
2. You're given a number N. If N is divisible by 5 or 11 but not both then print 
"ONE"(without quotes). If N is divisible by both 5 and 11 then print "BOTH"(without 
quotes). If N is not divisible by 5 or 11 then print "NONE"(without quotes).

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
6. Raju is planning to visit his favourite restaurant. He shall travel to it by bus. Only 
the buses whose numbers are divisible by 5 or by 6 shall take him to his destination. You 
are given a bus number N. Find if Raju can take the bus or not. Print YES if he can take 
the bus, otherwise print NO.

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
(without quotes) if it can form a valid triangle with an area greater than 0, 
otherwise print "NO" (without quotes).

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
<br />

```
16. Your program is to use the brute-force approach in order to find the Answer to 
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
17. Given an Integer N, write a program to reverse it.

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
18. Lapindrome is defined as a string which when split in the middle, gives two 
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
19.  You are developing a smartphone app. You have a list of potential customers for 
your app. Each customer has a budget and will buy the app at your declared price if 
and only if the price is less than or equal to the customer's budget. You want to fix 
a price so that the revenue you earn from the app is maximized. Find this maximum 
possible revenue. For instance, suppose you have 4 potential customers and their 
budgets are 30, 20, 53 and 14. In this case, the maximum revenue you can get is 60.

Input

    Line 1: N, the total number of potential customers.
    Lines 2 to N+1: Each line has the budget of a potential customer.

Output

    The output consists of a single integer, the maximum possible revenue you 
    can earn from selling your app.

Sample Input 1

    4
    30
    20
    53
    14

Sample Output 1

    60

Sample Input 2

    5
    40
    3
    65
    33
    21

Sample Output 2

    99


Test data

    Each customers' budget is between 1 and 10^8, inclusive.
    Subtask 1 (30 marks) : 1 ≤ N ≤ 5000.
    Subtask 2 (70 marks) : 1 ≤ N ≤ 5×10^5.

Live evaluation data

    There are 15 test inputs on the server during the exam. The grouping into 
    subtasks is as follows.

    • Subtask 1: Test inputs 0,…,5
    • Subtask 2: Test inputs 6,…,14


Note

    The answer might not fit in a variable of type int. We recommend that you use 
    variables of type long long to read the input and compute the answer. If you use 
    printf and scanf, you can use %lld for long long. 
```
<br />

```
20. Most problems on CodeChef highlight chef's love for food and cooking but little is 
known about his love for racing sports. He is an avid Formula 1 fan. He went to watch 
this year's Indian Grand Prix at New Delhi. He noticed that one segment of the circuit 
was a long straight road. It was impossible for a car to overtake other cars on this segment. Therefore, a car had to lower down its speed if there was a slower car in front 
of it. While watching the race, Chef started to wonder how many cars were moving at 
their maximum speed.

Formally, you're given the maximum speed of N cars in the order they entered the 
long straight segment of the circuit. Each car prefers to move at its maximum speed. 
If that's not possible because of the front car being slow, it might have to lower its 
speed. It still moves at the fastest possible speed while avoiding any collisions. For 
the purpose of this problem, you can assume that the straight segment is infinitely long.

Count the number of cars which were moving at their maximum speed on the straight segment.

Input

    The first line of the input contains a single integer T denoting the number of test cases to follow. Description of each test case contains 2 lines. The first of these lines contain a single integer N, the number of cars. The second line contains N space separated integers, denoting the maximum speed of the cars in the order they entered the long straight segment.

Output

    For each test case, output a single line containing the number of cars which were moving at their maximum speed on the segment.

Sample Input

    3
    1
    10
    3
    8 3 6
    5
    4 5 1 2 3

Output

    1
    2
    2

Constraints

    1 ≤ T ≤ 100
    1 ≤ N ≤ 10,000
    
All speeds are distinct positive integers that fit in a 32 bit signed integer.
Each input file will not be larger than 4 MB (4,000,000,000 bytes) in size. 
```
<br />

```
21. The most important part of a GSM network is so called Base Transceiver Station (BTS).
These transceivers form the areas called cells (this term gave the name to the cellular 
phone) and every phone connects to the BTS with the strongest signal (in a little 
simplified view). Of course, BTSes need some attention and technicians need to check their 
function periodically.

The technicians faced a very interesting problem recently. Given a set of BTSes to visit, 
they needed to find the shortest path to visit all of the given points and return back to 
the central company building. Programmers have spent several months studying this problem 
but with no results. They were unable to find the solution fast enough. After a long time, 
one of the programmers found this problem in a conference article. Unfortunately, he found 
that the problem is so called "Traveling Salesman Problem" and it is very hard to solve. If 
we have N BTSes to be visited, we can visit them in any order, giving us N! possibilities 
to examine. The function expressing that number is called factorial and can be computed as 
a product:

1.2.3.4....N
The number is very high even for a relatively small N

The programmers understood they had no chance to solve the problem. But because they have 
already received the research grant from the government, they needed to continue with their 
studies and produce at least some results. So they started to study behaviour of the 
factorial function.

For example, they defined the function Z. For any positive integer N, Z(N) is the number of 
zeros at the end of the decimal form of number N!. They noticed that this function never 
decreases. If we have two numbers N1<N2 then Z(N1)≤Z(N2). It is because we can never "lose" 
any trailing zero by multiplying by any positive number. We can only get new and new zeros. 
The function Z is very interesting, so we need a computer program that can determine its 
value efficiently.

Input

    There is a single positive integer T on the first line of input (equal to about 
    100000). It stands for the number of numbers to follow. Then there are T lines, 
    each containing exactly one positive integer number N, 1≤N≤10^9.

Output

    For every number N, output a single line containing the single 
    non-negative integer Z(N)

Sample Input

    6
    3
    60
    100
    1024
    23456
    8735373

Sample Output

    0
    14
    24
    253
    5861
    2183837
```
<br />

```
22. Little Elephant was fond of inventing new games. After a lot of research, Little 
Elephant came to know that most of the animals in the forest were showing less interest to 
play the multi-player games. Little Elephant had started to invent single player games, and 
succeeded in inventing the new single player game named COIN FLIP.

In this game the player will use N coins numbered from 1 to N, and all the coins will be 
facing in "Same direction" (Either Head or Tail), which will be decided by the player 
before starting of the game.

The player needs to play N rounds. In the k-th round the player will flip the face of the 
all coins whose number is less than or equal to k. That is, the face of coin i will be 
reversed, from Head to Tail, or, from Tail to Head, for i≤k.

Elephant needs to guess the total number of coins showing a particular face after playing 
N rounds. Elephant really becomes quite fond of this game COIN FLIP so Elephant plays 
G times. Please help the Elephant to find out the answer.

Input

    The first line of input contains an integer T, denoting the number of test cases. 
    Then T test cases follow.

    The first line of each test contains an integer G, denoting the number of games played 
    by Elephant. Each of the following G lines denotes a single game, and contains 3 
    space-separated integers I, N, Q, where I denotes the initial state of the coins, 
    N denotes the number of coins and rounds, and Q, which is either 1, or 2 as 
    explained below.

    Here I=1 means all coins are showing Head in the start of the game, and I=2 means all 
    coins are showing Tail in the start of the game. Q=1 means Elephant needs to guess the 
    total number of coins showing Head in the end of the game, and Q=2 means Elephant needs 
    to guess the total number of coins showing Tail in the end of the game.

Output

    For each game, output one integer denoting the total number of coins showing the 
    particular face in the end of the game.

Constraints

    1≤T≤10
    1≤G≤2000
    1≤N≤10
    1≤I≤2
    1≤Q≤2

Sample Input

    1
    2
    1 5 1
    1 5 2

Sample Output

    2
    3

Explanation

    In the 1st game in Example, I=1, so initial arrangement of coins are H H H H H, and now 
    Elephant will play 5 rounds and coin faces will be changed as follows< After the 1st 
    Round: T H H H H After the 2nd Round: H T H H H After the 3rd Round: T H T H H After 
    the 4th Round: H T H T H After the 5th Round: T H T H T Finally Q=1, so we need to find 
    the total number of coins showing Head, which is 2

    In the 2nd game in Example: This is similar to the 1st game, except Elephant needs to 
    find the total number of coins showing Tail. So the Answer is 3. (Please see the final 
    state of the coins in the 1st game)
```