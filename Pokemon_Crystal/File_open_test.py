'''
Created on Mar 31, 2021

@author: Balu
'''



from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(bg = 'tan', width = 500, height = 400,)
 
canvas.pack()  
player2 = ImageTk.PhotoImage(Image.open("Pokemon Essentials v18.1 2020-09-28/Graphics/Battlers/077.png"))
player = ImageTk.PhotoImage(Image.open("Pokemon Essentials v18.1 2020-09-28/Graphics/Battlers/021sb.png"))
player2base = ImageTk.PhotoImage(Image.open("Pokemon Essentials v18.1 2020-09-28/Graphics/Battlebacks/cave1_base1.png"))
playerbase = ImageTk.PhotoImage(Image.open("Pokemon Essentials v18.1 2020-09-28/Graphics/Battlebacks/cave1_base0.png"))
Background = ImageTk.PhotoImage(Image.open("Pokemon Essentials v18.1 2020-09-28/Graphics/Battlebacks/cave1_bg.png"))
HPbar1 = ImageTk.PhotoImage(Image.open("Pokemon Essentials v18.1 2020-09-28/Graphics/Pictures/Battle/databox_thin.png"))
HPbar2 = ImageTk.PhotoImage(Image.open("Pokemon Essentials v18.1 2020-09-28/Graphics/Pictures/Battle/databox_thin_foe.png"))
main_menu = ImageTk.PhotoImage(Image.open("Pokemon Essentials v18.1 2020-09-28/Graphics/Pictures/Battle/overlay_fight.png"))

canvas.create_image(0, 15, anchor=NW, image=Background)
canvas.create_image(250, 55, anchor=NW, image=player2base)
canvas.create_image(300, 0, anchor=NW, image=player2)
canvas.create_image(-200, 245, anchor=NW, image=playerbase)
canvas.create_image(25, 150, anchor=NW, image=player)
canvas.create_image(250, 170, anchor=NW, image=HPbar1)
canvas.create_image(0, 25, anchor=NW, image=HPbar2)
canvas.create_image(0, 300, anchor=NW, image=main_menu)
root.mainloop()

