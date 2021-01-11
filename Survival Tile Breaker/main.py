"""
Welcome to the Survival Tile Breaker Game!!!
by Michael Christopher, Stud ID: 2440047362
Here are all of the code that allows the game to work properly
This game is coded in python with a huge help from the "python arcade library" created by Paul Vincent Craven

More info of python arcade library: 
https://arcade.academy/

This code can be found on my github:
https://github.com/EuphosiouX/PDM-FinalProject

Reference for some of the code and where I learn Arcade library:
https://arcade.academy/examples/index.html
https://www.youtube.com/watch?v=2qP1M1Nf__w&list=PL1P11yPQAo7pPlDlFEaL3IUbcWnnPcALI 

"""
# Required module and library in this code
import arcade
import random
import os
import re

# Setup the app window's size and name
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Survival Tile Breaker'

# Variable for the player sprite movement speed
PLAYER_SPEED = 7


def file_opener(file='Highscore.txt', mode='r'):
    '''
    Functions to handle .txt file
    Takes 2 argument (the_file_name, file_handling_mode)
    '''    
    f = open(file, mode)
    if mode == 'r': # Return every integers found in the .txt file
        high_score_list = re.findall(r'\d+', f.read())
        high_score_string = "".join(high_score_list)
        high_score = int(high_score_string)
        return high_score
    else:
        return f # Return f itself

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------

# Go to, https://arcade.academy/examples/view_instructions_and_game_over.html#view-instructions-and-game-over for reference
class MainMenu(arcade.View):
    '''
    Class to create the main menu window
    Derived from built in arcade class "View"
    '''
    def on_draw(self):
        '''
        Draw the main menu layout
        '''
        # Start the render
        arcade.start_render()

        # Variable for highscore
        high_score = file_opener()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture('Sprite/MainMenu.png'))
        # Show the highscore in the main menu
        arcade.draw_text('{}'.format(high_score), 
                         SCREEN_WIDTH/2,
                         SCREEN_HEIGHT/4,
                         arcade.color.WHITE,
                         font_size=24,
                         anchor_x='center',
                         anchor_y='center')
    
    def on_key_press(self, key, key_modifier):
        """
        Called if keys in keyboard are pressed.
        """  
        # Go to instruction if ENTER key is pressed
        if key == arcade.key.ENTER:           
            instruction = Instruction()
            self.window.show_view(instruction)

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------

class Instruction(arcade.View):
    '''
    Class to create the instruction window
    Derived from built in arcade class "View"
    '''
    def on_draw(self):
        '''
        Draw the instruction layout
        '''
        # Start the render
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture('Sprite/Instruction.png'))

    def on_key_press(self, key, key_modifier):
        """
        Called if keys in keyboard are pressed.
        """  
        # Go to instruction2 if ENTER key is pressed
        if key == arcade.key.ENTER:
            instruction2 = Instruction2()
            self.window.show_view(instruction2)

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------

class Instruction2(arcade.View):
    '''
    Class to create the instruction2 window
    Derived from built in arcade class "View"
    '''
    def on_draw(self):
        '''
        Draw the main menu layout
        '''
        # Start the render
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture('Sprite/Instruction2.png'))

    def on_key_press(self, key, key_modifier):
        """
        Called if keys in keyboard are pressed.
        """  
        # Go to the game if ENTER is pressed
        if key == arcade.key.ENTER:
            game = Game()
            self.window.show_view(game)

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------

class FallingStar(arcade.Sprite):
    '''
    Class to assign the stars sprite behaviour
    Derived from built in arcade class "Sprite"
    '''
    def update(self):
        '''
        Logic of the stars behaviour
        '''
        self.center_y -=2

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------

class Game(arcade.View):
    """
    Main application class
    Class to create the instruction2 window
    Derived from built in arcade class "View"
    """
    def __init__(self):
        '''
        Instantiation
        '''
        super().__init__()
        """
        Setup the game variables
        Setup every sprites and sprite lists 
        """
        # Create sprite list
        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.tiles_list = arcade.SpriteList()
        self.bottom_line_list = arcade.SpriteList()
        self.gold_star_list = arcade.SpriteList()
        self.silver_star_list = arcade.SpriteList()
        self.bronze_star_list = arcade.SpriteList()

        # Create arrow key variable
        self.right = False
        self.left = False
        self.up = False
        self.down = False

        # Create ball sprite
        self.ball = arcade.Sprite('Sprite/Ball.png')
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = 100
        self.ball.change_x = 5
        self.ball.change_y = 5
        self.ball_list.append(self.ball)

        # Create player sprite
        self.player = arcade.Sprite('Sprite/Player.png')
        self.player.center_x = SCREEN_WIDTH/2
        self.player.center_y = 50
        self.player_list.append(self.player)

        # Create bottom line sprite
        self.bottom_line = arcade.Sprite('Sprite/BottomLine.png')
        self.bottom_line.center_x = SCREEN_WIDTH/2
        self.bottom_line.center_y = 5
        self.bottom_line_list.append(self.bottom_line)

        # Other variable
        self.level = 1
        self.score = 0       
        self.life = 3
        self.hit_counter = 0

        # Set the game to level 1
        self.level_1()   
     
        # variable for highscore
        self.high_score = file_opener()

    def gold_star_setup(self):
        '''
        Function to setup the gold star sprite
        '''
        self.gold_star = FallingStar('Sprite/StarGold.png')
        self.gold_star.center_x = random.randrange(SCREEN_WIDTH)
        self.gold_star.center_y = SCREEN_HEIGHT + 30
        self.gold_star_list.append(self.gold_star)

    def silver_star_setup(self):
        '''
        Function to setup the silver star sprite
        '''
        self.silver_star = FallingStar('Sprite/StarSilver.png')
        self.silver_star.center_x = random.randrange(SCREEN_WIDTH)
        self.silver_star.center_y = SCREEN_HEIGHT + 30
        self.silver_star_list.append(self.silver_star)

    def bronze_star_setup(self):
        '''
        Function to setup the bronze star sprite
        '''
        self.bronze_star = FallingStar('Sprite/StarBronze.png')
        self.bronze_star.center_x = random.randrange(SCREEN_WIDTH)
        self.bronze_star.center_y = SCREEN_HEIGHT + 30
        self.bronze_star_list.append(self.bronze_star)

    def star_hit_player(self, star_list, score):
        '''
        Function to create the scoring sytem if the stars are catched by the player
        Takes 3 arguments (self, the_star_list, the_score_of_each_star)
        '''
        star_hit_list = arcade.check_for_collision_with_list(self.player, star_list)
        for star in star_hit_list:
            star.remove_from_sprite_lists()
            self.score += score

    def star_off_screen(self, star_list):
        '''
        Function to remove star from the sprite list if it is failed to be catched by the player
        '''
        star_hit_list = arcade.check_for_collision_with_list(self.bottom_line, star_list)
        for star in star_hit_list:
            star.top = self.bottom_line.top
            star.remove_from_sprite_lists()

    def level_1(self):
        '''
        Function to setup the tiles in level 1
        '''
        for x in range (100, SCREEN_WIDTH-90, 90):
            tiles = arcade.Sprite('Sprite/Tiles.png')
            tiles.center_x = x
            tiles.center_y = 640
            self.tiles_list.append(tiles)
        
    def level_2(self):
        '''
        Function to setup the tiles in level 2
        '''
        for x in range(100, SCREEN_WIDTH-90, 90):
            for y in range(400, SCREEN_HEIGHT-40, 40):
                tiles = arcade.Sprite('Sprite/Tiles.png')
                tiles.center_x = x
                tiles.center_y = y
                self.tiles_list.append(tiles)
    
    def level_3(self):
        '''
        Function to setup the tiles in level 3
        '''
        add_left = 55
        sub_right = 45

        for y in range(400, SCREEN_HEIGHT-40, 40):
            add_left += 45
            sub_right += 45
            for x in range(add_left, SCREEN_WIDTH - sub_right, 90):           
                tiles = arcade.Sprite('Sprite/Tiles.png')
                tiles.center_x = x
                tiles.center_y = y
                self.tiles_list.append(tiles)
            
    def level_4(self):
        '''
        Function to setup the tiles in level 4
        '''
        add_left = 55
        sub_right = 45 

        for y in range(SCREEN_HEIGHT - 80, 400, -40):
            add_left += 45
            sub_right += 45
            for x in range(add_left, SCREEN_WIDTH - sub_right, 90):           
                tiles = arcade.Sprite('Sprite/Tiles.png')
                tiles.center_x = x
                tiles.center_y = y
                self.tiles_list.append(tiles)
    
    def level_5(self):
        '''
        Function to setup the tiles in level 5
        '''
        coordinate = [[30, 640], [30, 600], [30, 560], [30, 520], [30, 480], [30, 440], [30, 400], [120, 400], [210, 400],
                      [380, 620], [470, 640], [470, 600], [470, 560], [470, 520], [470, 480], [470, 440], [470, 400], [360, 400], [560, 400],
                      [740, 640], [740, 600], [740, 560], [740, 520], [740, 480], [740, 440], [740, 400], [830, 640], [865, 610], [890, 580], 
                      [865, 550], [830, 520], [865, 490], [890, 460], [865, 430], [830, 400],
                      [1180, 640], [1110, 600], [1075, 560], [1060, 520], [1075, 480], [1110, 440], [1180, 400]]
        
        for coor in coordinate:
            tiles = arcade.Sprite('Sprite/Tiles.png')
            tiles.center_x = coor[0]
            tiles.center_y = coor[1]
            self.tiles_list.append(tiles)

    def next_level(self):
        '''
        Function to reset the position of the ball after finishing the current level and add level by one
        '''
        self.ball.center_x = self.player.center_x
        self.ball.center_y = 100
        self.level += 1

    def on_show(self):
        '''
        Set background color
        '''
        arcade.set_background_color(arcade.color.YANKEES_BLUE)

    def on_draw(self):
        """
        Draw the game layout
        """
        # Start the render
        arcade.start_render()      
        
        # Draw score box
        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, 
                                     SCREEN_HEIGHT/3, 
                                     400, 
                                     200, 
                                     arcade.color.BLUE_SAPPHIRE)

        # Draw score text
        arcade.draw_text('SCORE: {}'.format(self.score), 
                         SCREEN_WIDTH/2, 
                         SCREEN_HEIGHT/3 + 50, 
                         arcade.color.WHITE, 
                         font_size=24, 
                         anchor_x='center', 
                         anchor_y='center')       

        # Draw highscore text
        arcade.draw_text('HIGHSCORE: {}'.format(self.high_score), 
                         SCREEN_WIDTH/2, 
                         SCREEN_HEIGHT/3, 
                         arcade.color.WHITE, 
                         font_size=24, 
                         anchor_x='center', 
                         anchor_y='center')

        # Draw life text
        arcade.draw_text('LIFE: {}'.format(self.life), 
                         SCREEN_WIDTH/2, 
                         SCREEN_HEIGHT/3 - 50, 
                         arcade.color.WHITE, 
                         font_size=24, 
                         anchor_x='center', 
                         anchor_y='center')

        # Drae every sprite
        self.player_list.draw()
        self.ball_list.draw()
        self.tiles_list.draw()
        self.bottom_line_list.draw()
        self.gold_star_list.draw()
        self.silver_star_list.draw()
        self.bronze_star_list.draw()     

    def on_update(self, delta_time):
        """
        All of the movement logic
        """
        # Update the sprite list
        self.gold_star_list.update()
        self.silver_star_list.update()
        self.bronze_star_list.update()

        # Makes the ball bounce off if it hit the player
        if arcade.check_for_collision(self.ball, self.player):
            self.ball.change_y *= -1
            self.hit_counter += 1
        
        # change the ball x movement if it hits the left/right side of the tiles
        # Go to, https://arcade.academy/examples/sprite_bouncing_coins.html#sprite-bouncing-coins fo reference
        self.ball.center_x += self.ball.change_x
        tiles_hit_list = arcade.check_for_collision_with_list(self.ball, self.tiles_list)
        for tiles in tiles_hit_list:
            if self.ball.change_x > 0:
                self.ball.right = tiles.left
            elif self.ball.change_x < 0:
                self.ball.left = tiles.right
            tiles.remove_from_sprite_lists()
            self.ball.change_x *= -1
            self.hit_counter += 1
            self.score += 20

        # change the ball y movement if it hits the top/bottom side of the tiles
        # Go to, https://arcade.academy/examples/sprite_bouncing_coins.html#sprite-bouncing-coins fo reference
        self.ball.center_y += self.ball.change_y
        tiles_hit_list = arcade.check_for_collision_with_list(self.ball, self.tiles_list)
        for tiles in tiles_hit_list:
            if self.ball.change_y > 0:
                self.ball.top = tiles.bottom
            elif self.ball.change_y < 0:
                self.ball.bottom = tiles.top
            tiles.remove_from_sprite_lists()
            self.ball.change_y *= -1
            self.hit_counter += 1
            self.score += 20

        # Call star_hit_player function
        self.star_hit_player(self.gold_star_list, 30)
        self.star_hit_player(self.silver_star_list, 20)
        self.star_hit_player(self.bronze_star_list, 10)

        # Call star_off_screen function
        self.star_off_screen(self.gold_star_list)
        self.star_off_screen(self.silver_star_list)
        self.star_off_screen(self.bronze_star_list)

        # Go to next levels if every tiles in the current level are already destroyed
        # Go to, https://arcade.academy/examples/sprite_collect_coins_diff_levels.html#example-sprite-collect-coins-diff-levels for reference
        if len(self.tiles_list) == 0:
            if self.level == 1:
                self.next_level()
                self.level_2()
            elif self.level == 2:
                self.next_level()
                self.level_3()
            elif self.level == 3:
                self.next_level()
                self.level_4()
            elif self.level == 4:
                self.next_level()
                self.level_5()  
         
        # Keep the ball bouncing from the sides and top
        if self.ball.center_x < 5 or self.ball.center_x > SCREEN_WIDTH - 5:
            self.ball.change_x *= -1
            self.hit_counter += 1
        if self.ball.center_y > SCREEN_HEIGHT - 5:
            self.ball.change_y *= -1
            self.hit_counter += 1

        # Reset and substract the life if the player failed to keep the ball bouncing
        if arcade.check_for_collision(self.ball, self.bottom_line):
            self.ball.center_x = self.player.center_x
            self.ball.center_y = 100
            self.life -= 1   

        # Game over when life reach zero or final level are finished
        game_over = GameOver(self)
        if len(self.tiles_list) == 0 and self.level == 5:            
            self.window.show_view(game_over) 
        if self.life < 1:  
            self.window.show_view(game_over)     

        # Move the player if key pressed and keep the player onscreen
        if self.right: 
            self.player.center_x += PLAYER_SPEED
        if self.left: 
            self.player.center_x -= PLAYER_SPEED
        if self.player.center_x < 100:
            self.left = False
        if self.player.center_x > SCREEN_WIDTH - 100:
            self.right = False
        
        # Spawn random star from the ceiling every 10 bounces 
        # 20 bounces is for safety measures because sometimes it counts up to more than 10
        if self.hit_counter == 10 or self.hit_counter == 20:
            show_random_star = random.randrange(1, 4)
            if show_random_star == 1:
                self.gold_star_setup()
            if show_random_star == 2:
                self.silver_star_setup()
            if show_random_star == 3:
                self.bronze_star_setup()
            self.hit_counter = 0

        # Rewrite the Highscore.txt with current score if the current score is higher than the current highscore
        f = file_opener(mode='r+')
        if self.score > self.high_score:
            self.high_score = self.score
            f.write('DO NOT EDIT MANUALLY!!!\nHighscore: {}'.format(self.high_score))       

    def on_key_press(self, key, key_modifier):
        """
        Called if keys in keyboard are pressed.
        """     
        # Set key RIGHT/LEFT pressed to true
        if key == arcade.key.RIGHT: 
            self.right = True
        if key == arcade.key.LEFT: 
            self.left = True
        # Go to pause if ESCAPE key is pressed    
        if key == arcade.key.ESCAPE: 
            self.right = False
            self.left = False
            pause = Pause(self)
            self.window.show_view(pause)

    def on_key_release(self, key, key_modifier):
        """
        Called whenever the user lets off a previously pressed key.
        """
        # Set key pressed back to false
        if key == arcade.key.RIGHT:
            self.right = False
        if key == arcade.key.LEFT:
            self.left = False

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------

# Go to, https://arcade.academy/examples/view_pause_screen.html#view-pause-screen foor reference
class Pause(arcade.View):
    '''
    Class to create the pause window
    Derived from built in arcade class "View"
    '''  
    def __init__(self, game):
        '''
        Instantiation
        '''
        super().__init__()
        self.game = game

    def on_draw(self):
        '''
        Draw the pause layout
        '''
        # Start the render
        arcade.start_render()      
        
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture('Sprite/Pause.png'))
        
        # Variables for player and ball
        player = self.game.player
        ball = self.game.ball
        
        # Draw current palyer and ball position
        player.draw()
        ball.draw()

    def on_key_press(self, key, key_modifier):
        """
        Called if keys in keyboard are pressed.
        """    
        # Resume game if ENTER is pressed
        if key == arcade.key.ENTER:   
            self.window.show_view(self.game)
        # Reset game if X is presses
        elif key == arcade.key.X:  
            game = Game()
            self.window.show_view(game)
        # Go to main menu if ESCAPE is pressed
        elif key == arcade.key.ESCAPE:
            main_menu = MainMenu()
            self.window.show_view(main_menu)

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------

class GameOver(arcade.View):
    '''
    Class to create the pause window
    Derived from built in arcade class "View"
    '''        
    def __init__(self, game):
        '''
        Instantiation
        '''
        super().__init__()
        self.game = game      

    def on_draw(self):
        '''
        Draw the pause layout
        '''
        # Start the render
        arcade.start_render()     
        
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture('Sprite/GameOver.png'))

        # Variables for score and highscore
        score = self.game.score
        high_score = self.game.high_score

        # Draw score text
        arcade.draw_text('{}'.format(score), 
                            SCREEN_WIDTH/2, 
                            SCREEN_HEIGHT/3 + 130, 
                            arcade.color.WHITE, 
                            font_size=24, 
                            anchor_x='center', 
                            anchor_y='center')
        # Draw highscore text
        arcade.draw_text('{}'.format(high_score), 
                            SCREEN_WIDTH/2, 
                            SCREEN_HEIGHT/3 + 30, 
                            arcade.color.WHITE, 
                            font_size=24, 
                            anchor_x='center', 
                            anchor_y='center')
        
    def on_key_press(self, key, key_modifier):
        """
        Called if keys in keyboard are pressed.
        """   
        # Restart the game if Y is pressed
        if key == arcade.key.Y:
            game = Game()
            self.window.show_view(game)
        # Go to main menu if N is pressed
        elif key == arcade.key.N:
            main_menu = MainMenu()
            self.window.show_view(main_menu)

def main():
    """ Main method """
    # Check if Highscore.txt exist or not, create one if it does not
    if os.path.exists("Highscore.txt"):
        # Setup the window attributes and run the program
        window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        menu = MainMenu()
        window.show_view(menu)
        arcade.run()
    else:
        f = file_opener(mode='w')
        f.write('DO NOT EDIT MANUALLY!!!\nHighscore: 0') # Write the Highscore.txt
        os.system( "attrib +h Highscore.txt") # Makes the file hidden so it is harder to access manually
        print('FIRST LAUNCH SETUP SUCCESSFUL, RUN AGAIN THE PROGRAM TO START PLAYING') # Tell the users that the setup is successful and to run again the program(Showed on the terminal)

if __name__ == "__main__":
    ''' Call main method'''
    main()