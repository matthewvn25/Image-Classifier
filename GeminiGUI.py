import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
   
  
LARGEFONT =("Verdana", 20) 
   
class GeminiScraper(tk.Tk): 
      
    # __init__ function for class GeminiScraper  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs) 
          
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)
    
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
        # initializing frames to an empty array 
        self.frames = {}   
   
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (HomePage, Scraper, LearningSets, FindWaifu, FinishedScreen): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # HomePage, Scraper, LearningSets respectively with  
            # for loop 
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(HomePage) 
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise()
        

   
# first window frame HomePage 
   
class HomePage(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
           
        # label of frame Layout 2 
        label = ttk.Label(self, text ="Welcome to Find your Waifu", font = LARGEFONT) 
          
        # putting the grid in its place by using 
        # grid 
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
  
   
        button1 = ttk.Button(self, text ="Scraper", 
        command = lambda : controller.show_frame(Scraper)) 
      
        # putting the button in its place by 
        # using grid 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
   
        ## button to show frame 2 with text layout2 
        button2 = ttk.Button(self, text ="Set Up Learning Sets", 
        command = lambda : controller.show_frame(LearningSets)) 
      
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
        ## button to show frame 3 with text layout3
        button3 = ttk.Button(self, text ="Find Waifu(sort images)", 
        command = lambda : controller.show_frame(FindWaifu)) 
      
        # putting the button in its place by 
        # using grid 
        button3.grid(row = 3, column = 1, padx = 10, pady = 10) 
   
# second window frame Scraper  
class Scraper(tk.Frame): 
      
    def __init__(self, parent, controller): 
          
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Scraper", font = LARGEFONT) 
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
   
        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="HomePage", 
                            command = lambda : controller.show_frame(HomePage)) 
      
        # putting the button in its place  
        # by using grid 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
   
        # button to show frame 2 with text 
        # layout2 
        button2 = ttk.Button(self, text ="Set Up Learning Sets", 
                            command = lambda : controller.show_frame(LearningSets)) 
      
        # putting the button in its place by  
        # using grid 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
        
        ## button to show frame 3 with text layout3
        button3 = ttk.Button(self, text ="Find Waifu(sort images)", 
        command = lambda : controller.show_frame(FindWaifu)) 
      
        # putting the button in its place by 
        # using grid 
        button3.grid(row = 3, column = 1, padx = 10, pady = 10) 
        
        
        # Create the Label and Entry widgets for scraper
        lbl1 = tk.Label(self, text="How many images do you want to scrape?(1-1000):")
        ent1 = tk.Entry(self, width=10)
        # Use the grid geometry manager to place the Label and
        # Entry widgets in the first and second columns of the
        # first row of the grid
        lbl1.grid(row=0, column=2, sticky="e")
        ent1.grid(row=0, column=3)
   
        ## button to show frame 4 with text layout4
        button4 = ttk.Button(self, text ="Begin Scrapping", 
        command = lambda : controller.show_frame(HomePage)) 
      
        # putting the button in its place by 
        # using grid 
        button4.grid(row = 1, column = 3, padx = 10, pady = 10) 
   
   
   
# third window frame LearningSets 
class LearningSets(tk.Frame):  
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Set Up Learning Sets", font = LARGEFONT) 
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
   
        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="Scraper", 
                            command = lambda : controller.show_frame(Scraper)) 
      
        # putting the button in its place by  
        # using grid 
        button1.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
        # button to show frame 3 with text 
        # layout3 
        button2 = ttk.Button(self, text ="HomePage", 
                            command = lambda : controller.show_frame(HomePage)) 
      
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        ## button to show frame 3 with text layout3
        button3 = ttk.Button(self, text ="Find Waifu(sort images)", 
        command = lambda : controller.show_frame(FindWaifu)) 
      
        # putting the button in its place by 
        # using grid 
        button3.grid(row = 3, column = 1, padx = 10, pady = 10) 
        
        
        # Create the Label and Entry widgets for Learning Sets
        lbl1 = tk.Label(self, text="Enter the name of your category:")
        ent1 = tk.Entry(self, width=20)
        # Use the grid geometry manager to place the Label and
        # Entry widgets in the first and second columns of the
        # first row of the grid
        lbl1.grid(row=0, column=2, sticky="e")
        ent1.grid(row=0, column=3)
        
        ## button to show frame 4 with text layout4
        button4 = ttk.Button(self, text ="Create", 
        command = lambda : controller.show_frame(LearningSets)) 
      
        # putting the button in its place by 
        # using grid 
        button4.grid(row = 1, column = 3, padx = 10, pady = 10) 
        
# fourth window frame find waifu
class FindWaifu(tk.Frame):  
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Find Waifu(sort images)", font = LARGEFONT) 
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
   
        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="Scraper", 
                            command = lambda : controller.show_frame(Scraper)) 
      
        # putting the button in its place by  
        # using grid 
        button1.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
        # button to show frame 3 with text 
        # layout3 
        button2 = ttk.Button(self, text ="HomePage", 
                            command = lambda : controller.show_frame(HomePage)) 
      
        # putting the button in its place by 
        # using grid 
        button2.grid(row = 1, column = 1, padx = 10, pady = 10) 
        
        
        # button to show frame 3 with text 
        # layout3 
        button3 = ttk.Button(self, text ="Set Up Learning Sets", 
                            command = lambda : controller.show_frame(LearningSets)) 
        # putting the button in its place  
        # by using grid 
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        # Create the Label and Entry widgets for find waifu
        lbl1 = tk.Label(self, text="Enter a percent threshold")
        ent1 = tk.Entry(self, width=10)
        # Use the grid geometry manager to place the Label and
        # Entry widgets in the first and second columns of the
        # first row of the grid
        lbl1.grid(row=0, column=2, sticky="e")
        ent1.grid(row=0, column=3)
        
        ## button to show frame 4 with text layout4
        button4 = ttk.Button(self, text ="Find Waifu (sort images)", 
        command = lambda : controller.show_frame(FinishedScreen)) 
      
        # putting the button in its place by 
        # using grid 
        button4.grid(row = 1, column = 3, padx = 10, pady = 10) 
   
# fourth window frame LearningSets 
class FinishedScreen(tk.Frame):  
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        
        label = ttk.Label(self, text ="Your waifus are found!", font = LARGEFONT) 
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
   
        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="Click here to enter your waifus folder", 
                            command = lambda : controller.show_frame(FinishedScreen))
      
        # putting the button in its place by  
        # using grid 
        button1.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
   
# Driver Code 
app = GeminiScraper() 
app.title("Gemini Scraper")

load = Image.open("background.jpg")
render = ImageTk.PhotoImage(load)
label = tk.Label(image=render)
label.image = render
label.pack()


app.mainloop() 