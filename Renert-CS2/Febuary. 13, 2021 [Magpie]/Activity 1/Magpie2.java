/**
 * A program to carry on conversations with a human user.
 * This is the initial version that:  
 * <ul><li>
 *       Uses indexOf to find strings
 * </li><li>
 * 		    Handles responding to simple words and phrases 
 * </li></ul>
 * This version uses a nested if to handle default responses.
 * @author Laurie White (feat. CS2)
 * 		   iCS2 Remix
 * @version April 2012
 */
public class Magpie2
{
	/**
	 * Get a default greeting 	
	 * @return a greeting
	 */
	public String getGreeting()
	{
		return "Hello, let's talk.";
	}

	private int findKeyWord(String statement, String goal, int startP)
	{
		String phrase = statement.trim();
		// The only change to incorporate the startP is in the line below
		int psn = phrase.toLowerCase().indexOf(
				goal.toLowerCase(), startP);

		// Refinement--make sure the goal isn't part of a
		// word
		while (psn >= 0)
		{
			// Find the string of length 1 before and after
			// the word
			String before = " ", after = " ";
			if (psn > 0)
			{
				before = phrase.substring(psn - 1, psn)
						.toLowerCase();
			}

			

			// If before and after aren't letters, we've found the word. This section detects plurals ending with 's' only.	
			boolean beforeChar = ((before.compareTo("a") < 0) || (before.compareTo("z") > 0));
			boolean afterChar = ((after.compareTo("a") < 0) || (after.compareTo("z") > 0));

			if (!afterChar && (after.equals('s'))); {
				after = " ";

				if (psn + goal.length() < phrase.length())
				{
					after = phrase.substring(
							psn + goal.length() + 1,
							psn + goal.length() + 2)
							.toLowerCase();
				}
				boolean afterPlural = ((after.compareTo("a") < 0) || (after.compareTo("z") > 0));

				if (afterPlural) {
					afterChar = true;
				}
			}

			if (beforeChar && afterChar)
			{
				return psn;
			}

			// The last position didn't work, so let's find
			// the next, if there is one.
			psn = phrase.indexOf(goal.toLowerCase(),
					psn + 1);

		}
		return -1;
	}

	/**
	 * Gives a response to a user statement
	 * 
	 * @param statement
	 *            the user statement
	 * @return a response based on the rules given
	 */
	public String getResponse(String statement)
	{
		String response = "";
		if (findKeyword(statement, "no") >= 0)
		{
			response = "Why so negative?";
		}
		else if ((findKeyword(statement, "mother") >= 0)
				|| findKeyword(statement, "father") >= 0
				|| findKeyword(statement, "sister") >= 0
				|| findKeyword(statement, "brother") >= 0)
		{
			response = "Tell me more about your family.";
		}
		else if ((findKeyword(statement, "dog") >= 0)
				|| (findKeyword(statement, "cat") >= 0)
				|| (findKeyword(statement, "pet bird") >= 0)
				|| (findKeyword(statement, "pet rabbit") >= 0))
		{
			response = "That's cool. Tell me more about your pets.";
		}

		else
		{
			response = getRandomResponse();
		}
		return response;
	}

	/**
	 * Search for one word in phrase. The search is not case
	 * sensitive. This method will check that the given goal
	 * is not a substring of a longer string (so, for
	 * example, "I know" does not contain "no"). The search
	 * begins at the beginning of the string.
	 * 
	 * @param statement
	 *            the string to search
	 * @param goal
	 *            the string to search for
	 * @return the index of the first occurrence of goal in
	 *         statement or -1 if it's not found
	 */
	private int findKeyword(String statement, String goal) {
		return findKeyword(statement, goal);
	}

	/**
	 * Pick a default response to use if nothing else fits.
	 * @return a non-committal string
	 */
	private String getRandomResponse()
	{
		final int NUMBER_OF_RESPONSES = 7;
		double r = Math.random();
		int whichResponse = (int)(r * NUMBER_OF_RESPONSES);
		String response = "";
		
		if (whichResponse == 0)
		{
			response = "Interesting, tell me more.";
		}
		else if (whichResponse == 1)
		{
			response = "Hmmm.";
		}
		else if (whichResponse == 2)
		{
			response = "Do you really think so?";
		}
		else if (whichResponse == 3)
		{
			response = "You don't say.";
		}
		else if (whichResponse == 4)
		{
			response = "Okay...";
		}
		else if (whichResponse == 5)
		{
			response = "Really?";
		}
		else if (whichResponse == 6)
		{
			response = "Cool.";
		}
		else if (whichResponse == 7)
		{
			response = "Strange!";
		}

		return response;
	}
}
