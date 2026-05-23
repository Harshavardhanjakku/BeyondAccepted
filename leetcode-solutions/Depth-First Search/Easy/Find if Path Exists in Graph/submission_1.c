# Problem: Find if Path Exists in Graph
# Difficulty: Easy
# Topic: Depth-First Search
# Language: c
# Submission: 1

#include<stdlib.h>

int find(int x, int *root){
    if(x == root[x])
        return x;
    return root[x] = find(root[x],root);
}

void unionSet(int x, int y, int *root){
    int rootX = find(x,root);
    int rootY = find(y,root);

    if(rootX != rootY){
        root[rootY] = rootX;
    }
}

bool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination) {
    int grid[n][n];
    int root[n];

    for( int i = 0 ; i < n ; i++)
        root[i] = i;


    for( int i = 0 ; i < edgesSize ; i++){
        unionSet(edges[i][0],edges[i][1],root);
    }

    // dfs(n,grid,visited,source,destination);
    return find(source,root) == find(destination,root);
}
