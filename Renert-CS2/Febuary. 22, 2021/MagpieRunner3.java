import java.util.Scanner;

/**
 * A simple class to run the Magpie class.
 * @author Laurie White (CS2 Class Remix)
 * @version Febuary 2021
 */
public class MagpieRunner3
{

	/**
	 * Create a Magpie, give it user input, and print its replies.
	 */
	public static void main(String[] args)
	{
		Magpie3 maggie = new Magpie3();
		
		System.out.println (maggie.getGreeting());
		Scanner sc = new Scanner (System.in);
		String statement = sc.nextLine();
		
		while ((!statement.equals("Bye")) && (!statement.equals("Bye.")) && (!statement.equals("Bye!")))
		{
			System.out.println (maggie.getResponse(statement));
			statement = sc.nextLine();
		}

		sc.close();
	}

}