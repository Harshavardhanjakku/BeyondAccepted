# Problem: Word Search
# Difficulty: Medium
# Topic: Array
# Language: c
# Submission: 2

#include <stdbool.h>

bool dfs(char** board, int m, int n, int r, int c,
         char* word, int ind, int length, int** visited) {
 
    if (r < 0 || c < 0 || r >= m || c >= n)
        return false;
    if (visited[r][c] || board[r][c] != word[ind])
        return false;

    
    if (ind == length - 1)
        return true;

    visited[r][c] = 1;

    bool found =
        dfs(board, m, n, r, c + 1, word, ind + 1, length, visited) ||
        dfs(board, m, n, r, c - 1, word, ind + 1, length, visited) ||
        dfs(board, m, n, r + 1, c, word, ind + 1, length, visited) ||
        dfs(board, m, n, r - 1, c, word, ind + 1, length, visited);

    visited[r][c] = 0;    
    return found;
}

bool exist(char** board, int boardSize, int* boardColSize, char* word) {
    int m = boardSize;
    int n = boardColSize[0];

    int length = 0;
    while (word[length] != '\0') length++;
 
    int** visited = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        visited[i] = (int*)calloc(n, sizeof(int));
    } 
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == word[0]) {
                if (dfs(board, m, n, i, j, word, 0, length, visited)) { 
                    for (int k = 0; k < m; k++) free(visited[k]);
                    free(visited);
                    return true;
                }
            }
        }
    } 
    for (int k = 0; k < m; k++) free(visited[k]);
    free(visited);

    return false;
}

