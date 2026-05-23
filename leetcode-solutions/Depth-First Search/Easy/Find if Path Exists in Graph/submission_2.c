# Problem: Find if Path Exists in Graph
# Difficulty: Easy
# Topic: Depth-First Search
# Language: c
# Submission: 2

bool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination) {
    if (source == destination)
        return true;

    typedef struct Node {
        int val;
        struct Node* next;
    } Node;

    Node** graph = (Node**)calloc(n, sizeof(Node*));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0], v = edges[i][1];
        Node* node1 = (Node*)malloc(sizeof(Node));
        node1->val = v; node1->next = graph[u]; graph[u] = node1;
        Node* node2 = (Node*)malloc(sizeof(Node));
        node2->val = u; node2->next = graph[v]; graph[v] = node2;
    }

    bool* visited = (bool*)calloc(n, sizeof(bool));
    int* queue = (int*)malloc(n * sizeof(int));
    int front = 0, rear = 0;
    queue[rear++] = source;
    visited[source] = true;

    while (front < rear) {
        int curr = queue[front++];
        if (curr == destination) {
            free(visited); free(queue);
            for (int i = 0; i < n; ++i) {
                Node* temp = graph[i];
                while (temp) {
                    Node* next = temp->next;
                    free(temp);
                    temp = next;
                }
            }
            free(graph);
            return true;
        }

        Node* temp = graph[curr];
        while (temp) {
            if (!visited[temp->val]) {
                visited[temp->val] = true;
                queue[rear++] = temp->val;
            }
            temp = temp->next;
        }
    }

    free(visited); free(queue);
    for (int i = 0; i < n; ++i) {
        Node* temp = graph[i];
        while (temp) {
            Node* next = temp->next;
            free(temp);
            temp = next;
        }
    }
    free(graph);

    return false;
}

