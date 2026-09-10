# Overview

This assessment evaluates your ability to perform the following tasks in accordance with ICTPRG547 Apply advanced programming skills in another language:

 - **Performance elements**:
    - 1.4 Code sorting algorithm using programming techniques
    - 3.2 Detect and resolve errors of syntactical, logical and design origin
    - 3.3 Design and document required tests
    - 4.1 Develop and document solution according to debugging test results

You will demonstrate your performance by providing evidence that you can "code at least one sorting algorithm", and "test and debug the code to resolve errors of a syntactical, logical, or design origin".

To succeed you must use a "systematic, analytical processes in complex, non-routine situations, setting goals, gathering relevant information, and identifying, and evaluating, options against the agreed criteria".

## 2. General instructions

> CRITICAL: Failure to follow these instructions will lead to an NYC

- Copy this file into a `docs` folder in your assessment repo (that is, the repo you created for POR1/POR2)
- Add and commit this file to your repository and associate the tag `por3-start`:
  - Copy and `add` this file to your repository under the `docs` folder
  - `git commit -m "chore: add task overview to my repo"
  - `git tag por3-start`
  - `git push origin main --tags`
  - Optional: you may want to complete this work in a branch
  - On your last commit, add an **annotated** tag `por3-finish`:
    - `git tag -a por3-finish -m "marks my original submission completed in class"`
    - `git push origin main --tags`
- Commit changes after you complete each task
- Push changes to your GitHub repository
- Ensure that your original tests still pass as well as any additional tests
- Ensure you submit your git repo (`.git/`) along with your assessment submission

> **IMPORTANT:** While some aspects of this task are done under exam-like conditions, this is **not** an exam.
> You are _encouraged_ to ask questions of your assessor both about the test itself and its coding requirements. You can also ask your neighbors for help, but you must not copy their work. If you are unsure about anything, ask your assessor.


### 2.1 What if I can't complete this work in class?

It is expected that the majority of this work will be completed in class, under supervision.
Therefore, even if your work is incomplete at the close of class you will need to submit it with:
- The code and `.git/' folder at the state it was in at 17:00 on the day of your class.
- An annotated tag `por3-incomplete` on your last commit
- A comment highlighting that the work is incomplete and what you managed to do
- A completed statement of authenticity (see below)

Submit the work within a week of class. Your assessor will determine if a significant enough portion of the work was done in class. If it is not, you may need to undertake additional validation before a CO is attained.


## 3. Players have scores now

### 3.1. Task: Add scores to players

Add a private instance variable to the Player class that will hold the score (a positive integer value).

Since we want our existing tests to pass, we will make this parameter optional and set a default value of 0.

Provide a getter (property) and a setter method for this value.

> **Recommended:** If you don't already have a `__repr__` method in your Player class, add one now to help with debugging. It should present as follows: `Player(name='Alice', uid='01', score=10)` and ideally get the class name dynamically: `self.__class__.__name__`

#### 3.1.1. Success criteria
You can mark this task as complete when you have (your assessor will use a similar list):
- [ ] Correct use of private instance variable
- [ ] Score is optional (in the constructor) and defaults to 0
- [ ] Use of properties to create a getter and setter
- [ ] Raising ValueError if someone attempts to set a non-positive value
- [ ] Existing tests pass
- [ ] At least one (and ideally only one) commit showing the above changes

## 4. Sorting players

### 4.1. Task: Add unit tests for sorting players

Add the following unit tests to the `test_player.py` file:

```python
def test_sort_players(self):
    players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5), Player("Charlie", uid='03', score=15)]
    # note: ensure initialization code is valid for **your** implementation.
    # For example, is your parameter called uid? is the first parameter name?

    # do **not** change the following code:
    sorted_players = sorted(players)

    # players must be sorted by score as shown here:
    manually_sorted_players = [Player("Bob", uid='02', score=5), Player("Alice", uid='01', score=10), Player("Charlie", uid='03', score=15)]

   self.assertListEqual(sorted_players, manually_sorted_players)

```

> **Note:** If you have made other changes to the initializer of your player update the above code to reflect this change - you must not make any other changes to the test code above.

### 4.2. Task: Interpret unit tests

What was the outcome of running the above unit test, copy paste the output **for just this particular test** below:

```text
Copy the traceback you got when you ran the test here.
(.venv) (base) MacBook-Pro-5:SRUS-NT-Games nonokatakahashi$ python3 -m unittest test.player_test.PlayerTest.test_sort_players
E
======================================================================
ERROR: test_sort_players (test.player_test.PlayerTest.test_sort_players)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/nonokatakahashi/PycharmProjects/SRUS-NT-Games/test/player_test.py", line 25, in test_sort_players                                                                                                        
    sorted_players = sorted(players)
TypeError: '<' not supported between instances of 'Player' and 'Player'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### 4.3. Success criteria

- [x] Unit test added to `test_player.py`
- [x] Unit test output provided
- [x] Unit test output reflects the error in `sorted(players)` (if you are getting another error read the instructions CAREFULLY)

#### 4.3.1. Question: What dunder method is required for Python to sort players?

The tests checks that calling sorted on a list of players will sort them by score.

What is the **only** magic method that must be implemented in the player class for the `sorted` function to succeed?

**Hint:** if you don't recall this from class, the error message you got when you ran the test will help you.
-------
> Answer Here
> the error message said < is not supported between instance of Player and Player which shows that sorted compares the 
> items with <. I think __lt__ is the method python call for that operator.
-------
#### 4.3.2. Task: Implement the magic method in the Player class

Add a test case to test_player to test the comparison operator you are about to add - ensure you do not test a dunder method directly!

```python
def test_players_can_be_compared_by_score(self):
    # note: ensure initialization code is valid for **your** implementation
    alice = Player("Alice", uid='01', score=10)
    bob = Player("Bob", uid='02', score=5)

    # Add the appropriate expression to the following assert test
    self.assertTrue(<your comparison expression>)
    # or, event better
    self.assert<AppropriateComparisonMethod>(alice, bob)
```

Run the test and confirm that your error resembles the previous error

```text
INSERT ERROR OUTPUT HERE
(.venv) (base) MacBook-Pro-5:SRUS-NT-Games nonokatakahashi$ python3 -m unittest test.player_test.PlayerTest.test_players_can_be_compared_by_score
E
======================================================================
ERROR: test_players_can_be_compared_by_score (test.player_test.PlayerTest.test_players_can_be_compared_by_score)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/nonokatakahashi/PycharmProjects/SRUS-NT-Games/test/player_test.py", line 36, in test_players_can_be_compared_by_score                                                                                              
    self.assertGreater(alice, bob)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/unittest/case.py", line 1298, in assertGreater                                                                                                          
    if not a > b:
           ^^^^^
TypeError: '>' not supported between instances of 'Player' and 'Player'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

- Implement the appropriate magic method in the Player class and ensure you pass this test
- It is likely (indeed desirable) that you still won't pass the `test_sort_players` test
- Commit your changes

#### 4.3.3. Success criteria

- [ ] Unit test added to `test_player.py`
- [ ] Magic method implemented in `Player` class
- [ ] Initial Failed Unit test output provided
- [ ] Unit test runs successfully with submitted code
- [ ] Dunder method not employed directly
- [ ] At least one commit capturing the above changes

#### 4.3.4. Task: Are we sorted yet?

Rerun `test_sort_players` does the test pass? If not, include the output below:

```text
Your output here
(.venv) (base) MacBook-Pro-5:SRUS-NT-Games nonokatakahashi$ python3 -m unittest test.player_test.PlayerTest.test_sort_players
F
======================================================================
FAIL: test_sort_players (test.player_test.PlayerTest.test_sort_players)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/nonokatakahashi/PycharmProjects/SRUS-NT-Games/test/player_test.py", line 30, in test_sort_players
    self.assertListEqual(sorted_players, manually_sorted_players)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [Play[60 chars]d='01', score=10), Player (name='Charlie', uid='03', score=15)] != [Play[60 chars]d='01', score=10), Player (name='Charlie', uid='03', score=15)]                                    
                                                                                                                 
First differing element 0:                                                                                       
Player (name='Bob', uid='02', score=5)                                                                           
Player (name='Bob', uid='02', score=5)                                                                           
                                                                                                                 
  [Player (name='Bob', uid='02', score=5),                                                                       
   Player (name='Alice', uid='01', score=10),                                                                    
   Player (name='Charlie', uid='03', score=15)]                                                                  

----------------------------------------------------------------------
Ran 1 test in 0.004s

FAILED (failures=1)
```

##### 4.3.4.1 Question: why did the equality comparison fail?
Why did the test fail (note: if it doesn't fail, it means there is something you have already done before you were asked to do so - if that's the case, you need to figure out what that is!)?
-------
> Answer here
> Sorting output shows the players in score order 5, 10, 15.
> Failure comes from assertListEqual which compares the elements with ==.
> Player has no __eq__ so Python falls back to checking if two names point to the same object.
> two lists are built from separate instances so == returns False even though the values match.

-------
Add the necessary code to the Player class to ensure that the `test_sort_players` test passes.

#### 4.3.5. Success criteria

- [x] Correct explanation of why `test_sort_players` failed/passed
- [x] Correct implementation of the magic method in the `Player` class
- [x] `test_sort_players` passes when run against the submitted code
- [x] At least one commit capturing the above changes

## 5. Implement a custom sorting algorithm

The senior developer on your team believes that a custom sorting algorithm would be more efficient than the built-in `sorted` function (you grit your teeth, sigh, and realize you need this job!).

They have asked you to implement a custom sorting algorithm that will sort a list of players by score.

To help you get started they have provided you with some example code that they wrote in their undergraduate days.

Unless something goes wrong, you will need to remain faithful to the algorithm they have provided - you can change variable names, but you must not change the algorithm itself.

Remember, they wrote it at university, so they probably didn't use PEP8 or adhere to professional coding standards. If only they had gone to TAFE!

```python
def sort_quickly(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return sort_quickly(left) + [pivot] + sort_quickly(right)
```

### 5.1. Question: complexity

What is the expected time and space complexity of the above algorithm? You can answer using big O or in plain English but in both cases you MUST justify your answer.

> Time: O(n log n) on average, O(n²) in the worst case.
> Each call checks every element once, so that is n comparisons.
> If the pivot is near the middle, the list is cut in half each time and there are about log n levels.
> If the pivot is always the smallest or largest value, one side keeps n-1 elements so there are n levels.
> 
> Space: O(n log n) on average, O(n²) in the worst case
> The algorithm does not sort in place. Every call makes two new lists,
> so each level needs room for another n elements and the levels add up.
> The recursion also uses stack space for each level.

### 5.2. Task: Implement the custom sorting algorithm

#### 5.2.1. Create a new method in the Player class

Use the sample above (and its algorithm) as a starting point to implement a `classmethod` in the Player class that takes a list of players and returns a list of players sorted by score in **descending** order. Top scores come first!

#### 5.2.2. Create a test cases

Add a separate test case to `test_player.py` to test your custom sorting algorithm

Include your code below:

```python
# YOUR CUSTOM Sorting here
    def test_sort_by_score(self):
        players = [Player(player_id='01', player_name="Alice", score=10),
                   Player(player_id='02', player_name="Bob", score=5),
                   Player(player_id='03', player_name="Charlie", score=15)]

        result = Player.sort_by_score(players)

        self.assertEqual([15, 10, 5], [player.score for player in result])

```

#### 5.2.3. Success criteria

- [x] Custom sorting algorithm implemented in the `Player` class as `classmethod`
- [x] Custom sorting algorithm sorts in descending order
- [x] Custom sorting algorithm compares players using their score (via the rich comparison operators)
- [x] Custom sorting algorithm tested in `test_player.py` and tests passed
- [x] At least one commit capturing the above changes

### 5.3. Test your custom sorting algorithm at scale

The senior developer is impressed with your work and asks you to test your custom sorting algorithm with a list of 1000 players. They provide you with a script that will generate a list of 1000 players with random scores.

```python
import random
from player import Player


players = [Player(f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
```

#### 5.3.1. Task: Create a test case to sort 1000 players

Using the code above as a starting point, create a test case to test your custom sort algorithm - you can test it against the `sorted` function to ensure it is working correctly.

Include your test case below:

```python

# YOUR TEST CASE HERE
    def test_sort_by_score_one_thousand_player(self):
        players = [Player(player_id=f"{i:03}",
                   player_name=f"Player {i}",
                   score=random.randint(1, 1000))
                   for i in range(1000)]

        result = Player.sort_by_score(players)
        expected = sorted(players, reverse=True)

        self.assertEqual([player.score for player in expected],
                         [player.score for player in result])

```

#### 5.3.2. Success criteria

- [x] Test case added to `test_player.py`
- [x] Test case sorts 1000 players correctly when compared to `sorted` function
- [x] Test case passes when run against the submitted code
- [x] At least one commit capturing the above changes

#### 5.3.3. Task: Testing sorting sorted players

You had a scary thought - and decided to test your custom sorting algorithm against a list of players that are already sorted by score. You are worried that your algorithm might not be efficient in this case.

#### 5.3.4. Task: Create a test case to sort 1000 sorted players

Create a test case that tries to sort 1000 players that are already sorted.

If you get a failure, include the failure below:

```text
YOUR FAILURE HERE
(.venv) (base) MacBook-Pro-5:SRUS-NT-Games nonokatakahashi$ python3 -m unittest test.player_test
....E..
======================================================================
ERROR: test_sort_by_score_one_thousand_sorted_player (test.player_test.PlayerTest.test_sort_by_score_one_thousand_sorted_player)                                                                                                
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/nonokatakahashi/PycharmProjects/SRUS-NT-Games/test/player_test.py", line 66, in test_sort_by_score_one_thousand_sorted_player                                                                                    
    result = Player.sort_by_score(players)
  File "/Users/nonokatakahashi/PycharmProjects/SRUS-NT-Games/app/player.py", line 44, in sort_by_score
    return cls.sort_by_score(higher) + [pivot] + cls.sort_by_score(lower)
           ~~~~~~~~~~~~~~~~~^^^^^^^^
  File "/Users/nonokatakahashi/PycharmProjects/SRUS-NT-Games/app/player.py", line 44, in sort_by_score
    return cls.sort_by_score(higher) + [pivot] + cls.sort_by_score(lower)
           ~~~~~~~~~~~~~~~~~^^^^^^^^
  File "/Users/nonokatakahashi/PycharmProjects/SRUS-NT-Games/app/player.py", line 44, in sort_by_score
    return cls.sort_by_score(higher) + [pivot] + cls.sort_by_score(lower)
           ~~~~~~~~~~~~~~~~~^^^^^^^^
  [Previous line repeated 980 more times]
  File "/Users/nonokatakahashi/PycharmProjects/SRUS-NT-Games/app/player.py", line 39, in sort_by_score
    if player > pivot:
       ^^^^^^^^^^^^^^
RecursionError: maximum recursion depth exceeded

----------------------------------------------------------------------
Ran 7 tests in 0.079s

FAILED (errors=1)
```

##### 5.3.4.1 Question: Why does the algorithm fail on presorted values?

Provide a reason why this test failed (if you got a recursion errors, you need to explain **why** that happened with a sorted list, but not an unsorted list).

If your implementation did not fail, you must nevertheless explain why the senior developers algorithm has worse space complexity for presorted values.

> The pivot is always the first player. In a sorted list that player has the lowest score
> so every other player goes into higher and lower stays empty.
> Each call removes only one player, so the recursion goes 1000 levels deep and Python stops it with RecursionError.
> In a random list the pivot is usually near the middle,
> so the two sides are about equal and the depth is only about 10 levels.
> A sorted list is therefore the worst case: the time becomes O(n²)
> and the space grows the same way because every call builds new lists.

Propose a fix to your sorting algorithm that fixes this issue.

```python
# YOUR FIX HERE
@classmethod
    def sort_by_score(cls, players):
        """Return a new list of players sorted by score, highest first"""
        if len(players) <= 1:
            return players

        middle = len(players) // 2
        pivot = players[middle]
        rest = players[:middle] + players[middle + 1:]

        higher = []
        lower = []
        for player in rest:
            if player > pivot:
                higher.append(player)
            else:
                lower.append(player)

        return cls.sort_by_score(higher) + [pivot] + cls.sort_by_score(lower)

# Highlight what the fix was
take the pivot from the middle of the list instead of the front so already sorted list is still split into two halves.
```

#### 5.3.5. Success criteria

- [x] Test case added to `test_player.py`
- [x] Test case passes only when changes above are added
- [x] Explanation of why the algorithm fails on presorted values
- [x] Fix to the algorithm provided
- [x] At least one commit capturing the above changes

## 6. Task: Authenticity of in class work

Complete the following snippet before you submit:

```text
I, <name and student number>, completed this work in class <room number>, on <date>, under the supervision of <assessor's name>.
```

Or (if not completed in class):

```text
I, <name and student number>, completed this work outside of the scheduled hours. I emailed <assessors name>, on <date>, along with my documented reason for non-attendance, and have scheduled a time to meet to discuss my work.

I understand that until I meet my assessor to confirm that this work is a valid and true representation of my abilities to write and debug a sorting algorithm in Python, this submission cannot be considered complete.

```

## 7. Submit your work

- [ ] Ensure all tasks are complete and tests pass
- [ ] Answer all questions in your own words
- [ ] Complete the statement of authenticity
- [ ] Include `.git` showing each task committed (you must show at least 5 commits)
- [ ] Annotated tag of your last commit as `por3-finish`
- [ ] Push your changes to your GitHub repository
- [ ] Submit a zip of your repository to the LMS (ensure you do not add the `.venv` or `__pycache__` folders)

---
End of assessment task