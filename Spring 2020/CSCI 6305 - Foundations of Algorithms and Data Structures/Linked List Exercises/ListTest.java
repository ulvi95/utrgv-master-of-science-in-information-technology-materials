// Fig. 22.5: ListTest.java
// ListTest class to demonstrate List capabilities.
import com.deitel.ch22.List;
import com.deitel.ch22.Card;
import com.deitel.ch22.EmptyListException;
import java.util.Random;

public class ListTest 
{
   public static void main( String[] args )
   {
      Random randomNumbers = new Random();
      int position;
              
      /*
      List< Integer > list = new List< Integer >(); // create a List

      // insert integers in list
      list.insertAtFront( -1 );
      list.print();
      list.insertAtFront( 0 );
      list.print();
      list.insertAtBack( 1 );
      list.print();
      list.insertAtBack( 5 );
      list.print();

      // remove objects from list; print after each removal
      try 
      { 
         int removedItem = list.removeFromFront();
         System.out.printf( "\n%d removed\n", removedItem );
         list.print();

         removedItem = list.removeFromFront();
         System.out.printf( "\n%d removed\n", removedItem );
         list.print();

         removedItem = list.removeFromBack();
         System.out.printf( "\n%d removed\n", removedItem );
         list.print();

         removedItem = list.removeFromBack();
         System.out.printf( "\n%d removed\n", removedItem );
         list.print();
      } // end try
      catch ( EmptyListException emptyListException ) 
      {
         emptyListException.printStackTrace();
      } // end catch
      
      list.insertAtFront( 8 );
      list.print();
      list.insertAtFront( 4 );
      list.print();
      list.insertAtBack( 3 );
      list.print();
      list.insertAtBack( 2 );
      list.print();
      
      int key = 3;
      position = list.linearSearch(key);
      if ( position == -1 )
          System.out.printf( "Item: %d was not found in the list.\n", key );
      else
          System.out.printf( "Item: %d was found at position %d in the list.\n", key, position );
      
      */
      
      String[] faces = { "Ace", "Deuce", "Three", "Four", "Five", "Six", 
         "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King" };
      String[] suits = { "Hearts", "Diamonds", "Clubs", "Spades" };
      
      List< Card > deck1 = new List< Card >("Deck1"); // create a List
      Card card;
      int face, suit;
      
      for ( int i=0; i<5; i++ )
      {
      
        face =  randomNumbers.nextInt( 13 );
        suit =  randomNumbers.nextInt( 4 );
        card = new Card( faces[ face ], suits[ suit ] );
        deck1.insertInOrder(card);
        //deck1.insertAtFront(card);
        deck1.print();
      
      }
      
      List< Card > deck2 = new List< Card >("Deck2"); // create a List
      
      for ( int i=0; i<5; i++ )
      {
      
        face =  randomNumbers.nextInt( 13 );
        suit =  randomNumbers.nextInt( 4 );
        card = new Card( faces[ face ], suits[ suit ] );
        deck2.insertInOrder(card);
        deck2.print();
      
      }
      
      deck1.join(deck2);
      
      card = new Card( faces[ 0 ], suits[ 0 ] );
      deck1.insertInOrder(card);
      
      
      System.out.printf( "\n\n\n");
      deck1.print();
      
      Card keyCard = new Card( faces[ 0 ], suits[ 0 ] );
      position = deck1.linearSearch(keyCard);
      if ( position == -1 )
          System.out.printf( "Item: %s was not found in the list.\n", keyCard );
      else
          System.out.printf( "Item: %s was found at position %d in the list.\n", keyCard, position );
      
      
   } // end main
} // end class ListTest


/**************************************************************************
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
