#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Yukun Shan
# email: yshan@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Haichen Xu
# partner's email: xhcbu@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for row in range(3):
            for col in range(3):
                self.tiles[row][col] = digitstr[row*3 + col]
                if self.tiles[row][col] == '0':
                    self.blank_r = row
                    self.blank_c = col
        ### Add your other method definitions below. ###

    def __repr__(self):
        """ returns a string representation of a Board object
        """
        s = ''
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] == '0':
                    s += '_'
                else:
                    s += self.tiles[row][col] 
                s += ' '
            s += '\n'
        return s
    
    def move_blank(self, direction):
        """ that takes as input a string direction that specifies the
        direction in which the blank should move, and that attempts to
        modify the contents of the called Board object accordingly.
        Not all moves are possible on a given Board; for example, it
        isn’t possible to move the blank down if it is already in the 
        bottom row. The method should return True or False to indicate 
        whether the requested move was possible.
        """
        if direction != 'up' and \
           direction != 'down' and \
           direction != 'left' and \
           direction != 'right':
               return False
        else:
            if direction == 'up':
                if (self.blank_r - 1) in range(3):
                    self.blank_r -= 1
                    self.tiles[self.blank_r + 1][self.blank_c] = self.tiles[self.blank_r][self.blank_c]
                    self.tiles[self.blank_r][self.blank_c] = '0'
                    return True
                else:
                    return False
                
            elif direction == 'down':
                if (self.blank_r + 1) in range(3):
                    self.blank_r += 1
                    self.tiles[self.blank_r - 1][self.blank_c] = self.tiles[self.blank_r][self.blank_c]
                    self.tiles[self.blank_r][self.blank_c] = '0'
                    return True
                else:
                    return False
                
            elif direction == 'left':
                if (self.blank_c - 1) in range(3):
                    self.blank_c -= 1
                    self.tiles[self.blank_r][self.blank_c + 1] = self.tiles[self.blank_r][self.blank_c]
                    self.tiles[self.blank_r][self.blank_c] = '0'
                    return True
                else:
                    return False
                
            elif direction == 'right':
                if (self.blank_c + 1) in range(3):
                    self.blank_c += 1
                    self.tiles[self.blank_r][self.blank_c - 1] = self.tiles[self.blank_r][self.blank_c]
                    self.tiles[self.blank_r][self.blank_c] = '0'
                    return True
                else:
                    return False
 
    def digit_string(self):
        """ returns the string of digits that was used when creating the Board. 
        However, this won’t always be the case, because the string returned by 
        digit_string() should reflect any changes that have been made to the
        tiles.
        """
        s = ''
        for row in range(3):
            for col in range(3):
                s += self.tiles[row][col]
        return s
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy 
        of the called object (i.e., of the object represented by self).
        """
        new_board = Board(self.digit_string())
        return new_board
        
        
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board 
        object that are not where they should be in the goal state. You 
        should not include the blank cell in this count, even if it’s not
        where it should be in the goal state.
        """
        result = 0
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] != '0':
                    if self.tiles[row][col] != GOAL_TILES[row][col]:
                        result += 1
        return result
    
    def num_false_row(self):
        """ counts and returns the number of tiles in the called Board object 
        that have differenct rows compared to the Goal state.
        """
        result = 0
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] != '0':
                    if self.tiles[row][col] == '1':
                        if row != 0:
                            result += 1
                    elif self.tiles[row][col] == '2':
                        if row != 0:
                            result += 1
                    elif self.tiles[row][col] == '3':
                        if row != 1:
                            result += 1
                    elif self.tiles[row][col] == '4':
                        if row != 1:
                            result += 1
                    elif self.tiles[row][col] == '5':
                        if row != 1:
                            result += 1
                    elif self.tiles[row][col] == '6':
                        if row != 2:
                            result += 1
                    elif self.tiles[row][col] == '7':
                        if row != 2:
                            result += 1
                    elif self.tiles[row][col] == '8':
                        if row != 2:
                            result += 1 
        return result
    
    def num_false_col(self):
        """ counts and returns the number of tiles in the called Board object
        tha have differenct columns compared to the Goal state.
        """
        result = 0
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] != '0':
                    if self.tiles[row][col] == '1':
                        if col != 1:
                            result += 1
                    elif self.tiles[row][col] == '2':
                        if col != 2:
                            result += 1
                    elif self.tiles[row][col] == '3':
                        if col != 0:
                            result += 1
                    elif self.tiles[row][col] == '4':
                        if col != 1:
                            result += 1
                    elif self.tiles[row][col] == '5':
                        if col != 2:
                            result += 1
                    elif self.tiles[row][col] == '6':
                        if col != 0:
                            result += 1
                    elif self.tiles[row][col] == '7':
                        if col != 1:
                            result += 1
                    elif self.tiles[row][col] == '8':
                        if col != 2:
                            result += 1 
        return result
        
        
        
        
    def __eq__(self, other):
        """ can be called when the == operator is used to compare two Board
        objects. The method should return True if the called object (self)
        and the argument (other) have the same values for the tiles attribute,
        and False otherwise.
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        









