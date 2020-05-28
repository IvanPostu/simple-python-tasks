from enum import Enum

class Variants(Enum):
  ROCK = 3
  PAPER = 1
  SCISSORS = 2

  @staticmethod
  def min_val():
    return 1

  @staticmethod
  def max_val():
    return 3