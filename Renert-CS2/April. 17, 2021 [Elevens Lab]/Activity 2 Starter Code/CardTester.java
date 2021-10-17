/**
 * This is a class that tests the Card class.
 */
public class CardTester {

	/**
	 * The main method in this class checks the Card operations for consistency.
	 *	@param args is not used.
	 */
	public static void main(String[] args) {
		/* *** TO BE IMPLEMENTED IN ACTIVITY 1 *** */
		Card threeOfHearts = new Card("3", "Hearts", 3);
		Card anotherThreeOfHearts = new Card("3", "Hearts", 3);
		Card fiveOfSpades = new Card("5", "Spades", 5);
		Card jackOfClubs = new Card("Jack", "Clubs", 11);

		System.out.println(threeOfHearts);
		System.out.println(fiveOfSpades);
		System.out.println(jackOfClubs);

		System.out.println(threeOfHearts.matches(anotherThreeOfHearts));
		System.out.println(fiveOfSpades.matches(jackOfClubs));
	}
}
