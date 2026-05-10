 import java.util.*;

class GraphTraversal 
{
      private int n;
      public ArrayList<ArrayList<Integer>> adjList;
      
      public void addEdge(int u, int v)
      {
         adjList.get(u).add(v);
         adjList.get(v).add(u);
      }
      
      public GraphTraversal(int n)  // constructor for node intialization 
      {
         this.n=n;
         adjList= new ArrayList<>();
         for (int i=0; i<n; i++)
         {
           adjList.add(new ArrayList<>());
         }
      }
      
      
      public void dfsRecur(int node, boolean[] visited)
      {
          System.out.print(node + " ");
          visited[node]=true;
          
          for (int neighbor : adjList.get(node))
          {
             if (!visited[neighbor])
             {
                 dfsRecur(neighbor,visited);
             }
          
          }
      }
	  
	  public void bfsRecursive(Queue<Integer> queue, boolean[] visited) 
	{
	      if (queue.isEmpty()) return;
	      int node = queue.poll();
	      System.out.print(node + " ");
	      for (int neighbor : adjList.get(node)) 
		  {
	             if (!visited[neighbor]) {
				 visited[neighbor] = true;
	             queue.add(neighbor);
	            }
	      }
	bfsRecursive(queue, visited); 
	 }
      public static void main (String[] args)
      {
        GraphTraversal graph = new GraphTraversal(6);
        graph.addEdge(0,1);
        graph.addEdge(0,2);
        graph.addEdge(1,3);
        graph.addEdge(2,4);
        graph.addEdge(3,5);
        
        
        System.out.println("DFS Traversal : ");
        boolean[] visited = new boolean[6];
        graph.dfsRecur(0,visited);
		
	    System.out.println("\n\nBFS Traversal:");
	    visited = new boolean[6];
	    Queue<Integer> queue = new LinkedList<>();
	    visited[0] = true;
	    queue.add(0);
	    graph.bfsRecursive(queue, visited);
      }
}
