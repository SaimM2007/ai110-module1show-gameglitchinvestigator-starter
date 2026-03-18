# FIX: Refactored get_range_for_difficulty, parse_guess, check_guess, and update_score into logic_utils.py using Copilot Agent mode

def get_range_for_difficulty(difficulty: str):
    """
    Return the (low, high) number range for a given difficulty level.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard".

    Returns:
        A tuple (low, high) representing the inclusive guessing range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse raw user input into an integer guess.

    Args:
        raw: The raw string input from the user.

    Returns:
        A tuple (ok, guess_int, error_message) where ok is a bool,
        guess_int is the parsed integer or None, and error_message is a
        string or None.
    """
    if raw is None:
        return False, None, "Enter a guess."
    if raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):
    """
    Compare a guess to the secret number and return the outcome and hint.

    Args:
        guess: The player's guessed integer.
        secret: The secret number to guess.

    Returns:
        A tuple (outcome, message) where outcome is "Win", "Too High", or
        "Too Low", and message is a hint string for the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    try:
        # FIX: swapped return messages so Too High says Go LOWER and Too Low says Go HIGHER, refactored into logic_utils.py using Copilot Agent mode
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update the player's score based on the outcome of a guess.

    Args:
        current_score: The player's score before this guess.
        outcome: The result of the guess, one of "Win", "Too High", or "Too Low".
        attempt_number: The current attempt number, used to scale win points.

    Returns:
        The updated score as an integer.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points
    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5
    if outcome == "Too Low":
        return current_score - 5
    return current_score