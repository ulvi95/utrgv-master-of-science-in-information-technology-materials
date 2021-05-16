/**********************************************************************
* Ulvi Bajarani CSCI 6302.01 Fall 2019 Lab 04: Airline Reservations System *
* *
***********************************************************************/


import java.util.Scanner;

public class Plane_BajaraniUlvi {
    public static void seat_describer(boolean[] seats2)
    {
        System.out.println("F means a Free Place, R Means a reserved place:");
        for(int index = 1; index <= (seats2.length - 1); index++)
        {   
            if (seats2[index] == false)
                System.out.printf("%d F\n", index);
            else
                System.out.printf("%d R\n", index);
        }
        
    }
    public static void main (String args[])
    {
    
    boolean seats[] = new boolean[16];
    int first = 0; // First initialisation of the first class places
    int economy = 0; // First initialisation of the economy class places
    Scanner type = new Scanner(System.in); // Type Scanner 
    
    for (int index = 1; index <= 6; index++) // Couting first class places
    {
    if (seats[index] == false)
    first++;
    }
    for (int index = 7; index <= 15; index++) // Couting first class places
    {
    if (seats[index] == false)
    economy++;
    }
    
    System.out.println("Please type 1 for First Class");
    System.out.println("Please type 2 for Economy");
    System.out.println("Please type 0 to exit");
    int input = type.nextInt();
    int change; // Input for changing decision

    int economy_index = 7; // For indexing cases.
    int first_index = 1; // For indexing cases.
    
while (input != 0 && (first > 0 || economy > 0) )
{
    
    if (input == 1 && first > 0)
    {
        seats[first_index] = true;
        first--;
        System.out.printf("First Class, seat #%d\n", first_index);
        first_index++;
    }
    else if (input == 1 && economy > 0)
    {
    System.out.println("First Class is full. Economy Class?");
    System.out.println("1. Yes, 2. No");
    change = type.nextInt(); // Input for changing decision    
    if (change == 1)
    {
    seats[economy_index] = true;
    economy--;
    System.out.printf("Economy Class, seat #%d\n", economy_index);
    economy_index++;
    }
    else if (change == 2)
    {
    System.out.println("Next flight leaves in 3 hours.");
    }
    }
    
    else if (input == 2 && economy > 0)
    {
            seats[economy_index] = true;
            economy--;
            System.out.printf("Economy Class, seat #%d\n", economy_index);
            economy_index++;
            
    }
                
    
    else if (input == 2 && first > 0)
    {
            System.out.println("Economy Class is full. First Class?");
            System.out.println("1. Yes, 2. No");
            change = type.nextInt(); // Input for changing decision
                
    if (change == 1)
    {
    seats[first_index] = true;
    first--;
    System.out.printf("Economy Class, seat #%d\n", first_index);
    first_index++;
    }
    else if (change == 2)
    {
    System.out.println("Next flight leaves in 3 hours.");
    }
    }
            
    else if (input != 1 && input != 2)
    {
    System.out.println("Wrong input.");
    }
    

    System.out.println("Please type 1 for First Class");
    System.out.println("Please type 2 for Economy");
    System.out.println("Please type 0 to exit");
    input = type.nextInt();

}
    if (first == 0 && economy == 0)
    System.out.println("There is no place.");
    seat_describer(seats);
    System.out.println("The program has done its work. Bye!");
    
  
}

}
    
