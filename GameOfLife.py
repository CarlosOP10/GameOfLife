#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
from Cell import Cell

class GameOfLife:

  def __init__(self,numberOfRows,numberOfColumns,matrix,generation):
    self.numberOfRows=numberOfRows
    self.numberOfColumns=numberOfColumns
    self.matrix=[[]]
    self.numberOfGenerations=1
    self.generation=generation
    for row in range(numberOfRows):
      for column in range(numberOfColumns):
        if matrix[row][column]==Cell.LIVING_CELL.value:
          self.matrix[row].append(Cell.LIVING_CELL)
        else:
          self.matrix[row].append(Cell.DEAD_CELL)
      self.matrix.append([])

  def countNeighbours(self,neighbours):
    numberOfLivingCells=0
    numberOfDeadCells=0
    for row,column in neighbours:
      if self.matrix[row][column]==Cell.LIVING_CELL:
        numberOfLivingCells+=1
      else:
        numberOfDeadCells+=1
    return numberOfLivingCells,numberOfDeadCells

  def validateNeighbours(self,positionRow,positionColumn):
    neighbours=[(positionRow-1,positionColumn-1),(positionRow-1,positionColumn),(positionRow-1,positionColumn+1),
                (positionRow,positionColumn-1),(positionRow,positionColumn+1),(positionRow+1,positionColumn-1),
                (positionRow+1,positionColumn),(positionRow+1,positionColumn+1)]
    neighbours=filter(lambda x: not ((x[0]>self.numberOfRows-1 or x[0]<0) or (x[1]>self.numberOfColumns-1 or x[1]<0)),neighbours)
    return self.countNeighbours(neighbours)

  def killCell(self,positionRow,positionColumn):
    self.matrix[positionRow][positionColumn]=Cell.DEAD_CELL
  
  def toReviveCell(self,positionRow,positionColumn):
    self.matrix[positionRow][positionColumn]=Cell.LIVING_CELL

  def createNewGeneration(self):
    numberOfLivingCells=0
    haveNextGeneration=False
    for row in range(self.numberOfRows):
      for column in range(self.numberOfColumns):
        numberOfLivingCells=self.validateNeighbours(row,column)[0]
        if self.matrix[row][column]==Cell.LIVING_CELL and (numberOfLivingCells<2 or numberOfLivingCells>3):
          self.killCell(row,column)
          haveNextGeneration=True
        elif self.matrix[row][column]==Cell.DEAD_CELL and (numberOfLivingCells==3):
          self.toReviveCell(row,column)
          haveNextGeneration=True

    return haveNextGeneration

  def printMatrix(self):
    for row in range(self.numberOfRows):
      for column in range(self.numberOfColumns):
        print(self.matrix[row][column].value,end=" ")
      print('')
  
  def getGenerations(self):
    count=1
    print("Generation: ", self.numberOfGenerations)
    self.printMatrix()
    while self.createNewGeneration() and count<self.generation:
      count+= 1 
      self.numberOfGenerations+=1
      print("Generation: ", self.numberOfGenerations)
      self.printMatrix()
    return self.numberOfGenerations