from enum import Enum
from random import\
	randint,\
	seed


seed(20220522)


_RPS_NAMES = ("r", "p", "s")
_RPS_NAMES_MAX_I = len(_RPS_NAMES) - 1


class RpsElement:

	def __init__(self, name, winner):
		self._name = name
		self._winner = winner

	def __eq__(self, other):
		return self._name == other._name

	def __gt__(self, other):
		return self._name == other._winner

	def __lt__(self, other):
		return self._winner == other._name

	def fight(self, other):
		result = 0

		if self > other:
			result = 1
		
		elif self < other:
			result = -1

		return result


class RpsChoice(Enum):
	ROCK = RpsElement("r", "p")
	PAPER = RpsElement("p", "s")
	SCISSORS = RpsElement("s", "r")

	@staticmethod
	def from_name(name):
		choice = None

		for member in RpsChoice:

			if member.value._name == name:
				choice = member

		return choice


def rand_elem_name():
	rand_index = randint(0, _RPS_NAMES_MAX_I)
	elem_name = _RPS_NAMES[rand_index]
	return elem_name


def rps_game(elem1, elem2=None):
	if isinstance(elem1, str):
		elem1 = RpsChoice.from_name(elem1).value

	if elem2 is None:
		elem2 = RpsChoice.random().value

	elif isinstance(elem2, str):
		elem2 = RpsChoice.from_name(elem2).value

	return elem1.fight(elem2)
