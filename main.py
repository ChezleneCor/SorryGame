# Program name: main.py
# Author: Chez'lene Cornwall
# Date last updated: 11/17/2022
# Purpose: Play the game of sorry

import tkinter as tk
import random


#Initialize window

class Page(tk.Tk):
    """Initializing parent class for pages"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for P in (StartPage, PlayerNamesPage, GamePage, WinnersPage):
            frame = P(container, self)
            self.frames[P] = frame
            frame.grid(row=0, column=0, sticky="nsew")  
            
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        """Displayes the current window"""
        frame = self.frames[cont]
        
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Define the players IntVar as an instance attribute
        self.players = tk.IntVar()
        self.players.get()
        self.players.set("2")

        
        # Confirm number of players
        numPlayers_label = tk.Label(self, text="Please select the number of people will be playing today.")
        numPlayers_label.pack()
        tk.Radiobutton(self, text = "2", variable= self.players, value= 2).pack() 
        tk.Radiobutton(self, text = "3", variable= self.players, value= 3).pack() 
        tk.Radiobutton(self, text = "4", variable= self.players, value= 4).pack()
        
        #Button to call numPlayers function
        submit_button = tk.Button(
            self,
            text = "Submit",
            command= lambda : self.numPlayers(controller, selection)
        )
        submit_button.pack()  
        
    def numPlayers(self, controller):
        """Retrieves the value of the selected radio button and moves
        to next page of the program"""
        # Get the selected value from the redio button
        global selection
        selection = self.players.get()
        
        # Show the next page in the game
        controller.show_frame(PlayerNamesPage)
        
        # Return the selected value
        return selection

class PlayerNamesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #defining selection variable inside function
        self.selection = selection
        print(self.selection)
        
        # Define the player StringVar as an instance attribute
        self.player1 = tk.StringVar()
        self.player1.get()
        self.player1.set("")
        
        self.player2 = tk.StringVar()
        self.player2.get()
        self.player2.set("")

        self.player3 = tk.StringVar()
        self.player3.get()
        self.player3.set("")
        
        self.player4 = tk.StringVar()
        self.player4.get()
        self.player4.set("")
        
        label = tk.Label(self, text = "Please enter the names of today's players.")
        label.pack(pady=10, padx=10)
        
        #Getting the needed players names
        
        tk.Label(self, text = "Player 1").pack(side= "left")
        tk.Entry(self, textvariable= self.player1).pack(side="right")
        
        tk.Label(self, text = "Player 2").pack(side= "left")
        tk.Entry(self, textvariable= self.player2).pack(side="right")
        
        if self.selection == "4":
            tk.Label(self, text = "Player 3").pack(side= "left")
            tk.Entry(self, textvariable= self.player3).pack(side="right")
            
            tk.Label(self, text = "Player 4").pack(side= "left")
            tk.Entry(self, textvariable= self.player4).pack(side="right")
        elif self.selection == "3":
            tk.Label(self, text = "Player 3").pack(side= "left")
            tk.Entry(self, textvariable= self.player3).pack(side="right")
            
        
                
        #Button to call platerNames function
        play_button = tk.Button(
            self,
            text = "Let's Play",
            command= lambda : self.playerNames(controller)
        )
        play_button.pack()
        
    def playerNames(self, controller):
        """Gathers player names from user"""
        
        global players #initializing global dictionary for player names & positions
        players = {
            "Player 1" : 
                {'name': "", 'position' : 0},
            "Player 2":
                {'name' : "", 'position' : 0},
            'Player 3':
                {'name' : "", 'position' : 0},
            'Player 4' :
                {'name' : "", 'position' : 0}
        }
        players["Player 1"]['name'] = self.player1.get()
        players["Player 2"]['name'] = self.player2.get()
        
        if selection == 3:
            players["Player 3"]['name'] = self.player3.get()
            players['Player 4'].pop()
        elif selection == 4:
            players["Player 3"]['name'] = self.player3.get()
            players["Player 4"]['name'] = self.player4.get()
                
        #Displaying GamePage
        controller.show_frame(GamePage)
            
        #Returning the string value of the player's names
        return players
        

        
class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Please ...")
        label.pack(side = "top", fill = "both", expand = True)
        
        rollDie_button = tk.Button(
            self,
            text = "Roll Dice",
            command= lambda : functions.rollDie(PlayerNamesPage.playerName)
        )
        rollDie_button.pack()
        
    def evaluateTurn(die1, die2, position):
        """Evaluates the players roll"""
   
        # combining the 2 dies to get a total
        roll = die1 + die2
        
        if die1 == die2:
            pass
        
        if roll == 2:
            position += 2
        elif roll == 3:
            position +=3
        elif roll == 4:
            position -= 1
        elif roll == 5:
            position -=2
        elif roll == 6:
            position +=6
        elif roll == 7:
            temp = position
            
        return position
            
            
                
    def rollDie(self, die1, die2, player):
        """Simulates rolling 2 dice"""
        
        # generating random numbers to represent the roll of 2 dice
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        
        #Calling evaluateTurn function to get the player's new position
        players[player]['position'] = self.evaluateTurn(die1, die2)
        
        return
        
class WinnersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "We have a winner!.")
        label.pack(side = "top", fill = "both", expand = True)

root= Page()
root.title("Sorry!")
root.geometry("700x600")
root.attributes('-topmost', 1)
root.mainloop()