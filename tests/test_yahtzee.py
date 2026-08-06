import random
import unittest

from yahtzee import (
    _bonus,
    create_empty_scorecard,
    evaluate,
    has_straight,
    reroll,
    roll_dice,
)


class YahtzeeRulesTests(unittest.TestCase):
    def test_empty_scorecard_has_thirteen_unused_categories(self):
        card = create_empty_scorecard()
        self.assertEqual(len(card), 13)
        self.assertTrue(all(score is None for score in card.values()))

    def test_rolls_stay_within_die_bounds(self):
        random.seed(42)
        dice = roll_dice(100)
        self.assertEqual(len(dice), 100)
        self.assertTrue(all(1 <= die <= 6 for die in dice))

    def test_straights_ignore_duplicate_faces(self):
        self.assertTrue(has_straight([1, 2, 3, 4, 4], 4))
        self.assertFalse(has_straight([1, 1, 3, 4, 5], 5))

    def test_scoring_patterns(self):
        full_house = evaluate([2, 2, 3, 3, 3])
        self.assertEqual(full_house["full_house"], 25)
        self.assertEqual(full_house["three_of_a_kind"], 13)

        yahtzee = evaluate([6, 6, 6, 6, 6])
        self.assertEqual(yahtzee["yahtzee"], 50)
        self.assertEqual(yahtzee["chance"], 30)

    def test_upper_bonus_threshold(self):
        self.assertEqual(_bonus(62), 0)
        self.assertEqual(_bonus(63), 35)

    def test_reroll_preserves_a_complete_hand(self):
        self.assertEqual(reroll([6, 5, 4, 3, 2], [6, 5, 4, 3, 2]), [2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
