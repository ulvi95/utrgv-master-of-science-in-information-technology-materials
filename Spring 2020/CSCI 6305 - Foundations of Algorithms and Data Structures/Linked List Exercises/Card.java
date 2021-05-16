// Fig. 7.9: Card.java
// Card class represents a playing card.
package com.deitel.ch22;

public class Card implements Comparable<Card>
{
   private String face; // face of card ("Ace", "Deuce", ...)
   private String suit; // suit of card ("Hearts", "Diamonds", ...)

   // two-argument constructor initializes card's face and suit
   public Card( String cardFace, String cardSuit )
   {
      face = cardFace; // initialize face of card
      suit = cardSuit; // initialize suit of card
   } // end two-argument Card constructor

   // return String representation of Card
   public String toString() 
   { 
      return face + " of " + suit;
   } // end method toString
      
   @Override
   public boolean equals(Object o) 
   {
        Card other = (Card) o;
        return this.face == other.face && this.suit == other.suit;
   }
   
   @Override
   public int compareTo(Card other) 
   {
        int thisFace;
        switch ( this.face )
        {
            case "Deuce": thisFace = 2; break;
            case "Three": thisFace = 3; break;
            case "Four": thisFace = 4; break;
            case "Five": thisFace = 5; break;
            case "Six": thisFace = 6; break;
            case "Seven": thisFace = 7; break;
            case "Eight": thisFace = 8; break;
            case "Nine": thisFace = 9; break;
            case "Ten": thisFace = 10; break;
            default: thisFace = 11; break;
        }
        int otherFace;
        switch ( other.face )
        {
            case "Deuce": otherFace = 2; break;
            case "Three": otherFace = 3; break;
            case "Four": otherFace = 4; break;
            case "Five": otherFace = 5; break;
            case "Six": otherFace = 6; break;
            case "Seven": otherFace = 7; break;
            case "Eight": otherFace = 8; break;
            case "Nine": otherFace = 9; break;
            case "Ten": otherFace = 10; break;
            default: otherFace = 11; break;
        }
        if (thisFace > otherFace)
            return 1;
        else if (thisFace == otherFace)
            return 0;
        else
            return -1;
   }
   
} // end class Card


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
