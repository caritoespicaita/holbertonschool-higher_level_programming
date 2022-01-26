0x09. Python - Everything is object
---
<iframe src="https://giphy.com/embed/wAjfQ9MLUfFjq" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/batman-look-whoa-wAjfQ9MLUfFjq">via GIPHY</a></p>
---
Learning Objectives
---
- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions
---
Tasks
---
0-answer.txt: What function would you use to print the type of an object?.

1-answer.txt: How do you get the variable identifier (which is the memory address in the CPython implementation)?.

2-answer.txt: Do a and b point to the same object? >>> a = 89.

3-answer.txt Do a and b point to the same object? >>> a = 89 >>> b = 89.

4-answer.txt Do a and b point to the same object? >>> a = 89 >>> b = a".

5-answer.txt: Do a and b point to the same object? >>> a = 89 >>> b = a + 1.

6-answer.txt: What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = s1 >>> print(s1 == s2).

7-answer.txt: What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = s1 >>> print(s1 is s2).

8-answer.txt: What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = "Holberton" >>> print(s1 is s2).

9-answer.txt: What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = "Holberton" >>> print(s1 is s2).

10-answer.txt: What do these 3 lines print >>> l1 = [1, 2, 3] >>> l2 = [1, 2, 3] >>> print(l1 == l2).

11-answer.txt: What do these 3 lines print >>> l1 = [1, 2, 3] >>> l2 = [1, 2, 3] >>> print(l1 is l2).

12-answer.txt: What do these 3 lines print >>> l1 = [1, 2, 3] >>> l2 = l1 >>> print(l1 == l2).

13-answer.txt: What do these 3 lines print >>> l1 = [1, 2, 3] >>> l2 = l1 >>> print(l1 is l2).

14-answer.txt: What does this script print? l1 = [1, 2, 3], l2 = l1, l1.append(4), print(l2).

15-answer.txt:. What does this script print? l1 = [1, 2, 3], l2 = l1, l1 = l1 + [4], print(l2).

16-answer.txt: What does this script print?; def increment(n):, n += 1; a = 1, increment(a), print(a).

17-answer.txt: What does this script print?; def increment(n):, n.append(4); l = [1, 2, 3], increment(l), print(l).

18-answer.txt: What does this script print?; def assign_value(n, v):, n = v; l1 = [1, 2, 3], l2 = [4, 5, 6], assign_value(l1, l2), assign_value(l1, l2).

19-copy_list.py: Function def copy_list(l): that returns a copy of a list.

20-answer.txt: Is a a tuple? a = ().

21-answer.txt: Is a a tuple? a = (1, 2).

22-answer.txt: Is a a tuple? a = (1).

23-answer.txt: Is a a tuple? a = (1,).

24-answer.txt: What does this script print?; a = (1), b = (1), a is b.

25-answer.txt: What does this script print?; a = (1, 2), b = (1, 2), a is b.

26-answer.txt:.What does this script print?; a = (), b = (), a is b.

27-answer.txt: Will the last line of this script print 139926795932424? >>> a = [1, 2, 3, 4] >>> id(a), 139926795932424 >>> a = a + [5] >>> id(a).

28-answer.txt: Will the last line of this script print 139926795932424? >>> a = [1, 2, 3] >>> id(a), 139926795932424 >>> a += [4] >>> id(a).