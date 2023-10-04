---
tags:
  - "#notes"
  - programming-level-1
  - slss
  - y2023
  - natural-language-processing
---

# Syntax Errors

* These types of errors are ones where you run your code and something breaks
	* We don't follow the rules completely
	* i.e. When we forget a closing quotation (\")
* Relatively easy to fix, especially if you are using a newer version of Python
* Syntax <=> Rules

# Semantic Errors

* Much more challenging (in Ubial's opinion) to squash
* When your code doesn't "mean" what you actually mean

```python
user_response = input("Do you like to eat food?")

if user_response == "yes":
	print("You passed the human test.")
else:
	print("You must be some sort of robot.")
```

The problem with the above code is subtle. What I (Mr. Ubial) mean is that if the user answers with ANYTHING affirmative, the code should go into the `"yes"` block.

One way to solve this problem is to use [[Strings#String Methods|String Methods]]. We can use `.lower()` to catch all permutations of capital letters.
```python
user_response = input("Do you like to eat food?")

# YES yes YeS yEs YEs yES
if user_response.lower() == "yes":
	print("You passed the human test.")
else:
	print("You must be some sort of robot.")
```