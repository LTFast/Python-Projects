""" Battleship CPU actions
"""

import random, turtle

class CpuMode:
    """ Computer's moves are based on a random search or hunt mode. If the computer
        is in hunt mode, it will search every square around a hit.
    """
    
    def __init__(self, NUM_SQ):
        self.mode = "random"
        self.cpu_hit_stack = []
        self.cpu_score = 0
        self.NUM_SQ = NUM_SQ
        self.hit_choices = []
        
    def check_mode_random(self):
        """ Check if the CPU should be in random mode
        Returns:
            cpu_mode (str): determines if in random mode or hunt mode
        """
        if self.cpu_hit_stack == []:
                self.cpu_mode = "random"
                return True
        else:
                self.cpu_mode = "hunt"
                return False
                      
    def random_search(self, cpu_hist_board):
        """ Moves involved when searching randomly, Computer picks a valid random
            coordinate and updates the history board
        """
        not_chosen = True
        while not_chosen:
            self.cpu_x = random.randint(0, 9)
            self.cpu_y = random.randint(0, 9)
            
            # Check if chosen before
            if cpu_hist_board[self.cpu_x][self.cpu_y ] == False:
                not_chosen = False
        cpu_hist_board[self.cpu_x][self.cpu_y ] = True
        return cpu_hist_board

    def set_grid_coord(self):
        """ Set the grid coordinates
        Returns:
            grid_coor (tuple): Grid coordinates of the CPU's square choice
        """
        grid_coor = (self.cpu_x, self.cpu_y)
        return grid_coor


    def hunt_search(self, cpu_hist_board):
        """ Hunt for the hits. Update the history board

        Returns:
            cpu_hist_board (list): List that records previously clicked squares
        """



        # Check if chosen before 
        not_chosen = True
        while not_chosen:

            # Choose a coordinate from the stack if not empty
            # print("CPU stack:", self.cpu_hit_stack)
            if self.cpu_hit_stack != []:
                next_move = self.cpu_hit_stack.pop()
                self.cpu_x = next_move[0]
                self.cpu_y = next_move[1]
                #print("CPU Hunt Coord: ", self.cpu_x, self.cpu_y)

                # Check if chosen before
                if cpu_hist_board[self.cpu_x][self.cpu_y ] == False:
                    not_chosen = False

            # Go back to random mode if stack is empty
            else:
                self.cpu_mode = "random"
                cpu_hist_board = self.random_search(cpu_hist_board)
                not_chosen = False
            
        cpu_hist_board[self.cpu_x][self.cpu_y ] = True
        return cpu_hist_board
      

    def add_cpu_guesses(self):
        """ Adds future cpu guesses to a stack
        """
        up = (self.cpu_x - 1, self.cpu_y)
        down = (self.cpu_x + 1, self.cpu_y)
        left = (self.cpu_x , self.cpu_y - 1)
        right = (self.cpu_x, self.cpu_y + 1)
                    
        if self.cpu_x - 1 >= 0:
            self.cpu_hit_stack.append(up)

        if self.cpu_x + 1 < self.NUM_SQ: 
            self.cpu_hit_stack.append(down)

        if self.cpu_y - 1 >= 0:     
            self.cpu_hit_stack.append(left)

        if self.cpu_y + 1 < self.NUM_SQ: 
            self.cpu_hit_stack.append(right)


    def check_cpu_hit(self, player_target_board):
        """ Check if CPU made a hit
        """
        if player_target_board[self.cpu_x][self.cpu_y] == True:
            self.cpu_mode = "hunt"
            return True
        else:
            return False

    def update_total_score(self):
        """ Update the CPU's total score
        """
        self.cpu_score += 1


        """
            def reset_stack(self):
                 #Reset the stack
            
                self.cpu_hit_stack = []
        """
        """
            def reset_hit_choices(self):
                self.hit_choices = []
        """
    def check_cpu_won(self, total_win_points):
        """ Check if the computer won. If so, stop the game
        """
        if  self.cpu_score >= total_win_points:
            print("The Computer Won!")
            turtle.onscreenclick(None)

    def handle_hit(self, screen, grid_coor, player_ship_type_coordinate, cpu_ship_type_points):
        """ Handle a hit by updating the score

        Returns:
            current_ship_type (str): Current type of ship hit
            cpu_ship_type_points (dict): Update version of the ship type hit tally
        """

        # Add to CPUScore,  Draw Hit
        self.update_total_score()
        screen.draw_hit(grid_coor)

        # Record Last hit, Add surrounding hits in SearchStack 
        self.cpu_last_hit = grid_coor
        self.hit_choices.append(grid_coor)
        self.add_cpu_guesses()
        

        # Identify shiptype, Add tally to CpuShipTypes, Print if sunk shipo                
        current_ship_type = player_ship_type_coordinate[grid_coor]
        cpu_ship_type_points[current_ship_type] += 1

        return current_ship_type, cpu_ship_type_points
        

        


                    


    
