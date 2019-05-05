""" Battleship Game

    This is a program based on the game Battleship. The game is a two player game (Human vs. Computer).
    @LTFast
"""
import battleship_view as view
import battleship_cpu as cpu
import turtle, math, random

class Battleship:
    """ The Battleship class is the main blue print of the game.

    Attributes:
        BOAT_SIZES (dict): References the length of each boatsize
        NUM_SQ (int): Number of squares that make up one side of the game board
        SIZE_SQ (int): Size of each square
        player_score (int): Human player's score

        player_ship_type_points (dict): Tally if a player's ship is sunk
        cpu_ship_type_points (dict): Tally if the computer's ship is sunk

    """

    BOAT_SIZES = {'CARRIER': 5, 'BATTLESHIP': 4, 'CRUISER': 3, 'SUBMARINE': 3, 'DESTROYER': 2}
    NUM_SQ = 10
    SIZE_SQ = 50
    player_score = 0

    player_ship_type_points = {'CARRIER': 0, 'BATTLESHIP': 0, 'CRUISER': 0, 'SUBMARINE': 0, 'DESTROYER': 0}
    cpu_ship_type_points = {'CARRIER': 0, 'BATTLESHIP': 0, 'CRUISER': 0, 'SUBMARINE': 0, 'DESTROYER': 0}

    def __init__(self):
        """ Initializes the boards to be created and places/draws the ships.

        """
        self.screen = view.BattleshipView()
        self.place_ship_mode = True
        self.total_win_points = self.calc_total_win_points()
        
        # Fill boards
        self.player_hist_board = self.fill_initial_board()
        self.cpu_hist_board = self.fill_initial_board()
        self.player_target_board = self.fill_initial_board()
        self.cpu_target_board = self.fill_initial_board()

        # Randomize Boats, Store Ship Locations and Ship Types
        self.player_ship_loc, self.player_ship_type_coordinate = self.randomize_boats(0, 9)
        self.cpu_ship_loc, self.cpu_ship_type_coordinate = self.randomize_boats(0, 9)

        # Create the Target Boards
        self.player_target_board = self.fill_target_board(self.player_target_board, self.player_ship_loc)
        self.cpu_target_board = self.fill_target_board(self.cpu_target_board, self.cpu_ship_loc)

        # Automatically Draw Player's Ships
        self.screen.draw_ships(self.player_ship_loc)
        self.cpu_mode = cpu.CpuMode(self.NUM_SQ)

        # First turn set to the player
        self.turn = "player"       

    def calc_total_win_points(self):
        """ Calculates the number of points needed to win
        Returns:
            total_pts (int): Number of points needed to win
        """
        total_pts = 0
        for boat in self.BOAT_SIZES:
            total_pts += self.BOAT_SIZES[boat]
        return total_pts
        
    def fill_initial_board(self):
        """ Fills a board initially with False values to keep track of guess history
        Returns:
            new_board (list): The new history board containing only False values
        """
        new_board = []
        for row in range(self.NUM_SQ):
            row = []
            for col in range(self.NUM_SQ):
                row.append(False)
            new_board.append(row)
        return new_board
            

    def randomize_boats(self, grid_min, grid_max):
        """ The main function that will ask helper functions to randomize the boats
        Returns:
            ship_locations (list): List of tuples for parts of each ship
            ship_type_coordinate (dict): Reference of coordinate to the ship type
        """
        ship_locations = []
        ship_type_coordinate = {}

        # Get info from each ship
        for boat in self.BOAT_SIZES:
            boat_name = boat
            boat_size = self.BOAT_SIZES[boat]         

            # Keep picking a point until the ship can correctly placed
            location_invalid = True
            while location_invalid:
                
                # Choose a random point and orientation on the board
                start_x = random.randint(grid_min,grid_max)
                start_y = random.randint(grid_min,grid_max)
                orientation = random.choice(["vertical","horizontal"])

                # Check if the boat is inside
                if self.boat_inside(orientation, boat_size, start_x, start_y, grid_max):
                    location_invalid = False
                    # Creates points and checks if ship overlaps
                    location_invalid, possible_locations = self.check_create_points(orientation, ship_locations, boat_size, start_x, start_y, location_invalid)

                    # Add points to ship_locations if not overlapping
                    if not location_invalid:
                        for point in possible_locations:
                            ship_locations.append(point)
                            ship_type_coordinate[point] = boat_name
                            
        return ship_locations, ship_type_coordinate
                            
    def boat_inside(self, orientation, boat_size, start_x, start_y, grid_max):
        """ Check if the boat is inside the board
        Args:
            orientation (str): Ship is vertical or horizontal
            coord_to_add (int): the coordinate that will be used to add
                        (depends if the ship is vertical or horizontal)
            start_x (int): The randomly chosen starting x coordinate of a ship
            start_y (int): The randomly chosen starting y coordinate of a ship
        Returns:
            True/False (bool): True if boat is inside the board, False otherwise
        """
        if orientation == "vertical":
            if start_x + (boat_size - 1) <= grid_max:
                return True
            else:
                return False
        elif orientation == "horizontal":
            if start_y + (boat_size - 1) <= grid_max:
                return True
            else:
                return False       
    
    def check_create_points(self, orientation, ship_locations, boat_size, start_x, start_y, location_invalid):
        """ Check if the coordinates for the ship do not overlap.
        If it does, the location_valid variable will equal true,
        which will make the program choose a new set of coordinates
        to place the ships.

        Args:
            orientation (str): Ship is vertical or horizontal
            coord_to_add (int): the coordinate that will be used to add
                        (depends if the ship is vertical or horizontal)
            start_x (int): The randomly chosen starting x coordinate of a ship
            start_y (int): The randomly chosen starting y coordinate of a ship
            ship_locations (list): The list that contains the coordinate locations
                                of ships placed on the board
            boat_size (int): The number of square a ship takes.
            location_invalid (bool): variable used for the conditionals to
                            decide if a ship is choosing a valid ship location.
        Returns:
            location_invalid (bool): Boolean that ensures that a ship is placed
                            inside a board and not overlapping other ships
            possible_locations (list): Temporary list added into ship_locations list
                            only if the points are valid to add on the baord.
            
        """
        # Determine if the ship is vertical/horizontal for calculation
        if orientation == "vertical":
            coord_to_add = start_x
        elif orientation == "horizontal":
            coord_to_add = start_y

        # Create an empty list of possible location to add to ship_locations 
        possible_locations = []

        # Create a new coordinate
        for point in range(boat_size):                          
            coord = self.input_new_coord(orientation, coord_to_add, start_x, start_y)      

            # Check if ship overlaps a previously placed ship, create a list
            # of coordinates to potentially place in the board
            if coord in ship_locations:
                location_invalid = True
            possible_locations.append(coord)
            coord_to_add += 1
        
        return location_invalid, possible_locations

    def input_new_coord(self, orientation, coord_to_add, start_x, start_y):
        """ Check if the orientation is horizontal/vertical then add
            points to the correct coordinate (add to x or y)

        Args:
            orientation (str): Ship is vertical or horizontal
            coord_to_add (int): the coordinate that will be used to add
                        (depends if the ship is vertical or horizontal)
            start_x (int): The randomly chosen starting x coordinate of a ship
            start_y (int): The randomly chosen starting y coordinate of a ship
        Returns:
            coord (tuple): the new coordinate created (dependent on orientation)
        """
        if orientation == "vertical":
            coord = (coord_to_add,start_y)
        elif orientation == "horizontal":
            coord = (start_x, coord_to_add)
        return coord

    def fill_target_board(self, target_board, ship_locations):
        """ Fill the target board with True values to keep track of the ship locations
        Returns:
            target_board (list): Target board of Boolean values to keep track of ship locations
        """
        for boat in ship_locations:
            target_board[boat[0]][boat[1]] = True
        return target_board
            

    def convert_coordinates(self):
        """ Convert the cartesian coordinates from the Turtle to colum/rows in the grid
        """
        self.row = math.ceil(self.y / -50) + 4
        self.col = math.floor(self.x / 50) + 11
        if self.col > 9:
            self.col -= 2

    def inbounds(self):
        """ Check if the click is inside Board 2
        Returns:
            True/False: True if the click was inside board 2, False if not
        """
        if self.row >= 0 and self.row < 10 and self.col >= 10 and self.col < 20:
            return True
        else:
            return False

    def check_not_clicked(self):
        """ Check if the player clicked the square previously
        Args:
            self only
        Returns:True/False True means not clicked in the past. False means clicked.            
        """
        if not self.player_hist_board[self.row][self.col - 10]:
            return True
        else:
            return False

    def validate_coordinates(self):
        """ Validate if coordinates that the user clicked are correct
        Args:
            self only
        Returns
            True/False (bool): True if the coordinates are correct, False otherwise.
        """
        if self.inbounds():
            if self.check_not_clicked():         
                return True
        else:
            return False

    def play_game(self):
        """ Initiates event listening for the mouse clicks
        """
        turtle.onscreenclick(self.press)

    def press(self, x, y):
        """ Once mouse is clicked, The player's choice of square is registered as a hit or miss.
            Points are tallied and determined if ships are sunk. If the player does not win,
            the computer will initiate its turn.
            
        """
        self.turn = "player"
        # Player's Move
        self.x = x
        self.y = y
               
        self.convert_coordinates()
        grid_coor = (self.row, self.col)
        # Tuple with coordinates (y adjusted to minus 10)
        grid_coor_converted = (self.row, self.col - 10)

        # Validate if the click is in the board and not yet clicked
        if self.validate_coordinates():
            # Record that the square was clicked
            self.player_hist_board[self.row][self.col - 10] = True

            # For a hit, Draw on the screen and update points
            if self.cpu_target_board[self.row][self.col - 10] == True:
                self.screen.draw_hit(grid_coor)
                self.player_score += 1
                self.current_ship_type = self.cpu_ship_type_coordinate[grid_coor_converted]
                self.player_ship_type_points[self.current_ship_type] += 1

                # Check if the ship sunk
                self.check_ship_sunk()

                # Stop mouseclick event listening if the player wins
                if self.player_score >= self.total_win_points:
                    print("You Won!")
                    turtle.onscreenclick(None)

                # CPU plays if player did not win
                else:
                    self.set_cpu_move()                  
            else:
                self.screen.draw_miss(grid_coor)
                self.set_cpu_move()
        else:
            # Click is invalid
            pass
        
    def set_cpu_move(self):
        """ Store that it is now the computer's turn
        """
        self.turn = "cpu"

        # Handle random search
        if self.cpu_mode.check_mode_random():

            # CPU checks historyboard, Picks a random square, Updates Historyboard
            self.cpu_hist_board = self.cpu_mode.random_search(self.cpu_hist_board)                  
            grid_coor = self.cpu_mode.set_grid_coord()
            
            # Handle if CPU picks a hit, Set to hunt mode
            if self.cpu_mode.check_cpu_hit(self.player_target_board):

                self.current_ship_type, self.cpu_ship_type_points = self.cpu_mode.handle_hit(self.screen, grid_coor, self.player_ship_type_coordinate, self.cpu_ship_type_points)
                self.check_ship_sunk()
                
                # Check if cpu won
                self.cpu_mode.check_cpu_won(self.total_win_points)             

            # CPU picks a miss
            else: 
                self.screen.draw_miss(grid_coor)
                self.cpu_hist_board[self.cpu_mode.cpu_x][self.cpu_mode.cpu_y ] = True            
                
        # CPU hunts for all squares surrounding a hit
        else:
            # Pick a coordinate off the stack until a valid point chosen, if not found search another random coordinate        
            self.cpu_hist_board = self.cpu_mode.hunt_search(self.cpu_hist_board)
            grid_coor = self.cpu_mode.set_grid_coord()

            # Handle if CPU picks a hit
            if self.cpu_mode.check_cpu_hit(self.player_target_board):
                self.current_ship_type, self.cpu_ship_type_points = self.cpu_mode.handle_hit(self.screen, grid_coor, self.player_ship_type_coordinate, self.cpu_ship_type_points)
                self.check_ship_sunk()
                
                # Check if cpu won
                self.cpu_mode.check_cpu_won(self.total_win_points)

            # CPU picks a miss
            else:
                self.screen.draw_miss(grid_coor)
                self.cpu_hist_board[self.cpu_mode.cpu_x][self.cpu_mode.cpu_y ] = True
                
    def check_ship_sunk(self):
        """ Check who sunk the ship. Player or CPU
        """          
        if self.turn == "player":
            if self.player_ship_type_points[self.current_ship_type] >= self.BOAT_SIZES[self.current_ship_type]:
                print("YOU SUNK A", self.current_ship_type)

        elif self.turn == "cpu":
            if self.cpu_ship_type_points[self.current_ship_type] >= self.BOAT_SIZES[self.current_ship_type]:
                print("THE COMPUTER SUNK YOUR", self.current_ship_type)

                          

def main():
    """ Starts the Battleship 
    """
    game = Battleship()
    print("Welcome to Battleship")
    game.play_game()  

if __name__ == "__main__":
    main()


