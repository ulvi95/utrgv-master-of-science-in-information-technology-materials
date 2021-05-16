/******************************************************************************
* Ulvi Bajarani   CSCI 6302.01 Fall 2019     Lab #2: Sales Commission Calculator   *
*                                                                                  *
******************************************************************************
*/

import java.util.Scanner; // Improting Scanner Method for inputs

public class Sales_BajaraniUlvi {
    public static void main( String[] args ){
        
        double total = 200; // total earnings.
        int counter = 1; // counter for the while statement.
        Scanner productCount = new Scanner(System.in); // Input for the number of products
        int numberOfProduct; // Variable for the number of products 
        
        while (counter <= 4 ){
           System.out.printf("Enter the count of product %d\n", counter);
           numberOfProduct = productCount.nextInt(); // Setting a variable to a Integer input
           
           // Exit statement for illegal number of products.
           if (numberOfProduct < 0)
           {
               
               System.out.println("Illegal number of products.");
               counter = 5;
               
           }
               
           
           // If statement for product N1
           if (counter == 1) 
           {
               
               total = total + numberOfProduct * 239.99 * .09;
           
           }
                   
           
           // If statement for product N2
           if (counter == 2) 
           {
               
               total = total + numberOfProduct * 129.75 * .09;
               
           }
                       
           
           // If statement for product N3
           if (counter == 3) 
           {
               
               total = total + numberOfProduct * 99.95 * .09;
               
           }
           
           // If statement for product N4
           if (counter == 4) 
           {
               
               total = total + numberOfProduct * 350.89 * .09;
               
           }
           
           counter++;
        
        }
        System.out.printf("Total earnings from products is %.2f \n", total); // Printing total earnings.
    }
}
