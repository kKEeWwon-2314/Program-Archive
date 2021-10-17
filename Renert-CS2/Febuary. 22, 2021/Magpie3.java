/**
 * A program to carry on conversations with a human user.
 * This is the initial version that:  
 * <ul><li>
 *       Uses indexOf to find strings
 * </li><li>
 * 		    Handles responding to simple words and phrases 
 * </li></ul>
 * This version uses a nested if to handle default responses.
 * @author Laurie White (CS2 Class Remix)
 * @version Febuary 2021
 */
public class Magpie3
{
	private String[] randomResponses = {
		"Interesting, tell me more.",
		"Hmmm.",
		"Do you really think so?",
		"You don't say.",
		"Cool!",
		"Alright.",
		"Are you sure about that?"
	};

	/**
	 * Get a default greeting 	
	 * @return a greeting
	 */
	public String getGreeting()
	{
		return "Hello, let's talk.";
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
		// String r1 = "I like MCHC"; 

		String response = "";
		if (findKeyword(statement, "no") >= 0)
		{
			response = "Why?";
		}
		else if (findKeyword(statement, "I like ") >= 0)
		{
			// System.out.println(findKeyword(statement, "I like"));
			int i = findKeyword(statement, "I like");
			String like = statement.substring(i + 7);

			response = "What do you like about " + like + "?";
		}
		else if (findKeyword(statement, "mother") >= 0
				|| findKeyword(statement, "father") >= 0
				|| findKeyword(statement, "sister") >= 0
				|| findKeyword(statement, "brother") >= 0)
		{
			response = "Tell me more about your family.";
		}
		else if (findKeyword(statement, "Hello") >= 0
				|| findKeyword(statement, "Wassup") >= 0
				|| findKeyword(statement, "Sure") >= 0)
		{
			response = "Let's get talking.";
		}
		else if ((findKeyword(statement, "cat") >= 0) 
				|| (findKeyword(statement, "dog") >= 0) 
				|| (findKeyword(statement, "bird") >= 0)) 
		{
			response = "Tell me more about your pets!";
		}
		else if ((findKeyword(statement, "Kevin") >= 0)
				|| findKeyword(statement, "Leif") >= 0
				|| findKeyword(statement, "Anika") >= 0
				|| findKeyword(statement, "Shailah") >= 0) 
		{
			response = "They're in your CS2 class, right?";
		}
		else if ((findKeyword(statement, "programming") >= 0)
				|| findKeyword(statement, "code") >= 0
				|| findKeyword(statement, "development") >= 0
				|| findKeyword(statement, "git") >= 0) 
		{
			response = "Tell me more about coding.";
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
	 * example, "I know" does not contain "no").
	 * 
	 * @param statement
	 *            the string to search
	 * @param goal
	 *            the string to search for
	 * @param startPos
	 *            the character of the string to begin the
	 *            search at
	 * @return the index of the first occurrence of goal in
	 *         statement or -1 if it's not found
	 */
	private int findKeyword(String statement, String goal, int startPos)
	{
		String phrase = statement.trim();
		phrase = phrase.replaceAll("\\s", ".");
		goal = goal.replaceAll("\\s", ".");

		// The only change to incorporate the startPos is in the line below
		int psn = phrase.toLowerCase().indexOf(
				goal.toLowerCase(), startPos);

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
				// "I like dogs"
				// psn = 7
				// phrase.substring(psn -1, psn)
				// == " "
			}
			if (psn + goal.length() < phrase.length())
			{
				after = phrase.substring(
						psn + goal.length(),
						psn + goal.length() + 1)
						.toLowerCase();
			}

			// If before and after aren't letters, we've
			// found the word
			boolean beforeChar = ((before.compareTo("a") < 0) || (before.compareTo("z") > 0)); // before is not a
			
			boolean afterChar = ((after.compareTo("a") < 0) || (after.compareTo("z") > 0));

			// This section detects if we are using a plural form of our goal word
			if (!afterChar && (after.equals("s"))) {

				// Make sure the character after the s is not a letter.
				// Prevents cases where the word "nose" triggers the keyword "no", for example
				after = " ";

				if ((psn + goal.length() + 1) < phrase.length())
				{
					after = phrase.substring(
							psn + goal.length() + 1,
							psn + goal.length() + 2)
							.toLowerCase();
				}
				// "nose"
				// after = "e"
				boolean afterPlural = ((after.compareTo("a") < 0) || (after.compareTo("z") > 0));

				if (afterPlural) {
					afterChar = true;
				}
			}

			if (beforeChar && afterChar)
			{
				return psn;
			}

			// The last position didn't work, so let's find the next, if there is one.
			psn = phrase.indexOf(goal.toLowerCase(),
					psn + 1);

		}

		return -1;
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
	private int findKeyword(String statement, String goal)
	{
		return findKeyword(statement, goal, 0);
	}

	/**
	 * Pick a default response to use if nothing else fits.
	 * @return a non-committal string
	 */
	private String getRandomResponse()
	{
		double r = Math.random();
		int whichResponse = (int)(r * randomResponses.length);
		String response = "";

		response = randomResponses[whichResponse];

		return response;
	}
}
