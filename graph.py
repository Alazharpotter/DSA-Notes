class DFS_Graphs:

    def __init__(self,num_nodes,edges):
        
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        print(self.data)

    # recursive approach
    def dfs(self,starting_node,visited):

        # create a list to mark down if node has been visited or not
        visited[starting_node] = True
        print(starting_node)
        
        for neighbouring_node in self.data[starting_node]:
            if not visited[neighbouring_node]:
                
                self.dfs(neighbouring_node,visited)
            
                


        pass


num_nodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
#3print(type(edges))
dfs_ex = DFS_Graphs(num_nodes,edges)

visited = [False]*num_nodes

dfs_ex.dfs(1,visited)
        