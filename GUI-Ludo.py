from tkinter import *
import random
from PIL import Image, ImageTk # type: ignore
import sys,os

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
    
def show_custom_message(image_path,text,root):
    msg_box = Toplevel(root)
    msg_box.title("Game Over")
    msg_box.geometry("300x200")
    msg_box.resizable(False, False)
    msg_box.iconbitmap(r"Ludo-Images/1490877818-sport-badges05_82419.ico")
    msg_box.protocol("WM_DELETE_WINDOW", sys.exit)

    # Center window
    msg_box.update_idletasks()
    x = (msg_box.winfo_screenwidth() - 300) // 2
    y = (msg_box.winfo_screenheight() - 200) // 2
    msg_box.geometry(f"+{x}+{y}")

    # Load background image
    
    bg_image = Image.open(image_path).resize((300, 200))
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Canvas setup
    canvas = Canvas(msg_box, width=300, height=200, highlightthickness=0, bd=0)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.image = bg_photo  # Prevent garbage collection

    # Message text
    canvas.create_text(
        150, 75,
        text=text,
        font=("Arial", 15, "bold"),
        fill="white"
    )

    # Create Restart Button
    restart_btn = Button(
        msg_box,
        text="⟳ Restart",
        font=("Arial", 12, "bold"),
        bg="green",
        fg="white",
        width=10,
        relief=RAISED,
        bd=4,
        command=lambda: [show(),msg_box.destroy(), root.destroy(),initialize_variables(),ludo()]
    )

    # Create Quit Button
    quit_btn = Button(
        msg_box,
        text="❌ Quit",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        width=10,
        relief=RAISED,
        bd=4,
        command=sys.exit
    )

    # Place buttons on the canvas with spacing between
    canvas.create_window(85, 140, window=restart_btn)
    canvas.create_window(215, 140, window=quit_btn)

def show():
    print("Restart working")    


# ==================== GLOBAL VARIABLES ====================
# Game state
turn_count = 0
dice_count = 0
turn_ = None
elected_red_pawn = 0
elected_green_pawn = 0
elected_yellow_pawn = 0
elected_blue_pawn = 0

# UI elements
root = None
dice = {}
dice_image = None
bg_image = None
inner_border = None
bgm_image=None
# Dice images
dice_images = [
    "Ludo-Images/dice-six-faces-one.png",
    "Ludo-Images/dice-six-faces-two.png",
    "Ludo-Images/dice-six-faces-three.png",
    "Ludo-Images/dice-six-faces-four.png",
    "Ludo-Images/dice-six-faces-five.png",
    "Ludo-Images/dice-six-faces-six.png"
]

# Player pawns
red_pice_image = [["", ""], ["", ""]]
red_labels = [["", ""], ["", ""]]
red_pawn_image_path_home = {}

green_pice_image = [["", ""], ["", ""]]
green_labels = [["", ""], ["", ""]]
green_pawn_image_path_home = {}

blue_pice_image = [["", ""], ["", ""]]
blue_labels = [["", ""], ["", ""]]
blue_pawn_image_path_home = {}

yellow_pice_image = [["", ""], ["", ""]]
yellow_labels = [["", ""], ["", ""]]
yellow_pawn_image_path_home = {}

# Board labels
top_labels = [[None for _ in range(3)] for _ in range(6)]
bottom_labels = [[None for _ in range(3)] for _ in range(6)]
left_labels = [[None for _ in range(6)] for _ in range(3)]
right_labels = [[None for _ in range(6)] for _ in range(3)]
center_labels = [[None for _ in range(2)] for _ in range(2)]

# Tracking dictionaries
label_image_paths = {}
label_pawn_count = {}
pawn_images = {}

# Stamp positions
stamp_labels = []
home_stamps = []
star_stamps = []
red_at_stamps = {}
green_at_stamps = {}
blue_at_stamps = {}
yellow_at_stamps = {}

# Pawn image paths
red_pawn_images = [
    r"Ludo-Images/red_pawn.png",
    r"Ludo-Images/red_pawn_horizontal-L-R.png",
    r"Ludo-Images/red_pawn_horizontal-R-L.png"
]
green_pawn_images = [
    r"Ludo-Images/green-pawn_horizontal-R-L.png",
    r"Ludo-Images/green-pawn_horizontal-L-R.png",
    r"Ludo-Images/green-pawn.png"
]
yellow_pawn_images = [
    r"Ludo-Images/yellow_pawn_horizontal-R-L.png",
    r"Ludo-Images/yellow_pawn_horizontal-L-R.png",
    r"Ludo-Images/yellow_pawn.png"
]
blue_pawn_images = [
    r"Ludo-Images/blue_pawn_horizontal-R-L.png",
    r"Ludo-Images/blue_pawn_horizontal-L-R.png",
    r"Ludo-Images/blue_pawn.png"
]

def initialize_variables():
    # Game state
    global turn_count, dice_count, turn_
    global elected_red_pawn, elected_green_pawn, elected_yellow_pawn, elected_blue_pawn

    # UI elements
    global root, dice, dice_image, bg_image, inner_border

    # Dice images
    global dice_images

    # Player pawns
    global red_pice_image, red_labels, red_pawn_image_path_home
    global green_pice_image, green_labels, green_pawn_image_path_home
    global blue_pice_image, blue_labels, blue_pawn_image_path_home
    global yellow_pice_image, yellow_labels, yellow_pawn_image_path_home

    # Board labels
    global top_labels, bottom_labels, left_labels, right_labels, center_labels

    # Tracking dictionaries
    global label_image_paths, label_pawn_count, pawn_images

    # Stamp positions
    global stamp_labels, home_stamps, star_stamps
    global red_at_stamps, green_at_stamps, blue_at_stamps, yellow_at_stamps

    # Pawn image paths
    global red_pawn_images, green_pawn_images, yellow_pawn_images, blue_pawn_images


    # ==================== GLOBAL VARIABLES ====================
    # Game state
    turn_count = 0
    dice_count = 0
    turn_ = None
    elected_red_pawn = 0
    elected_green_pawn = 0
    elected_yellow_pawn = 0
    elected_blue_pawn = 0

    # UI elements
    root = None
    dice = {}
    dice_image = None
    bg_image = None
    inner_border = None
    bgm_image=None
    # Dice images
    dice_images = [
        "Ludo-Images/dice-six-faces-one.png",
        "Ludo-Images/dice-six-faces-two.png",
        "Ludo-Images/dice-six-faces-three.png",
        "Ludo-Images/dice-six-faces-four.png",
        "Ludo-Images/dice-six-faces-five.png",
        "Ludo-Images/dice-six-faces-six.png"
    ]

    # Player pawns
    red_pice_image = [["", ""], ["", ""]]
    red_labels = [["", ""], ["", ""]]
    red_pawn_image_path_home = {}

    green_pice_image = [["", ""], ["", ""]]
    green_labels = [["", ""], ["", ""]]
    green_pawn_image_path_home = {}

    blue_pice_image = [["", ""], ["", ""]]
    blue_labels = [["", ""], ["", ""]]
    blue_pawn_image_path_home = {}

    yellow_pice_image = [["", ""], ["", ""]]
    yellow_labels = [["", ""], ["", ""]]
    yellow_pawn_image_path_home = {}

    # Board labels
    top_labels = [[None for _ in range(3)] for _ in range(6)]
    bottom_labels = [[None for _ in range(3)] for _ in range(6)]
    left_labels = [[None for _ in range(6)] for _ in range(3)]
    right_labels = [[None for _ in range(6)] for _ in range(3)]
    center_labels = [[None for _ in range(2)] for _ in range(2)]

    # Tracking dictionaries
    label_image_paths = {}
    label_pawn_count = {}
    pawn_images = {}

    # Stamp positions
    stamp_labels = []
    home_stamps = []
    star_stamps = []
    red_at_stamps = {}
    green_at_stamps = {}
    blue_at_stamps = {}
    yellow_at_stamps = {}

    # Pawn image paths
    red_pawn_images = [
        "Ludo-Images/red_pawn.png",
        "Ludo-Images/red_pawn_horizontal-L-R.png",
        "Ludo-Images/red_pawn_horizontal-R-L.png"
    ]
    green_pawn_images = [
        "Ludo-Images/green-pawn_horizontal-R-L.png",
        "Ludo-Images/green-pawn_horizontal-L-R.png",
        "Ludo-Images/green-pawn.png"
    ]
    yellow_pawn_images = [
        "Ludo-Images/yellow_pawn_horizontal-R-L.png",
        "Ludo-Images/yellow_pawn_horizontal-L-R.png",
        "Ludo-Images/yellow_pawn.png"
    ]
    blue_pawn_images = [
        "Ludo-Images/blue_pawn_horizontal-R-L.png",
        "Ludo-Images/blue_pawn_horizontal-L-R.png",
        "Ludo-Images/blue_pawn.png"
    ]

def red_block():
        global red_pice_image
        global red_labels

        border_frame1 = Frame(inner_border, bg="red", width=250, height=230)
        border_frame1.grid(row=0,column=0)
        red=Frame(border_frame1,bd=10,bg="red",width=250, height=230)
        red.pack(padx=5,pady=5)

        for i in range(0,2):
            for j in range(0,2):
                image_path=r"Ludo-Images/board-or-table-game-red-figure-20196.png"
                image= Image.open(image_path)
                image = image.resize((100, 100),Image.Resampling.LANCZOS) 
                red_pice_image[i][j] = ImageTk.PhotoImage(image)
                red_labels[i][j]=Button(red,image=red_pice_image[i][j],  bd=1, relief="solid")
                red_labels[i][j].grid(row=i,column=j,ipadx=10,ipady=2)
                red_pawn_image_path_home[red_labels[i][j]]=r"Ludo-Images/board-or-table-game-red-figure-20196.png"

def green_block():
        global green_pice_image
        global green_labels
        border_frame2 = Frame(inner_border, bg="green", width=250, height=230)
        border_frame2.grid(row=0,column=2)
        green=Frame(border_frame2,bd=10,bg="green",width=250, height=230)
        green.pack(padx=5,pady=5)

        for i in range(0,2):
            for j in range(0,2):
                image_path=r"Ludo-Images/board-or-table-game-green-figure-20194.png"
                image = Image.open(image_path)
                image = image.resize((100, 100),Image.Resampling.LANCZOS) 
                green_pice_image[i][j] = ImageTk.PhotoImage(image)
                green_labels[i][j]=Button(green,image=green_pice_image[i][j],  bd=1, relief="solid")
                green_labels[i][j].grid(row=i,column=j,ipadx=10,ipady=2)
                green_pawn_image_path_home[green_labels[i][j]]=r"Ludo-Images/board-or-table-game-green-figure-20194.png"

def blue_block():
        global blue_pice_image
        global blue_labels
        border_frame3 = Frame(inner_border, bg="blue", width=250, height=230)
        border_frame3.grid(row=2,column=0)
        blue=Frame(border_frame3,bd=10,bg="blue",width=250, height=230)
        blue.pack(padx=5,pady=5)


        for i in range(0,2):
            for j in range(0,2):
                image_path=r"Ludo-Images/board-or-table-game-blue-figure-20193.png"
                image = Image.open(image_path)
                image = image.resize((100, 100),Image.Resampling.LANCZOS) 
                blue_pice_image[i][j] = ImageTk.PhotoImage(image)
                blue_labels[i][j]=Button(blue,image=blue_pice_image[i][j],  bd=1, relief="solid")
                blue_labels[i][j].grid(row=i,column=j,ipadx=10,ipady=2)
                blue_pawn_image_path_home[blue_labels[i][j]]=r"Ludo-Images/board-or-table-game-blue-figure-20193.png"


def yellow_block():
        global yellow_pice_image
        global yellow_labels
        border_frame4 = Frame(inner_border, bg="yellow", width=250, height=230)
        border_frame4.grid(row=2,column=2)
        yellow=Frame(border_frame4,bd=10,bg="yellow",width=250, height=230)
        yellow.pack(padx=5,pady=5)

        for i in range(0,2):
            for j in range(0,2):
                image_path=r"Ludo-Images/board-or-table-game-yellow-figure-20195 (2).png"
                image = Image.open(image_path)
                image = image.resize((100, 100),Image.Resampling.LANCZOS) 
                yellow_pice_image[i][j] = ImageTk.PhotoImage(image)
                yellow_labels[i][j]=Button(yellow,image=yellow_pice_image[i][j],bd=1, relief="solid")
                yellow_labels[i][j].grid(row=i,column=j,ipadx=10,ipady=2)
                yellow_pawn_image_path_home[yellow_labels[i][j]]=r"Ludo-Images/board-or-table-game-yellow-figure-20195 (2).png"


def top_block():
        global top_labels
        f=Frame(inner_border,bg="black",width=250,height=250)
        f.grid(row=0,column=1)
        ff=Frame(f,width=250,height=250)
        ff.pack(padx=2,pady=2)
        for i in range(0,6):
            for j in range(0,3):
                if ((j==1 and i!=0) or (j==2 and i==1)):
                    top_labels[i][j]=Button(ff,text="",  bd=1, relief="solid",width=9,height=2,bg="green")
                    top_labels[i][j].grid(row=i,column=j)
                else:    
                    top_labels[i][j]=Button(ff,text="",  bd=1, relief="solid",width=9,height=2)
                    top_labels[i][j].grid(row=i,column=j)


def bottom_block():
        global bottom_labels
        f=Frame(inner_border,bg="black",width=300,height=300)
        f.grid(row=2,column=1)
        ff=Frame(f,width=300,height=300)
        ff.pack(padx=2,pady=2)
        for i in range(0,6):
            for j in range(0,3):
                if ((j==1 and i!=5) or (j==0 and i==4)):
                    bottom_labels[i][j]=Button(ff,text="",  bd=1, relief="solid",width=9,height=2,bg="blue")
                    bottom_labels[i][j].grid(row=i,column=j)
                else:    
                    bottom_labels[i][j]=Button(ff,text="",  bd=1, relief="solid",width=9,height=2)
                    bottom_labels[i][j].grid(row=i,column=j)


def left_block():
        global left_labels
        f=Frame(inner_border,bg="black",width=250,height=250)
        f.grid(row=1,column=0,sticky="n")
        ff=Frame(f,width=250,height=250)
        ff.pack(padx=2,pady=2)
        for i in range(0,3):
            for j in range(0,6):
                if ((i==1 and j!=0) or (i==0 and j==1)):
                    left_labels[i][j]=Button(ff,text="",  bd=1, relief="solid",width=5,height=4,bg="red")
                    left_labels[i][j].grid(row=i,column=j)
                else:    
                    left_labels[i][j]=Button(ff,text="",  bd=1, relief="solid",width=5,height=4)
                    left_labels[i][j].grid(row=i,column=j)


def right_block():
        global right_labels
        f=Frame(inner_border,bg="black",width=20)
        f.grid(row=1,column=2)
        ff=Frame(f,width=250,height=250)
        ff.pack(padx=2,pady=2)
        for i in range(0,3):
            for j in range(0,6):
                if ((i==1 and j!=5) or (i==2 and j==4)):
                    right_labels[i][j]=Button(ff,text="",  bd=1, relief="solid",width=5,height=4,bg="yellow")
                    right_labels[i][j].grid(row=i,column=j)
                else:    
                    right_labels[i][j]=Button(ff,text="",  bd=1, relief="solid",width=5,height=4)
                    right_labels[i][j].grid(row=i,column=j)

def center_block():
        global center_labels
        f=Frame(inner_border,bg="black",width=500,height=300)
        f.grid(row=1,column=1)
        ff=Frame(f,width=450,height=350)
        ff.pack(padx=2,pady=2)
        for i in range(0,2):
            for j in range(0,2):
                center_labels[i][j]=Button(ff,text="",bd=1, relief="solid",width=14,height=6)
                center_labels[i][j].grid(row=i,column=j)
                center_labels[i][j].grid_propagate(False)    

        center_labels[0][0]["bg"]="red"
        center_labels[0][1]["bg"]="green"
        center_labels[1][0]["bg"]="blue"
        center_labels[1][1]["bg"]="yellow"

def ludo():
    # Game state
    global turn_count, dice_count, turn_
    global elected_red_pawn, elected_green_pawn, elected_yellow_pawn, elected_blue_pawn

    # UI elements
    global root, dice, dice_image, bg_image, inner_border

    # Dice images
    global dice_images

    # Player pawns
    global red_pice_image, red_labels, red_pawn_image_path_home
    global green_pice_image, green_labels, green_pawn_image_path_home
    global blue_pice_image, blue_labels, blue_pawn_image_path_home
    global yellow_pice_image, yellow_labels, yellow_pawn_image_path_home

    # Board labels
    global top_labels, bottom_labels, left_labels, right_labels, center_labels

    # Tracking dictionaries
    global label_image_paths, label_pawn_count, pawn_images

    # Stamp positions
    global stamp_labels, home_stamps, star_stamps
    global red_at_stamps, green_at_stamps, blue_at_stamps, yellow_at_stamps

    # Pawn image paths
    global red_pawn_images, green_pawn_images, yellow_pawn_images, blue_pawn_images

    root=Tk()
    root.geometry("1500x1500")
    root.title("Ludo™ – Let the Dice Decide!")
    root.iconbitmap(r"Ludo-Images/favicon.ico")
    #board structure
    #background iamge and border frames for the board
    inner_border=None
    def bankground_and_border():
        global bgm_image
        global inner_border
        #backgorund
        image_path = r"Ludo-Images/360_F_459280851_POFE4rBfkESIy1WPAocsxnyyaZbSsYFt.jpg"
        image = Image.open(image_path)
        image = image.resize((1550, 1500))  # Resize to fit the window
        bgm_image = ImageTk.PhotoImage(image)

        # Place image as background
        bg_label = Label(root, image=bgm_image)
        bg_label.place(relwidth=1, relheight=1)  # Stretch to full window
        bg_label.lower()  # Send it to the background

        #board boreder
        outer_border= Frame(root, bg="black", width=900, height=900)
        outer_border.pack(pady=45)
        inner_border= Frame(outer_border, width=900, height=900)
        inner_border.pack(padx=2,pady=2)
    bankground_and_border()

    #colour region
    #RED
    red_block()

    #GREEN
    green_block()

    #BLUE
    blue_block()

    #YELLOW
    yellow_block()

    #small divisions frame
    #top
    top_block()

    #bottom
    bottom_block()

    #left
    left_block()

    #right
    right_block()

    #center
    center_block()

    #stamps
    def stamps():
        image_path_1=r"Ludo-Images/red_star_2cm.png"
        image = Image.open(image_path_1)
        top_labels[2][0].update()
        w= top_labels[2][0].winfo_width()
        h= top_labels[2][0].winfo_height()
        image=image.resize((w, h), Image.Resampling.LANCZOS)
        photo= ImageTk.PhotoImage(image)
        top_labels[2][0].config(width=w-4, height=h-4)
        top_labels[2][0].config(image=photo)
        top_labels[2][0].image =photo # keep reference

        image_path_2=r"Ludo-Images/green_star_5cm.png"
        image = Image.open(image_path_2)
        right_labels[0][3].update()
        w= right_labels[0][3].winfo_width()
        h= right_labels[0][3].winfo_height()
        image=image.resize((w, h), Image.Resampling.LANCZOS)
        photo= ImageTk.PhotoImage(image)
        right_labels[0][3].config(width=w-4, height=h-4)
        right_labels[0][3].config(image=photo)
        right_labels[0][3].image =photo # keep reference

        image_path_2=r"Ludo-Images/green_star_5cm.png"
        image = Image.open(image_path_2)
        right_labels[0][3].update()
        w= right_labels[0][3].winfo_width()
        h= right_labels[0][3].winfo_height()
        image=image.resize((w, h), Image.Resampling.LANCZOS)
        photo= ImageTk.PhotoImage(image)
        right_labels[0][3].config(width=w-4, height=h-4)
        right_labels[0][3].config(image=photo)
        right_labels[0][3].image =photo # keep reference

        image_path_3=r"Ludo-Images/yellow_star_5cm.png"
        image = Image.open(image_path_3)
        bottom_labels[3][2].update()
        w= bottom_labels[3][2].winfo_width()
        h= bottom_labels[3][2].winfo_height()
        image=image.resize((w, h), Image.Resampling.LANCZOS)
        photo= ImageTk.PhotoImage(image)
        bottom_labels[3][2].config(width=w-4, height=h-4)
        bottom_labels[3][2].config(image=photo)
        bottom_labels[3][2].image =photo # keep reference

        image_path_4=r"Ludo-Images/blue_star_2cm.png"
        image = Image.open(image_path_4)
        left_labels[2][2].update()
        w= left_labels[2][2].winfo_width()
        h= left_labels[2][2].winfo_height()
        image=image.resize((w, h), Image.Resampling.LANCZOS)
        photo= ImageTk.PhotoImage(image)
        left_labels[2][2].config(width=w-4, height=h-4)
        left_labels[2][2].config(image=photo)
        left_labels[2][2].image =photo # keep reference

    stamps()   

    #dice
    global dice_image
    dice_images = [
        r"Ludo-Images/dice-six-faces-one.png",
        r"Ludo-Images/dice-six-faces-two.png",
        r"Ludo-Images/dice-six-faces-three.png",
        r"Ludo-Images/dice-six-faces-four.png",
        r"Ludo-Images/dice-six-faces-five.png",
        r"Ludo-Images/dice-six-faces-six.png",
            ]

    turn_count=0
    dice_image=None
    dice=None

    #turn process
    turn_=None
    def turn():
        global turn_count
        global turn_
        if((turn_count-1)%4==0):
            turn_="red"
        elif((turn_count%2==0 and turn_count%4!=0)):
            turn_="green" 
        elif((turn_count-1)%2==0):
            turn_="yellow"   
        elif(turn_count%4==0):
            turn_="blue" 

    #gameplay

    #reset all blocks
    def reset_blocks():
        global top_labels,bottom_labels,left_labels,right_labels,center_labels
        for m in range(6):
            for n in range(3):         
                top_labels[m][n].config(command=lambda: None) 
                bottom_labels[m][n].config(command=lambda: None) 
        for m in range(3):
            for n in range(6):
                left_labels[m][n].config(command=lambda: None) 
                right_labels[m][n].config(command=lambda: None) 
        for m in range(2):
            for n in range(2):
                center_labels[m][n].config(command=lambda:None)        
    #pawn movement
    dice_count = 0  # Update this dynamically in your game
    pawn_images={}

    label_image_paths = {}

    # For left and right labels (3x6)
    for m in range(3):
        for n in range(6):
            label_image_paths[left_labels[m][n]] = ""
            label_image_paths[right_labels[m][n]] = ""

    # For top and bottom labels (6x3)
    for m in range(6):
        for n in range(3):
            label_image_paths[top_labels[m][n]] = ""
            label_image_paths[bottom_labels[m][n]] = ""



    label_pawn_count = {}

    # For left amd right labels (3x6)
    for m in range(3):
        for n in range(6):
            label_pawn_count[left_labels[m][n]] = 0
            label_pawn_count[right_labels[m][n]] = 0

    # For top and bottom labels (6x3)
    for m in range(6):
        for n in range(3):
            label_pawn_count[top_labels[m][n]] = 0
            label_pawn_count[bottom_labels[m][n]] = 0


    #overlapping pawns        
    stamp_labels=[top_labels[2][0],right_labels[0][3],bottom_labels[3][2],left_labels[2][2],top_labels[1][2],right_labels[2][4],bottom_labels[4][0],left_labels[0][1]]
    home_stamps=[top_labels[1][2],right_labels[2][4],bottom_labels[4][0],left_labels[0][1]]
    star_stamps=[top_labels[2][0],right_labels[0][3],bottom_labels[3][2],left_labels[2][2]]
    red_at_stamps={}
    green_at_stamps={}
    blue_at_stamps={}
    yellow_at_stamps={}
    # Add keys with value 0 from stamp_labels
    for label in stamp_labels:
        red_at_stamps[label] = 0
        green_at_stamps[label] = 0
        blue_at_stamps[label] = 0
        yellow_at_stamps[label] = 0

            
    def stamp_iamge_update(m,n,current_labels):
        import random
        global turn_
        print(yellow_at_stamps[current_labels[m][n]], " before condition yellow_at_stamps")
        print(green_at_stamps[current_labels[m][n]], " before condition green_at_stamps")
        print(blue_at_stamps[current_labels[m][n]], " before condition blue_at_stamps")
        print(red_at_stamps[current_labels[m][n]], " before condition red_at_stamps")
        print(label_image_paths[current_labels[m][n]])
        
        def remove_pawn_image(label):
            w = label.winfo_width()
            h = label.winfo_height()
            empty_img = PhotoImage(width=w - 4, height=h - 4)
            label.config(image=empty_img)
            label.image = empty_img
        


        def add_random_overlapping_pawn(label):
            w = label.winfo_width()
            h = label.winfo_height()
            path_list = []
            
            if label == top_labels[1][2]:
                if yellow_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/yellow_pawn_horizontal-L-R.png")
                if green_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/green-pawn_horizontal-L-R.png")
                if blue_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/blue_pawn_horizontal-L-R.png")
                if red_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/red_pawn_horizontal-L-R.png")

            elif label == left_labels[0][1]:
                if yellow_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/yellow_pawn.png")
                if green_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/green-pawn.png")
                if blue_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/blue_pawn.png")
                if red_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/red_pawn.png")

            elif label == right_labels[2][4]:
                if yellow_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/yellow_pawn.png")
                if green_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/green-pawn.png")
                if blue_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/blue_pawn.png")
                if red_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/red_pawn.png")        

            elif label == bottom_labels[4][0]:
                if yellow_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/yellow_pawn_horizontal-R-L.png")
                if green_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/green-pawn_horizontal-R-L.png")
                if blue_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/blue_pawn_horizontal-R-L.png")
                if red_at_stamps[label] > 0:
                    path_list.append(r"Ludo-Images/red_pawn_horizontal-R-L.png")
            
            if path_list:
                print(label_image_paths[label])
                new_path = random.choice(path_list)
                image = Image.open(new_path).resize((w, h), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                label.config(width=w - 4, height=h - 4, image=photo)
                label.image = photo
                label_image_paths[label]= new_path
                print(label_image_paths[label])


        def conditions(label):
            # RED
            if turn_ == "red" and red_at_stamps[label] > 0:
                if label_image_paths[label] in red_pawn_images:
                    remove_pawn_image(current_labels[m][n])
                    red_at_stamps[label] -= 1
                    label_pawn_count[label] -= 1
                    add_random_overlapping_pawn(current_labels[m][n])
                else:
                    red_at_stamps[label] -= 1
                    if label in home_stamps:
                        label_pawn_count[label] -= 1

            # GREEN
            elif turn_ == "green" and green_at_stamps[label] > 0:
                if label_image_paths[label] in green_pawn_images:
                    remove_pawn_image(current_labels[m][n])
                    green_at_stamps[label] -= 1
                    label_pawn_count[label] -= 1
                    add_random_overlapping_pawn(current_labels[m][n])
                else:
                    green_at_stamps[label] -= 1
                    if label in home_stamps:
                        label_pawn_count[label] -= 1
            # BLUE
            elif turn_ == "blue" and blue_at_stamps[label] > 0:
                if label_image_paths[label] in blue_pawn_images:
                    remove_pawn_image(current_labels[m][n])
                    blue_at_stamps[label] -= 1
                    label_pawn_count[label] -= 1
                    add_random_overlapping_pawn(current_labels[m][n])
                else:
                    blue_at_stamps[label] -= 1
                    if label in home_stamps:
                        label_pawn_count[label] -= 1

            # YELLOW
            elif turn_ == "yellow" and yellow_at_stamps[label] > 0:
                if label_image_paths[label] in yellow_pawn_images:
                    remove_pawn_image(current_labels[m][n])
                    yellow_at_stamps[label] -= 1
                    label_pawn_count[label] -= 1
                    add_random_overlapping_pawn(current_labels[m][n])
                else:
                    yellow_at_stamps[label] -= 1
                    if label in home_stamps:
                        label_pawn_count[label] -= 1

        if current_labels[m][n] in stamp_labels:
            label = current_labels[m][n]
            conditions(label)


        print(yellow_at_stamps[current_labels[m][n]], " after condition yellow_at_stamps")
        print(green_at_stamps[current_labels[m][n]], " after condition green_at_stamps")
        print(blue_at_stamps[current_labels[m][n]], " after condition blue_at_stamps")
        print(red_at_stamps[current_labels[m][n]], " after condition red_at_stamps")


            
    def place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path):
        global pawn_images,dice_count

        #color contrast
        if(current_labels[new_m][new_n] in [left_labels[0][1],left_labels[1][1],left_labels[1][2],left_labels[1][3],left_labels[1][4],left_labels[1][5]]):
            current_labels[new_m][new_n].config(bg="#960018")

        elif (current_labels[new_m][new_n] in [top_labels[1][2],top_labels[1][1],top_labels[2][1],top_labels[3][1],top_labels[4][1],top_labels[5][1]] ):
            current_labels[new_m][new_n].config(bg="#102b0a")  

        elif (current_labels[new_m][new_n] in [right_labels[2][4], right_labels[1][0], right_labels[1][1], right_labels[1][2], right_labels[1][3], right_labels[1][4]]):
            current_labels[new_m][new_n].config(bg="#97754c")

        elif (current_labels[new_m][new_n] in [bottom_labels[4][0],bottom_labels[4][1],bottom_labels[3][1],bottom_labels[2][1],bottom_labels[1][1],bottom_labels[0][1]]):
            current_labels[new_m][new_n].config(bg="#191970")


                
        if current_labels[new_m][new_n] not in star_stamps:
            label = current_labels[new_m][new_n]
            label.update()
            w = label.winfo_width()
            h = label.winfo_height()
            image = Image.open(image_path)
            #for fitting in center lebel
            if current_labels==center_labels:
                image=image.resize((w, h), Image.Resampling.LANCZOS)
            else:
                image=image.resize((w-5, h-4), Image.Resampling.LANCZOS)

            photo= ImageTk.PhotoImage(image)
            label.config(width=w-4, height=h-4)
            label.config(image=photo)
            label.image =photo # keep reference
            # Save to prevent garbage collection
            pawn_images[f"{label_name}_{new_m}_{new_n}"] = photo

        print(f"Placing image at [{new_m}][{new_n}] in label set {label_name}")    

        if new_m!=m or new_n!=n:
            reset_blocks()
            reset_pawn_selection()


   
    
    #elimination_repetition 
    def elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count):
        global label_pawn_count,label_image_paths,stamp_labels,turn_count
        import random
        print("Entered")
        empty_list = []
        if label_image_paths[current_labels[new_m][new_n]] in red_pawn_images and label_image_paths[previous_labels[m][n]] not in red_pawn_images and (current_labels[new_m][new_n] not in stamp_labels ):
                print("in red Elimination")
                for i in range(0, 2):
                    for j in range(0, 2):
                        if red_pawn_image_path_home[red_labels[i][j]] == "empty":
                            empty_list.append([i, j])  # ✅ fixed append syntax

                if empty_list:  # ✅ check to avoid crash if list is empty
                    i, j = random.choice(empty_list)
                    image_path = r"Ludo-Images/board-or-table-game-red-figure-20196.png"
                    image = Image.open(image_path)
                    image = image.resize((100, 100), Image.Resampling.LANCZOS)
                    image = ImageTk.PhotoImage(image)
                    red_pawn_image_path_home[red_labels[i][j]] = image_path
                    red_labels[i][j].config(image=image)
                    red_labels[i][j].image = image

                if dice_count!=6:    
                    turn_count-=1

        elif label_image_paths[current_labels[new_m][new_n]] in red_pawn_images and label_image_paths[previous_labels[m][n]] in red_pawn_images and (current_labels[new_m][new_n] not in stamp_labels):
            label_pawn_count[current_labels[new_m][new_n]]+=1   

        # Elimination logic for all colors

        elif label_image_paths[current_labels[new_m][new_n]] in green_pawn_images and label_image_paths[previous_labels[m][n]] not in green_pawn_images and (current_labels[new_m][new_n] not in stamp_labels):
            empty_list = []
            for i in range(0, 2):
                for j in range(0, 2):
                    if green_pawn_image_path_home[green_labels[i][j]] == "empty":
                        empty_list.append([i, j])

            if empty_list:
                i, j = random.choice(empty_list)
                image_path = r"Ludo-Images/board-or-table-game-green-figure-20194.png"
                image = Image.open(image_path)
                image = image.resize((100, 100), Image.Resampling.LANCZOS)
                image = ImageTk.PhotoImage(image)
                green_pawn_image_path_home[green_labels[i][j]] = image_path
                green_labels[i][j].config(image=image)
                green_labels[i][j].image = image

            if dice_count!=6:    
                    turn_count-=1

        elif label_image_paths[current_labels[new_m][new_n]] in yellow_pawn_images and label_image_paths[previous_labels[m][n]] not in yellow_pawn_images and (current_labels[new_m][new_n] not in stamp_labels):
            empty_list = []
            for i in range(0, 2):
                for j in range(0, 2):
                    if yellow_pawn_image_path_home[yellow_labels[i][j]] == "empty":
                        empty_list.append([i, j])

            if empty_list:
                i, j = random.choice(empty_list)
                image_path = r"Ludo-Images/board-or-table-game-yellow-figure-20195 (2).png"
                image = Image.open(image_path)
                image = image.resize((100, 100), Image.Resampling.LANCZOS)
                image = ImageTk.PhotoImage(image)
                yellow_pawn_image_path_home[yellow_labels[i][j]] = image_path
                yellow_labels[i][j].config(image=image)
                yellow_labels[i][j].image = image

            if dice_count!=6:    
                    turn_count-=1

        elif label_image_paths[current_labels[new_m][new_n]] in blue_pawn_images and label_image_paths[previous_labels[m][n]] not in blue_pawn_images and current_labels[new_m][new_n] not in stamp_labels:
            empty_list = []
            for i in range(0, 2):
                for j in range(0, 2):
                    if blue_pawn_image_path_home[blue_labels[i][j]] == "empty":
                        empty_list.append([i, j])

            if empty_list:
                i, j = random.choice(empty_list)
                image_path = r"Ludo-Images/board-or-table-game-blue-figure-20193.png"
                image = Image.open(image_path)
                image = image.resize((100, 100), Image.Resampling.LANCZOS)
                image = ImageTk.PhotoImage(image)
                blue_pawn_image_path_home[blue_labels[i][j]] = image_path
                blue_labels[i][j].config(image=image)
                blue_labels[i][j].image = image

            if dice_count!=6:    
                    turn_count-=1

        # Cases where same color pawn lands on same color pawn
        elif label_image_paths[current_labels[new_m][new_n]] in red_pawn_images and label_image_paths[previous_labels[m][n]] in red_pawn_images and current_labels[new_m][new_n] not in stamp_labels:
            label_pawn_count[current_labels[new_m][new_n]] += 1
        elif label_image_paths[current_labels[new_m][new_n]] in green_pawn_images and label_image_paths[previous_labels[m][n]] in green_pawn_images and current_labels[new_m][new_n] not in stamp_labels:
            label_pawn_count[current_labels[new_m][new_n]] += 1
        elif label_image_paths[current_labels[new_m][new_n]] in yellow_pawn_images and label_image_paths[previous_labels[m][n]] in yellow_pawn_images and current_labels[new_m][new_n] not in stamp_labels:
            label_pawn_count[current_labels[new_m][new_n]] += 1
        elif label_image_paths[current_labels[new_m][new_n]] in blue_pawn_images and label_image_paths[previous_labels[m][n]] in blue_pawn_images and current_labels[new_m][new_n] not in stamp_labels:
            label_pawn_count[current_labels[new_m][new_n]] += 1

        # Case for empty positions
        elif (label_image_paths[current_labels[new_m][new_n]] == "" or label_image_paths[current_labels[new_m][new_n]] == "path removed") and current_labels[new_m][new_n] not in stamp_labels:
            label_pawn_count[current_labels[new_m][new_n]] += 1
        #Stamp cases    
        elif current_labels[new_m][new_n] in stamp_labels:
            print("hello")
            if label_image_paths[previous_labels[m][n]] in red_pawn_images :
                red_at_stamps[current_labels[new_m][new_n]]+=1
            elif label_image_paths[previous_labels[m][n]] in green_pawn_images:
                green_at_stamps[current_labels[new_m][new_n]]+=1
            elif label_image_paths[previous_labels[m][n]] in blue_pawn_images:
                blue_at_stamps[current_labels[new_m][new_n]]+=1
            elif label_image_paths[previous_labels[m][n]] in yellow_pawn_images:
                yellow_at_stamps[current_labels[new_m][new_n]]+=1

            if current_labels[new_m][new_n] in home_stamps:
                label_pawn_count[current_labels[new_m][new_n]] += 1


    #image remover
    def image_remove(m,n,current_labels):
            
            print(label_pawn_count[current_labels[m][n]], " before condition")


            if(label_pawn_count[current_labels[m][n]]==1 and current_labels[m][n] not in stamp_labels):
                label_width = current_labels[m][n].winfo_width()
                label_height = current_labels[m][n].winfo_height()
                empty_img = PhotoImage(width=label_width-4, height=label_height-4)  # A blank image
                current_labels[m][n].config(image=empty_img)
                current_labels[m][n].image = empty_img  # Keep a reference
                label_pawn_count[current_labels[m][n]]-=1
                print(label_pawn_count[current_labels[m][n]]," image changes ")

            elif (label_pawn_count[current_labels[m][n]]>1 and current_labels[m][n] not in stamp_labels):
                label_pawn_count[current_labels[m][n]]-=1
                print(label_pawn_count[current_labels[m][n]], " image doesn't changes ")
            else:
                print("working")
                stamp_iamge_update(m,n,current_labels) 
                print(label_pawn_count[current_labels[m][n]], " after stamp condition")
        

    def colour_contrast(m,n, current_labels):
                #color contrast
                #for red (home)
                if(current_labels[m][n] in [left_labels[0][1],left_labels[1][1],left_labels[1][2],left_labels[1][3],left_labels[1][4],left_labels[1][5]] ) and label_pawn_count[current_labels[m][n]]==0:
                    current_labels[m][n].config(bg="red")
                elif(current_labels[m][n] in [left_labels[0][1],left_labels[1][1],left_labels[1][2],left_labels[1][3],left_labels[1][4],left_labels[1][5]] ) and label_pawn_count[current_labels[m][n]]>0:
                    current_labels[m][n].config(bg="#960018")  
                #for green (home)
                if current_labels[m][n] in [top_labels[1][2], top_labels[1][1], top_labels[2][1],
                                        top_labels[3][1], top_labels[4][1], top_labels[5][1]]:
                    if label_pawn_count[current_labels[m][n]] == 0:
                        current_labels[m][n].config(bg="green")  # Bright green for empty
                    elif label_pawn_count[current_labels[m][n]] >0:
                        current_labels[m][n].config(bg="#102b0a")  # Dark green for occupied
                #for yellow (home)
                if current_labels[m][n] in [right_labels[2][4], right_labels[1][0], right_labels[1][1],
                                        right_labels[1][2], right_labels[1][3], right_labels[1][4]]:
                    if label_pawn_count[current_labels[m][n]] == 0:
                        current_labels[m][n].config(bg="yellow")  # Bright gold for empty
                    elif label_pawn_count[current_labels[m][n]] > 0:
                        current_labels[m][n].config(bg="#97754c")  # Tan/brown for occupied
                #for blue(home)
                if current_labels[m][n] in [bottom_labels[4][0], bottom_labels[4][1], bottom_labels[3][1],
                                        bottom_labels[2][1], bottom_labels[1][1], bottom_labels[0][1]]:
                    if label_pawn_count[current_labels[m][n]] == 0:
                        current_labels[m][n].config(bg="blue")  # Bright blue for empty
                    elif label_pawn_count[current_labels[m][n]]> 0:
                        current_labels[m][n].config(bg="#191970")  # Dark blue for occupied

    def get_new_loc(label_name,current_labels,m, n, dice_count):
        global label_image_paths,elected_red_pawn,elected_green_pawn,elected_blue_pawn,elected_yellow_pawn,turn_count,turn_
        print(f"Clicked: {label_name}[{m}][{n}] with dice: {dice_count}")
        print(label_image_paths[current_labels[m][n]])
        new_m=None
        new_n=None
        print("hi")
        previous_labels=current_labels
        # Add your logic here

        #for red pawns
        if turn_=="red" and  (label_image_paths[current_labels[m][n]] in red_pawn_images or ( red_at_stamps.get(current_labels[m][n], 0)>0 and current_labels[m][n] in stamp_labels) ):
            print("inside red condition")
            print(f"Label name is: {label_name}")
            #image remover
            image_remove(m,n,current_labels)
            #color contrast    
            colour_contrast(m,n, current_labels)

            if label_name=="left_labels":
                print("Inside left_block condition")
                if m==0 and (5-n)>=dice_count:
                    print("Moving within left block in first row")
                    new_n=n+dice_count
                    new_m=m
                    image_path = r"Ludo-Images/red_pawn.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:   
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                elif m==2 and n>=dice_count:
                    print("Moving within left block in third row")
                    new_n=n-dice_count
                    new_m=m
                    image_path = r"Ludo-Images/red_pawn.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                elif m==2 and n<dice_count:
                    if dice_count-n==1:
                        print("Moving within left block in first coloumn")
                        new_n=0 
                        new_m=1
                        image_path = r"Ludo-Images/red_pawn.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                    else:
                        print("Moving within left block in fifth coloumn")
                        new_n=dice_count-n-1
                        new_m=1  
                        image_path = r"Ludo-Images/red_pawn.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                elif m==1 and 5-n>=dice_count:
                    print("Moving within left block in second row")
                    new_n=n+dice_count
                    new_m=m    
                    image_path = r"Ludo-Images/red_pawn.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                # Center block condition only for red
                else:
                    if m==1 and dice_count-(5-n)==1:
                        print("Moving to the center block")
                        current_labels=center_labels
                        elected_red_pawn+=1
                        new_n=0
                        new_m=0
                        current_labels[new_m][new_n].config(bg="#D40000")
                        image_path = r"Ludo-Images/board-or-table-game-red-figure-20196.png"
                    
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)
                        if elected_red_pawn==4:
                            text="🎉 RED Wins! 🏆🥇🔥"
                            image_path=r"Ludo-Images/ChatGPT Image Jun 16, 2025, 02_02_31 PM.png"
                            show_custom_message(image_path,text,root)

                    elif m==0 and (5-n)<dice_count:
                        print("Crossing to top block")
                        current_labels=top_labels
                        new_n=0
                        new_m=6-(dice_count-(5-n)) 
                        image_path = r"Ludo-Images/red_pawn_horizontal-L-R.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-L-R.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)  

                    else:
                        #As it is if conditions are not satisfied for center block
                        new_n=n
                        new_m=m
                        image_path = r"Ludo-Images/red_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

            if label_name=="top_labels":
                print("Inside top_block condition")
                if (n==0 and m>=dice_count):
                    print("Moving within top block in first coloumn")
                    new_n=0
                    new_m=m-dice_count
                    image_path = r"Ludo-Images/red_pawn_horizontal-L-R.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-L-R.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                elif(n==0 and m<dice_count) :
                    if(dice_count-m<=2):
                        print("moving within top block in top row")
                        new_m=0
                        new_n=dice_count-m 
                        image_path = r"Ludo-Images/red_pawn_horizontal-L-R.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-L-R.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)  

                    else:
                        print("moving within top block in third coloumn")
                        new_n=2
                        new_m=dice_count-m-2
                        image_path = r"Ludo-Images/red_pawn_horizontal-L-R.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-L-R.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                elif(n==1 and m==0): 
                    if dice_count==1:
                        new_n=n+1
                        new_m=0
                    else:
                        new_n=2
                        new_m=dice_count-1       
                    image_path = r"Ludo-Images/red_pawn_horizontal-L-R.png"
                    
                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-L-R.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)
                        
                elif(n==2 and 5-m>=dice_count):
                    print("moving within top block in third coloumn")
                    new_n=2
                    new_m=m+dice_count
                    image_path = r"Ludo-Images/red_pawn_horizontal-L-R.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-L-R.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)  

                else:
                    print("Crossing to right block")
                    current_labels=right_labels
                    new_n=dice_count-(5-m)-1
                    new_m=0
                    image_path = r"Ludo-Images/red_pawn.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

            if label_name == "right_labels":
                print("Inside right_block condition")
                if m==0 and (5-n) >= dice_count:
                    print("Moving within right block in top row")
                    new_m = 0
                    new_n = n + dice_count
                    image_path = r"Ludo-Images/red_pawn.png"
                    
                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

                elif m==0 and (5-n)<dice_count:
                    if(dice_count-(5-n)<=2):
                        print("Moving within right block in fifth coloumn")
                        new_m = dice_count-(5-n)
                        new_n = 5
                        image_path = r"Ludo-Images/red_pawn.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("moving within top block in third row")
                        new_n=5-(dice_count-(5-n)-2)
                        new_m=2
                        image_path = r"Ludo-Images/red_pawn.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                elif m==1 and n==5:
                    if dice_count==1:
                        print("moving within top block in fifth coloumn")
                        new_n=5
                        new_m=m+1
                        image_path = r"Ludo-Images/red_pawn.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                    else:
                        print("moving within top block in third row")
                        new_n=5-(dice_count-1)
                        new_m=2       
                        image_path = r"Ludo-Images/red_pawn.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

                elif (m==2 and n>=dice_count):
                    print("moving within top block in third row")
                    new_n=n-dice_count        
                    new_m=2
                    image_path = r"Ludo-Images/red_pawn.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)
                else:
                    print("Crossing to bottom block")
                    current_labels=bottom_labels
                    new_n=2    
                    new_m=dice_count-n-1
                    image_path = r"Ludo-Images/red_pawn_horizontal-R-L.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-R-L.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)

            if label_name == "bottom_labels":
                print("Inside bottom_block condition")
                if n == 2 and 5-m>=dice_count:
                    print("Moving within bottom in third column")
                    new_n=2
                    new_m = m+dice_count
                    image_path = r"Ludo-Images/red_pawn_horizontal-R-L.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-R-L.png"
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

                elif n == 2 and 5-m<dice_count:
                    if dice_count-(5-m)<=2:
                        print("Moving within bottom in third row")
                        new_n=n-(dice_count-(5-m))
                        new_m=5
                        image_path = r"Ludo-Images/red_pawn_horizontal-R-L.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-R-L.png"
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

                    else:
                        print("Moving within bottom in first column")
                        new_n=0
                        new_m=5-(dice_count-(5-m)-2)    
                        image_path = r"Ludo-Images/red_pawn_horizontal-R-L.png"

                        #calling elimination_repetition the pawn is placed at the new label        
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-R-L.png"
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

                elif n==1 and m==5:
                    print("Moving within bottom in first column or third row")
                    new_n=0
                    new_m=6-dice_count
                    image_path = r"Ludo-Images/red_pawn_horizontal-R-L.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-R-L.png"
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

                elif n==0 and m>=dice_count:
                    print("Moving within bottom in first column")
                    new_n=0
                    new_m=m-dice_count
                    image_path = r"Ludo-Images/red_pawn_horizontal-R-L.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn_horizontal-R-L.png"
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

                else:
                    print("Crossing to left block")
                    current_labels=left_labels
                    new_n=6-(dice_count-m) 
                    new_m=2
                    image_path = r"Ludo-Images/red_pawn.png"

                    #calling elimination_repetition the pawn is placed at the new label        
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/red_pawn.png"
                    place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)
        #for green pawns            
        elif turn_=="green" and (label_image_paths[current_labels[m][n]] in green_pawn_images  or (green_at_stamps.get(current_labels[m][n], 0)>0 and current_labels[m][n] in stamp_labels )):
            print("inside green condition")
            print(f"Label name is: {label_name}")
            #image remover
            image_remove(m,n,current_labels)
            #color contrast    
            colour_contrast(m,n, current_labels)

            if label_name == "left_labels":
                print("Inside left_block condition")
                if m == 0 and (5 - n) >= dice_count:
                    print("Moving within left block in first row")
                    new_n = n + dice_count
                    new_m = m
                    image_path = r"Ludo-Images/green-pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif m == 2 and n >= dice_count:
                    print("Moving within left block in third row")
                    new_n = n - dice_count
                    new_m = m
                    image_path = r"Ludo-Images/green-pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif m == 2 and n < dice_count:
                    print("Moving within left block in first coloumn")
                    if dice_count - n <= 2:
                        print("Moving within right block in fifth coloumn")
                        new_m = 2 - (dice_count - n)
                        new_n = 0
                        image_path = r"Ludo-Images/green-pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("moving within top block in third row")
                        new_n = (dice_count - n - 2)
                        new_m = 0
                        image_path = r"Ludo-Images/green-pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif m == 1 and n == 0:
                    if dice_count == 1:
                        print("moving within left block in fifth coloumn")
                        new_n = 0
                        new_m = m - 1    
                    else:
                        print("moving within right block in third row")
                        new_n = (dice_count - 1)
                        new_m = 0
                    image_path = r"Ludo-Images/green-pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)    
                else:
                    print("Crossing to top block")
                    current_labels = top_labels
                    new_n = 0
                    new_m = 6 - (dice_count - (5 - n))
                    image_path = r"Ludo-Images/green-pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

            if label_name == "top_labels":
                print("Inside top_block condition")
                if n == 0 and m >= dice_count:
                    print("Moving within top block in first coloumn")
                    new_n = 0
                    new_m = m - dice_count
                    image_path = r"Ludo-Images/green-pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif n == 0 and m < dice_count:
                    if dice_count - m == 1:
                        print("moving within top block in top row")
                        new_m = 0
                        new_n = 1
                        image_path = r"Ludo-Images/green-pawn_horizontal-L-R.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("moving within top block in third coloumn")
                        new_n = 1
                        new_m = dice_count - m - 1
                        image_path = r"Ludo-Images/green-pawn_horizontal-L-R.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif n == 1 and 5-m>=dice_count:
                    new_n = 1
                    new_m = m+dice_count
                    image_path = r"Ludo-Images/green-pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif n == 2 and 5 - m >= dice_count:
                    print("moving within top block in third coloumn")
                    new_n = 2
                    new_m = m + dice_count
                    image_path = r"Ludo-Images/green-pawn_horizontal-L-R.png" 
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                # Center block condition only for green    
                else:
                    if n==1 and dice_count-(5-m)==1:
                        print("Moving to the center block")
                        current_labels=center_labels
                        elected_green_pawn+=1
                        new_n=1
                        new_m=0
                        current_labels[new_m][new_n].config(bg="#102b0a")
                        image_path = r"Ludo-Images/board-or-table-game-green-figure-20194.png"
                    
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"

                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)
                        if elected_green_pawn==4:
                            text="🎉 GREEN Wins! 🏆🥇🔥"
                            image_path=r"Ludo-Images/ChatGPT Image Jun 16, 2025, 01_54_59 PM.png"
                            show_custom_message(image_path,text,root)

                    elif n==2 and (5-m)<dice_count:
                        print("Crossing to right block")
                        current_labels = right_labels
                        new_n = dice_count - (5 - m) - 1
                        new_m = 0
                        image_path = r"Ludo-Images/green-pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        #As it is if conditions are not satisfied for center block  
                        new_n = n
                        new_m = m
                        image_path = r"Ludo-Images/green-pawn_horizontal-L-R.png" 
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
            if label_name == "right_labels":
                print("Inside right_block condition")
                if m == 0 and (5 - n) >= dice_count:
                    print("Moving within right block in top row")
                    new_m = 0
                    new_n = n + dice_count
                    image_path = r"Ludo-Images/green-pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif m == 0 and (5 - n) < dice_count:
                    if dice_count - (5 - n) <= 2:
                        print("Moving within right block in fifth coloumn")
                        new_m = dice_count - (5 - n)
                        new_n = 5
                        image_path = r"Ludo-Images/green-pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("moving within right block in third row")
                        new_n = 5 - (dice_count - (5 - n) - 2)
                        new_m = 2
                        image_path = r"Ludo-Images/green-pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif m == 1 and n == 5:
                    if dice_count == 1:
                        print("moving within right block in fifth coloumn")
                        new_n = 5
                        new_m = m + 1
                    else:
                        print("moving within right block in third row")
                        new_n = 5 - (dice_count - 1)
                        new_m = 2
                    image_path = r"Ludo-Images/green-pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif m == 2 and n >= dice_count:
                    print("moving within right block in third row")
                    new_n = n - dice_count        
                    new_m = 2
                    image_path = r"Ludo-Images/green-pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                else:
                    print("Crossing to bottom block")
                    current_labels = bottom_labels
                    new_n = 2    
                    new_m = dice_count - n - 1
                    image_path = r"Ludo-Images/green-pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

            if label_name == "bottom_labels":
                print("Inside bottom_block condition")
                if n == 2 and 5 - m >= dice_count:
                    print("Moving within bottom in third column")
                    new_n = 2
                    new_m = m + dice_count
                    image_path = r"Ludo-Images/green-pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif n == 2 and 5 - m < dice_count:
                    if dice_count - (5 - m) <= 2:
                        print("Moving within bottom in third row")
                        new_n = n - (dice_count - (5 - m))
                        new_m = 5
                        image_path = r"Ludo-Images/green-pawn_horizontal-R-L.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within bottom in first column")
                        new_n = 0
                        new_m = 5 - (dice_count - (5 - m) - 2)    
                        image_path = r"Ludo-Images/green-pawn_horizontal-R-L.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif n == 1 and m == 5:
                    print("Moving within bottom in first column or third row")
                    new_n = 0
                    new_m = 6 - dice_count
                    image_path = r"Ludo-Images/green-pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                elif n == 0 and m >= dice_count:
                    print("Moving within bottom in first column")
                    new_n = 0
                    new_m = m - dice_count
                    image_path = r"Ludo-Images/green-pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                else:
                    print("Crossing to left block")
                    current_labels = left_labels
                    new_n = 6 - (dice_count - m) 
                    new_m = 2
                    image_path = r"Ludo-Images/green-pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]]==0:
                        label_image_paths[previous_labels[m][n]]="path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]]= image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
        
        #for yellow pawns 
        elif turn_=="yellow" and (label_image_paths[current_labels[m][n]] in yellow_pawn_images or (yellow_at_stamps.get(current_labels[m][n], 0)>0 and current_labels[m][n] in stamp_labels)):
            print("inside yellow condition")
            print(f"Label name is: {label_name}")
            # Image remover
            image_remove(m, n, current_labels)
            # Color contrast    
            colour_contrast(m, n, current_labels)

            if label_name == "left_labels":
                print("Inside left_block condition")
                if m == 0 and (5 - n) >= dice_count:
                    print("Moving within left block in first row")
                    new_n = n + dice_count
                    new_m = m
                    image_path = r"Ludo-Images/yellow_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 2 and n >= dice_count:
                    print("Moving within left block in third row")
                    new_n = n - dice_count
                    new_m = m
                    image_path = r"Ludo-Images/yellow_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 2 and n < dice_count:
                    print("Moving within left block in first column")
                    if dice_count - n <= 2:
                        print("Moving within left block in first column")
                        new_m = 2 - (dice_count - n)
                        new_n = 0
                        image_path = r"Ludo-Images/yellow_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within left block in third row")
                        new_n = (dice_count - n - 2)
                        new_m = 0
                        image_path = r"Ludo-Images/yellow_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 1 and n == 0:
                    if dice_count == 1:
                        print("Moving within left block in first column")
                        new_n = 0
                        new_m = m - 1
                    else:
                        print("Moving within left block in third row")
                        new_n = (dice_count - 1)
                        new_m = 0
                    image_path = r"Ludo-Images/yellow_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                else:
                    print("Crossing to top block")
                    current_labels = top_labels
                    new_n = 0
                    new_m = 6 - (dice_count - (5 - n))
                    image_path = r"Ludo-Images/yellow_pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

            elif label_name == "top_labels":
                print("Inside top_block condition")
                if n == 0 and m >= dice_count:
                    print("Moving within top block in first column")
                    new_n = 0
                    new_m = m - dice_count
                    image_path = r"Ludo-Images/yellow_pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 0 and m < dice_count:
                    if dice_count - m <= 2:
                        print("Moving within top block in top row")
                        new_m = 0
                        new_n = dice_count - m
                        image_path = r"Ludo-Images/yellow_pawn_horizontal-L-R.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within top block in third column")
                        new_n = 2
                        new_m = dice_count - m - 2
                        image_path = r"Ludo-Images/yellow_pawn_horizontal-L-R.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 1 and m == 0:
                    if dice_count == 1:
                        new_n = n + 1
                        new_m = 0
                    else:
                        new_n = 2
                        new_m = dice_count - 1
                    image_path = r"Ludo-Images/yellow_pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 2 and 5 - m >= dice_count:
                    print("Moving within top block in third column")
                    new_n = 2
                    new_m = m + dice_count
                    image_path = r"Ludo-Images/yellow_pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                else:
                    print("Crossing to right block")
                    current_labels = right_labels
                    new_n = dice_count - (5 - m) - 1
                    new_m = 0
                    image_path = r"Ludo-Images/yellow_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

            elif label_name == "right_labels":
                print("Inside right_block condition")
                if m == 0 and (5 - n) >= dice_count:
                    print("Moving within right block in top row")
                    new_m = 0
                    new_n = n + dice_count
                    image_path = r"Ludo-Images/yellow_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 0 and (5 - n) < dice_count:
                    if dice_count - (5 - n) <= 1:
                        print("Moving within right block in fifth column")
                        new_m = 1
                        new_n = 5
                        image_path = r"Ludo-Images/yellow_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within right block in first coloumn")
                        new_n = 5- (dice_count - (5 - n) - 1)
                        new_m = 1
                        image_path = r"Ludo-Images/yellow_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 1 and n>=dice_count:
                    print("Moving within right block in second row")
                    new_n = n-dice_count
                    new_m = 1
                    image_path = r"Ludo-Images/yellow_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 2 and n >= dice_count:
                    print("Moving within right block in third row")
                    new_n = n - dice_count
                    new_m = 2
                    image_path = r"Ludo-Images/yellow_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                # Center block condition only for yellow
                else:
                    if m==1 and dice_count-n==1:
                        print("Moving to the center block")
                        current_labels=center_labels
                        elected_yellow_pawn+=1
                        new_n=1
                        new_m=1
                        current_labels[new_m][new_n].config(bg="#97754c")
                        image_path = r"Ludo-Images/board-or-table-game-yellow-figure-20195 (2).png"
                    
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)
                        if elected_yellow_pawn==4:
                            text="🎉 YELLOW Wins! 🏆🥇🔥"
                            image_path=r"Ludo-Images/ChatGPT Image Jun 16, 2025, 01_47_20 PM.png"
                            show_custom_message(image_path,text,root)

                    elif m==2 and n<dice_count:
                        print("Crossing to bottom block")
                        current_labels = bottom_labels
                        new_n = 2
                        new_m = dice_count - n - 1
                        image_path = r"Ludo-Images/yellow_pawn_horizontal-R-L.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

                    else:
                        #As it is if conditions are not satisfied for center block
                        new_n=n
                        new_m=m
                        image_path = r"Ludo-Images/yellow_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]=r"Ludo-Images/yellow_pawn.png"
                        place_pawn_image(label_name,current_labels, new_m, new_n, n, m, image_path)
                        
        

            elif label_name == "bottom_labels":
                print("Inside bottom_block condition")
                if n == 2 and 5 - m >= dice_count:
                    print("Moving within bottom in third column")
                    new_n = 2
                    new_m = m + dice_count
                    image_path = r"Ludo-Images/yellow_pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 2 and 5 - m < dice_count:
                    if dice_count - (5 - m) <= 2:
                        print("Moving within bottom in third row")
                        new_n = n - (dice_count - (5 - m))
                        new_m = 5
                        image_path = r"Ludo-Images/yellow_pawn_horizontal-R-L.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within bottom in first column")
                        new_n = 0
                        new_m = 5 - (dice_count - (5 - m) - 2)
                        image_path = r"Ludo-Images/yellow_pawn_horizontal-R-L.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 1 and m == 5:
                    print("Moving within bottom in first column or third row")
                    new_n = 0
                    new_m = 6 - dice_count
                    image_path = r"Ludo-Images/yellow_pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 0 and m >= dice_count:
                    print("Moving within bottom in first column")
                    new_n = 0
                    new_m = m - dice_count
                    image_path = r"Ludo-Images/yellow_pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                else:
                    print("Crossing to left block")
                    current_labels = left_labels
                    new_n = 6 - (dice_count - m)
                    new_m = 2
                    image_path = r"Ludo-Images/yellow_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

        #for blue pawns
        elif turn_=="blue"and (label_image_paths[current_labels[m][n]] in blue_pawn_images or (blue_at_stamps.get(current_labels[m][n], 0)>0 and current_labels[m][n] in stamp_labels)):
            print("inside blue condition")
            print(f"Label name is: {label_name}")
            # Image remover
            image_remove(m, n, current_labels)
            # Color contrast    
            colour_contrast(m, n, current_labels)

            if label_name == "left_labels":
                print("Inside left_block condition")
                if m == 0 and (5 - n) >= dice_count:
                    print("Moving within left block in first row")
                    new_n = n + dice_count
                    new_m = m
                    image_path = r"Ludo-Images/blue_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 2 and n >= dice_count:
                    print("Moving within left block in third row")
                    new_n = n - dice_count
                    new_m = m
                    image_path = r"Ludo-Images/blue_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 2 and n < dice_count:
                    print("Moving within left block in first column")
                    if dice_count - n <= 2:
                        print("Moving within left block in fifth column")
                        new_m = 2 - (dice_count - n)
                        new_n = 0
                        image_path = r"Ludo-Images/blue_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within left block in third row")
                        new_n = (dice_count - n - 2)
                        new_m = 0
                        image_path = r"Ludo-Images/blue_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 1 and n == 0:
                    if dice_count == 1:
                        print("Moving within left block in fifth column")
                        new_n = 0
                        new_m = m - 1
                    else:
                        print("Moving within left block in third row")
                        new_n = (dice_count - 1)
                        new_m = 0
                    image_path = r"Ludo-Images/blue_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                else:
                    print("Crossing to top block")
                    current_labels = top_labels
                    new_n = 0
                    new_m = 6 - (dice_count - (5 - n))
                    image_path = r"Ludo-Images/blue_pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

            elif label_name == "top_labels":
                print("Inside top_block condition")
                if n == 0 and m >= dice_count:
                    print("Moving within top block in first column")
                    new_n = 0
                    new_m = m - dice_count
                    image_path = r"Ludo-Images/blue_pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 0 and m < dice_count:
                    if dice_count - m <= 2:
                        print("Moving within top block in top row")
                        new_m = 0
                        new_n = dice_count - m
                        image_path = r"Ludo-Images/blue_pawn_horizontal-L-R.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within top block in third column")
                        new_n = 2
                        new_m = dice_count - m - 2
                        image_path = r"Ludo-Images/blue_pawn_horizontal-L-R.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 1 and m == 0:
                    if dice_count == 1:
                        new_n = n + 1
                        new_m = 0
                    else:
                        new_n = 2
                        new_m = dice_count - 1
                    image_path = r"Ludo-Images/blue_pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 2 and 5 - m >= dice_count:
                    print("Moving within top block in third column")
                    new_n = 2
                    new_m = m + dice_count
                    image_path = r"Ludo-Images/blue_pawn_horizontal-L-R.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                else:
                    print("Crossing to right block")
                    current_labels = right_labels
                    new_n = dice_count - (5 - m) - 1
                    new_m = 0
                    image_path = r"Ludo-Images/blue_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

            elif label_name == "right_labels":
                print("Inside right_block condition")
                if m == 0 and (5 - n) >= dice_count:
                    print("Moving within right block in top row")
                    new_m = 0
                    new_n = n + dice_count
                    image_path = r"Ludo-Images/blue_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 0 and (5 - n) < dice_count:
                    if dice_count - (5 - n) <= 2:
                        print("Moving within right block in fifth column")
                        new_m = dice_count - (5 - n)
                        new_n = 5
                        image_path = r"Ludo-Images/blue_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within right block in third row")
                        new_n = 5 - (dice_count - (5 - n) - 2)
                        new_m = 2
                        image_path = r"Ludo-Images/blue_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 1 and n == 5:
                    if dice_count == 1:
                        print("Moving within right block in fifth column")
                        new_n = 5
                        new_m = m + 1
                    else:
                        print("Moving within right block in third row")
                        new_n = 5 - (dice_count - 1)
                        new_m = 2
                    image_path = r"Ludo-Images/blue_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif m == 2 and n >= dice_count:
                    print("Moving within right block in third row")
                    new_n = n - dice_count
                    new_m = 2
                    image_path = r"Ludo-Images/blue_pawn.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                else:
                    print("Crossing to bottom block")
                    current_labels = bottom_labels
                    new_n = 2
                    new_m = dice_count - n - 1
                    image_path = r"Ludo-Images/blue_pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)

            elif label_name == "bottom_labels":
                print("Inside bottom_block condition")
                if n == 2 and 5 - m >= dice_count:
                    print("Moving within bottom in third column")
                    new_n = 2
                    new_m = m + dice_count
                    image_path = r"Ludo-Images/blue_pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 2 and 5 - m < dice_count:
                    if dice_count - (5 - m) == 1:
                        print("Moving within bottom in third row")
                        new_n = 1
                        new_m = 5
                        image_path = r"Ludo-Images/blue_pawn_horizontal-R-L.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        print("Moving within bottom in first column")
                        new_n = 1
                        new_m = 5 - (dice_count - (5 - m) - 1)
                        image_path = r"Ludo-Images/blue_pawn_horizontal-R-L.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 1 and m >=dice_count:
                    new_n = 1
                    new_m = m-dice_count
                    image_path = r"Ludo-Images/blue_pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                
                elif n == 0 and m >= dice_count:
                    print("Moving within bottom in first column")
                    new_n = 0
                    new_m = m - dice_count
                    image_path = r"Ludo-Images/blue_pawn_horizontal-R-L.png"
                    elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                    if label_pawn_count[previous_labels[m][n]] == 0:
                        label_image_paths[previous_labels[m][n]] = "path removed"
                    if current_labels[new_m][new_n] not in star_stamps:
                        label_image_paths[current_labels[new_m][new_n]] = image_path
                    place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                # Center block condition only for blue
                else:
                    if n==1 and dice_count-m==1:
                        current_labels=center_labels
                        new_n = 0
                        new_m = 1
                        current_labels[new_m][new_n].config(bg="#191970")
                        image_path = r"Ludo-Images/board-or-table-game-blue-figure-20193.png"
                        elected_blue_pawn+=1
                
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                    
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                        if elected_blue_pawn==4:
                            text="🎉 BLUE Wins! 🏆🥇🔥"
                            image_path=r"Ludo-Images/ChatGPT Image Jun 16, 2025, 01_51_19 PM.png"
                            show_custom_message(image_path,text,root)


                    elif n==0 and m<dice_count:    
                        print("Crossing to left block")
                        current_labels = left_labels
                        new_n = 6 - (dice_count - m)
                        new_m = 2
                        image_path = r"Ludo-Images/blue_pawn.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]] == 0:
                            label_image_paths[previous_labels[m][n]] = "path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]] = image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)
                    else:
                        #As it is if conditions are not satisfied for center block  
                        new_n = n
                        new_m = m
                        image_path = r"Ludo-Images/blue_pawn_horizontal-R-L.png"
                        elimination_repetition(m,n,new_m,new_n,current_labels,previous_labels,dice_count)
                        if label_pawn_count[previous_labels[m][n]]==0:
                            label_image_paths[previous_labels[m][n]]="path removed"
                        if current_labels[new_m][new_n] not in star_stamps:
                            label_image_paths[current_labels[new_m][new_n]]= image_path
                        place_pawn_image(label_name, current_labels, new_m, new_n, n, m, image_path)


    def set_label_commands():
        global dice_count
        for m in range(6):
            for n in range(3):
                if isinstance(top_labels[m][n], Button):
                    top_labels[m][n]['command'] = lambda m=m, n=n: get_new_loc("top_labels", top_labels,m, n,dice_count)
                if isinstance(bottom_labels[m][n], Button):
                    bottom_labels[m][n]['command'] = lambda m=m, n=n: get_new_loc("bottom_labels", bottom_labels,m, n,dice_count)
        for m in range(3):
            for n in range(6):
                if isinstance(left_labels[m][n], Button):
                    left_labels[m][n]['command'] = lambda m=m, n=n: get_new_loc("left_labels", left_labels, m, n,dice_count)
                if isinstance(right_labels[m][n], Button):
                    right_labels[m][n]['command'] = lambda m=m, n=n: get_new_loc("right_labels", right_labels, m, n,dice_count)

        for m in range(2):
            for n in range(2):
                if isinstance(center_labels[m][n], Button):
                    center_labels[m][n]['command'] = None
                    
    # Call this after all blocks are initialized



    #check for 6 conditon and make the buttons unclickable
    def reset_pawn_selection():
        global red_labels,green_labels,blue_labels,yellow_labels
        """Disables clicking on all red pawns after each turn"""
        for i in range(2):
            for j in range(2):
                red_labels[i][j].config(command=lambda: None)  # Disable pawn selection
        for i in range(2):
            for j in range(2):
                blue_labels[i][j].config(command=lambda: None)  # Disable pawn selection        
        for i in range(2):
            for j in range(2):
                green_labels[i][j].config(command=lambda: None)  # Disable pawn selection
        for i in range(2):
            for j in range(2):
                yellow_labels[i][j].config(command=lambda: None)  # Disable pawn selection


    def selected_pawn_out(m,n):
        global dice_count
        global top_labels,left_labels,right_labels,bottom_labels,turn_
        global red_pice_image,green_pice_image,yellow_pice_image,blue_pice_image
        global label_image_paths
    

        if((red_pawn_image_path_home[red_labels[m][n]]!="empty" and turn_=="red") or (green_pawn_image_path_home[green_labels[m][n]]!="empty"and turn_=="green") or (yellow_pawn_image_path_home[yellow_labels[m][n]]!="empty" and turn_=="yellow") or (blue_pawn_image_path_home[blue_labels[m][n]]!="empty" and turn_=="blue") ):
            reset_blocks()
            reset_pawn_selection()

        if turn_=="red" and red_pawn_image_path_home[red_labels[m][n]]!="empty":
            empty_img =PhotoImage(width=100, height=100)  # A blank image
            red_labels[m][n].config(image=empty_img)
            red_labels[m][n].image = empty_img  # Keep a reference
            red_pawn_image_path_home[red_labels[m][n]]="empty"
            image_path = r"Ludo-Images/red_pawn.png"
            image = Image.open(image_path)
            image = image.resize((39, 65), Image.Resampling.LANCZOS)
            left_labels[0][1].config(height=0,width=0 )
            left_labels[0][1].config(bg="#960018")
            red_pice_image[m][n] = ImageTk.PhotoImage(image)  # Store image in a global variable
            left_labels[0][1].config(image=red_pice_image[m][n])  # Place pawn on board

            label_image_paths[left_labels[0][1]]=r"Ludo-Images/red_pawn.png"
            label_pawn_count[left_labels[0][1]]+=1
            red_at_stamps[left_labels[0][1]] += 1

        elif turn_=="green" and green_pawn_image_path_home[green_labels[m][n]]!="empty":
            empty_img =PhotoImage(width=100, height=100)  # A blank image
            green_labels[m][n].config(image=empty_img)
            green_labels[m][n].image = empty_img  # Keep a reference
            green_pawn_image_path_home[green_labels[m][n]]="empty"
            image_path = r"Ludo-Images/green-pawn_horizontal-L-R.png"
            image = Image.open(image_path)
            image = image.resize((67, 35), Image.Resampling.LANCZOS)
            top_labels[1][2].config(height=0,width=0 )
            top_labels[1][2].config(bg="#102b0a")
            green_pice_image[m][n] = ImageTk.PhotoImage(image)  # Store image in a global variable
            top_labels[1][2].config(image=green_pice_image[m][n])  # Place pawn on board

            label_image_paths[top_labels[1][2]]=r"Ludo-Images/green-pawn_horizontal-L-R.png"
            label_pawn_count[top_labels[1][2]]+=1
            green_at_stamps[top_labels[1][2]] += 1

        elif turn_=="yellow"and yellow_pawn_image_path_home[yellow_labels[m][n]]!="empty":
            empty_img =PhotoImage(width=100, height=100)  # A blank image
            yellow_labels[m][n].config(image=empty_img)
            yellow_labels[m][n].image = empty_img # Keep a reference
            yellow_pawn_image_path_home[yellow_labels[m][n]]="empty"
            image_path =r"Ludo-Images/yellow_pawn.png"
            image = Image.open(image_path)
            image = image.resize((39, 65), Image.Resampling.LANCZOS)
            right_labels[2][4].config(height=0,width=0 )
            right_labels[2][4].config(bg="#97754c")
            yellow_pice_image[m][n] = ImageTk.PhotoImage(image)  # Store image in a global variable
            right_labels[2][4].config(image=yellow_pice_image[m][n])  # Place pawn on board

            label_image_paths[right_labels[2][4]]=r"Ludo-Images/yellow_pawn.png"
            label_pawn_count[right_labels[2][4]]+=1
            yellow_at_stamps[right_labels[2][4]] += 1


        elif turn_=="blue"and blue_pawn_image_path_home[blue_labels[m][n]]!="empty":
            empty_img =PhotoImage(width=100, height=100)  # A blank image
            blue_labels[m][n].config(image=empty_img)
            blue_labels[m][n].image = empty_img  # Keep a reference
            blue_pawn_image_path_home[blue_labels[m][n]]="empty"
            image_path = r"Ludo-Images/blue_pawn_horizontal-R-L.png"
            image = Image.open(image_path) 
            image = image.resize((67, 35), Image.Resampling.LANCZOS)
            bottom_labels[4][0].config(height=0,width=0)
            bottom_labels[4][0].config(bg="#191970")
            blue_pice_image[m][n] = ImageTk.PhotoImage(image)  # Store image in a global variable
            bottom_labels[4][0].config(image=blue_pice_image[m][n])  # Place pawn on board

            label_image_paths[bottom_labels[4][0]]=r"Ludo-Images/blue_pawn_horizontal-R-L.png"
            label_pawn_count[bottom_labels[4][0]]+=1
            blue_at_stamps[bottom_labels[4][0]] += 1

    def pawn_select():

        global turn_, red_labels, blue_labels, green_labels, yellow_labels
        if turn_ == "red":
            for i in range(2):
                for j in range(2):
                    red_labels[i][j].config(command=lambda m=i, n=j: selected_pawn_out(m,n)) 
            
        elif turn_ == "blue":
            for i in range(2):
                for j in range(2):
                    blue_labels[i][j].config(command=lambda m=i, n=j: selected_pawn_out(m,n))
            

        elif turn_ == "green":
            for i in range(2):
                for j in range(2):
                    green_labels[i][j].config(command=lambda m=i, n=j: selected_pawn_out(m,n))
        

        elif turn_ == "yellow":
            for i in range(2):
                for j in range(2):
                    yellow_labels[i][j].config(command=lambda m=i, n=j: selected_pawn_out(m,n))
            


    def player_focus():
        for color, labels in [("red", red_labels), ("green", green_labels),
                            ("blue", blue_labels), ("yellow", yellow_labels)]:
            state = NORMAL if turn_ == color else DISABLED
            bg_color = "white" if turn_ == color else "#cccccc"  # Light ash color
        
            for i in range(2):
                for j in range(2):
                    labels[i][j].config(state=state, bg=bg_color)
            

    # "6" turn repeate process
    def turn_repeate():
        global turn_count
        global dice_count
        if dice_count==6:
            turn_count=turn_count -1
        
    #dice roll process
    def diceroll(event):
        global turn_
        global dice_count
        global turn_count
        #Here the previous dice_count is used the updated dice_count is not included in this callings
        turn_count+=1
        turn_repeate() 
        turn()
        player_focus() 
        roll_animation()
        print(turn_)
        print("turn count: ",turn_count)
        print("Before roll animation finishes - dice count: ",dice_count)
    def dice_code():
        global dice_image
        global dice
        image_path = r"Ludo-Images/perspective-dice-six-faces-random.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((100, 100))  # Resize to 100x100
        dice_image = ImageTk.PhotoImage(resized_image)
        dice = Button(root,image=dice_image,bd=10, width=100, height=100)
        dice.place(x=1250,y=350)
        dice.bind("<Button-1>",diceroll)
    dice_code()
    def update_image(image_path):
        global dice_image  
        original_image = Image.open(image_path)
        resized_image = original_image.resize((100, 100))
        dice_image = ImageTk.PhotoImage(resized_image)
        dice["image"] = dice_image
        
    def roll_animation(count=15):
        global dice_count
        if count > 0:
            random_image = random.choice(dice_images)  # Pick a random dice face
            update_image(random_image)  # Update dice image
            root.after(5, lambda: roll_animation(count - 1))  # Repeat after 100ms
        else:
            final_image_path = random.choice(dice_images)  # Final dice face
            update_image(final_image_path) # Show final result       
            dice_count = dice_images.index(final_image_path) + 1
            print("After roll animation finishes - dice count: ",dice_count)
        
            set_label_commands()        
            if dice_count==6 :   
                pawn_select()
            else:
                reset_pawn_selection()
            set_label_commands()

    root.mainloop()
ludo()