// Exercise 18.20 Solution: Maze.java
// Program traverses a maze.

public class Maze
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
      boolean result = mazeTraversal( ROW_START, COLUMN_START );

      if ( !result )
         System.out.println( "Maze has no solution." );
   } // end method traverse

   // traverse maze recursively
   public boolean mazeTraversal( int row, int column )
   {
       // TO BE COMPLETED
       
       
       
       
       
   } // end method mazeTraversal


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
} // end class Maze

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
