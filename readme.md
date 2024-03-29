# Data Structures and Algorithms

My implementations of various data structures and algorithms in Python, based on ISIS-1225 course at Universidad de los Andes and the book _Algorithms_ by Robert Sedgewick and Kevin Wayne.

## Table of Contents

### 1. Linear structures
<br>    1.1 [Interface](#LinearInterface)
<br>    1.1.1 [Lists](#lists)
<br>    A. [ArrayLists](#arraylists)
<br>    A.1 [DynamicArrayLists](#dynamicarraylists)
<br>    A.2 [StaticArrayLists](#staticarraylists)
<br>    B. [LinkedLists](#linkedlists)
<br>    B.1 [SinglyLinkedLists](#singlylinkedlists)
<br>    B.2 [DoublyLinkedLists](#doublylinkedlists)
<br>    B.3 [CircularLinkedLists](#circularlinkedlists)
<br>    1.1.2 [Stacks](#stacks)
<br>    A. [ArrayStacks](#arraystacks)
<br>    B. [LinkedStacks](#linkedstacks)
<br>    1.1.3 [Queues](#queues)
<br>    A. [ArrayQueues](#arrayqueues)
<br>    B. [LinkedQueues](#linkedqueues)
<br>    1.2. Sorting algorithms
<br>    1.2.1 [Selection sort](#selection-sort)
<br>    1.2.2 [Insertion sort](#insertion-sort)
<br>    1.2.3 [Shell sort](#shell-sort)
<br>    1.2.4 [Merge sort](#merge-sort)
<br>    1.2.5 [Quick sort](#quick-sort)
<br>    1.2.6 [Heap sort](#heap-sort)
<br>    1.2.7 [Counting Sort](#counting-sort)
<br>    1.2.8 [Radix Sort](#radix-sort)
<br>    1.3. Searching algorithms
<br>    1.3.1 [Sequential search](#sequential-search)
<br>    1.3.2 [Binary search](#binary-search)
### 2. Hash structures
<br>    2.1 [ADT](#adtMap)
<br>    2.1.1 [Map](#map)
<br>    A. [HashMap](#hashmap)
<br>    2.2 [Hash tables](#hash-tables)
<br>    2.2.1 [Separate chaining](#separate-chaining)
<br>    2.2.2 [Linear probing](#linear-probing)
### 3. Tree structures
<br>    3.1 [ADT](#adtTree)
<br>    3.1.1 [Tree](#tree)
<br>    A. [BinaryTree](#binarytree)
<br>    B. [BinarySearchTree](#binarysearchtree)
<br>    C. [AVLTree](#avltree)
<br>    D. [2-3Tree](#2-3tree)
<br>    E. [RedBlackTree](#redblacktree)
<br>    3.1.2 [PriorityQueue](#priorityqueue)
<br>    A. [Heap](#heap)
<br>    3.1.3 [SegmentTree](#segmenttree)
<br>    3.2 [Tree Algorithms](#tree-algorithms)
<br>    3.2.1 [Tree traversal](#tree-traversal)
<br>    A. [Pre-order traversal](#pre-order-traversal)
<br>    B. [In-order traversal](#in-order-traversal)
<br>    C. [Post-order traversal](#post-order-traversal)
<br>    3.2.2 [Lowest Common Ancestor](#lowest common ancestor)
### 4. Graphs
<br>    4.1 [ADT](#adtGraph)
<br>    4.1.1 [Graph](#graph)
<br>    A. [DirectedGraph](#directedgraph)
<br>    B. [UndirectedGraph](#undirectedgraph)
<br>    4.1.2 [Graph Representation](#graph-representation)
<br>    A. [Adjacency Matrix](#adjacency-matrix)
<br>    B. [Adjacency List](#adjacency-list)
<br>    4.2 [Graph Algorithms](#graph-algorithms)
<br>    4.2.1 [Route search](#route-search)
<br>    A. [Breadth-first search](#breadth-first-search)
<br>    B. [Depth-first search](#depth-first-search)
<br>    4.2.2 [Toplogical sort](#toplogical-sort)
<br>    A. [Kahn's algorithm](#kahns-algorithm)
<br>    4.2.3 [Strongly connected components](#strongly-connected-components)
<br>    A. [Kosaraju's algorithm](#kosarajus-algorithm)
<br>    4.2.4 [Covering Trees](#covering-trees)
<br>    A. [Prim's algorithm](#prims-algorithm)
<br>    B. [Kruskal's algorithm](#kruskals-algorithm)
<br>    4.2.5 [Shortest paths](#shortest-paths)
<br>    A. [Dijkstra's algorithm](#dijkstras-algorithm)
<br>    B. [Bellman-Ford algorithm](#bellman-ford-algorithm)
<br>    C. [Floyd-Warshall algorithm](#floyd-warshall-algorithm)
<br>    4.2.6 [Network flow](#network-flow)
<br>    4.2.7 [Cycles](#cycles)
<br>    A. [Cycle detection](#cycle-detection)
### 5. Strings
<br>    5.1 [ADT](#adtString)
<br>    5.1.1 [String](#string)
<br>    A. [Trie](#trie)
<br>    B. [Suffix Tree](#suffix-tree)
<br>    5.2 [String Algorithms](#string-algorithms)
<br>    5.2.1 [Substring search](#substring-search)
<br>    A. [Brute force](#brute-force)
<br>    C. [Boyer-Moore](#boyer-moore)
<br>    D. [Rabin-Karp](#rabin-karp)
<br>    E. [Z algorithm](#z-algorithm)
<br>    5.2.2 [Regular expressions](#regular-expressions)
### 6. Linear algebra
<br>    6.1 [ADT](#adtMatrix)
<br>    6.1.1 [Matrix](#matrix)
<br>    6.2 [Matrix Algorithms](#matrix-algorithms)
<br>    6.2.1 [Solving linear systems](#solving-linear-systems)
<br>    A. [Gaussian elimination](#gaussian-elimination)
