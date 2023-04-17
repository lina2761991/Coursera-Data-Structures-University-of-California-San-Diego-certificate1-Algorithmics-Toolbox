Coursera-Data-Structures-University-of-California-San-Diego-certificate1-Algorithmics-Toolbox
this is wht i did in the first certificate of data structure certification of University Of San Diego called "Algorithmic tool box"
				
# week 1 <br/>
## Stress Testing :<br/>
Stress testing generates random tests in an infinite loop and for each test, it launches your solution on this test and an alternative solution on the same test and compares the results<br/>
Stress testing is also known as Endurance Testing or Torture Testing.It is used to determine how an application or system behaves when under extreme levels of stress. This testing puts the system or application through scenarios designed to push it beyond its normal limits.<br/>
The aim is to find out how stable your product is by stretching it beyond its bandwidth capability. Stress testing evaluates how an application will behave beyond normal conditions and normal peak load.<br/>

### A stress test consists of:<br/>

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
	
## Notes<br/>
Stress testing can include various activities such as:

	* Overloading the system with lots of jobs
	* Removing system components
	* Checking the behaviour when the number of users suddenly increases (known as spike tests)
	* Checking the sustainability of a system over a period of time through a gradual increase in the number of users (known as soak tests)


How Do You Stress Test a Software?


	 • Plan your test: The first thing to do is plan the test out. At this point, you’ll be gathering the data to be used in the test and defining the goals you 		have for the test itself.
	 • Create automation scripts: Now you’re ready to create automation scripts to be used in the test. You’ll also want to create the test data ou will use in this scenario.
	 • Script execution: You should now have everything you need ready for the test, so you’ll be ready to execute that script. Run the script, and store the results you get from the test.
	 • Result analysis: You have the data, so now you’ll look at the test results. From this, you should be able to identify any bottlenecks in the system.
	 • Optimization: Now you’ve done your analysis, you’ll be able to make the necessary changes. That may be fine-tuning the system, changing configurations, or optimizing the code to meet your goals.
	 
	 
	 
 a bottleneck refers to a component that limits the potential of other hardware due to differences in the maximum capabilities of the two components.
	    
#### Tasks done in this part:<br/>
sum_of_two_digits and maximum_pairwise_product<br/>
# week 2<br/>
## Big O notation:<br/>
big-Θ is used when the running time is the same for all cases, big-O for the worst case running time, and big-Ω for the best case running time. 
keep in mind:v
  constant <log(6) n < log(2) n < n^0.5 < n < n log n < n^2 < n^2 log n < 2^n(this is called exponential) < n!<br/>
 if f grows slower than g, then f certainly grows no faster than g <br/>






the 3 most common algorithmic design technics are; greedy algorithms, divide and conquer and dynamic programming<br/>
## Tasks done in this part:
fibonacci_number<br/>
last_digit_of_fibonacci_number<br/>
greatest_common_diviser<br/>
least_common_mltiple<br/>
# week 3<br/>

## Greedy algorithm<br/>
A greedy algorithm, as the name suggests, always makes the choice that seems to be the best at that moment. This means that it makes a locally-optimal choice in the hope that this choice will lead to a globally-optimal solution.<br/>
Pros: simple, easy and run fast <br/>
Cons: doesn't provide global optimum solution<br/>
How do you decide which choice is optimal?<br/>
Assume that you have an objective function that needs to be optimized (either maximized or minimized) at a given point. A Greedy algorithm makes greedy choices at each step to ensure that the objective function is optimized. The Greedy algorithm has only one shot to compute the optimal solution so that it never goes back and reverses the decision.<br/>
### Greedy algorithms have some advantages and disadvantages:<br/>

	 1.It is quite easy to come up with a greedy algorithm (or even multiple greedy algorithms) for a problem.
	 2. Analysing the run time for greedy algorithms will generally be much easier than for other techniques (like Divide and conquer). For the Divide and conquer technique, it is not clear whether the technique is fast or slow. This is because at each level of recursion the size of gets smaller and the number of sub-problems increases.
	 3. The difficult part is that for greedy algorithms you have to work much harder to understand correctness issues.Even with the correct algorithm, it is hard to prove why it is correct. Proving that a greedy algorithm is correct is more of an art than a science. It involves a lot of creativity.
		
Example of greedy algorithm is:<br/>
knapsack problem(the spices problem)  – money change  – selection sort(with each iteration we select the minimum number and then swap it with the next number if it was smaller, its complexity is O(n²)) <br/>
### Notes:<br/>
Greedy means that the algorithm on each step selects some option which is locally the best. That is, it has no look-ahead.<br/> 
Greedy algorithms they cover as much as possible of the cases and solutions (that's why they r called greedy)<br/>
if we have something sorted, the greedy move can be faster after sorting (which what we did in the knapsack problem)<br/>
#### Python notes:<br/>
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. <br/>
   
   Example:

	fruits = ["apple","banana","cherry","kiwi","mango"]
	newlist = []

	for x in fruits:
	    if"a" in x:
		newlist.append(x)
	print(newlist) 

	A lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression.<br/>
	Example:<br/>
	lst.sort(key = lambda x: x[0]/x[1], reverse = True)<br/>
	

# week 4<br/>
## Divide and conquer algorithm<br/>
If you want to solve a problem using a divide-and-conquer strategy, you have to think about the following three steps: <br/>

	1. Breaking a problem into smaller sub-problems. (divide part)
	2. Solving each sub-problem recursively. (conquer part)
	3. Combining a solution to the original problem out of solutions to sub-problems. The first two steps are the “divide” part, whereas the last step is the 	   “conquer” part. We illustrate this approach with a number of problems of progressing difficulty and then proceed to the programming challenges. (merge part)
	
	
To use the divide and conquer algorithm, recursion is used. <br/>
The complexity of the divide and conquer algorithm is calculated using the master theorem<br/>
The master theorem is used in calculating the time complexity of recurrence relations (divide and conquer algorithms) in a simple and quick way. <br/>
T(n) = aT(n/b) + f(n),<br/>
where,<br/>
n = size of input<br/>
a = number of subproblems in the recursion<br/>
n/b = size of each subproblem. All subproblems are assumed to have the same size.<br/>
f(n) = cost of the work done outside the recursive call, which includes the cost of dividing the problem and the cost of merging the solutions<br/>
master theorem in a nutshell (it's part of the divide and conquer because it needs recursion)<br/>

selection sort doesn't depend on the input data, its quadratic o( n² )<br/>
merge sort is faster than selection sort, its speed is o(n log n );<br/>
 splitting is what does the log n cuz we keep splitting by 2 while n is the fact of merging and organizing <br/>
any comparison algorithm can be shown as a huge tree ( cuz we'll always make choices )<br/>
#### Binary search algorithm<br/>
##### the general steps:<br/>

	1.Initialize the start and end indices of the search range, such that the range includes the entire input array.
	2.While the start index is less than or equal to the end index, repeat the following steps:
 	a. Compute the middle index of the current range.
 	b. If the target element is equal to the middle element, return the middle index.
 	c. If the target element is less than the middle element, set the end index to be one less than the middle index.
 	d. If the target element is greater than the middle element, set the start index to be one more than the middle index.
	3.If the target element is not found in the array, return -1.
	
	
##### the algorithm:<br/>

	BinarySearch(K[0..n − 1],q)
	minIndex ← 0
	maxIndex ← n − 1
	while maxIndex ≥ minIndex:
		midIndex ← ⌊(minIndex + maxIndex)/2⌋
		if K[midIndex] = q:
			return midIndex
		else if K[midIndex] < q:
			minIndex ← midIndex + 1
		else:
			maxIndex ← midIndex − 1
		return −1
    
#### Quick sort algorithm<br/>
##### the general steps:<br/>

    1. Choose a pivot element from the array.
    2. Partition the array into two parts based on the pivot, with all elements smaller than the pivot on the left, and all elements larger on the right.
    3. Recursively apply QuickSort to the left and right sub-arrays.
    4. Merge the sorted sub-arrays to get the final sorted array.
    
There are different ways to choose a pivot element, such as selecting the first or last element in the array,i worked with selecting the last element 
##### python code of quick sort <br/><br/>


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
		
# week 5 + 6 <br/>

## Dynamic programming <br/>

Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for the same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of sub-problems so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial. <br/>
=>whenever there's recursion, we can do dynamic programming to reduce the time complexity and not calculate something twice <br/>
Tabulation and memoization are two techniques used in dynamic programming to optimize the execution of a function that has repeated and expensive computations. <br/>

### Memoization <br/>
#### Meaning : <br/>
The term “Memoization” comes from the Latin word “memorandum” (to remember), which is commonly shortened to “memo” in American English, and which means “to transform the results of a function into something to remember.”<br/>
#### What it does : <br/>
Memoization is a top-down approach where we cache the results of function calls and return the cached result if the function is called again with the same inputs. It is used when we can divide the problem into sub-problems and the sub-problems have overlapping sub-problems. <br/>
is well-suited for problems that have a relatively small set of inputs. <br/>

#### Fibonacci using memoization <br/> <br/>


	def fibonacci(n, cache={}):
		if n in cache:
			return cache[n]
		if n == 0:
			result = 0
		elif n == 1:
			result = 1
		else:
			result = fibonacci(n-1) + fibonacci(n-2)
		cache[n] = result
		return result
	
	
	
### Notes 
In the memoization implementation, we use a dictionary object called cache to store the results of function calls, and we use recursion to compute the results. <br/>

### Tabulation <br/>
#### what it does <br/>
Tabulation is a bottom-up approach where we store the results of the subproblems in a table and use these results to solve larger subproblems until we solve the entire problem. It is used when we can define the problem as a sequence of subproblems and the subproblems do not overlap. Tabulation is typically implemented using iteration and is well-suited for problems that have a large set of inputs.<br/> 

#### Fibonacci using tabulation <br/> <br/>


	def fibonacci(n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		else:
			table = [0] * (n + 1)
			table[0] = 0
			table[1] = 1
			for i in range(2, n+1):
				table[i] = table[i-1] + table[i-2]
			return table[n]


##### Notes
In the tabulation implementation, we use an array called table to store the results of subproblems, and we use iteration to compute the results. <br/>

==> Both implementations achieve the same result, but the approach used is different. Memoization is a top-down approach that uses recursion, while tabulation is a bottom-up approach that uses iteration. <br/>

great article that sums up the difference between memoization and tabulation <br/>
https://www.geeksforgeeks.org/tabulation-vs-memoization/?ref=rp<br/>
difference between dynamic programming and divide and conquer is that in dynamic programming the sub-problems overlap( they r in common at some point (repetition) but in divide and conquer they don’t overlap.+<br/>

# General Notes <br/>
the number of leaves in a tree must be at least n!<br/>
The worst case runing algorithm is at least the depth of d<br/>
l = 2^D , l is the number of leaves and D is the depth of the tree<br/>
merge sort algorithm uses sort and conquire  => o (n log n ) <br/>
quick sort algorithm is comparison based <br/>
runing time is O (n log n )<br/>
efficient in practice <br/>
when we have a recursive code at the end , we call it a tail recursion eliminator <br/>


What to do if your solution doesn’t work?<br/>

	1. Wrong answer
	2. Time/memory limit exceeded
	3. Failed (runtime error) 


the steps to follow :<br/>

	* verify that you didn't exceed the constraints 
	* Design some general test(s) for which you know the correct answer. Don’t look at your code’s answer for this test before you figure out what the answer should be with a pen and paper.
	* If you got a time limit exceeded error measures how long your program works for the larger inputs. The following functions help measure the CPU time since the start of the program
	
python time.clock() returns the floating-point value in seconds.<br/>

Measure the time for small tests, medium tests, and large tests. You may encounter one of the possible outcomes: <br/>
– Your program works for small and medium tests in time, but for larger tests, it is more than 10 times slower than needed (or just hangs for the large tests). In that case you probably have complexity issues. You may want to: <br/>
	∗ Measure the time parts of the program take separately (for example, how much time reading the input/printing the output take)<br/>
	∗ Compute the actual number of operations your algorithm and its parts do and see if it is as expected.<br/>
	∗ Check if you pass references to your functions (only applies to c++, in java and python is always referenced)<br/>

if __name__ == '__main__' in python meaning =>  It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module<br/>

#### the use of under score in python : <br/>

	* Python automatically stores the value of the last expression in the interpreter to a particular variable called "_." 
	* Underscore(_) is also used to ignore the values.  
	* ignoring a value a, _, b = (1, 2, 3) # a = 1, b = 3 
	* Use in Looping,You can use underscore(_) as a variabl<br/>e in looping.
	for _ in range(5): print(_) 
	* Single Pre Underscore is used for internal use. Most of us don't use it because of that reason.

#### single_postunderscore
	name_<br/>
	Sometimes if you want to use Python Keywords as a variable, function or class names, you can use this convention for that<br/>
	You can avoid conflicts with the Python Keywords by adding an underscore at the end of the name which you want to use.<br/>
	
#### the key differences between sys.stdin and input() are:<br/>
    • input() reads input until a newline character is encountered, while sys.stdin reads the entire input stream until the end-of-file or input signal is received.
    • input() returns input as a string, while sys.stdin returns the input as a string using the read() method.
