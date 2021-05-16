/****************************************************************
* Ulvi Bajarani CSCI 6305.01 Spring 2020 Program 3: Maze_BajaraniUlvi *
****************************************************************/

public class Maze_BajaraniUlvi
{
   static final int DOWN = 0;
   static final int RIGHT = 1;
   static final int UP = 2;
   static final int LEFT = 3;
   static final int ROW_START = 2;
   static final int COLUMN_START = 0;
   static int move = 0;
   static char maze[][] =
      { { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' },
        { '#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#' },
        { '.', '.', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#' },
        { '#', '#', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#' },
        { '#', '.', '.', '.', '.', '#', '#', '#', '.', '#', '.', '.' },
        { '#', '#', '#', '#', '.', '#', '.', '#', '.', '#', '.', '#' },
        { '#', '.', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#' },
        { '#', '#', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#' },
        { '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#' },
        { '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '.', '#' },
        { '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#' },
        { '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' } };


   // method calls mazeTraversal with correct starting point and direction
   public void traverse()
   {
      boolean result = mazeTraversal( ROW_START, COLUMN_START, maze );

      if ( !result )
         System.out.println( "Maze has no solution." );
      else
      {
          System.out.println( " The solution is:" );
          System.out.println();
          printMaze(); // To describe the initial position.
      }
   } // end method traverse

   //The function to check if the value is available to move.
    public boolean SafetyCheck (int row, int column, char[][] maze)
   {
       return (row >= 0 && column >= 0 && column <= maze[0].length-1 && row <= maze.length && maze[row][column] == '.');
   }
   
    // traverse maze recursively
    public boolean mazeTraversal( int row, int column, char[][] maze)
   {
       // TO BE COMPLETED
       if (column == maze[0].length-1 && maze[row][column] == '.')
       {
           maze[row][column] = 'E'; //The end of the path.
           return true;
       }
       
       if (SafetyCheck(row, column, maze) == true)
       {
       maze[row][column] = 'x';
       if (mazeTraversal(row-1,column, maze) == true) // the Movement to North.
       return true;
       if (mazeTraversal(row,column+1, maze) == true) // the Movement to East.
       return true;
       if (mazeTraversal(row+1,column, maze) == true) // the Movement to South.
       return true;
       if (mazeTraversal(row,column-1, maze) == true) // the Movement to West.
       return true;
       maze[row][column] = '0'; // the correction in the Dead End.
       return false;
       }
       return false;
    }
    
    // end method mazeTraversal


   // draw maze
   public void printMaze()
   {

      // for each space in maze
      for ( int row = 0; row < maze.length; row++ )
      {
         for ( int column = 0; column < maze[ row ].length;
            column++ )
         {
            if ( maze[ row ][ column ] == '0' )
               System.out.print( " ." );
            else
               System.out.print( " " + maze[ row ][ column ] );
         }

       
         System.out.println();
      } // end for

      System.out.println();
   } // end method printMaze
} // end class Maze_BajaraniUlvi

/*************************************************************************
* (C) Copyright 1992-2012 by Deitel & Associates, Inc. and               *
* Pearson Education, Inc. All Rights Reserved.                           *
*                                                                        *
* DISCLAIMER: The authors and publisher of this book have used their     *
* best efforts in preparing the book. These efforts include the          *
* development, research, and testing of the theories and programs        *
* to determine their effectiveness. The authors and publisher make       *
* no warranty of any kind, expressed or implied, with regard to these    *
* programs or to the documentation contained in these books. The authors *
* and publisher shall not be liable in any event for incidental or       *
* consequential damages in connection with, or arising out of, the       *
* furnishing, performance, or use of these programs.                     *
*************************************************************************/
