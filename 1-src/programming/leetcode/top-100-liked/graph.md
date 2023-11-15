# The Graph of [*Top 100 Liked*](https://leetcode.com/studyplan/top-100-liked/) in C++

There are too few Graph problems, so it is not enough to summarize them. Moreover, the knowledge points of these problems are mainly BFS, DFS, and 2D arrays. In this situation, what should be mastered are templates of [BFS](https://en.wikipedia.org/wiki/Breadth-first_search), [DFS](https://en.wikipedia.org/wiki/Depth-first_search), and their derived forms.

To solve a Graph problem, there are 2 steps:

1. Find the template.
2. Change the template.

## 0x01 [Number of Islands](https://leetcode.com/problems/number-of-islands/)

---

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Constraints**:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

---

The code:

```C++
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    ans += 1;
                }
            }
        }

        return ans;
    }

    void dfs(vector<vector<char>>& grid, int p, int q) {
        if (grid[p][q] == '0') {
            return;
        }

        grid[p][q] = '0';
        int m = grid.size();
        int n = grid[0].size();
        int dir[5] = {1, 0, -1, 0, 1};
        for (int i = 0; i < 4; i++) {
            int pp = p + dir[i];
            int qq = q + dir[i + 1];

            if (pp >= 0 && pp < m && qq >= 0 && qq < n) {
                dfs(grid, pp, qq);
            } 
        }
    }
};
```

## 0x02 [Course Schedule](https://leetcode.com/problems/course-schedule/)

---

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Constraints**:

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All the pairs `prerequisites[i]` are **unique**.

---

The code:

```C++
class Solution {
public:
    vector<vector<int>> edges;
    vector<int> nodes;
    bool ans = true;

    void dfs(int node) {
        nodes[node] = 1;
        for (auto next: edges[node]) {
            if (nodes[next] == 0) {
                dfs(next);
            }
            else if (nodes[next] == 1) {
                ans = false;
                return;
            }
        }
        nodes[node] = 2;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        edges.resize(numCourses);
        nodes.resize(numCourses);
        for (auto pre: prerequisites) {
            edges[pre[1]].push_back(pre[0]);
        }

        for (int i = 0; i < numCourses; i++) {
            dfs(i);
        }

        return ans;
    }
};
```

## 0x03 [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

---

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return `-1`*.

**Constraints**:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

---

The code:

```C++
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int dis[15][15];
        memset(dis, -1, sizeof(dis));
        int ans = -1;
        int fresh = 0;
        int m = grid.size();
        int n = grid[0].size();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push(make_pair(i, j));
                    dis[i][j] = 0;
                }
                else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        if (fresh == 0) {
            return 0;
        }

        int dir[5] = {0, -1, 0, 1, 0};

        while (q.empty() == false) {
            pair<int, int> now = q.front();
            for (int i = 0; i < 4; i++) {
                int xx = now.first + dir[i];
                int yy = now.second + dir[i + 1];
                if (xx >= 0 && xx < m && yy >= 0 && yy < n && grid[xx][yy] == 1 && dis[xx][yy] == -1) {
                    fresh -= 1;
                    dis[xx][yy] = dis[now.first][now.second] + 1;
                    q.push(make_pair(xx, yy));
                }
            }
            q.pop();
        }

        if (fresh == 0) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    ans = max(ans, dis[i][j]);
                }
            }
        }

        return ans;
    }
};
```
