import turtle as turt

class BattleshipView:
    """ Blueprint for functions involved with the game user interface

    Attributes:
        B1_LEFT (int): Board 1 top-left x position 
        B1_UP (int): Board 1 top-left y position
        B2_LEFT (int): Board 2 top-left x position
        B2_UP (int): Board 2 top-left y position
    """

    # Top Left Board Corner Coordinates
    B1_LEFT = -550
    B1_UP = 250
    B2_LEFT = 50
    B2_UP = 250
    
    def __init__(self):
        """ Setup up screen with two 10 x 10 square boards
        """
        self.NUM_SQ = 10
        self.SIZE_SQ = 50
        self.screen_setup()
        
    def screen_setup(self):
        """ Coordinates screen setup functions
        """
        turt.setup(2 * (self.NUM_SQ * self.SIZE_SQ + 2 * self.SIZE_SQ)  )
        turt.ht()
        self.screen = turt.Turtle()
        self.screen.ht()
        self.screen.speed(15)
        self.draw_screen()
        self.write_text()

    def draw_screen(self):
        """ Draws the borders and lines of the screen
        """
        self.set_board1_corner()
        self.draw_border()
        self.set_board2_corner()
        self.draw_border()
        self.set_board1_corner()
        self.screen.right(90)
        self.draw_vertical_lines()
        self.draw_horizontal_lines()
        self.set_board2_corner()
        self.draw_vertical_lines()
        self.draw_horizontal_lines()

    def write_text(self):
        """ Writes text on the screen
        """
        turt.penup()
        turt.setposition(0, 270) 
        turt.write("BATTLESHIP", align="center", font=("Helvetica", "45", "bold"))
        turt.setposition(-550, -280)
        turt.write("YOUR SHIPS", font=("Helvetica", "20", "bold"))
        turt.setposition(50, -280) 
        turt.write("COMPUTER'S BOARD (CLICK HERE)", font=("Helvetica", "20", "bold"))

        
    def set_board1_corner(self):
        """ Sets the corner for board 1 (player's board)
        """
        left = self.B1_LEFT
        up = self.B1_UP
        self.screen.penup()
        self.screen.setposition(left, up)   
    
    def set_board2_corner(self):
        """ Sets the corner for board 2 (cpu's board)
        """
        left = self.B2_LEFT
        up = self.B2_UP
        self.screen.penup()
        self.screen.setposition(left, up)

    def draw_border(self):
        """ Helper function drawing the board borders
        """
        self.screen.color("white", "#004c4c")
        self.screen.pensize(5)
        self.screen.pendown()
        self.screen.begin_fill()
        for i in range(4):
            self.screen.forward(self.NUM_SQ * self.SIZE_SQ)
            self.screen.right(90)
        self.screen.end_fill()

    def draw_vertical_lines(self):
        """ Helper function drawing the vertical lines
        """
        self.screen.pensize(5)
        self.screen.pendown()
        self.screen.color("white")
        for i in range(self.NUM_SQ // 2):
            self.screen.forward(self.NUM_SQ * self.SIZE_SQ)
            self.screen.left(90)
            self.screen.forward(self.SIZE_SQ)
            self.screen.left(90)
            self.screen.forward(self.NUM_SQ * self.SIZE_SQ)
            self.screen.right(90)
            self.screen.forward(self.SIZE_SQ)
            self.screen.right(90)
            
    def draw_horizontal_lines(self):
        """ Helper function drawing the horizontal lines
        """
        self.screen.pendown()
        self.screen.color("white")
        for i in range(self.NUM_SQ // 2):
            self.screen.forward(self.SIZE_SQ)
            self.screen.right(90)
            self.screen.forward(self.NUM_SQ * self.SIZE_SQ)
            self.screen.left(90)
            self.screen.forward(self.SIZE_SQ)
            self.screen.left(90)
            self.screen.forward(self.NUM_SQ * self.SIZE_SQ)
            self.screen.right(90)

    def draw_ships(self, player_target_board):
        """ Draw ships
        """
        for grid_coor in player_target_board:
            self.screen.penup()
            self.screen.setposition(self.B1_LEFT + self.SIZE_SQ * grid_coor[0], self.B1_UP - self.SIZE_SQ * grid_coor[1])
            self.screen.color("white", "black")
            self.screen.pendown()
            self.screen.begin_fill()
            for i in range(4):
                self.screen.forward(self.SIZE_SQ)
                self.screen.left(90)
            self.screen.end_fill()

    def set_board_pos_miss(self, grid_coor):
        
        if grid_coor[1] >= 0 and grid_coor[1] < self.NUM_SQ:
            self.screen.setposition(self.B1_LEFT + self.SIZE_SQ * grid_coor[0], self.B1_UP - self.SIZE_SQ * grid_coor[1])
        else:
            x =  self.B2_LEFT + self.SIZE_SQ * (grid_coor[1] - 10) 
            y = self.B2_UP - self.SIZE_SQ * (grid_coor[0])  
            self.screen.setposition(x, y)

    def draw_miss(self, grid_coor):
        self.screen.penup()
        self.set_board_pos_miss(grid_coor)
        self.screen.pensize(5)
        self.screen.color("white", "lightblue")
        self.screen.pendown()
        self.screen.begin_fill()
        for i in range(4):
            self.screen.forward(self.SIZE_SQ)
            self.screen.left(90)
        self.screen.end_fill()

    def set_board_pos_hit(self, grid_coor):
        """ Set the board position at the top left corner of the proper board
        """

        # Set at the top left corner of board 1
        if grid_coor[1] >= 0 and grid_coor[1] < self.NUM_SQ:
            x = self.B1_LEFT + self.SIZE_SQ * grid_coor[0] + 19
            y = self.B1_UP - self.SIZE_SQ * grid_coor[1] - 25
            self.screen.setposition(x, y)
        # Set at the top left corner of board 2
        else:
            x =  self.B2_LEFT + self.SIZE_SQ * (grid_coor[1] - 10) + 21
            y = self.B2_UP - self.SIZE_SQ * (grid_coor[0]) - 25
            
            self.screen.setposition(x, y)

    def draw_hit(self, grid_coor):
        """ Draw a star for the square that was a hit
        """
        self.screen.penup()
        self.screen.pensize(2)
        self.set_board_pos_hit(grid_coor)
        self.screen.begin_fill()
        self.screen.pendown()
        self.screen.color("black", "orange")
        for i in range(5):
            self.screen.forward(20)
            self.screen.left(144)
            self.screen.forward(20)
        self.screen.penup()
        self.screen.end_fill()
        



            
