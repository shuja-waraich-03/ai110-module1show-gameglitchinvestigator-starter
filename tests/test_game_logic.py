from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_outcome_to_hint_mapping_is_correct():
    """Verify game hints match each outcome direction."""
    hint_by_outcome = {
        "Win": "🎉 Correct!",
        "Too High": "📉 Go LOWER!",
        "Too Low": "📈 Go HIGHER!",
    }

    assert hint_by_outcome[check_guess(50, 50)] == "🎉 Correct!"
    assert hint_by_outcome[check_guess(60, 50)] == "📉 Go LOWER!"
    assert hint_by_outcome[check_guess(40, 50)] == "📈 Go HIGHER!"


def test_update_score_penalizes_both_wrong_outcomes():
    assert update_score(50, "Too High", 1) == 45
    assert update_score(50, "Too Low", 1) == 45


def test_update_score_win_has_minimum_bonus():
    # Very late win should still award at least +10 points.
    assert update_score(25, "Win", 100) == 35
