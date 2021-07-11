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
4.  You are developing a smartphone app. You have a list of potential customers for 
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
5. Most problems on CodeChef highlight chef's love for food and cooking but little is 
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
6. The most important part of a GSM network is so called Base Transceiver Station (BTS).
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
7. Little Elephant was fond of inventing new games. After a lot of research, Little 
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
<br />

```
8.  You might have heard about our new goodie distribution program aka the "Laddu Accrual 
System". This problem is designed to give you a glimpse of its rules. You can read the page 
once before attempting the problem if you wish, nonetheless we will be providing all the 
information needed here itself.

Laddu Accrual System is our new goodie distribution program. In this program, we will be 
distributing Laddus in place of goodies for your winnings and various other activities 
(described below), that you perform on our system. Once you collect enough number of 
Laddus, you can then redeem them to get yourself anything from a wide range of CodeChef 
goodies.

Let us know about various activities and amount of laddus you get corresponding to them.

    Contest Win (CodeChef’s Long, Cook-Off, LTIME, or any contest hosted with us) : 
        300 + Bonus (Bonus = 20 - contest rank). Note that if your rank is > 20, 
        then you won't get any bonus.
    Top Contributor on Discuss : 300
    Bug Finder : 50 - 1000 (depending on the bug severity). It may also fetch you a 
        CodeChef internship!
    Contest Hosting : 50

You can do a checkout for redeeming laddus once a month. The minimum laddus redeemable at 
Check Out are 200 for Indians and 400 for the rest of the world.

You are given history of various activities of a user. The user has not redeemed any of the 
its laddus accrued.. Now the user just wants to redeem as less amount of laddus he/she can, 
so that the laddus can last for as long as possible. Find out for how many maximum number 
of months he can redeem the laddus.

Input

    The first line of input contains a single integer T denoting number of test cases
    For each test case:
        First line contains an integer followed by a string denoting activities, origin 
        respectively, where activities denotes number of activities of the user, origin 
        denotes whether the user is Indian or the rest of the world. origin can be "INDIAN" 
        or "NON_INDIAN".
        
        For each of the next activities lines, each line contains an activity.
        An activity can be of four types as defined above.
            Contest Win : Input will be of form of CONTEST_WON rank, where rank denotes the 
            rank of the user.
            Top Contributor : Input will be of form of TOP_CONTRIBUTOR.
            Bug Finder : Input will be of form of BUG_FOUND severity, where severity 
            denotes the severity of the bug.
            Contest Hosting : Input will be of form of CONTEST_HOSTED.

Output

    For each test case, find out the maximum number of months for which the user can 
    redeem the laddus accrued. 

Constraints

    1 ≤ T, activities ≤ 100
    1 ≤ rank ≤ 5000
    50 ≤ severity ≤ 1000

Subtasks
    
    There is only a single subtask with 100 points.

Sample Input

    2
    4 INDIAN
    CONTEST_WON 1
    TOP_CONTRIBUTOR
    BUG_FOUND 100
    CONTEST_HOSTED
    4 NON_INDIAN
    CONTEST_WON 1
    TOP_CONTRIBUTOR
    BUG_FOUND 100
    CONTEST_HOSTED

Sample Output

    3
    1
```
<br />

```
9.  Consider a very long K-digit number N with digits d0, d1, ..., dK-1 (in decimal 
notation; d0 is the most significant and dK-1 the least significant digit). This number is 
so large that we can't give it to you on the input explicitly; instead, you are only given 
its starting digits and a way to construct the remainder of the number.

Specifically, you are given d0 and d1; for each i ≥ 2, di is the sum of all preceding (more 
significant) digits, modulo 10 — more formally, the following formula must hold: Determine if N is a multiple of 3.

Input

    The first line of the input contains a single integer T denoting the number of test 
    cases. The description of T test cases follows.
    The first and only line of each test case contains three space-separated integers K, 
    d0 and d1.

Output

    For each test case, print a single line containing the string "YES" (without quotes) 
    if the number N is a multiple of 3 or "NO" (without quotes) otherwise.

Constraints

    1 ≤ T ≤ 1000
    2 ≤ K ≤ 10^12
    1 ≤ d0 ≤ 9
    0 ≤ d1 ≤ 9

Sample Input

    3
    5 3 4
    13 8 1
    760399384224 5 1

Sample Output
    NO
    YES
    YES

Explanation

    Example case 1: The whole number N is 34748, which is not divisible by 3, 
    so the answer is NO.

    Example case 2: The whole number N is 8198624862486, which is divisible by 3, 
    so the answer is YES.
```