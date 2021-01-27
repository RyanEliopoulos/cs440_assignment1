"""TicTacToe. A module for playing a simple game.

Ryan Paulos
CS450 Assignment 1
1/26/2021



Answer the following questions using your implementation:

1. Is it significantly better to play as 'X', or 'O', or neither?

2. Describe an approach that will allow you to test if all first moves
   are equally good for 'X'. The method should be valid (yields
   correct results) and efficient (use minimal calculation).

3. Using the method described in (2), are all first moves for 'X'
   equally good?  If so, what are the odds that 'X' will win?  If not
   which is the best move for 'X' and how much does it improve the
   odds 'X' will win over the second best move?

3. If 'X' moves into the bottom middle square, what is O's best
   response? (i.e.  the response that is *least likely* to yield a win
   for X)?

4. As the board gets bigger, is X's first move more, or less,
   strategically important?

"""
import sys


def int_input(state, mover):
    print("%s's turn...(0..%d)" % (TicTacToe.Chrs[mover], len(state)-1))
    while True:
        try:
            return int(input())
        except ValueError:
            print("Hmm. try again...")



class TicTacToe():
    """A Class representing the game of TicTacToe."""
    Column = 0
    Row = 1
    Diagonal = 2
    StaleMate = 3
    Chrs = {0: ' ', 1: 'X', -1: 'O'}

    def __init__(self, n=3):
        """Create a n-by-n tic-tac-toe game. n=3 by default"""

        self.n = n
        self.n2 = n**2
        self.reset()

    def reset(self, state=None):
        """Reset the game to the specified state, or to an empty board.

        A state is encoded as a list (or tuple) of elements in {-1, 0, 1}.
        -1 represents an 'O' (player 2), 0 represents an empty space and
        1 represents an 'X' (player 1).  The state is assumed to have an
        appropriate number of 'X's relative to the number of 'O's. A state
        represents a particular board configuration from the top-left, working
        across and then down the board. So, index 0 of the state/board is
        always the upper left corner of the board, index n-1 is the upper
        right corner and index n is one row down from the top on the left side.

        Once the reset method completes, the board instance variable is set
        to a list representation of the state that was passed in.  Thus,
        while the state may be immutable, the *board* instance variable is
        guaranteed to be mutable, and distinct from the state.

        Why is this important? Because we want to be able to
        distinguish the *board* as it exists at the current moment of
        the game. But we also want to represent arbitrary board
        positions that could exist in the past or future (these are
        states).

        """

        if state:
            ones = sum([i for i in state if i == 1])
            negs = sum([1 for i in state if i == -1])
            # ones (x's) go first

            assert ones == negs or ones == negs+1, "X's (1's) go first."
            assert len(state) == self.n2, "the specified state is not the correct length"
            # The game state is kept here as a list of values.
            # 0  indicates the space is unoccupied;
            # 1  indicates the space is occupied by Player 1 (X)
            # -1 indicates the space is occupied by Player 2 (O)
            self.board = list(state)
            s = sum(state)
            if s == 0:
                self.turn = 1  # indicate it's X's turn
            else:
                self.turn = -1 # indicate it's O's turn

        else:
            self.board = [0]*(self.n2)
            self.turn = 1  # if the board is empty, it's X's turn

    def move(self, where):
        """_ Part 1: Implement This Method _

        Make the current player's move at the specified location/index and
        change turns to the next player; where is an index into the board in
        the range 0..(n**2-1)

        If the specified index is a valid move, modify the board,
        change turns and return True.

        Return False if the specified index is unopen, or does not exist"""

        pass

    def show(self, stream=sys.stdout):
        """_ Part 2: Implement This Method _

        Displays the board on the specified stream."""

        pass

    def is_win(self):
        """_ Part 3: Implement This Method _

        Determines if the current board configuration is an end game.
        For a board of size n, a win requires one player to have n tokens
        in a line (vertical, horizontal or diagonal).

        Returns:
         (TicTacToe.Column, c, player): if player wins in column c
         (TicTacToe.Row, r, player): if player wins in row r
         (TicTacToe.Diagonal, 0, player): if player wins via
           a diagonal in the upper-left corner
         (TicTacToe.Diagonal, 1, player): if player wins via a
           diagonal in the upper-right corner
         (TicTacToe.StaleMate, 0, 0): if the game is a stalemate
         False: if the end state is not yet determined
        """
        # column win
        pass

    def describe_win(self, win):
        """Provides a text representation of an end-game state."""
        reason = {TicTacToe.Row: "Row", TicTacToe.Column: "Column",
                  TicTacToe.Diagonal: "Diagonal"}

        if win[0] == TicTacToe.StaleMate:
            return "StaleMate!"
        if win[0] == TicTacToe.Diagonal:
            if win[1] == 0:
                where = "Upper Left"
            else:
                where = "Upper Right"
        else:
            where = "%d" % win[1]
        return "%s (%d) wins @ %s %s" % (TicTacToe.Chrs[win[2]], win[2],
                                         reason[win[0]], where)

    def play(self, movefn=int_input, outstream=None, showwin=True):
        """_ Part 4: Implement This Method _

        Play the game of tictactoe!

        Arguments:
        movefn - a function that will provide possibly valid moves.
        outstream - a stream on which to show the game (if provided)
        showwin - if True, explicitly indicate the game is over
                  and describe the win

        Play should work (roughly) as follows:
         - verify the game is not in an end state
         - if outstream is provided, display the game state (using show())
         - acquire the next move from the movefn (see note below).
         - repeat steps above

         when an end state is reached:
         - print the state (if outstream is defined) and
         - print 'Game Over!' along with a description of the win
           if showwin is True.

        the movefn should take two arguments:
          (1) the game state; and (2) the current player
        """
        pass

    def get_state(self):
        """Get the state of the board as an immutable tuple"""
        return tuple(self.board)


def mc(state, n, debug=False):
    """_ Part 5: Implement This Method _

    Run a monte-carlo experiment in which we play the game using random
    moves.  Start each game at the specified state and run n
    simulations. Record the distribution of outcomes. Monte-carlo
    experiments such as this are used to evaluate states in complex
    games such as chess and go.

    Return a 4-tuple of:
    (games played, % won by player-1, % won by player-2, % stalemates)

    """

    pass


if __name__ == "__main__":
    import argparse
    import random
    parser = argparse.ArgumentParser()
    parser.add_argument("--play", action='store_true')
    parser.add_argument("--state",
                        help="initial state comprised of values in {0,1,2}")
    parser.add_argument("--mc", type=int, default=1000,
                        help="monte carlo trials; default=%(default)s")
    parser.add_argument("-n", type=int, default=3,
                        help="board length,width; default=%(default)s")
    args = parser.parse_args()

    if args.state:
        # At the command line state will come in as a string drawn
        # from {0,1,2}.  -1 is not used here since it's awkwardly
        # two characters.
        assert len(args.state) == args.n**2, \
            "Expected string with %d elements" % (args.n**2)

        # state is input from set {0,1,2} but needs to be translated into
        # {0,1,-1} by changing '2' entries to -1.
        state = [int(z) for z in args.state]
        stateset = set(state)
        assert stateset.issubset(set([0, 1, 2])), \
            "Expected string with elements 0,1,2"
        state = [-1 if s == 2 else s for s in state]
        state = tuple(state)
        print("State is:", state)
    else:
        state = tuple([0]*(args.n**2))

    t = TicTacToe(args.n)
    if args.play:
        t.reset(state)
        t.play(outstream=sys.stdout)

    elif args.mc:
        (games, one, two, stale) = mc(state, args.mc)
        print("%d trials: 1 wins %.2f, "
              "-1 wins %.2f, stalemates %.2f" % (games, one, two, stale))