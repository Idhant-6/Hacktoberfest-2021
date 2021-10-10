# Python3 code for printing shortest path between
# two vertices of unweighted graph

# utility function to form edge between two vertices
# source and dest
def add_edge(adj, src, dest):

    adj[src].append(dest);
    adj[dest].append(src);

# a modified version of BFS that stores predecessor
# of each vertex in array p
# and its distance from source in array d
def BFS(adj, src, dest, v, pred, dist):

    # a queue to maintain queue of vertices whose
    # adjacency list is to be scanned as per normal
    # DFS algorithm
    queue = []

    # boolean array visited[] which stores the
    # information whether ith vertex is reached
    # at least once in the Breadth first search
    visited = [False for i in range(v)];

    # initially all vertices are unvisited
    # so v[i] for all i is false
    # and as no path is yet constructed
    # dist[i] for all i set to infinity
    for i in range(v):

        dist[i] = 1000000
        pred[i] = -1;
    
    # now source is first to be visited and
    # distance from source to itself should be 0
    visited[src] = True;
    dist[src] = 0;
    queue.append(src);

    # standard BFS algorithm
    while (len(queue) != 0):
        u = queue[0];
        queue.pop(0);
        for i in range(len(adj[u])):
        
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.append(adj[u][i]);

                # We stop BFS when we find
                # destination.
                if (adj[u][i] == dest):
                    return True;

    return False;

# utility function to print the shortest distance
# between source vertex and destination vertex
def printShortestDistance(adj, s, dest, v):
    
    # predecessor[i] array stores predecessor of
    # i and distance array stores distance of i
    # from s
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)];

    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")

    # vector path stores the shortest path
    path = []
    crawl = dest;
    crawl = dest;
    path.append(crawl);
    
    while (pred[crawl] != -1):
        path.append(pred[crawl]);
        crawl = pred[crawl];
    

    # distance from source is in distance array
    print("Shortest path length is : " + str(dist[dest]), end = '')

    # printing path from source to destination
    print("\nPath is : : ")
    
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=' ')
        
# Driver program to test above functions
if __name__=='__main__':
    
    # no. of vertices
    v = int(input("Enter the no of vertices in graph: "))
    

    # array of vectors is used to store the graph
    # in the form of an adjacency list
    adj = [[] for i in range(v)];

    # Creating graph given in the above diagram.
    # add_edge function takes adjacency list, source
    # and destination vertex as argument and forms
    # an edge between them..
    print("Enter vertices to connect. \n##Vertex index starts with 0")
    while 1:
            add_edge(adj, int(input("Enter first vertex index: \n")), int(input("Enter second vertex index: \n")))
            c = input("Wanna connect more vertices? :")
            if (c == "N" or c == "n"):
                break
    
    source = int(input("Enter source vertex: "))
    dest = int(input("Enter destination vertex: "))
    printShortestDistance(adj, source, dest, v);

    # This code is contributed by rutvik_56
