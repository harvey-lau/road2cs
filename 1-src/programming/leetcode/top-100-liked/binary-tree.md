# The Binary Tree of [*Top 100 Liked*](https://leetcode.com/studyplan/top-100-liked/) in C++

## 0x01 Common Pattern

A [binary tree](https://en.wikipedia.org/wiki/Binary_tree) is a tree data structure in which each node has at most two children, referred to as the left child and the right child.

A binary tree problem has 2 key elements:

- Traversal order
- Answer

To solve a binary tree problem, there are 2 steps:

1. Select a proper traversal order: pre-, in-, post-, or level-.
2. Get the answer in the recursive traversal process.

The template of a binary tree problem is:

```C++
class Solution {
public:
    Type ans;

    Type traversal(TreeNode* root) {
        if (root == nullptr) {
            return Type;
        }
        // Get the answer.
        traversal(TreeNode* root->left);
        traversal(TreeNode* root->right);

        return Type;
    }

    Type BTreeProblem(TreeNode* root) {
        return ans;
    }
}
```

## 0x02 Problems

### 1. [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

---

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

**Constraints**:

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

The code:

```C++
class Solution {
public:

    void inTra(TreeNode *root, vector<int> &ans) {
        if (root == nullptr) {
            return;
        }
        inTra(root->left, ans);
        ans.push_back(root->val);
        inTra(root->right, ans);

        return;
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        inTra(root, ans);

        return ans;
    }
};
```

### 2. [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

---

Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).

**Constraints**:

- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

---

The code:

```C++
class Solution {
public:
    bool isEqual(TreeNode *root1, TreeNode *root2) {
        if (root1 == nullptr && root2 == nullptr) {
            return true;
        }
        else if (root1 == nullptr || root2 == nullptr) {
            return false;
        }
        if (root1->val == root2->val) {
            return isEqual(root1->left, root2->right) && isEqual(root1->right, root2->left);
        }

        return false;
    }

    bool isSymmetric(TreeNode* root) {
        return isEqual(root->left, root->right);
    }
};
```

### 3. [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Constraints**:

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

---

The code:

```C++
class Solution {
public:
    int deepest(TreeNode* root, int res) {
        if (root == nullptr) {
            return res;
        }
        int x = deepest(root->left, res + 1);
        int y = deepest(root->right, res + 1);

        return max(x, y);
    }

    int maxDepth(TreeNode* root) {
        int ans = 0;
        ans = deepest(root, 0);

        return ans;
    }
};
```

### 4. [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

---

Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a **height-balanced** binary search tree*.

> A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Constraints**:

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in a **strictly increasing** order.

---

The code:

```C++
class Solution {
public:
    TreeNode* addOne(vector<int> nums, int ll, int rr) {
        if (ll > rr) {
            return nullptr;
        }

        int M = (ll + rr) / 2;
        TreeNode* root = new TreeNode(nums[M]);
        root->left = addOne(nums, ll, M - 1);
        root->right = addOne(nums, M + 1, rr);

        return root;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int n = nums.size();

        return addOne(nums, 0, n - 1);
    }
};
```

### 5. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

---

Given the `root` of a binary tree, invert the tree, and return *its root*.

**Constraints**:

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

The code:

```C++
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) {
            return root;
        }
        if (root->left == nullptr && root->right == nullptr) {
            return root;
        }

        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        invertTree(root->left);
        invertTree(root->right);

        return root;
    }
};
```

### 6. [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

---

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Constraints**:

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

---

The code:

```C++
class Solution {
public:
    int ans = 0;

    int depth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int x = depth(root->left);
        int y = depth(root->right);

        ans = max(ans, x + y);

        return max(x, y) + 1;
    }

    int diameterOfBinaryTree(TreeNode* root) {
        depth(root);
        return ans;
    }
};
```

### 7. [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

---

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

> A **subtree** of `treeName` is a tree consisting of a node in `treeName` and all of its descendants.

**Constraints**:

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

---

The code:

```C++
class Solution {
public:
    vector<int> arr;
    void inorder(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        if (root->left != nullptr) {
            inorder(root->left);
        }
        arr.push_back(root->val);
        if (root->right != nullptr) {
            inorder(root->right);
        }
        return;
    }

    bool isValidBST(TreeNode* root) {
        inorder(root);
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i - 1] >= arr[i]) {
                return false;
            }
        }
        
        return true;
    }
};
```

### 8. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

---

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

**Constraints**:

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

---

The code:

```C++
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root == nullptr) {
            return ans;
        }
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty() == true) {
            int n = q.size();
            vector<int> ans_i;
            for (int i = 0; i < n; i++) {
                TreeNode* now = q.front();
                ans_i.push_back(now->val);
                if (now->left != nullptr) {
                    q.push(now->left);
                }
                if (now->right != nullptr) {
                    q.push(now->right);
                }
                q.pop();
            }
            ans.push_back(ans_i);
        }
        
        return ans;
    }
};
```

### 9. [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

---

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

**Constraints**:

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of **unique** values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is **guaranteed** to be the preorder traversal of the tree.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.

---

The code:

```C++
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = preorder.size();
        if (n == 0) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(preorder[0]);
        vector<int> preorder_left, preorder_right, inorder_left, inorder_right;
        int i = 0;
        for(; i < n; i++) {
            if (inorder[i] == preorder[0]) {
                break;
            }
            inorder_left.push_back(inorder[i]);
        }
        for(i++; i < n; i++) {
            inorder_right.push_back(inorder[i]);
        }

        for (int j = 1; j < n; j++) {
            if (j <= inorder_left.size()) {
                preorder_left.push_back(preorder[j]);
            }
            else {
                preorder_right.push_back(preorder[j]);
            }
        }

        root->left = buildTree(preorder_left, inorder_left);
        root->right = buildTree(preorder_right, inorder_right);

        return root;
    }
};
```

### 10. [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

---

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a [pre-order traversal](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR) of the binary tree.

**Constraints**:

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

---

The code:

```C++
class Solution {
public:
    vector<int> arr;

    void preorder(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        arr.push_back(root->val);
        preorder(root->left);
        preorder(root->right);

        return;
    }

    void flatten(TreeNode* root) {
        preorder(root);

        int n = arr.size();
        if (n == 0 || n == 1) {
            return;
        }
        root->left = nullptr;
        root->right = nullptr;
        for (int i = 1; i < n; i++) {
            TreeNode* temp = new TreeNode(arr[i]);
            root->right = temp;
            root = root->right;
        }
    }
};
```

### 11. [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

---

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

**Constraints**:

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

The code:

```C++
class Solution {
public:
    vector<int> ans;

    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) {
            return ans;
        }

        queue<TreeNode*> q;
        q.push(root);
        while (q.size() != 0) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode* now = q.front();
                if (now->left != nullptr) {
                    q.push(now->left);
                }
                if (now->right != nullptr) {
                    q.push(now->right);
                }
                if (i == n - 1) {
                    ans.push_back(now->val);
                }
                q.pop();
            }
        }

        return ans;
    }
};
```

### 12. [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

---

Given the `root` of a binary search tree, and an integer `k`, return *the `k-th` smallest value (**1-indexed**) of all the values of the nodes in the tree*.

**Constraints**:

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

---

The code:

```C++
class Solution {
public:
    vector<int> arr;

    void inorder(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        inorder(root->left);
        arr.push_back(root->val);
        inorder(root->right);

        return;
    }

    int kthSmallest(TreeNode* root, int k) {
        inorder(root);
        int n = arr.size();

        return arr[k - 1];
    }
};
```

### 13. [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

---

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to [the definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Constraints**:

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

---

The code:

```C++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) {
            return nullptr;
        }

        if (root == p || root == q) {
            return root;
        }

        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        if (left == nullptr) {
            return right;
        }
        if (right == nullptr) {
            return left;
        }
        return root;
    }
};
```

### 14. [Path Sum III](https://leetcode.com/problems/path-sum-iii)

---

Given the `root` of a binary tree and an integer `targetSum`, return *the number of paths where the sum of the values along the path equals `targetSum`*.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

**Constraints**:

- The number of nodes in the tree is in the range `[0, 1000]`.
- `-10^9 <= Node.val <= 10^9`
- `-1000 <= targetSum <= 1000`

---

The code:

```C++
class Solution {
public:
    int pathSum_i(TreeNode* root, long targetSum) {
        int res = 0;
        if (root == nullptr) {
            return res;
        }

        if (root->val == targetSum) {
            res += 1;
        }
        res += pathSum_i(root->left, targetSum - root->val);
        res += pathSum_i(root->right, targetSum - root->val);

        return res;
    }

    int pathSum(TreeNode* root, long targetSum) {
        int ans = 0;
        if (root == nullptr) {
            return ans;
        }

        ans += pathSum_i(root, targetSum);
        ans += pathSum(root->left, targetSum);
        ans += pathSum(root->right, targetSum);

        return ans;
    }
};
```

### 15. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

PS: this problem is wrongly classified into the Binary Search problems by LeetCode.

---

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum** of any **non-empty** path*.

**Constraints**:

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-1000 <= Node.val <= 1000`

---

The code:

```C++
class Solution {
public:
    int ans = INT_MIN;

    int ans_i(TreeNode* root) {
        int res = 0;
        if (root == nullptr) {
            return res;
        }

        int left = max(ans_i(root->left), 0);
        int right = max(ans_i(root->right), 0);

        int temp = root->val + left + right;
        ans = max(ans, temp);

        return root->val + max(left, right);
    }

    int maxPathSum(TreeNode* root) {
        ans_i(root);

        return ans;
    }
};
```

## 0x03 Summary

In my opinion, the Binary Tree problems rely on the number of problems you solved and your summarizing ability. If you solve the Binary Tree problem from Easy to Hard. You can find some clear routines:

- Traversal or recursion is essential. Every problem needs it. If not, you even cannot print the value of a leaf TreeNode. How can you return the answer almost involving all TreeNodes.
- It is fixed to end the recursive process, aka `root == nullptr`. Relatively, you should fine-tune the condition of Backtracking problems for avoiding some errors or returning the answer.
- Moreover, there is no need to deal with some annoying boundary test cases.

I think the most difficult part of Binary Tree problems is logic (or algorithm itself). We may come up with a solution but fail to pass all test cases. After checking the result of unpassed test case, it shows that the solution must be changed with another algorithm because the logic of the original one has some flaws, which acquires rewriting the whole code. For some difficult problems, we may not be able to think of a solution.

That's why the number and summarizing matter.
