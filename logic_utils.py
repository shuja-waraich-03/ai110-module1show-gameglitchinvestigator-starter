

# Fix: AI helped move it from app.py to logic_utils.py but it did not fix the logic itself, i had to tell it to make the range for harder larger, it assumed that the ranges were correct
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
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
    Compare guess to secret and return outcome.

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        guess_val = int(guess)
        secret_val = int(secret)
    except (TypeError, ValueError):
        raise ValueError("guess and secret must be numeric")

    if guess_val == secret_val:
        return "Win"
    if guess_val > secret_val:
        return "Too High"
    return "Too Low"

#Fix: i had to tell the AI how the logic should work
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in {"Too High", "Too Low"}:
        return current_score - 5

    return current_score
