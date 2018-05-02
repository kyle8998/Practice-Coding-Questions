# Problem 10: Regular Expression Matching


#### Difficulty: Hard

#### Problem

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```

The matching should cover the entire input string (not partial).

**Note:**

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

#### Example

<pre>

Input:

s = "aa"

p = "a"

Output: false

Explanation: "a" does not match the entire string "aa".

</pre>

<pre>

Input:

s = "mississippi"

p = "mis*is*p*."

Output: false

</pre>