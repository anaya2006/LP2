class GraphColor 
{   
    private int V;
	private int numColors;
    private int [][] graph;
	private int[] colors;
	private String [] colorNames = {" ","red","green","blue"};
	
	public GraphColor (int[][] adjacencyMat, int numColors)
	{
		V=adjacencyMat.length;
		graph=adjacencyMat;
		colors=new int [V];
	}
	
	public boolean isSafe(int v, int c)
	{
		for (int i=0; i<V; i++)
		{
			if (graph[v][i]==1 && colors[i]==c)
			{
				return false;
			}
		}
		return true;
	}
	
	public boolean solveGraphColoring (int v, int m)
	{
		if (v==V)
		{
			printsolution();
			return true;
		}
		
		for (int c=1; c<=m; c++)
		{
			if (isSafe(v,c))
			{
				colors[v]=c;
				if(solveGraphColoring(v+1,m))
				{
					return true;
				}
				colors[v]=0;
			}
		}
		return false;
	}
	
	public void printsolution()
	{
		System.out.println("Vertex -> Color ");
		for (int i=0; i<V; i++)
		{
			System.out.println(" "+i+" -> "+ colorNames[colors[i]]);
		}
	}
	
	public void solve (int m)
	{
		if(!solveGraphColoring(0,m))
		{
			System.out.println("No solution :( ");
		}
	}
	
	public static void main (String[] args)
	{
		int [] [] graph = {
			{0,1,1,1},
			{1,0,1,0},
			{1,1,0,1},
			{1,0,1,0}
	       };
	   int numColors=3;
	   
	   GraphColor gc= new GraphColor(graph,numColors);
	   gc.solve(numColors);
	}
}