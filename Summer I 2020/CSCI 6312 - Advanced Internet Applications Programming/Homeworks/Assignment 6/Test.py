import kivy
from random import randint
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 1 #Making it 1 column to make it look nicer for mobile

    #Define the buttons so the user can select one and bind them
        self.txtLabel = Label(text='Play Paper, Rock, Scissors')

        self.btnRock = Button(text='Rock')
        self.btnRock.bind(on_press=self.pressed)

        self.btnPaper = Button(text='Paper')
        self.btnPaper.bind(on_press=self.pressed)

        self.btnScissors = Button(text='Scissors')
        self.btnScissors.bind(on_press=self.pressed)

        #Add the buttons to the grid to the displayed
        self.add_widget(self.txtLabel)
        self.add_widget(self.btnRock)
        self.add_widget(self.btnPaper)
        self.add_widget(self.btnScissors)
#Defining the function for when the buttons are pressed
    def pressed(self, instance):
    #We list the possible choices and pick a random one
        choices = ['Rock', 'Paper', 'Scissors']

        #We need to generate a random number to use as the computer's move
        computer = choices[randint(0,2)]

        #Read the player's choice
        player = instance.text

        #Display your choice and the computer's to the console and window
        print('You picked ' + player + ' and the computer picked ' + computer)
        self.txtLabel.text = 'The computer picked ' + computer

        #Now we find the winner
        if player == computer:
            winner = 'Draw'
        elif player == 'Rock' and computer == 'Scissors':
            winner = 'You win!'
        elif player == 'Rock' and computer == 'Paper':
            winner = 'The computer wins...'
        elif player == 'Paper' and computer == 'Rock':
            winner = 'You win!'
        elif player == 'Paper' and computer == 'Scissors':
            winner = 'The computer wins...'
        elif player == 'Scissors' and computer == 'Paper':
            winner = 'You win!'
        else:
            winner = 'The computer wins...'
        #Output the winner to the console and window
        if winner == 'Draw':
            print('It was a draw. Try again!')
            self.txtLabel.text += '\nIt was a draw. Try again.'
        else:
            print(winner)
            self.txtLabel.text += '\n' + winner

class MyApp(App): #build function
    def build(self):
        return LoginScreen()

if __name__=="__main__": #run the App
    MyApp().run()
