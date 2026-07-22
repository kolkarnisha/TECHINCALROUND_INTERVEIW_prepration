# 𝗛𝗮𝗻𝗱𝘀-𝗼𝗻 𝗿𝗲𝗮𝗹𝘁𝗶𝗺𝗲𝗹𝗼𝗼 𝗰𝗵𝘂𝘀𝗲𝗲 𝗽𝗿𝗼𝗯𝗹𝗲𝗺𝗲𝘀 𝗮𝗻𝗱 𝗱𝗼𝘄𝗻 𝗮𝗿𝗲 𝘀𝗶𝗺𝗽𝗹𝗲

1. Grade calculator (10 min)
# if, elif
Write a function get_grade(marks) that takes a score and returns:
A+ if marks >= 90, A if >= 80, B if >= 70, C if >= 60, D if >= 50, F otherwise.
Test with: 95, 82, 71, 55, 45. Print the grade for each
# Expected: 95 → A+ | 82 → A | 71 → B | 55 → D | 45 → F
HINT: if/elif chain. Strictest condition first (>= 90). The else catches everything below 50

2. Internship eligibility filter [10 min] - and, or, not, in
A company offers internships with these rules:
(a) CGPA >= 7.0 AND no active backlogs, OR
(b) CGPA >= 6.5 AND has at least 3 GitHub projects
Also: "CSE" or "IT" branch students get priority.
Write is_eligible(cgpa, backlogs, projects, branch) and test with 4 different profiles

Expected: (7.5, 0, 1, CSE) → True | (6.8, 1, 4, MECH) → True | (6.2, 0, 1, IT) → False
HINT: Combine (a) and (b) with 'or'. Use 'in' to check branch against a set. Use 'not' for backlog check.

3. Student profile validator[25 min] - truthy, in, ternary, nested
# Write validate_profile(student) that checks a student dict and returns a list of issues:
- Name must be a non-empty string (truthiness check)
- CGPA must be between 0.0 and 10.0 (comparison)
- Skills must be a non-empty set (truthiness)
- Email must contain '@' and '.' (in + and)
- GitHub projects must be 0 or more (comparison)
If no issues, print "Profile complete". Otherwise print each issue

Expected: Missing name, invalid CGPA, and missing '@' in email each produce a separate issue string.

HINT: Build an empty issues list. Use 'if not name:' for truthiness. Append strings to issues. At the end, 'if issues:' print them, 'else:' print success

4. Full company screener [open, if, elif, and, or, not, in, ternary, truthy, nested]
Build a CLI that:
1. Takes student profile as input (name, cgpa, backlogs, attendance, skills)
2. Screens against all 4 companies in the project database
3. For each company: print PASS/FAIL for each criterion using ternary labels (✓/✗)
4. At the end, print how many companies they're eligible for
5. If eligible for none, print specific advice on what to improve (which CGPA to reach, which skills to add)
Bonus: add a 5th company of your own with custom criteria.

Expected: Open-ended — evaluate on correct logic, readable output, and meaningful advice for the not-eligible case
Hide hint: Nested if for the screening stages. List comprehension to count eligible companies. Truthiness to check if skills set is non-empty. Ternary for ✓/✗ labels

### 𝗣𝘆𝘁𝗵𝗼𝗻 𝗟𝗼𝗼𝗽𝘀 + 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝘀 𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗲 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻𝘀
## 𝗟𝗲𝘃𝗲𝗹 𝟭: 𝗕𝗮𝘀𝗶𝗰 𝗟𝗼𝗼𝗽 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻𝘀
# 1. Print numbers from 1 to 10
Output:
1
2
3
...
10

# 2. Print numbers from 10 to 1
Output:
10
9
8
...
1

# 3. Print all even numbers from 1 to 100
Output:
2
4
6
...
100

# 4. Print all odd numbers from 1 to 100
Output:
1
3
5
...
99

# 5. Find sum of numbers from 1 to 100
Output: 5050

# 𝗟𝗲𝘃𝗲𝗹 𝟮: 𝗟𝗼𝗼𝗽𝘀 + 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝘀
6. Print numbers divisible by 5 between 1 and 100
Output:
5
10
15
...
100

7. Print numbers divisible by both 3 and 5
Output:
15
30
45
...
8. Count how many even numbers exist from 1 to 100
Expected: 50

9. Count how many odd numbers exist from 1 to 100
Expected: 50
10. Print squares of numbers from 1 to 20
Output:
1
4
9
16
...
400

## 𝗟𝗲𝘃𝗲𝗹 𝟯: 𝗨𝘀𝗲𝗿 𝗜𝗻𝗽𝘂𝘁 + 𝗟𝗼𝗼𝗽𝘀
# 11. Print multiplication table of a number
Input: 5
Output:
5 x 1 = 5
5 x 2 = 10
...

# 12. Find factorial of a number
Input: 5
Output: 120

# 13. Count digits in a number
Input: 12345
Output: 5

# 14. Find sum of digits
Input: 1234
Output: 10

# 15. Reverse a number
Input: 1234
Output: 4321

## 𝗟𝗲𝘃𝗲𝗹 𝟰: 𝗟𝗼𝗼𝗽 + 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝘀 + 𝗟𝗼𝗴𝗶𝗰
# 16. Check whether a number is Prime
Input: 13
Output: Prime

# 17. Print all Prime numbers from 1 to 100
Output:
2
3
5
7
11
...
97

# 18. Check Armstrong Number
Input: 153
Output: Armstrong

# 19. Check Palindrome Number
Input: 121
Output: Palindrome

# 20. Print Fibonacci Series
Input: 10
Output: 0 1 1 2 3 5 8 13 21 34

# 𝗟𝗲𝘃𝗲𝗹 𝟱: 𝗟𝗶𝘀𝘁𝘀 + 𝗟𝗼𝗼𝗽𝘀 + 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝘀
21. Find largest element in a list
nums = [10,45,20,89,12]
Output: 89
22. Find smallest element in a list
Output: 10

# 23. Count even numbers in list
nums = [10,11,12,13,14]
Output: 3
# 24. Print only odd numbers
Output:
11
13

# 25. Find sum of all elements
Output: 60

𝗟𝗲𝘃𝗲𝗹 𝟲: 𝗥𝗲𝗮𝗹-𝗧𝗶𝗺𝗲 𝗦𝘁𝘂𝗱𝗲𝗻𝘁 𝗣𝗿𝗼𝗯𝗹𝗲𝗺𝘀
# 26. Student Eligibility Checker
students = [
    {"name":"Dilli Prasad","cgpa":8.5},
    {"name":"William","cgpa":6.5},
    {"name":"Kareeshma","cgpa":9.1}
]

# Condition: CGPA >= 7
Output:
Dilli Prasad Eligible
Kareeshma Eligible

# 27. Find Topper Student
Output: Kareeshma
28. Count Eligible Students
Output: 2

# 29. Print students with CGPA above average
Calculate average first
30. Find students whose names start with 'R'
Output: ?

𝗟𝗲𝘃𝗲𝗹 𝟳: 𝗡𝗲𝘀𝘁𝗲𝗱 𝗟𝗼𝗼𝗽𝘀
31. Print Star Pattern
*
**
***
****
*****

32. Print Reverse Star Pattern
*****
****
***
**
*

33. Multiplication Grid
1 2 3
2 4 6
3 6 9

34. Print Triangle of Numbers
1
12
123
1234

35. Print Floyd's Triangle
1
2 3
4 5 6
7 8 9 10

36. What is an infinite loop?
37. What is the output?
for i in range(5):
    if i == 3:
        break
    print(i)

### 𝗠𝗶𝗻𝗶 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 - 𝗔𝗹𝗴𝗼𝗻𝗲𝘅 𝗦𝘁𝘂𝗱𝗲𝗻𝘁 𝗔𝘁𝘁𝗲𝗻𝗱𝗮𝗻𝗰𝗲 𝗦𝘆𝘀𝘁𝗲𝗺

𝗥𝗲𝗾𝘂𝗶𝗿𝗲𝗺𝗲𝗻𝘁𝘀:
Take 5 student names using loop
Store in list
Mark Present/Absent
Count Present Students
Count Absent Students
Display Attendance Report
