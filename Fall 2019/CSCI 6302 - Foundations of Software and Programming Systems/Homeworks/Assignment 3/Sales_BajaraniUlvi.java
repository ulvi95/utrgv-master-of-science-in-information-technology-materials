/****************************************************************
 * Ulvi Bajarani   CSCI 6302.01 Fall 2019     Lab#: XX      *
 *                                                          *
  ****************************************************************/


// Program calculates sales, based on an input of product
// number and quantity sold
import java.util.Scanner;

public class Sales
{
   // calculates sales for 5 products
   public static void main( String args[] )
   {
      Scanner input = new Scanner( System.in );
      
      double product1 = 0; // amount sold of first product
      double product2 = 0; // amount sold of second product
      double product3 = 0; // amount sold of third product
      double product4 = 0; // amount sold of fourth product
      double product5 = 0; // amount sold of fifth product

      /* Ask the user to enter product number */ 
      
      System.out.print("Enter product number (1-5) (0 to stop): ");
      int productNumber = input.nextInt();
      

      /* Create while statement that loops until sentinel is entered */
      
      /* If product number is not in 1-5, test if product number is not 0 */
      while (productNumber != 0)
      {
          /* Determine whether user's product number is in 1-5 */
          
          if ((productNumber > 0) && (productNumber <= 5))
          {
              /* If so, ask user to input the quantity sold */
              System.out.print("Enter quantity sold: ");
              int productQuantitySold = input.nextInt();
              
              /* Write a switch statement here that will compute the total
               for that product */
              
              switch (productNumber)
              {
                  case 1: product1 = product1 + productQuantitySold * 2.98;
                  break;
                  case 2: product2 = product2 + productQuantitySold * 4.50;
                  break;
                  case 3: product3 = product3 + productQuantitySold * 9.98;
                  break;
                  case 4: product4 = product4 + productQuantitySold * 4.49;
                  break;
                  case 5: product5 = product5 + productQuantitySold * 6.87;
                  break;
              }
          }
          else
          {
              /* Display error message for invalid product number */
              System.out.println("Invalid product number, please enter right one.");
          }
          
          /* Ask the user to enter another product number */
          System.out.print("Enter product number (1-5) (0 to stop): ");
          productNumber = input.nextInt();
      
      }
      /* end while loop */

      // print summary
      System.out.println();
      System.out.printf( "Product 1: $%.2f\n", product1 );
      System.out.printf( "Product 2: $%.2f\n", product2 );
      System.out.printf( "Product 3: $%.2f\n", product3 );
      System.out.printf( "Product 4: $%.2f\n", product4 );
      System.out.printf( "Product 5: $%.2f\n", product5 );
      /* write code here for the rest of the summary message it should contain
         the totals for the rest of the products, each on its own line */
   } // end main
} // end class Sales

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