import kivy
from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial
import time
import requests

class SwitchContainer(GridLayout): #create a class that uses the GridLayout module
    
    def __init__(self, **kwargs):
        super(SwitchContainer, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text="SW 1: ")) #create a label for SW1
        self.sw1 = Switch(active=False) #create a SwitchCompat for SW1 (default to OFF)
        self.add_widget(self.sw1) #add the created SwitchCompat to the screen
        self.sw1.disabled = True #make SW1 unclickable on the app
        
        
        self.add_widget(Label(text="LED 1: ")) #create a label for LED1
        self.led1 = Switch(active=False) #create a SwitchCompat for LED1 (default to OFF)
        self.add_widget(self.led1) #add the created SwitchCompat to the screen
        self.led1.disabled = False #by default a created SwitchCompat is clickable; so, there is no need
        #for this statement
        
        #schedule the JSONrequest function to trigger every 5 seconds to read/write database
        Clock.schedule_interval(self.JSONrequest, 5)
    
    
    def JSONrequest(self, *largs):
        
        if (self.sw1.active == True): #Get the sw1 active status and convert it to an integer
            SW1 = 1
        else:
            SW1 = 0
        if (self.led1.active == True): #Get the led1 active status and convert it to an integer
            LED1 = 1
        else:
            LED1 = 0
        
        #below are json request payload, the request itself, and the response
        data = {'username': 'Test','password':'Tester3', 'SW1': SW1, 'LED1': LED1} #json request payload
        res = requests.post("https://team2project3342.online/scripts/sync_app_data.php", json=data)
        r = res.json() #json response
        if SW1 != r['SW1']: #check the received value of SW1 & change it on the App if there is a mismatch
            if self.sw1.active == True:
                self.sw1.active = False
            else:
                self.sw1.active = True
        else:
            return
        

class SwitchExample(App):
    def build(self): #build
        return SwitchContainer()
    
if __name__ == '__main__':
    SwitchExample().run() #run
    