/******************************
 * Ulvi Bajarani
 * CSCI 6302.01 Fall 2019 *
 * Lab #1: Numbers *             
 ******************************/                                                                       
import java.util.*;

public class Numbers_bajaraniUlvi {
    public static void main(String args[]){
        
    Scanner Number = new Scanner(System.in);
    int enterNumber, enterInteger, enterMultiply1, enterMultiply2, fiveDigits;
            
    // The Menu.
    System.out.println("Choose the menu, entering the proper digit:");    
    System.out.println("1. Odd or Even?");
    System.out.println("2. Multiply or not?");
    System.out.println("3. Print all 5 digits");
    System.out.println("4. Exit the program");
    System.out.println("Enter the digit:");
    enterNumber = Number.nextInt();
    
    // The first option.
    if(enterNumber == 1)
    {   
        
        System.out.println("Enter the integer: ");
        enterInteger = Number.nextInt();
        
        if (enterInteger % 2 == 0)
            {
                System.out.printf("%d is even\n", enterInteger);
            }
            else
            {
                System.out.printf("%d is odd\n", enterInteger);
            }
    }
    // The second option.
    else if(enterNumber == 2){
        
        
        System.out.println("Enter the first multiply: ");
        enterMultiply1 = Number.nextInt();
        
        
        System.out.println("Enter the second multiply: ");
        enterMultiply2 = Number.nextInt();
        
        if((enterMultiply1 > enterMultiply2) && (enterMultiply1 % enterMultiply2 == 0))
                {
            System.out.printf("%d and %d are multiplies. \n", enterMultiply1, enterMultiply2);
    }
        else{
                    System.out.printf("%d and %d are not multiplies. \n", enterMultiply1, enterMultiply2);
                    }
}
    // The third option.
    else if(enterNumber == 3)
    {
        
        System.out.println("Enter five digits numbers:");
        fiveDigits = Number.nextInt();
        if ((fiveDigits >= 10000) && (fiveDigits <= 99999)){
            int a, b, c, d, e;
            a = fiveDigits / 10000;
            b = fiveDigits / 1000;
            c = fiveDigits / 100;
            d = fiveDigits / 10;
            e = fiveDigits;
            
            System.out.printf("The digits are: %d   %d   %d   %d   %d\n", a, b-a*10, c-b*10, d-c*10, e-d*10);
        }
        else {
            System.out.printf("The %d is not five digited number\n", fiveDigits);
        }
    // The fourth (quit) option.    
    }
    else if(enterNumber == 4)
    {
        System.out.println("You have quited from the program.");
    }
    // The error function. 
    else {
        System.out.println("You haven't entered proper digits.");
    }
}
}

