''' This is a python file to create highscore.txt on first launch '''
''' DO NOT RUN THIS .py FILE '''

import arcade
import main
import os
import time

def first_setup():
    ''' Function for first launch setup '''
    f = main.file_opener(mode='w') # Call file_opener function from main
    f.write('DO NOT EDIT MANUALLY!!!\nHighscore: 0') # Write the Highscore.txt
    os.system( "attrib +h Highscore.txt") # Makes the file hidden so it is harder to access manually
    print('FIRST LAUNCH SETUP SUCCESSFUL') # Tell the users that the setup is successful and to run again the program(Showed on the terminal)
