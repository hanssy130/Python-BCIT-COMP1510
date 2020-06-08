from unittest import TestCase
from A4.question3 import dijkstra


class TestDijkstra(TestCase):
    def test_dijkstra_valid_test(self):
        dutch = ["white", "blue", "blue", "red", "white", "red", "white"]
        dijkstra(dutch)
        solution = ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']
        self.assertEqual(dutch, solution)

    def test_dijkstra_two_items(self):
        test2 = ["blue", "white"]
        dijkstra(test2)
        solution = ["white", "blue"]
        self.assertEqual(test2, solution)

    def test_dijkstra_other_colour(self):
        test2 = ["blue", "white", "black"]
        dijkstra(test2)
        solution = ["white", "blue", "black"]
        self.assertEqual(test2, solution)