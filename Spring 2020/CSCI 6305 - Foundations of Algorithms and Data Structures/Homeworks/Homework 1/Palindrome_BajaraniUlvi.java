/****************************************************************
* Ulvi Bajarani CSCI 6305.01 Spring 2020 Program 1: Palindromes *
****************************************************************/

import java.util.*;

public class Palindrome_BajaraniUlvi
{
// The method to prepare the string. The first method is not case sensitive.
  public static String StringPreparatorNoCaseSensitive (String str)
  {

// an Empty string.     
    String Test = "";

    for (int i = 0; i < str.toCharArray().length; i++)
      {
	// The method isLetter from Character class to check the letter.
	if (Character.isLetterOrDigit(str.charAt(i)))
	  {
	    Test += str.charAt(i);
	  }

      }
    // The method toLowerCase from String class to switch all letters
    String Test2 = Test.toLowerCase();
    return Test2;

  }
  
 // The method to prepare the string. The second method is case sensitive.
  public static String StringPreparatorCaseSensitive (String str)
  {

// an Empty string.     
    String Test = "";

    for (int i = 0; i < str.toCharArray().length; i++)
      {
	// The method isLetter from Character class to check the letter.
	if (Character.isLetterOrDigit(str.charAt(i)))
	  {
	    Test += str.charAt(i);
	  }

      }
    return Test;

  }

  
// The function to calculate the array size and pass the value.
  public static int StringSizeCalculator (String str)
  {
    int StringLast = str.length() - 1;
    return StringLast;
  }

/*
The method takes string, start index (It is defined 0 as default),
and end index of the String array.  
*/
  public static boolean testPalindrome (String str, int start, int end)
  {
    char[] CharTest = str.toCharArray();

    if ((CharTest[start] != CharTest[end]))
      {
	return false;
      }

    else if ((CharTest[start] == CharTest[end])
	     && (end - start == 1 || end - start == 0))
      {
	return true;
      }
    else
        return testPalindrome(str, start+1, end-1);
  }
  
  public static void main(String args[])
  {
    //Testing the methods, let's try:
    Scanner input = new Scanner(System.in);
    System.out.println("Enter the string to check if it is a palindrome and press Enter:");
    
    String checker = input.nextLine();
    System.out.println();
    System.out.printf("%s is %s palindrome if it is no case sensitive.\n", checker, (testPalindrome( StringPreparatorNoCaseSensitive(checker) , 0, StringSizeCalculator(StringPreparatorNoCaseSensitive(checker)) )) ? "a" : "not a");
    System.out.printf("%s is %s palindrome if it is case sensitive.\n", checker, (testPalindrome( StringPreparatorCaseSensitive(checker) , 0, StringSizeCalculator(StringPreparatorNoCaseSensitive(checker)) )) ? "a" : "not a");
  }
}

