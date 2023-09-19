# The Dynamic Programming of [*Top 100 Liked*](https://leetcode.com/studyplan/top-100-liked/) in C++

## 0x01 Common Pattern

A [*Dynamic Programming (DP)*](https://en.wikipedia.org/wiki/Dynamic_programming) problem has 2 key attributes:

- [*Optimal sub-structure*](https://en.wikipedia.org/wiki/Optimal_substructure): the solution to a given optimization problem can be obtained by the combination of optimal solutions to its sub-problems.
- [*Overlapping sub-problems*](https://en.wikipedia.org/wiki/Overlapping_subproblems): any recursive algorithm solving the problem should solve the same sub-problems over and over.

For example, $F_i = F_{i - 1} + F_{i - 2}$ .

- Optimal sub-structure: the solution to $F_i$ can be obtained by the combination of $F_{i - 1}$ and $F_{i - 2}$ .
- Overlapping sub-problems: a recursive solution should solve $F_{i - 2}$ twice because $F_{i - 1} = F_{i - 2} + F_{i - 3}$ .

A DP problem has 3 key elements:

- DP model
- DP initial state
- DP state transition equation

To solve a DP problem, there are 3 steps:

1. Build a **DP model**. The most important component is $dp_i$ .
2. Determine **DP initial state**. $dp_1$ corresponds a **bottom-up** approach while $dp_n$ corresponds a **top-down** approach.
3. Find **DP state transition equation**. DP state transition equation should cause a "complete" [domino effect](https://en.wikipedia.org/wiki/Domino_effect).

## 0x02 Problems

### 1. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

---

Given a string `s`, return *the longest palindromic substring* in `s`.

> A string is **palindromic** if it reads the same forward and backward.
>
> A **substring** is a contiguous non-empty sequence of characters within a string.

**Constraints**:

- `1 <= s.length <= 1,000`
- `s` consist of only digits and English letters.

---

A brute-force solution is:

1. Substring: list all substrings of `s`.
2. Palindromic: judge whether every substring is palindromic or not.
3. Longest: record and update the longest string.

The time complexity is $O(n^3)$ .

> `n` means the length of `s`.

Every string problem deserves a try from the view of DP.

This problem needs the longest palindromic substring rather than its length. It means that we should know its all *eigenvalues* of target substring(s), $(i, j)$ or $(i, length)$ . The time complexity is $O(n^2)$ at least, which points to 2D DP. Noticing the *equivalence relation* of $i$ , $j$ , and palindrome, we can endow `dp[i][j]` with a meaning about palindrome. Intuitively, `dp[i][j]` can represent:

- The max length of palindromic substring(s) of `s[i...j]`.
- Whether `s[i...j]` is palindromic or not.

Generally, returning `dp[0][n - 1]` is the most common situation of DP string problems, but that `dp[i][j]` represents the max length of palindromic substring(s) of `s[i...j]` doesn't obtain the necessary eigenvalue $i$.

However, if `dp[i][j]` represents whether `s[i...j]` is palindromic or not, we can turn $O(n^2 \cdot n)$ to $O(n^2 + n^2)$ .

The 3 key elements of the "Longest Palindromic Substring" problem are:

1. DP model: `dp[i][j]` represents whether `s[i...j]` is palindromic or not.
2. DP initial state (bottom-up)
   - When `s[i...j].length() = 1`, `dp[i][i] = true`.
   - When `s[i...j].length() = 2`, if `s[i] == s[i + 1]`, `dp[i][i + 1] = true`, otherwise `dp[i][i + 1] = false`.
3. DP state transition equation: If `s[i] == s[j]`, `dp[i][j] = dp[i + 1][j - 1]`, otherwise `dp[i][j] = false`.

To get the final answer, `dp[i][j]` should be traversed by the length of substring in descending order.

The code:

```C++
// 5. Longest Palindromic Substring

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();

        // DP model: dp[i][j] represents whether s[i...j] is palindromic or not.
        vector<vector<bool>> dp(n, vector<bool>(n, false));

        // DP initial state (bottom-up)
        // s[i...j].length() = 1
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }
        // s[i...j].length() = 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) dp[i][i + 1] = true;
            else dp[i][i + 1] = false;
        }

        // DP state transition equation:
        // If s[i] == s[j], dp[i][j] = dp[i + 1][j - 1], otherwise dp[i][j] = false.
        for (int len = 3; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (i >= 0 && i < n && j >= 0 && j < n) {
                    if (s[i] == s[j]) dp[i][j] = dp[i + 1][j - 1];
                    else dp[i][j] = false;
                }
            }
        }

        // Traverse dp[i][j] by the length of substring in descending order.
        for (int len = n; len >= 1; len--) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (i >= 0 && i < n && j >= 0 && j < n) {
                    if (dp[i][j] == true) return s.substr(i, len);
                }
            }
        }

        return s;
    }
};
```

### 2. [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

---

Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses substring*.

> A **substring** is a contiguous non-empty sequence of characters within a string.

**Constraints**:

- `0 <= s.length <= 3 * 10,000`
- `s[i]` is `'('`, or `')'`.

---

A brute-force solution is:

1. Substring: list all substrings of `s`.
2. Valid (well-formed): judge whether every substring is valid (well-formed) or not.
3. Longest: record and update the length of longest string.

The time complexity is $O(n^3)$ .

> `n` means the length of `s`.

Can we solve it similar to the "Longest Palindromic Substring" problem? The FILO of stack isn't satisfy the DP model of "Longest Palindromic Substring". In other words, we can't domino it by similar DP initial state and DP state transition equation.

However, the string problems with `1` eigenvalue can be modeled as 1-D DP. Intuitively, `dp[i]` can represent:

- The max length of valid (well-formed) parentheses substring(s) `s[...i]`, or `t1`. `t1` ends at `s[i]`.
- The max length of valid (well-formed) parentheses substring(s) `s[i...]`, or `t2`. `t2` begins at `s[i]`.
- The max length of valid (well-formed) parentheses substring(s) `s[...j]` (`t3`) and `j <= i`. `t3` ends at `s[j]`.
- The max length of valid (well-formed) parentheses substring(s) `s[j...]` (`t4`) and `j >= i`. `t4` begins at `s[j]`.

Let's discuss them respectively:

- For `t1` model, `s[i]` should be `)`.
  - If `s[i - 1] == '('`, `dp[i] = dp[i - 2] + 2`.
  - If `s[i - 1] == ')'`, `s[i - 1 + 1 - dp[i - 1]]` should be `(` (the furthest one).
    - If `s[i - 1 + 1 - dp[i - 1] - 1] == '('`, `dp[i] = dp[i - 1] + 2 + dp[i - 1 + 1 - dp[i - 1] - 2]`.
    - If `s[i - 1 + 1 - dp[i - 1] - 1] == ')'`:
      - If there is a `(` before `s[i - 1 + 1 - dp[i - 1] - 1]`, that `(` corresponds to `s[i - 1]` and `dp[i - 1]` already includes it as a further `(`. Therefore, no transition.
      - If there is no `(`s before `s[i - 1 + 1 - dp[i - 1] - 1]`, `dp[i] = 0`. Therefore, no transition.
- For `t2` model, it is a top-down approach in the [contraposition](https://en.wikipedia.org/wiki/Contraposition) logic of `t1` model.
- For `t3` model, it doesn't satisfy the optimal sub-structure attribute. For example, `()()`. `dp[1] = dp[2] = 2`, but we don't know how to domino `dp[3]` by `s[3]` and previous `dp[i]`s. Actually, `t3` model is more suitable for the situation that whether include `s[i]` then `dp[i - 1] + s[i]` or not.
- For `t4` model, it is the contraposition logic of `t3` model too.

Okay! Now we summarize 3 key elements of the "Longest Valid Parentheses" problem in `t1` model as below:

1. DP model: `dp[i]` corresponds to `t1` model.
2. DP initial state (bottom-up): `dp[...] = 0`
3. DP state transition equation:

- If `s[i] == ')' && s[i - 1] == '('`, `dp[i] = dp[i - 2] + 2`.
- If `s[i] == ')' && s[i - 1] == ')' && s[i - 1 + 1 - dp[i - 1] - 1] == '('`, `dp[i] = dp[i - 1] + 2 + dp[i - 1 + 1 - dp[i - 1] - 2]`.

The answer is the max of `dp[i]`.

The code:

```C++
// 32. Longest Valid Parentheses

class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length();

        if (n == 0 || n == 1) return 0;

        int res = 0;

        // DP model: dp[i] corresponds to s[...i].
        // DP initial state (bottom-up): dp[...] = 0.
        vector<int> dp(n, 0);

        // DP state transition equation:
        for (int i = 1; i < n; i++) {
            if (s[i] == ')') {
                // case 1: ........()
                if (s[i - 1] == '(') {
                    if (i - 2 >= 0) dp[i] = dp[i - 2] + 2;
                    else dp[i] = 2;
                }
                // case 2: ...((...))
                else {
                    if (i - 1 - dp[i - 1] >= 0 && s[i - 1 - dp[i - 1]] == '(') {
                        if (i - 2 - dp[i - 1] >= 0) dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]];
                        else dp[i] = dp[i - 1] + 2;
                    }
                }
            }
            // The answer is the max of `dp[i]`.
            res = max(res, dp[i]);
        }

        return res;
    }
};
```

### 3. [Unique Paths](https://leetcode.com/problems/unique-paths/)

---

There is a robot on an `m * n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 1,000,000,000`.

**Constraints**:

- `1 <= m, n <= 100`

---

A brute-force idea is:

1. The number of all unique paths is $2^{m - 1 + n - 1}$.
2. The valid paths require $m - 1$ top-to-bottom steps and $n - 1$ left-to-right steps.

Then, it becomes a math problem: return the number of unique ways of placing $m - 1$ `'↓'` and $n - 1$ `'→'` in a line. Based on [*combinatorics*](https://en.wikipedia.org/wiki/Combinatorics), the answer is $C_{m + n - 2}^{m - 1}$ .

Can we solve the $C_{m}^{n}$ problem by DP? There is the formula $C_{m}^{n} = C_{m - 1}^{n} + C_{m - 1}^{n - 1}$ like $F_i = F_{i - 1} + F_{i - 2}$ .

The 3 key elements of the $C_{m}^{n}$ problem are:

1. DP model: `dp[m][n]` represents the value of $C_{m}^{n}$ .
2. DP initial state: `dp[m][0] = 1` and `dp[m][m] = 1`
3. DP state transition equation: `dp[m][n] = dp[m - 1][n] + dp[m - 1][n - 1]`

The code:

```C++
// 62. Unique Paths

class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 1 && n == 1) return 1;

        // DP model: dp[m][n] represents the value of C_{m}^{n}.
        vector<vector<int>> dp(m + n, vector<int> (m + n));

        // DP initial state: dp[m][0] = 1 and dp[m][m] = 1

        for (int i = 1; i <= m + n - 2; i++) {
            dp[i][0] = 1;
        }
        for (int i = 1; i <= m + n - 2; i++) {
            dp[i][i] = 1;
        }

        // DP state transition equation: dp[m][n] = dp[m - 1][n] + dp[m - 1][n - 1]

        int k = min(m, n); // To avoid integer overflow
        for (int i = 2; i <= m + n - 2; i++) {
            for (int j = 1; j <= k - 1; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
            }
        }

        return dp[m + n - 2][k - 1];
    }
};
```

Even though we don't reduce this problem to a DP math problem, it is a classic 2-D DP problem as below.

1. DP model: `dp[i][j]` represents the number of possible unique paths reaching `grid[i][j]`.
2. DP initial state: `dp[0][...] = 1` and `dp[...][0] = 1`
3. DP state transition equation: `dp[i][j] = dp[i][j - 1] + dp[i - 1][j]`

The code:

```C++
// 62. Unique Paths

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int> (n));

        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int i = 0; i < n; i++) {
            dp[0][i] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[m - 1][n - 1];
    }
};
```

### 4. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

---

Given a `m * n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note**: You can only move either down or right at any point in time.

**Constraints**:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

---

It is similar to the "Unique Paths" problem.

The 3 key elements of the "Minimum Path Sum" problem are:

1. DP model: `dp[i][j]` represents the minimum sum of path(s) ending at `grid[i][j]`.
2. DP initial state: `dp[0][...] = prefix sum` and `dp[...][0] = prefix sum`
3. DP state transition equation: `dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]`

The code:

```C++
// 64. Minimum Path Sum

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> dp(m, vector<int> (n));

        dp[0][0] = grid[0][0];

        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }

        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }

        return dp[m - 1][n -1];
    }
};
```

### 5. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

---

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Constraints**:

- `1 <= n <= 45`

---

The 3 key elements of the "Climbing Stairs" problem are:

1. DP model: `dp[i]` represents the answer of `n` steps.
2. DP initial state: `dp[0] = 1` (a trick) and `dp[1] = 1`
3. DP state transition equation: `dp[i] = dp[i - 2] + dp[i - 1]`

The code:

```C++
// 70. Climbing Stairs

class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n + 1);
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 2] + dp[i - 1];
        }

        return dp[n];
    }
};
```

### 6. [Edit Distance](https://leetcode.com/problems/edit-distance/)

---

Given two strings `word1` and `word2`, return *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

**Constraints**:

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

---

The code:

```C++
// 72. Edit Distance

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
                else {
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1;
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1);
                }
            }
        }

        return dp[m][n];
    }
};
```

### 7. [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

---

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

**Constraints**:

- `1 <= numRows <= 30`

---

The code:

```C++
// 118. Pascal's Triangle

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        for (int i = 0; i < numRows; i++) {
            vector<int> row(i + 1, 1);
            for (int j = 1; j < i; j++) {
                row[j] = res[i - 1][j - 1] + res[i - 1][j];
            }
            res.push_back(row);
        }

        return res; 
    }
};
```

### 8. [Word Break](https://leetcode.com/problems/word-break/)

---

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

**Constraints**:

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

---

The code:

```C++
// 139. Word Break

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int m = s.length();
        int n = wordDict.size();
        vector<int> dp(m + 1, false);
        dp[0] = true;

        for (int i = 1; i <= m; i++) {
            for (int j = 0; j < n; j++) {
                int k = wordDict[j].length();
                if (i - 1 + k <= m)
                    if (wordDict[j].compare(s.substr(i - 1, k)) == 0)
                        if (dp[i - 1] == true) dp[i - 1 + k] = true;
            }
        }
        if (dp[m] == 0) return false;
        return true;
    }
};
```

### 9. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

---

Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

> A **subarray** is a contiguous non-empty sequence of elements within an array.

**Constraints**:

- `1 <= nums.length <= 2 * 10,000`
- `-10 <= nums[i] <= 10`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

---

The code:

```C++
// 152. Maximum Product Subarray

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector(2, 1));

        dp[0][0] = nums[0];
        dp[0][1] = nums[0];

        int res = nums[0];

        for (int i = 1; i < n; i++) {
            dp[i][0] = max(max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i]), nums[i]);
            dp[i][1] = min(min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i]), nums[i]);
            res = max(res, dp[i][0]);
        }

        return res;
    }
};
```

### 10. [House Robber](https://leetcode.com/problems/house-robber/)

---

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array nums representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

**Constraints**:

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

---

The code:

```C++
// 198. House Robber

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();

        vector<vector<int>> dp(n, vector<int>(2));

        if (n == 1) return nums[0];

        dp[0][0] = 0;
        dp[0][1] = nums[0];
        dp[1][0] = nums[0];
        dp[1][1] = nums[1];

        for (int i = 2; i < n; i++) {
            dp[i][0] = max(dp[i - 2][1], dp[i - 1][1]);
            dp[i][1] = dp[i - 1][0] + nums[i];
        }

        return max(dp[n - 1][0], dp[n - 1][1]);
    }
};
```

### 11. [Perfect Squares](https://leetcode.com/problems/perfect-squares/)

---

Given an integer `n`, return *the least number of perfect square numbers that sum to `n`*.

A **perfect square** is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, `1`, `4`, `9`, and `16` are perfect squares while `3` and `11` are not.

**Constraints**:

- `1 <= n <= 10,000`

---

The code:

```C++
// 279. Perfect Squares

class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            for (int j = 1; i - j * j >= 0; j++) {
                dp[i] = min(dp[i], dp[i - j * j] + 1);
            }
        }

        return dp[n];
    }
};
```

### 12. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

---

Given an integer array `nums`, return *the length of the longest **strictly increasing subsequence***.

> A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Constraints**:

- `1 <= nums.length <= 2500`
- `-10,000 <= nums[i] <= 10,000`

---

The code:

```C++
// 300. Longest Increasing Subsequence

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1);
        int res = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) dp[i] = max(dp[i], dp[j] + 1);
            }
            res = max(res, dp[i]);
        }

        return res;
    }
};
```

### 13. [Coin Change](https://leetcode.com/problems/coin-change/)

---

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

**Constraints**:

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10,000`

---

The code:

```C++
// 322. Coin Change

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;

        int n = coins.size();
        vector<int> dp(amount + 1, INT_MAX);

        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int c: coins) {
                if (i >= c && dp[i - c] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - c] + 1);
                }
            }
        }

        if (dp[amount] == INT_MAX) return -1;
        else return dp[amount];
    }
};
```

### 14. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

---

Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise*.

**Constraints**:

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

---

The code:

```C++
// 416. Partition Equal Subset Sum

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();

        if (n == 1) return false;

        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }

        if (sum % 2 != 0) return false;

        int target = sum / 2;

        vector<bool> dp(target + 1, false);
        dp[0] = true;

        for (int c: nums) {
            for (int i = target; i >= c; i--) {
                dp[i] = dp[i] || dp[i - c];
            }
        }

        return dp[target];
    }
};
```

### 15. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

---

Given two strings `text1` and `text2`, return *the length of their longest **common subsequence***. If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

**Constraints**:

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

---

The code:

```C++
// 1143. Longest Common Subsequence

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1[i - 1] == text2[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
            }
        }

        return dp[m][n];
    }
};
```

## 0x03 Summary

As mentioned above, there are 3 key elements of a DP problem. We can deconstruct its solution into 3 steps.

### 1. DP Model

- 1-D DP
  - The max (min) length of string problem: 5-Longest Palindromic Substring.
  - The max (min) value of array problem: 152-Maximum Product Subarray and 198-House Robber.
  - The recursion problem: 70-Climbing Stairs, 139-Word Break, 279-Perfect Squares, 300-Longest Increasing Subsequence, 322-Coin Change, and 416-Partition Equal Subset Sum.
- 2-D DP: equivalence relation
  - The max (min) length of string problem: 32-Longest Valid Parentheses, 72-Edit Distance, and 1143-Longest Common Subsequence.
  - The max (min) value of array problem: 62-Unique Paths and 64-Minimum Path Sum.
  - The recursion problem: 118-Pascal's Triangle.

### 2. DP Initial State

- The initial value of DP array and the border matter.
- A good `dp[0]` is beneficial to the DP state transition equation and reduces the complexity of dealing with out of bounds indexes.

### 3. DP State Transition Equation

DP state transition equation depends on DP model. However, there are some common DP state transition equations:

- `dp[i]`, `dp[...i]`, and `dp[...j]`.
- `dp[i][2]`, `dp[i][c]`, and `dp[i][j]`.
- `int dp` and `bool dp`.

The domino effect of DP state transition equation must satisfy the [Mutually Exclusive and Collectively Exhaustive (MECE) principle](https://en.wikipedia.org/wiki/MECE_principle).
