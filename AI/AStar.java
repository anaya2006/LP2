import java.util.*;
class Node 
{
	int x,y;
	int f,g,h;
	int[][] state;
	Node parent;
	
	Node (int[][] state, int x, int y, int g, Node parent)
	{
		this.state=state;
		this.parent=parent;
		this.x=x;
		this.y=y;
		this.g=g;
		this.h= calculateHeuristic(state);
		this.f=this.g + this.h;	
	}
	
	static int calculateHeuristic(int [][] state)
	{
		int count=0;
		
		int[][] goal = {
			{1,2,3},
			{8,0,4},
		    {7,6,5}
		};
		
		for(int i=0; i<3; i++)
		{
			for (int j=0; j<3; j++)
			{
				if (state[i][j]!=0 && state[i][j]!=goal[i][j])
				{
					count++;
				}
			}
		}
		return count;	
	}
}

class AStar
{
	static boolean isGoal(int[][] state)
	{
		int[][] goal = {
			{1,2,3},
			{8,0,4},
		    {7,6,5}
		};
		
		return Arrays.deepEquals(state,goal);
	}
	
	static int[][] copy(int[][] state)
	{
		int[][] newState= new int[3][3];
		for (int i=0; i<3; i++)
		{
			newState[i]= state[i].clone();
		}
		return newState;
	}
	
	
	
	static void solve (int[][] state, int x, int y)
	{
		PriorityQueue<Node> open = new PriorityQueue<>(Comparator.comparingInt(n->n.f));
		Set<String> closed = new HashSet<>();
		
		int [] dx = {1,-1,0,0};
		int [] dy = {0,0,-1,1};
		
		open.add(new Node (state,x,y,0,null));
		
		while(!open.isEmpty())
		{
			Node current = open.poll();
			
			if(isGoal(current.state))
			{
				System.out.println("Solution found");
				printPath(current);
				return;
			}
			
			closed.add(Arrays.deepToString(current.state));
			
			for (int i=0; i<4; i++)
			{
				int nx= current.x + dx[i];
				int ny= current.y + dy[i];
				
				if(nx>=0 && nx<3 && ny>=0 && ny<3)
				{
					int [][] newState = copy(current.state);
					newState[current.x][current.y]= newState[nx][ny];
					newState[nx][ny]=0;
					
					if (closed.contains(Arrays.deepToString(newState)))
						continue; // i++
					
					open.add(new Node (newState, nx, ny, current.g+1, current));
					
				}
			}
		}
		System.out.println("Solution does not exist");
	}
	
	static void printPath (Node node)
	{
		if (node==null) return;
		printPath(node.parent);
		printSolution(node.state);
	}
	
	static void printSolution(int[][] state)
	{
		for(int i =0; i<3; i++)
		{
			for (int j=0; j<3; j++)
			{
				System.out.print(state[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public static void main (String[] args)
	{
		int[][] start = {
			{2,8,3},
			{1,6,4},
			{7,0,5}
	     };
		 
		solve(start,2,1);
	}
}