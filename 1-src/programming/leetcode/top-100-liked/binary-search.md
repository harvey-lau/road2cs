# The Binary Search of [*Top 100 Liked*](https://leetcode.com/studyplan/top-100-liked/) in C++

## 0x01 Common Pattern

[Binary Search (BS)](https://en.wikipedia.org/wiki/Binary_search_algorithm) is a search algorithm that finds the position of a target value within a sorted array.

A BS problem has 3 key elements:

- BS model
- BS halving
- BS returning

To solve a BS problem, there are 3 steps:

1. Build the **BS model** which indicates searching what and where.
2. **Halve** the search interval in a loop.
3. **Return** the solution in the search process.

The template of a BS problem is:

```C++
class Solution {
public:
    int bsProblem(Type inputs, Type target) {
        int L = 0;
        int R = n - 1;
        while (L <= R) {
            int M = (L + R) / 2;
            if (inputs[M] == target) {
                return ans;
            }
            else if (inputs[M] < target) {
                L = M + 1;
            }
            else {
                R = M - 1;
            }
        }

        return -1;
    }
}
```

The most obvious feature of BS problems is **sorted**. Moreover, they require an algorithm with `O(log n)` runtime complexity.

## 0x02 Problems

I show all code with an **ugly** template as below.

### 1. [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

---

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Constraints**:

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10^4 <= target <= 10^4`

---

The code:

```C++
// 35. Search Insert Position

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0;
        int right = n - 1;
        if (target <= nums[left]) {
            return left;
        }
        if (nums[right] < target) {
            return right + 1;
        }

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            else if (target < nums[mid]) {
                right = max(mid - 1, left);
            }
            else {
                left = min(mid + 1, right);
            }
        }

        if (target <= nums[left]) {
            return left;
        }
        else {
            return left + 1;
        }

        return -1;
    }
};
```

### 2. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of `target` if it is in `nums`, or `-1` if it is not in `nums`*.

You must write an algorithm with `O(log n)` runtime complexity.

**Constraints**:

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

---

The code:

```C++
// 33. Search in Rotated Sorted Array

class Solution {
public:
    int bs(vector<int>& arr, int t, int left, int right) {
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] == t) {
                return mid;
            }
            else if (t < arr[mid]) {
                right = max(mid - 1, left);
            }
            else {
                left = min(mid + 1, right);
            }
        }
        if (arr[left] == t) {
            return left;
        }

        return -1;
    }

    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0;
        int right = n - 1;
        int maxNum = 0;
        if (nums[0] < nums[n - 1]) {
            maxNum = n - 1;
        }
        else {
            while (left < right) {
                int mid = (left + right) / 2;
                if (nums[maxNum] <= nums[mid]) {
                    maxNum = mid;
                    left = min(mid + 1, right);
                }
                else {
                    right = max(mid - 1, left);
                }
            }
            if (nums[left] > nums[maxNum]) {
                maxNum = left;
            }
        }

        int ans = bs(nums, target, 0, maxNum);
        if (ans != -1) {
            return ans;
        }

        if (maxNum == n - 1) {
            return -1;
        }
        else {
            ans = bs(nums, target, maxNum + 1, n - 1);
            return ans;
        }

        return -1;
    }
};
```

### 3. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

---

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Constraints**:

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

---

The code:

```C++
// 34. Find First and Last Position of Element in Sorted Array

class Solution {
public:
    int bs1(vector<int>& arr, int t) {
        int n = arr.size();
        int ret = -1;
        if (n == 0) {
            return ret;
        }

        int left = 0;
        int right = n - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (t <= arr[mid]) {
                if(t == arr[mid]) {
                    ret = mid;
                }
                right = max(mid - 1, left);
            }
            else {
                left = min(mid + 1, right);
            }
        }
        if (arr[left] == t) {
            ret = left;
        }

        return ret;
    }

    int bs2(vector<int>& arr, int t) {
        int n = arr.size();
        int ret = -1;
        if (n == 0) {
            return ret;
        }

        int left = 0;
        int right = n - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] <= t) {
                if(t == arr[mid]) {
                    ret = mid;
                }
                left = min(mid + 1, right);
            }
            else {
                right = max(mid - 1, left);
            }
        }
        if (arr[right] == t) {
            ret = right;
        }

        return ret;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans = {-1, -1};
        int n = nums.size();
        if (n == 0) {
            return ans;
        }

        int ff = bs1(nums, target);
        int ll = bs2(nums, target);

        ans[0] = ff;
        ans[1] = ll;

        return ans;
    }
};
```

### 4. [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

---

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The `first` integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return *`true` if `target` is in `matrix` or `false` otherwise*.

You must write a solution in `O(log(m * n))` time complexity.

**Constraints**:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

---

The code:

```C++
// 74. Search a 2D Matrix

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int left = 0;
        int right = m * n - 1;

        while (left < right) {
            int mid = (left + right) / 2;
            int i = mid / n;
            int j = mid % n;
            if (matrix[i][j] == target) {
                return true;
            }
            else if (target < matrix[i][j]) {
                right = max(mid - 1, left);
            }
            else {
                left = min(mid + 1, right);
            }
        }
        if (matrix[left / n][left % n] == target) {
            return true;
        }

        return false;
    }
};
```

### 5. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n)` time complexity.

**Constraints**:

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

---

The code:

```C++
// 153. Find Minimum in Rotated Sorted Array

class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }

        if (nums[0] < nums[n - 1]) {
            return nums[0];
        }

        int left = 0;
        int right = n - 1;        
        int maxNum = 0;
        if (nums[0] < nums[n - 1]) {
            maxNum = n - 1;
        }
        else {
            while (left < right) {
                int mid = (left + right) / 2;
                if (nums[maxNum] <= nums[mid]) {
                    maxNum = mid;
                    left = min(mid + 1, right);
                }
                else {
                    right = max(mid - 1, left);
                }
            }
            if (nums[left] > nums[maxNum]) {
                maxNum = left;
            }
        }

        return nums[(maxNum + 1) % n];
    }
};
```

### 6. Median of Two Sorted Arrays

---

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Constraints**:

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

The code:

```C++
// 4. Median of Two Sorted Arrays

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        if (m < n) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int left = 0;
        int right = n * 2;

        while (left <= right) {
            int mid2 = (left + right) / 2;
            int mid1 = m + n - mid2;

            double L1 = (mid1 == 0)? INT_MIN: nums1[(mid1 - 1) / 2];
            double R1 = (mid1 == m * 2)? INT_MAX: nums1[(mid1) / 2];
            double L2 = (mid2 == 0)? INT_MIN: nums2[(mid2 - 1) / 2];
            double R2 = (mid2 == n * 2)? INT_MAX: nums2[(mid2) / 2];

            if (L1 > R2) {
                left = mid2 + 1;
            }
            else if (L2 > R1) {
                right = mid2 - 1;
            }
            else {
                return (max(L1, L2) + min(R1, R2)) / 2;
            }
        }

        return -1;
    }
};
```

## 0x03 Summary

Except some very hard problems, the BS problems is easy to be modelled. The difficulty is searching in a mutually exclusive and collectively exhaustive (MECE) way and returning answer at the index of `target`. An effective method to cope with it:

1. Write a template which guarantees the MECE searching and returning answer at the index of `target`. The template should update `L`, `R`, and `M` with a fixed pattern. For example, whether `M` equals the floor of `(L + R) / 2` or its ceil. Choose one pattern and don't change it until you find a better pattern.
2. Use the template to solve different problems and gather the experience of dealing with boundary test cases and some BS tricks. For example, 4-Median of Two Sorted Arrays. Even if we know its solution with the half line, it is hard to solve the Median of Two Sorted Arrays clearly because of the boundary test cases and BS tricks.
