#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import unittest
from GameOfLife import GameOfLife
from Cell import Cell

class TestGameOfLife(unittest.TestCase):

  def setUp(self):
    self.gameValidateEnum=GameOfLife(2,2,[['.','*'],
                                          ['*','.']])  

    self.gameValidateCountNeighbours=GameOfLife(2,3,[['.','.','.'],
                                                     ['*','.','*']])  

    self.gameValidateNeighbours=GameOfLife(4,8,[['.','.','.','.','.','.','.','.'],
                                                ['.','.','.','.','*','.','.','.'],
                                                ['.','.','.','*','*','.','.','.'],
                                                ['.','.','.','.','.','.','.','.']])

    self.validateKillToReviveCell=GameOfLife(3,2,[['.','*'],
                                                  ['.','.'],
                                                  ['*','.']])       
                                                       
  def testEnumDeadCellMatrix(self):
    self.assertEqual(self.gameValidateEnum.matrix[0][0],Cell.DEAD_CELL)

  def testEnumLivingCellMatrix(self):
    self.assertEqual(self.gameValidateEnum.matrix[0][1],Cell.LIVING_CELL)

  def testCountNeighbours(self):
    self.assertEqual(self.gameValidateCountNeighbours.countNeighbours([(0,0),(0,1),(1,0)]),(1,2))

  def testCountNeighbours2(self):
    self.assertNotEqual(self.gameValidateCountNeighbours.countNeighbours([(0,0),(0,1),(1,0)]),(0,2))

  def testCountNeighboursEmpty(self):
    self.assertEqual(self.gameValidateCountNeighbours.countNeighbours([]),(0,0))

  def testValidateNeighbours(self):
    self.assertEqual(self.gameValidateNeighbours.validateNeighbours(1,3),(3,5))

  def testValidateNeighboursBoundaries1(self):
    self.assertEqual(self.gameValidateNeighbours.validateNeighbours(0,0),(0,3))

  def testValidateNeighboursBoundaries2(self):
    self.assertEqual(self.gameValidateNeighbours.validateNeighbours(3,0),(0,3))

  def testValidateNeighboursBoundaries3(self):
    self.assertNotEqual(self.gameValidateNeighbours.validateNeighbours(0,7),(1,3))

  def testValidateNeighboursBoundaries4(self):
    self.assertNotEqual(self.gameValidateNeighbours.validateNeighbours(3,7),(1,0))
  
  def testkillCell(self):
    self.validateKillToReviveCell.killCell(0,1)
    self.assertEqual(self.validateKillToReviveCell.matrix[0][1],Cell.DEAD_CELL)

  def testkillCellThatIsDead(self):
    self.validateKillToReviveCell.killCell(0,0)
    self.assertNotEqual(self.validateKillToReviveCell.matrix[0][0],Cell.LIVING_CELL)

  def testToReviveCell(self):
    self.validateKillToReviveCell.toReviveCell(2,1)
    self.assertEqual(self.validateKillToReviveCell.matrix[2][1],Cell.LIVING_CELL)

  def testToReviveCellThatIsLife(self):
    self.validateKillToReviveCell.toReviveCell(2,0)
    self.assertNotEqual(self.validateKillToReviveCell.matrix[2][0],Cell.DEAD_CELL)
  
  def testCreateNewGeneration(self):
    game=GameOfLife(4,8,[['*','.','.','.','.','.','.','.'],
                         ['.','.','.','.','*','.','.','.'],
                         ['.','.','.','*','*','.','.','.'],
                         ['.','.','.','.','.','.','.','.']])
    self.assertEqual(game.createNewGeneration() , True)
  
  def testCreateNewGenerationFalse(self):
    game=GameOfLife(4,8,[['.','.','.','.','.','.','.','.'],
                         ['.','.','.','.','.','.','.','.'],
                         ['.','.','.','.','.','.','.','.'],
                         ['.','.','.','.','.','.','.','.']])
    self.assertEqual(game.createNewGeneration() , False)

  def testCreateNewGenerationNotEqual(self):
    game=GameOfLife(4,8,[['.','.','.','.','.','.','.','.'],
                         ['.','.','.','*','*','.','.','.'],
                         ['.','.','.','*','*','.','.','.'],
                         ['.','.','.','.','.','.','.','.']])
    self.assertNotEqual(game.createNewGeneration() , True)

  def testCreateNewGenerationEmpty(self):
    game=GameOfLife(0,0,[[]])
    self.assertEqual(game.createNewGeneration() , False)

  def testGetGenerations(self):
    game=GameOfLife(4,8,[['.','*','.','.','.','.','.','*'],
                         ['.','.','.','.','*','.','.','.'],
                         ['.','.','.','*','*','.','.','.'],
                         ['.','.','.','.','.','*','.','.']])
    self.assertEqual(game.getGenerations(), 3)

  def testGetGenerations2(self):
    game=GameOfLife(4,8,[['.','.','.','.','.','.','.','.'],
                         ['.','.','.','.','*','.','.','.'],
                         ['.','.','.','*','*','.','.','.'],
                         ['.','.','.','.','.','.','.','.']])
    self.assertEqual(game.getGenerations(), 2)

  def testGetGenerations3(self):
    game=GameOfLife(4,8,[['.','.','.','.','.','.','.','.'],
                         ['.','.','.','.','.','.','.','.'],
                         ['.','.','.','.','.','.','.','.'],
                         ['.','.','.','.','.','.','.','.']])
    self.assertEqual(game.getGenerations(), 1)
  
if __name__ == '__main__':
  unittest.main()

#Example when we change the characters
# def testChangeCharacter(self):
# game=GameOfLife(2,2,[['+','-'],['+','-']])
# self.assertEqual(game.createNewGeneration(),True)
# game.printMatrix()