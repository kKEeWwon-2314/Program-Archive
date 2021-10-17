import java.util.List;
import java.util.ArrayList;

/**
 * The ElevensBoard class represents the board in a game of Elevens.
 */
public class ElevensBoard extends Board {

	/**
	 * The size (number of cards) on the board.
	 */
	private static final int BOARD_SIZE = 9;

	/**
	 * The ranks of the cards for this game to be sent to the deck.
	 */
	private static final String[] RANKS =
		{"ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"};

	/**
	 * The suits of the cards for this game to be sent to the deck.
	 */
	private static final String[] SUITS =
		{"spades", "hearts", "diamonds", "clubs"};

	/**
	 * The values of the cards for this game to be sent to the deck.
	 */
	private static final int[] POINT_VALUES =
		{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0};

	/**
	 * Flag used to control debugging print statements.
	 * 
	 * [private static final boolean I_AM_DEBUGGING = false;]
	 */
	


	/**
	 * Creates a new <code>ElevensBoard</code> instance.
	 */
	 public ElevensBoard() {
	 	super(BOARD_SIZE, RANKS, SUITS, POINT_VALUES);
	 }

	/**
	 * Determines if the selected cards form a valid group for removal.
	 * In Elevens, the legal groups are (1) a pair of non-face cards
	 * whose values add to 11, and (2) a group of three cards consisting of
	 * a jack, a queen, and a king in some order.
	 * @param selectedCards the list of the indices of the selected cards.
	 * @return true if the selected cards form a valid group for removal;
	 *         false otherwise.
	 */
	@Override
	public boolean isLegal(List<Integer> selectedCards) {
		// Case 1: A pair that adds up to 11
		if (selectedCards.size() == 2) {
			int i1 = selectedCards.get(0);
			int i2 = selectedCards.get(1);
			
			Card c1 = cardAt(i1);
			Card c2 = cardAt(i2);

			if (c1.pointValue() + c2.pointValue() == 11) {
				return true;
			}
		}

		// Case 2: A set of three magique cards
		if (selectedCards.size() == 3) {
			ArrayList<String> ranks = new ArrayList<>();

			int i1 = selectedCards.get(0);
			int i2 = selectedCards.get(1);
			int i3 = selectedCards.get(2);
			
			Card c1 = cardAt(i1);
			Card c2 = cardAt(i2);
			Card c3 = cardAt(i3);

			ranks.add(c1.rank());
			ranks.add(c2.rank());
			ranks.add(c3.rank());

			if (ranks.contains("jack") && ranks.contains("queen") && ranks.contains("king")) {
				return true;
			}
		}

		return false;
	}

	/**
	 * Determine if there are any legal plays left on the board.
	 * In Elevens, there is a legal play if the board contains
	 * (1) a pair of non-face cards whose values add to 11, or (2) a group
	 * of three cards consisting of a jack, a queen, and a king in some order.
	 * @return true if there is a legal play left on the board;
	 *         false otherwise.
	 */
	@Override
	public boolean anotherPlayIsPossible() {
		// If another play is possible, there is at least 1 valid move
		List<Integer> validCards = cardIndexes();

		boolean hasJQK = containsJQK(validCards);
		boolean hasPair = containsPairSum11(validCards);

		if (hasJQK || hasPair) {
			return true;
		}
		return false;
	}

	/**
	 * Check for an 11-pair in the selected cards.
	 * @param selectedCards selects a subset of this board.  It is list
	 *                      of indexes into this board that are searched
	 *                      to find an 11-pair.
	 * @return true if the board entries in selectedCards
	 *              contain an 11-pair; false otherwise.
	 */
	private boolean containsPairSum11(List<Integer> selectedCards) {
		/* *** TO BE IMPLEMENTED IN ACTIVITY 9 *** */
		ArrayList<Integer> pointValues = new ArrayList<>();
		for (Integer index : selectedCards) {
			Card c = cardAt(index);
			pointValues.add(c.pointValue());
		}
		boolean pair1 = (pointValues.contains(1) && pointValues.contains(10));
		boolean pair2 = (pointValues.contains(2) && pointValues.contains(9));
		boolean pair3 = (pointValues.contains(3) && pointValues.contains(8));
		boolean pair4 = (pointValues.contains(4) && pointValues.contains(7));
		boolean pair5 = (pointValues.contains(3) && pointValues.contains(8));

		if (pair1 || pair2 || pair3 || pair4 || pair5) {
			return true;
		}
		return false;
	}

	/**
	 * Check for a JQK in the selected cards.
	 * @param selectedCards selects a subset of this board.  It is list
	 *                      of indexes into this board that are searched
	 *                      to find a JQK group.
	 * @return true if the board entries in selectedCards
	 *              include a jack, a queen, and a king; false otherwise.
	 */
	private boolean containsJQK(List<Integer> selectedCards) {
		/* *** TO BE IMPLEMENTED IN ACTIVITY 9 *** */
		ArrayList<String> ranks = new ArrayList<>();
		for (Integer index : selectedCards) {
			Card c = cardAt(index);
			ranks.add(c.rank());
		}
		// Return true as this is a valid move
		if (ranks.contains("jack") && ranks.contains("queen") && ranks.contains("king")) {
			return true;
		}

		return false;
	}
}
