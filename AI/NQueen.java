import java.util.Scanner;

class NQueen
{
	static int N;
	
	static boolean isSafe(int[][] board, int row, int col)
	{
		for (int i=0; i<col; i++)
		{
			if (board[row][i]==1)
				return false;
		}
		
		for (int i=row, j=col; i>=0 && j>=0; i--,j--)
		{
			if(board[i][j]==1)
				return false;
		}
		
		for (int i=row, j=col; i<N && j>=0; i++,j--)
		{
			if(board[i][j]==1)
				return false;
		}
	 return true;
	}
	
	static boolean solve(int[][] board, int col)
	{
		if (col>=N)
			return true;
		
		for (int i=0; i<N; i++)
		{
			if(isSafe(board,i,col))
			{
				board[i][col]=1;
				if (solve(board,col+1))
				 {return true;}
			    board[i][col]=0;
			}
		}
		return false;
	}
	
	static void printSolution(int[][] board)
	{
		for(int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				System.out.print(board[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter no of Queens : ");
		N=sc.nextInt();
		
		int[][] board = new int[N][N];
		
		if (solve(board,0))
		{
			System.out.println("Solution found");
			printSolution(board);
		} else 
		{
			System.out.println("Solution does not exist");
		}
		
		sc.close();	
	}
}