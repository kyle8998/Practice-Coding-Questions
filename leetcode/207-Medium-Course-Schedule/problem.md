# Problem 207: Course Schedule

#### Difficulty: Medium

#### Problem

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

**Note**

The input prerequisites is a graph represented by a list of edges, not adjacency matrices.

You may assume that there are no duplicate edges in the input prerequisites.

#### Example

<pre>
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
</pre>