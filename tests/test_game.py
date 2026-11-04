import unittest
from game import new_game, available_actions, apply_action, is_win, is_game_over

class TestMysteryIsland(unittest.TestCase):
    def setUp(self):
        self.player = new_game("Temple")

    def test_new_game_starts_correctly(self):
        self.assertEqual(self.player["name"], "Temple")
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertEqual(self.player["inventory"], [])
        self.assertFalse(self.player["game_over"])
        self.assertFalse(self.player["won"])

    def test_invalid_action_does_not_change_state(self):
        apply_action(self.player, "fly")
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_valid_move_changes_location_and_energy(self):
        apply_action(self.player, "go jungle")
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_wrong_direction_does_not_consume_energy(self):
        apply_action(self.player, "go lighthouse")
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_rope_can_be_collected_once(self):
        apply_action(self.player, "go jungle")
        apply_action(self.player, "take rope")
        apply_action(self.player, "take rope")
        self.assertEqual(self.player["inventory"].count("rope"), 1)

    def test_bridge_requires_rope(self):
        apply_action(self.player, "go jungle")
        apply_action(self.player, "go cave")
        apply_action(self.player, "go old bridge")

        energy_before = self.player["energy"]
        result = apply_action(self.player, "go lighthouse")

        self.assertIn("rope", result)
        self.assertEqual(self.player["location"], "Old Bridge")
        self.assertEqual(self.player["energy"], energy_before)

    def test_lantern_can_be_collected_once(self):
        apply_action(self.player, "go jungle")
        apply_action(self.player, "go cave")
        apply_action(self.player, "take lantern")
        apply_action(self.player, "take lantern")
        self.assertEqual(self.player["inventory"].count("lantern"), 1)

    def test_lighthouse_requires_lantern(self):
        apply_action(self.player, "go jungle")
        apply_action(self.player, "take rope")
        apply_action(self.player, "go cave")
        apply_action(self.player, "go old bridge")
        apply_action(self.player, "go lighthouse")
        result = apply_action(self.player, "light beacon")

        self.assertIn("lantern", result)
        self.assertFalse(is_win(self.player))

    def test_correct_path_wins_game(self):
        apply_action(self.player, "go jungle")
        apply_action(self.player, "take rope")
        apply_action(self.player, "go cave")
        apply_action(self.player, "take lantern")
        apply_action(self.player, "go old bridge")
        apply_action(self.player, "go lighthouse")
        apply_action(self.player, "light beacon")

        self.assertTrue(is_win(self.player))
        self.assertTrue(is_game_over(self.player))

    def test_running_out_of_energy_causes_loss(self):
        apply_action(self.player, "go jungle")
        apply_action(self.player, "go beach")
        apply_action(self.player, "go jungle")
        apply_action(self.player, "go beach")
        apply_action(self.player, "go jungle")

        self.assertEqual(self.player["energy"], 0)
        self.assertTrue(is_game_over(self.player))
        self.assertFalse(is_win(self.player))

    def test_quit_ends_game(self):
        apply_action(self.player, "quit")
        self.assertTrue(is_game_over(self.player))
        self.assertFalse(is_win(self.player))

    def test_replay_creates_fresh_state(self):
        self.player["inventory"].append("rope")
        self.player["energy"] = 2

        new_player = new_game("Temple")

        self.assertEqual(new_player["energy"], 5)
        self.assertEqual(new_player["inventory"], [])
        self.assertEqual(new_player["location"], "Beach")

if __name__ == "__main__":
    unittest.main()
