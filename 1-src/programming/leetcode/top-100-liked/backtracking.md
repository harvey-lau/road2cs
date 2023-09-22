# The Backtracking of [*Top 100 Liked*](https://leetcode.com/studyplan/top-100-liked/) in C++

## 0x01 Common Pattern

[BackTracking (BT)](https://en.wikipedia.org/wiki/Backtracking) is a class of algorithms for finding solutions to some problems, notably [constraint satisfaction problems](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem), that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

A BT problem has 3 key elements:

- BT search tree
- BT candidate extension step
- BT boundary

To solve a BT problem, there are 3 steps:

1. Build the **BT search tree**.
2. Follow the **BT candidate extension step** recursively.
3. Return all solutions at the **BT boundary**.

The template of a BT problem is:

```C++
class Solution {
public:
    vector<Type> btProblem(Type inputs) {
        vector<Type> ans;
        Type ans_i;
        // Step 1: build the BT search tree.
        bt(0, ans_i, ans, inputs);

        return ans;
    }

    void bt(int d, Type ins, Type &s, vector<Type> &ss) {
        // Step 3: return a solutions at the BT boundary.
        if (d == in.size()) {
            ss.push_back(s);
            return;
        }
        // Step 2: follow the BT candidate extension step recursively.
        for (in: ins) {
            s.push_back(in);
            bt(d + 1, ins, s, ss,);
            s.pop_back();
        }
        return;
    }
};
```

## 0x02 Problems

### 1. [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

---

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given [in the description of this problem](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description). Note that 1 does not map to any letters.

**Constraints**:

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

---

- BT search tree: the 0th layer is empty; the 1st layer is the mapping letters of `digits[0]`; the 2nd layer is the mapping letters of `digits[1]` which are repeated 3 or 4 times under the different nodes of the 1st layer... Without the 0th layer, the height of BT search tree is `digits.length`.
- BT candidate extension step: no pruning.
- BT boundary: `the searching depth == digits.length`

The code:

```C++
// 17. Letter Combinations of a Phone Number

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        string ans_i;
        int n = digits.size();
        if (n == 0) return ans;

        unordered_map<char, string> keyboard_9 {
          {'2', "abc"},
          {'3', "def"},
          {'4', "ghi"},
          {'5', "jkl"},
          {'6', "mno"},
          {'7', "pqrs"},
          {'8', "tuv"},
          {'9', "wxyz"}
        };
        
        bt(0, digits, keyboard_9, ans_i, ans);

        return ans;
    }

    void bt(int d, string nums, unordered_map<char, string> num_to_letter, string &s, vector<string> &ss) {
        if (d == nums.size()) {
            ss.push_back(s);
            return;
        }
        char now_num = nums[d];
        string now_letters = num_to_letter.at(now_num);
        for (char now_letter: now_letters) {
            s.push_back(now_letter);
            bt(d + 1, nums, num_to_letter, s, ss);
            s.pop_back();
        }
        return;
    }
};
```

### 2. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

---

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

**Constraints**:

- `1 <= n <= 8`

---

- BT search tree: the 0th layer is empty; the 1st layer is `(` and `)`; the 2nd layer is `(` and `)` which are repeated 2 times under the `(` and `)` of the 1st layer... Without the 0th layer, the height of BT search tree is `n`.
- BT candidate extension step: no pruning.
- BT boundary: `the searching depth == 2 * n`

However, we should judge whether a candidate is well-formed or not at the BT boundary.

The code:

```C++
// 22. Generate Parentheses

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string ans_i;
        bt(0, n, ans_i, ans);

        return ans;
    }

    void bt(int d, int n, string &s, vector<string> &ss) {
        if (d == 2 * n) {
            if (isValid(s)) ss.push_back(s);
            return;
        }

        s.push_back('(');
        bt(d + 1, n, s, ss);
        s.pop_back();
        s.push_back(')');
        bt(d + 1, n, s, ss);
        s.pop_back();

        return;
    }

    bool isValid(string s) {
        stack<char> st;
        int n = s.size();
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                st.push('(');
            }
            else {
                if (st.empty() == false && st.top() == '(') {
                    st.pop();
                }
                else {
                    st.push(')');
                }
            }
        }
        if (st.empty() == true) {
            return true;
        }
        else {
            return false;
        }

        return false;
    }
};
```

### 3. [Combination Sum](https://leetcode.com/problems/combination-sum/)

---

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`*. You may return the combinations in **any order**.

The **same** number may be chosen from candidates an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

> The **frequency** of an element `x` is the number of times it occurs in the array.

**Constraints**:

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

---

- BT search tree: the 0th layer is empty; the 1st layer is choosing candidates[i]; the 2nd layer is choosing candidates[i] which are repeated `candidates.length` times under the 1st layer... The height of BT search tree depends on `target`. For example, if `min(candidates[i]) = d` and `target = l`, the height of BT (without the 0th layer) is `l/d`.
- BT candidate extension step: no pruning.
- BT boundary: `Sigma(combination[i]) >= target`

We should collect combinations MECE at the BT boundary.

The code:

```C++
// 39. Combination Sum

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> ans_i;
        sort(candidates.begin(), candidates.end());
        bt(target, candidates, ans_i, ans);

        return ans;
    }

    void bt(int d, vector<int>& nums, vector<int> &v, vector<vector<int>> &vv) {
        if (d <= 0) {
            if (d == 0) {
                for (int i = 1; i < v.size(); i++) {
                    if (v[i] > v[i - 1]) {
                        return;
                    }
                }
                vv.push_back(v);
            }
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            v.push_back(nums[i]);
            bt(d - nums[i], nums, v, vv);
            v.pop_back();
        }

        return;
    }
};
```

### 4. [Permutations](https://leetcode.com/problems/permutations/)

---

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

**Constraints**:

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

---

- BT search tree: the 0th layer is empty; the 1st layer is choosing `nums[i]`; the 2nd layer is choosing `nums[i]` which are repeated `nums.length` times under the 1st layer... Without the 0th layer, the height of BT search tree is `nums.length`.
- BT candidate extension step: prune all chosen `nums[i]`(s). Therefore, we need a vector `visited` to record the chosen `nums[i]`(s).
- BT boundary: `the searching depth == nums.length`

The code:

```C++
// 46. Permutations

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) { 
        vector<vector<int>> ans;
        vector<int> ans_i;
        int n = nums.size();
        vector<bool> visited(n, false);
        bt(0, nums, visited, ans_i, ans);

        return ans;
    }

    void bt(int d, vector<int> &nums, vector<bool> &mark, vector<int> &v, vector<vector<int>> &vv) {
        int n = nums.size();
        if (d == n) {
            vv.push_back(v);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (mark[i] == false) {
                v.push_back(nums[i]);
                mark[i] = true;
                bt(d + 1, nums, mark, v, vv);
                v.pop_back();
                mark[i] = false;
            }
        }

        return;
    }
};
```

### 5. [N-Queens](https://leetcode.com/problems/n-queens/)

---

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Constraints**:

- `1 <= n <= 9`

---

If we give all queens a fixed row order like `1...n`, a permutation of `1...n` can represent the placing of queens. For example, `2431` means 4 queens are placed at (1, 2), (2, 4), (3, 3), and (4, 1) respectively. Based on this idea, we can further prune the solutions of last problem. The `permutations` problem satisfies the constraints of moving vertically and horizontally. The constraint of moving diagonally can be satisfied at the BT boundary by checking `j - i == v[i] - v[j] || i - j == v[i] - v[j]`. At last, mapping permutation to placement is the final step of solving the `N-Queens` problem.

The code:

```C++
// 51. N-Queens

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans_s;
        vector<vector<int>> ans;
        vector<int> ans_i;
        vector<bool> visited(n, false);
        bt(0, n, visited, ans_i, ans);

        if (ans.size() > 0) trans(ans_s, ans);

        return ans_s;
    }

    void bt(int d, int n, vector<bool> &mark, vector<int> &v, vector<vector<int>> &vv) {
        if (d == n) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (j - i == v[i] - v[j] || i - j == v[i] - v[j]) {
                      return;
                    }
                }
            }
            vv.push_back(v);
            return;
        }
        for (int i = 0; i < n; i++) {
            if (mark[i] == false) {
                v.push_back(i);
                mark[i] = true;
                bt(d + 1, n, mark, v, vv);
                v.pop_back();
                mark[i] = false;
            }
        }

        return;
    }

    void trans(vector<vector<string>> &sss, vector<vector<int>> vv) {
        int m = vv.size();
        int n = vv[0].size();

        for (int i = 0; i < m; i++) {
            vector<string> ss;
            for (int j = 0; j < n; j++) {
                string s(n, '.');
                for (int k = 0; k < n; k++) {
                    if (vv[i][j] == k) {
                        s[k] = 'Q';
                    }
                }
                ss.push_back(s);
            }
            sss.push_back(ss);
        }
        
        return;
    }
};
```

### 6. [Subsets](https://leetcode.com/problems/subsets/)

---

Given an integer array `nums` of **unique** elements, return *all possible subsets (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

> A **subset** of an array is a selection of elements (possibly none) of the array.

**Constraints**:

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

---

- BT search tree: the i-th layer is choosing `nums[i]` or not.
- BT candidate extension step: no pruning.
- BT boundary: `the searching depth == nums.length`

The code:

```C++
// 78. Subsets

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> ans_i;
        bt(0, nums, ans_i, ans);

        return ans;
    }

    void bt(int d, vector<int>& nums, vector<int> &v, vector<vector<int>> & vv) {
        int n = nums.size();
        if (d == n) {
            vv.push_back(v);
            return;
        }

        bt(d + 1, nums, v, vv);
        v.push_back(nums[d]);
        bt(d + 1, nums, v, vv);
        v.pop_back();
        
        return;
    }
};
```

### 7. [Word Search](https://leetcode.com/problems/word-search/)

---

Given an `m x n` grid of characters `board` and a string `word`, return *`true` if `word` exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Constraints**:

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

---

- BT search tree: the i-th layer is `up`, `down`, `left`, and `right`.
- BT candidate extension step: prune the unsatisfied directions.
- BT boundary: `the searching depth == word.length`

The code:

```C++
// 79. Word Search

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        char first = word[0];
        int m = board.size();
        int n = board[0].size();
        vector<vector<bool>> visited(m, vector<bool> (n, false));

        bool flag = false;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == first) {
                    visited[i][j] = true;
                    flag = flag || bt(1, board, word, i, j, visited);
                    visited[i][j] = false;
                }
            }
        }

        return flag;
    }

    bool bt(int d, vector<vector<char>>& board, string word, int a, int b, vector<vector<bool>>& mark) {
        int m = board.size();
        int n = board[0].size();
        int len = word.size();
        if (d == len) {
            return true;
        }

        bool flag = false;
        int dir[5] = {0, 1, 0, -1, 0};
        for (int i = 0; i < 4; i++) {
            int aa = a + dir[i];
            int bb = b + dir[i + 1];
            if (aa >= 0 && aa < m && bb >= 0 && bb < n) {
                if (mark[aa][bb] == false && board[aa][bb] == word[d]) {
                    mark[aa][bb] = true;
                    flag = flag || bt(d + 1, board, word, aa, bb, mark);
                    mark[aa][bb] = false;
                }
            }
        }

        return flag;
    }
};
```

### 8. [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

---

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return *all possible palindrome partitioning of `s`*.

> A **substring** is a contiguous non-empty sequence of characters within a string.
>
> A **palindrome** is a string that reads the same forward and backward.

**Constraints**:

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

---

- BT search tree: the i-th layer is `s-i.substr(0, l)` and `1 <= l <= s-i.length`.
- BT candidate extension step: prune the un-palindrome `s-i(1)` and further partition `s-i(2)` when `s-i(1)` is a palindrome string.
- BT boundary: `s-i(2).length == 0`

The code:

```C++
// 131. Palindrome Partitioning

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> ans_i;
        bt(s, ans_i, ans);
        
        return ans;
    }

    void bt(string s, vector<string> &ss, vector<vector<string>> &sss) {
        int n = s.size();
        if (n == 0) {
            sss.push_back(ss);
            return;
        }

        for (int i = 1; i <= n; i++) {
            string s1 = s.substr(0, i);
            string s2 = s.substr(i, n - i);
            if (isPal(s1)) {
                ss.push_back(s1);
                bt(s2, ss, sss);
                ss.pop_back();
            }
        }

        return;
    }

    bool isPal(string s) {
        int n = s.size();
        for (int i = 0; i < n / 2; i++) {
            if (s[i] != s[n - 1 - i]) {
                return false;
            }
        }

        return true;
    }
};
```

## 0x03 Summary

As mentioned above, there are 3 key elements of a BT problem. We can deconstruct its solution into 3 steps.

### 1. BT Search Tree

- Fixed depth and degree: 17-Letter Combinations of a Phone Number, 22-Generate Parentheses, 46-Permutations, 51-N-Queens, 78-Subsets, 79-Word Search.
- Unfixed depth and degree: 39-Combination Sum and 131-Palindrome Partitioning.

### 2. BT Candidate Extension Step

- `visited[]`
- `bool isSatisfied()`

### 3. BT Boundary

If we cannot prune sub-tree at the BT candidate extension step, the constraint satisfaction "pruning" may occur at the BT boundary.
