class Display():
    Score = 0
    Lives = 2
    Time = 120

    def printing_head(self):
        print("Number of Lives that you are left with : " + str(Display.Lives),)
        print("Your Time Left is : " + str(Display.Time))

    
    #def changing_yourscore(self):

    #def changing_yourlives(self):

    def changing_time(self):
        if Display.Time == 0:
            print("Sorry , your time is Over")
            print("Your Game Ends Here")
            quit()
        else:
            Display.Time -=1