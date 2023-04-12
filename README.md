# Coursera-Data-Structures-University-of-California-San-Diego-certificate1-Algorithmics-Toolbox
this is wht i did in the first certificate of data structure certification of University Of San Diego called "Algorithmic tool box"
					algorithmic toolbox 
**********************************week 1****************************
Stress Testing :
Stress testing generates random tests in an infinite loop and for each test, it launches your solution on this test and an alternative solution on the same test and compares the results
Stress testing is also known as Endurance Testing or Torture Testing.It is used to determine how an application or system behaves when under extreme levels of stress. This testing puts the system or application through scenarios designed to push it beyond its normal limits.
The aim is to find out how stable your product is by stretching it beyond its bandwidth capability. Stress testing evaluates how an application will behave beyond normal conditions and normal peak load.
A stress test consists of:
1. Your implementation of an algorithm. 
2. An alternative, trivial and slow, but correct implementation of an algorithm for the same problem.
3. A random test generator.
An example of stress testing:
calculating the max product of a list of numbers 
the steps we did:
1. do a while loop on both solutions 
2. give 2 solutions ; first one is simple (first reflection you had) and the second one is optimum
3. compare 2 results and display ok if they r equal, otherwise display both if they r different and break the while loop
4. once you face 2 different results, you visually determine the wrong output
5. you display the inputs that led to this result (debug)
6. correct the bug and run the test again 
7. once everything is fixed, you comment out the slow (first reflection) solution and you stick with the optimum solution, then you submit it
Notes
Stress testing can include various activities such as:
* Overloading the system with lots of jobs
* Removing system components
* Checking the behaviour when the number of users suddenly increases (known as spike tests)
* Checking the sustainability of a system over a period of time through a gradual increase in the number of users (known as soak tests)

How Do You Stress Test a Software?
    • Plan your test: The first thing to do is plan the test out. At this point, you’ll be gathering the data to be used in the test and defining the goals you have for the test itself.
    • Create automation scripts: Now you’re ready to create automation scripts to be used in the test. You’ll also want to create the test data ou will use in this scenario.
    • Script execution: You should now have everything you need ready for the test, so you’ll be ready to execute that script. Run the script, and store the results you get from the test.
    • Result analysis: You have the data, so now you’ll look at the test results. From this, you should be able to identify any bottlenecks in the system.
    • Optimization: Now you’ve done your analysis, you’ll be able to make the necessary changes. That may be fine-tuning the system, changing configurations, or optimizing the code to meet your goals.
a bottleneck refers to a component that limits the potential of other hardware due to differences in the maximum capabilities of the two components.
Tasks done in this part:
sum_of_two_digits and maximum_pairwise_product
**********************************week 2*****************************
Big O notation:
big-Θ is used when the running time is the same for all cases, big-O for the worst case running time, and big-Ω for the best case running time. 
keep in mind:
  constant <log(6) n < log(2) n < n^0.5 < n < n log n < n^2 < n^2 log n < 2^n(this is called exponential) < n!
 if f grows slower than g, then f certainly grows no faster than g 






the 3 most common algorithmic design technics are; greedy algorithms, divide and conquer and dynamic programming
Tasks done in this part:
fibonacci_number
last_digit_of_fibonacci_number
greatest_common_diviser
least_common_mltiple
**********************************week 3**************************
					greedy algorithm 

What is a 'Greedy algorithm'?
A greedy algorithm, as the name suggests, always makes the choice that seems to be the best at that moment. This means that it makes a locally-optimal choice in the hope that this choice will lead to a globally-optimal solution.
Pros: simple, easy and run fast 
Cons: doesn't provide global optimum solution
How do you decide which choice is optimal?
Assume that you have an objective function that needs to be optimized (either maximized or minimized) at a given point. A Greedy algorithm makes greedy choices at each step to ensure that the objective function is optimized. The Greedy algorithm has only one shot to compute the optimal solution so that it never goes back and reverses the decision.
Greedy algorithms have some advantages and disadvantages:
 1.	  It is quite easy to come up with a greedy algorithm (or even multiple greedy algorithms) for a problem.
 2.	  Analysing the run time for greedy algorithms will generally be much easier than for other techniques (like Divide and conquer). For the Divide and conquer technique, it is not clear whether the technique is fast or slow. This is because at each level of recursion the size of gets smaller and the number of sub-problems increases.
 3.	  The difficult part is that for greedy algorithms you have to work much harder to understand correctness issues. 
Even with the correct algorithm, it is hard to prove why it is correct. Proving that a greedy algorithm is correct is more of an art than a science. It involves a lot of creativity.
Example of greedy algorithm is:
knapsack problem(the spices problem)  – money change  – selection sort(with each iteration we select the minimum number and then swap it with the next number if it was smaller, its complexity is O(n²)) 
Notes:
Greedy means that the algorithm on each step selects some option which is locally the best. That is, it has no look-ahead. 
Greedy algorithms they cover as much as possible of the cases and solutions (that's why they r called greedy)
if we have something sorted, the greedy move can be faster after sorting (which what we did in the knapsack problem)
Python notes:
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. 
Example:
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if"a" in x:
        newlist.append(x)

print(newlist) 
A lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression.
Example:
lst.sort(key = lambda x: x[0]/x[1], reverse = True)

************************************week 4**************************
				divide and conquer algorithm
If you want to solve a problem using a divide-and-conquer strategy, you have to think about the following three steps: 
1. Breaking a problem into smaller sub-problems. (divide part)
2. Solving each sub-problem recursively. (conquer part) 
3. Combining a solution to the original problem out of solutions to sub-problems. The first two steps are the “divide” part, whereas the last step is the “conquer” part. We illustrate this approach with a number of problems of progressing difficulty and then proceed to the programming challenges. (merge part)
To use the divide and conquer algorithm, recursion is used. 
The complexity of the divide and conquer algorithm is calculated using the master theorem
The master theorem is used in calculating the time complexity of recurrence relations (divide and conquer algorithms) in a simple and quick way. 
T(n) = aT(n/b) + f(n),
where,
n = size of input
a = number of subproblems in the recursion
n/b = size of each subproblem. All subproblems are assumed to have the same size.
f(n) = cost of the work done outside the recursive call, which includes the cost of dividing the problem and the cost of merging the solutions
master theorem in a nutshell (it's part of the divide and conquer because it needs recursion)

selection sort doesn't depend on the input data, its quadratic o( n² )
merge sort is faster than selection sort, its speed is o(n log n );
 splitting is what does the log n cuz we keep splitting by 2 while n is the fact of merging and organizing 
any comparison algorithm can be shown as a huge tree ( cuz we'll always make choices )
quick sort algorithm
the general steps:
    1. Choose a pivot element from the array.
    2. Partition the array into two parts based on the pivot, with all elements smaller than the pivot on the left, and all elements larger on the right.
    3. Recursively apply QuickSort to the left and right sub-arrays.
    4. Merge the sorted sub-arrays to get the final sorted array.
There are different ways to choose a pivot element, such as selecting the first or last element in the array,i worked with selecting the last element 
python code of quick sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = []
        right = []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
************************************week 5***************************

				dynamic programming 

Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for the same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of sub-problems so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial. 
* In this part I did a quizz , about number of paths in which I used the Blaise Pascal triangle( each number is sthe sum of numbers above it )
=>whenever theres recursion, we can do dynamic programming to reduce the time complexity and not calculate smthg twice 


//////////////////////////////////////////////////////////////////////////////////////////////////////////////
Notes ;

the number of leaves in a tree must be at least n!
The worst case runing algorithm is at least the depth of d
l = 2^D , l is the number of leaves and D is the depth of the tree
merge sort algorithm uses sort and conquire  => o (n log n ) 
quick sort algorithm is comparison based 
runing time is O (n log n )
efficient in practice 
when we have a recursive code at the end , we call it a tail recursion eliminator 

Notes
What to do if your solution doesn’t work?
1. Wrong answer
2. Time/memory limit exceeded
3. Failed (runtime error) 


the steps to follow :
*verify that you didn't exceed the constraints 
*Design some general test(s) for which you know the correct answer. Don’t look at your
code’s answer for this test before you figure out what the answer should be with a pen
and paper.
*If you got a time limit exceeded error measures how long your program works for the
larger inputs. The following functions help measure the CPU time since the start of
the program
python time.clock() returns the floating-point value in seconds.

Measure the time for small tests, medium tests, and large tests. You may encounter one of
the possible outcomes:
– Your program works for small and medium tests in time, but for larger tests, it is
more than 10 times slower than needed (or just hangs for the large tests). In that
case you probably have complexity issues. You may want to:
∗ Measure the time parts of the program take separately (for example, how
much time reading the input/printing the output take)
∗ Compute the actual number of operations your algorithm and its parts do and
see if it is as expected.
∗ Check if you pass references to your functions (only applies to c++, in java
and python is always referenced)
NOTES: 
if __name__ == '__main__' in python meaning =>  It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module

Notes :
lambda function in python  its an anonymous function  can take any number of arguments but can have only one expression
lambda function is when an anonymous function is required for a short period of time
the use of under score in python :
* Python automatically stores the value of the last expression in the interpreter to a particular variable called "_."
*Underscore(_) is also used to ignore the values. 
## ignoring a value a, _, b = (1, 2, 3) # a = 1, b = 3 
*Use in Looping,You can use underscore(_) as a variable in looping.
for _ in range(5): print(_) 
*Single Pre Underscore is used for internal use. Most of us don't use it because of that reason. 


*single_postunderscore
name_
Sometimes if you want to use Python Keywords as a variable, function or class names, you can use this convention for that.
You can avoid conflicts with the Python Keywords by adding an underscore at the end of the name which you want to use.
* difference between input and sys.stdin 
he key differences between sys.stdin and input() are:
    • input() reads input until a newline character is encountered, while sys.stdin reads the entire input stream until the end-of-file or input signal is received.
    • input() returns input as a string, while sys.stdin returns the input as a string using the read() method.
