# The Greedy of [*Top 100 Liked*](https://leetcode.com/studyplan/top-100-liked/) in C++

A [greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm) is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage.

A greedy problem has 2 key properties:

- **Greedy choice property**: We can make whatever choice seems best at the moment and then solve the sub-problems that arise later. The choice made by a greedy algorithm may depend on choices made so far, but not on future choices or all the solutions to the subproblem.
- [*Optimal sub-structure*](https://en.wikipedia.org/wiki/Optimal_substructure): the solution to a given optimization problem can be obtained by the combination of optimal solutions to its sub-problems.

Do you recall [DP](https://github.com/harvey-lau/road2cs/blob/main/1-src/programming/leetcode/top-100-liked/dynamic-programming.md)? A difference between DP and Greedy is that the former has lots of problems while the latter is not the case. It is partly because the first property of Greedy is difficult to satisfy. Or, ignore it and forcefully apply a greedy algorithm to yield locally optimal solution. Overall, Greedy isn't the focus of Top 100 Liked. However, it is a trick that we can partly solve hard problems with a greedy algorithm to get a non-zero mark.

## 0x01 [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

**Constraints**:

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

The code:

```C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 1) {
            return 0;
        }

        int ans = 0;
        int buy = 100005;
        for (int i = 0; i < n; i++) {
            buy = min(buy, prices[i]);
            ans = max(ans, prices[i] - buy);
        }

        return ans;
    }
};
```

## 0x02 [Jump Game II](https://leetcode.com/problems/jump-game-ii/)

---

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

- `0 <= j <= nums[i]` and
- `i + j < n`

Return *the minimum number of jumps to reach `nums[n - 1]`*. The test cases are generated such that you can reach `nums[n - 1]`.

**Constraints**:

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

---

The code:

```C++
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        int now = 0;

        while (now < n - 1) {
            int next = now;
            int next_max = now + nums[now];
            for (int i = 1; i <= nums[now] && now + i < n; i++) {
                if (now + i >= n - 1) {
                    return ans + 1;
                }
                if (now + i + nums[now + i] >= next_max) {
                    next_max = now + i + nums[now + i];
                    next = now + i;
                }
            }
            now = next;
            ans++;
        }

        return ans;
    }
};
```

## 0x03 [Jump Game](https://leetcode.com/problems/jump-game/)

---

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return *`true` if you can reach the last index, or `false` otherwise*.

**Constraints**:

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

---

The code:

```C++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) {
            return true;
        }

        vector<bool> flag(n, false);
        if (nums[0] == 0) {
            return false;
        }
        else {
            flag[0] = true;
        }
        
        for(int i = 0; i < n; i++) {
            int farest = i + nums[i];
            if (flag[i] == true && farest >= n) {
                return true;
            }
            for (int j = i + 1; j <= farest && j < n; j++) {
                flag[j] = flag[i];
                if (flag[j] == true && j + nums[j] >= n) {
                    return true;
                }
            }
        }

        return flag[n - 1];
    }
};
```

## 0x04 [Partition Labels](https://leetcode.com/problems/partition-labels/)

---

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return *a list of integers representing the size of these parts*.

**Constraints**:

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

---

The code:

```C++
class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        int last[26];
        for (int i = 0; i < n; i++) {
            last[s[i] - 'a'] = i;
        }

        vector<int> ans;
        int start = 0;
        int end = 0;
        for (int i = 0; i < n; i++) {
            end = max(end, last[s[i] - 'a']);
            if (i == end) {
                ans.push_back(end - start + 1);
                start = end + 1;
            }
        }

        return ans;
    }
};
```
