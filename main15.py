
#problem in line 310-320-25
#uncommenct 326 and comment 325

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as filedialog
import pygame
#import keyboard
import os
import re
#import stagger as stg
from PIL import Image as pilmg
import io
from mutagen.mp3 import MP3 as muta



#from PIL import ImageTk, Image
global masterWin
def masterWin():

    global root

    root = Tk()

    #root.title("Calvin Player")

    #root.iconbitmap("Images/logo.ico") #"icon.ico"
    root.geometry("480x600") #("480x720")
    root.resizable(False,False)
    root.overrideredirect(1)
    root.attributes("-alpha", 0.9)
    root.attributes("-transparentcolor", "blue")
    #root["bg"] = "grMay"

    root.attributes("-topmost", True)

    '''wwidth = root.winfo_width()
    rwidth = root.winfo_reqwidth()
    print("wwidth: ", wwidth)
    print("rwidth", rwidth)'''

    pygame.mixer.init()

    

    #minimimg = PhotoImage(file="Images/minimz.png")

    #minimize to a litte tray
    def miniPlayer(*args):
        
        
        global root

        #winwidth = root.winfo_screenwidth()
        #winheight = root.winfo_screenheight()

        #windowWidth = root.winfo_reqwidth()
        #windowHeight = root.winfo_reqheight()

        #root.geometry("{0}x{1}".format(winwidth//3+windowWidth//8, winheight//4))

        root.geometry("266x85")
        title_bar.place_forget()  
        pathButton.place_forget()  
        
        closeB.place(x=240, y=5)
        minimB.place(x=10, y=5)  
        openB.place(x=40, y=5)
        topMostButton.place(x=65, y=5)


        openB.config(bg="#156f84")
        topMostButton.config(bg="#156f84")

        wallLabel.config(image=minibgimg)        

        def makeBig(*args):
            root.bind("<Alt-Control--KeyPress-m>", miniPlayer)

            
            try:
                playB2.place_forget()
            
                nextB2.place_forget()
                prevB2.place_forget()

                title_bar.place(x=45, y=10)
                closeB.place(x=440, y=15)
                minimB.place(x=20, y=15)
                openB.place(x=45, y=28)
                topMostButton.place(x=70, y=28)
                pathButton.place(x=100, y=30)
                
                wallLabel.config(image=wallimg)
                openB.config(bg="#44bfd3")
                topMostButton.config(bg="#44bfd3")

    
                root.geometry("480x600")
                minimB.config(command=miniPlayer)
                
                music_Label.place(y=240, anchor=CENTER, x=240)
                
                #playB.place(x=220, y=425)
        
                #nextB.place(x=325, y=430)
                #prevB.place(x=95, y=430)

                #pathButton.place(x=100, y=30)
                pathButton.config(command=showpath)
            except:
                pass

        root.bind("<Alt-Control--KeyPress-m>", makeBig)

        minimB.config(command=makeBig)



        


        music_Label.place_forget()

        #playB.place_forget()
        
        #nextB.place_forget()
        #prevB.place_forget()

        playB2.place(x=95, y=10)
        
        nextB2.place(x=200, y=40)
        prevB2.place(x=25, y=40)

        #pathButton.place_forget()


        #start.mainloop()

    #minimB = Button(image=minimimg, borderwidth=0, bg="#CB2161", command=miniPlayer)
    

    #borderwidth = 2     to be used in buttons
    #borderwidth, highlightthickness=4, highlightcolor="black", highlightbackground="black" 
    #button modes: relief= "groove", "solid", "ridge", "sunken", "raised", "flat"

    #playB = Button(text="play", borderwidth=0,  bg='#F0FFFF', fg='#FFFFFF', compound=LEFT, anchor="se", command=root.destroy)

    playimg = PhotoImage(file="Images/unpause.png")
    pauseimg = PhotoImage(file="Images/pause.png")
    nextimg = PhotoImage(file="Images/next.png")
    previmg = PhotoImage(file="Images/prev.png")
    
    #little button images go here...
    playimg2 = PhotoImage(file="Images/unpause1.png")
    pauseimg2 = PhotoImage(file="Images/pause1.png")
    nextimg2 = PhotoImage(file="Images/next1.png")
    previmg2 = PhotoImage(file="Images/prev1.png")
    

    wallimg = PhotoImage(file="Images/backg2.png")
    minibgimg = PhotoImage(file="Images/minibackg.png")
    pathimg = PhotoImage(file="Images/showpath.png")

    biglist = []

    


    

    #print(rwi)

    #laytime = Label(text=" ", bg="black", fg="white")

        
    def showplaytime(*args):
        timelive = pygame.mixer.music.get_pos()
        playtime.config(text=str(timelive))
        playtime.place(x=400, y=580)

    #root.after(1000, showplaytime)

    #length_Label = Label(text="track length", bg="#156f84", fg="white")
  
    global prevMusic

    global currentMusic
    currentMusic = 0
    
    def prevMusic(*args):

        global currentMusic

        if currentMusic > 0:

            currentMusic -= 1

            playB.config(image=playimg, command=play)
            playB2.config(image=playimg2, command=play)
            
            #nextB.config(command= lambda: nextMusic(musicNum+1))
            #prevB.config(command= lambda: prevMusic(musicNum-1))
    
            pygame.mixer.music.load(biglist[currentMusic])
            
            audio = muta(biglist[currentMusic])
            secs = int(audio.info.length)
            secns = int(audio.info.length)
            hrs = secs // 3600
            secs %= 3600

            mins = secs // 60
            secs %= 60

            total_length = f"{hrs}:{mins}:{secs}"
            print(total_length)

            length_Label.config(text=total_length)
            
            
            #pygame.mixer.music.play()

            wait = secns * 1000 + 500


            

            basename = os.path.basename(biglist[currentMusic])

            
            
            musicName.config(text=str(basename)[:-4])

            root.bind("<Control-Right>", nextMusic)
            root.bind("<Control-Left>", prevMusic)
            root.bind("<Control-KeyPress-n>", nextMusic)
            root.bind("<Control--KeyPress-p>", prevMusic)
            root.bind("<Alt-Control-KeyPress-o>", ask)
            root.bind("<Alt-Control-KeyPress-m>", miniPlayer)
            root.bind("<Alt-KeyPress-Up>", Up)
            #root.bind("<Alt--KeyPress-Down>", Down)


            def showpath(*args):

                openlabel.place_forget()
      
                nextlabel.place_forget()
                prevlabel.place_forget()
                    
                pathlabel.config(text=biglist[currentMusic])

                pathlabel.place(y=570, anchor=CENTER, x=233)
                pathlabel.after(4000, pathlabel.place_forget)

            def popshowpathlabelf(*args):
                popshowpathlabel.place(x=60, y=45)
                popshowpathlabel.after(4000, popshowpathlabel.place_forget)

            #pathButton.place(y=110, x=95)
            pathButton.config(command=showpath)
            pathButton.bind("<Enter>", popshowpathlabelf)

            #root.after(wait, nextMusic)
            def queue(*args):
                pos = pygame.mixer.music.get_pos()
                #print(pos)
                if (pos == -1) and (currentMusic < len(biglist)):
                    print("Not play\nCalling next")
                    nextMusic()
                root.after(1, queue)
                                
            
            #root.after(1, queue)
            pygame.mixer.music.play()
            queue()

  

    global nextMusic
    def nextMusic(*args):
        try:
            global currentMusic

            currentMusic += 1

            playB.config(image=playimg, command=play)
            playB2.config(image=playimg2, command=play)
            
            #nextB.config(command= lambda: nextMusic(musicNum+1))
            #prevB.config(command= lambda: prevMusic(musicNum-1))

            pygame.mixer.music.load(biglist[currentMusic])
            
            audio = muta(biglist[currentMusic])
            secs = int(audio.info.length)
            secns = int(audio.info.length)
            hrs = secs // 3600
            secs %= 3600

            mins = secs // 60
            secs %= 60

            total_length = f"{hrs}:{mins}:{secs}"
            print(total_length)

            length_Label.config(text=total_length)
            
            #pygame.mixer.music.play()

            wait = secns * 1000 + 500
            #print("time to wait: ", wait)
            #print("in secs: ", secns)
            #print(int(str(secs)+str("000")))


            #root.after(wait, nextMusic)



            basename = os.path.basename(biglist[currentMusic])

            
            musicName.config(text=str(basename)[:-4])

            
            root.bind("<Control-Right>", nextMusic)
            root.bind("<Control-Left>", prevMusic)
            root.bind("<Control-KeyPress-n>", nextMusic)
            root.bind("<Control--KeyPress-p>", prevMusic)
            root.bind("<Alt-Control--KeyPress-o>", ask)
            root.bind("<Alt-Control--KeyPress-m>", miniPlayer)



            def showpath(*args):
                openlabel.place_forget()
                
                nextlabel.place_forget()
                prevlabel.place_forget()
                
                pathlabel.config(text=biglist[currentMusic])
                pathlabel.place(y=570, anchor=CENTER, x =233)
                pathlabel.after(4000, pathlabel.place_forget)

            def popshowpathlabelf(*args):
                popshowpathlabel.place(x=60, y=45)
                popshowpathlabel.after(4000, popshowpathlabel.place_forget)

            #pathButton.place(y=30, x=100)
            pathButton.config(command=showpath)
            pathButton.bind("<Enter>", popshowpathlabelf)

            def queue(*args):
                pos = pygame.mixer.music.get_pos()
                #print(pos)
                if (pos == -1) and (currentMusic < len(biglist)):
                    print("Not play\nCalling next")
                    nextMusic()
                root.after(1, queue)
                                
            
            #root.after(1, queue)
            pygame.mixer.music.play()
            queue()

        except IndexError:
            print("last item on the list")

    
    #global ask
    
    def ask(*args):

        #initialdir="%Home%",
        filep = filedialog.askopenfilenames(initialdir="%Music%", title="Select audio files to open", filetypes=[("mp3 files", "*.mp3")]) #,("m4a files", "*.m4a")

        #mlist = os.listdir(filep)
        
        mlist = list(filep)
        #print(mlist)
        for i in mlist:
            biglist.append(i)

        #global lastTrack
        #lastTrack = biglist[0][-1]

        #print("big list: ", biglist[0])
        for i in range(len(biglist)):
            name = os.path.basename(biglist[i])
            #i += 1
            print(name)
        pygame.mixer.music.load(biglist[0])

        audio = muta(biglist[0])
        secs = int(audio.info.length)
        secns = int(audio.info.length)
        
        hrs = secs // 3600
        secs %= 3600

        mins = secs // 60
        secs %= 60

        total_length = f"{hrs}:{mins}:{secs}"
        print(total_length)

        length_Label.config(text=total_length)
        

        
        wait = secns * 1000 + 500
        #print("time to wait: ", wait)
        #print("in secs: ", secns)
        #print(int(str(secs)+str("000")))


        #root.after(wait, nextMusic)

        print("biglist: \n", biglist)




        #pygame.mixer.music.queue(nextMusic(x))
        #pygame.mixer.music.play()
        #pygame.mixer.music.set_volume(1.0)

        basename = os.path.basename(biglist[0])

        #filesize = os.path.getsize(biglist[0][0])
        #print(filesize)

        #print("the size of the file is: ")

        musicName.config(text=str(basename)[:-4])

        playB.config(image=playimg, command=play)
        playB2.config(image=playimg2, command=play)

        root.bind("<Control-Right>", nextMusic)
        root.bind("<Control-Left>", prevMusic)
        root.bind("<Control-KeyPress-n>", nextMusic)
        root.bind("<Control--KeyPress-p>", prevMusic)
        root.bind("<Alt-Control--KeyPress-o>", ask)
        root.bind("<Alt-Control--KeyPress-m>", miniPlayer)

        global showpath
        def showpath(*args):

            openlabel.place_forget()
            
            topmlabel.place_forget()
            

            pathlabel.config(text=biglist[0])
            pathlabel.after(4000, pathlabel.place_forget)

            pathlabel.place(y=570, anchor=CENTER, x=233)
        
        def popshowpathlabelf(*args):
            popshowpathlabel.place(x=60, y=45)
            popshowpathlabel.after(4000, popshowpathlabel.place_forget)

        #pathButton.place(x=100, y=5)
        pathButton.config(command=showpath)
        pathButton.bind("<Enter>", popshowpathlabelf)

        def queue(*args):
                pos = pygame.mixer.music.get_pos()
                #print(pos)
                if (pos == -1) and (currentMusic < len(biglist)):#or we can currentMusic != len(biglist-1)
                    print("Not play\nCalling next")
                    nextMusic()
                root.after(1, queue)
                                
            
        #root.after(1, queue)
        pygame.mixer.music.play()
        queue()
  

    global play 

    def play(*args):
        
        pygame.mixer.music.pause()

        def conf(*args):
            pygame.mixer.music.unpause()
            playB.config(image=playimg, command=play)
            playB2.config(image=playimg2, command=play)
            root.bind("<space>", play)


        playB.config(image=pauseimg, command=conf)
        playB2.config(image=pauseimg2, command=conf)
        root.bind("<space>", conf)

    

    root.bind("<space>", play)

    root.bind("<Control-Right>", nextMusic)
    root.bind("<Control-Left>", prevMusic)
    root.bind("<Control-KeyPress-n>", nextMusic)
    root.bind("<Control--KeyPress-p>", prevMusic)
    root.bind("<Alt-Control--KeyPress-o>", ask)
    root.bind("<Alt-Control--KeyPress-m>", miniPlayer)
    
    
    wallLabel = Label(image=wallimg, bg="blue")

    redB = PhotoImage(file="Images/close.png")
    greenB = PhotoImage(file="Images/minimz.png")

    closeB = Button(image=redB, borderwidth=0, bg="#156f84", activebackground="#156f84", command=root.destroy)
    minimB = Button(image=greenB, borderwidth=0, bg="#156f84", activebackground="#156f84", command=miniPlayer)

    global playB
    playB = Button(image=playimg, borderwidth=0, bg="#156f84", activebackground="#156f84", command=play)
    playB2 = Button(image=playimg2, 
        borderwidth=0, 
        bg="#156f84", 
        highlightcolor="red",
        activebackground="#156f84", 
        command=play)
    
    #tryna make the same button play and pause



    nextB = Button(image=nextimg, borderwidth=0, bg="#156f84", activebackground="#156f84", command= nextMusic)
    prevB = Button(image=previmg, borderwidth=0, bg="#156f84", activebackground="#156f84", command= prevMusic)
    
    #little buttons
    nextB2 = Button(image=nextimg2, borderwidth=0, bg="#156f84", activebackground="#156f84", command= nextMusic)
    prevB2 = Button(image=previmg2, borderwidth=0, bg="#156f84", activebackground="#156f84", command= prevMusic)
    

    #keyboard.press()
    '''if keyboard.press(hotkey="Space") == "Space":
        pygame.mixer.music.pause()
    '''

    def move_window(event):
        root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    titleimg = PhotoImage(file="Images/titlebar2.png")

    title_bar = Label(root, image=titleimg, borderwidth=0, bg="#156f84")
    
    length_Label = Label(text="", bg="#156f84", fg="white")

    #title_bar = Frame(root, image=titleimg, relief='flat',bg="#44bfd3", bd=1,height=30, width=385)

    #title_text=Label(title_bar, text="D11 Waves", font=("Consolas bold", 13), bg="#44bfd3", fg="white", anchor=CENTER)

    #get thumbnail here
    music_icon = PhotoImage(file="images/mainlogo.png")
    '''mp3_file = stg.read_tag("Amore.mp3")
    album = mp3_file.album
    thumb_data = mp3_file[stg.id3.APIC][0].data
    #thumbnailPic = mp3_file.picture
    dataIO = io.BytesIO(thumb_data)
    thumbIMAGEFile = pilmg.open(dataIO)
    thumbIMAGEFile.save("New album.png")
    lastThumbPic = PhotoImage(file="New album.png")
    print(album)'''

    
    music_Label = Label(image=music_icon, bg="#156f84") #bg="#BA2667"
    #music_Label = Label(image=lastThumbPic, bg="#CB2161") #bg="#BA2667"


    musicName = Label(text=" ", font=("consolas", 10), bg="#156f84", fg="white")

    pathlabel = Label(text=" ", font=("consolas", 10), bg="#156f84", fg="white")
    

    

    pathButton = Button(root,borderwidth=0, image=pathimg, text="path", bg="#44bfd3", activebackground="#156f84", fg="white")
    
    pathlabel.place(y=570, anchor=CENTER, x=233)
    #pathButton.place(x=100, y=30)


    wallLabel.place(x=-2, y=-2)

    title_bar.place(x=45, y=10)
    #title_text.place(x=150, y=2)
    playB.place(x=195, y=410)
    
    nextB.place(x=325, y=430)
    prevB.place(x=95, y=430)
    
    closeB.place(x=440, y=15)
    
    music_Label.place(y=240, anchor=CENTER, x =245)
    
    musicName.place(y=390, anchor=CENTER, x =233) #x=170, y=330

    #root.geometry('480x600')
    


    title_bar.bind('<B1-Motion>', move_window)
    #title_text.bind('<B1-Motion>', move_window)
    wallLabel.bind('<B1-Motion>', move_window)
    music_Label.bind('B1-Motion>', move_window)
    #home.bind('<B1-Motion>', move_window)

    #closeB.place(x=440, y=0)

    global vol
    vol = 0 

    #volUpImg = PhotoImage(file="Images/volUp.png")
    #volDownImg = PhotoImage(file="Images/volDown.png")



    
    def clear(*args):
        volLabel.config(text="")
        #volLabel.place_forget()


    def slideVolume(*args):
        #vol += 1 #0.4
        #pygame.mixer.music.set_volume(1.0)

        

        global vol
        get100 = volumeSlider.get()
        vol = int(get100) / 100

        if vol <= 0:
            pygame.mixer.music.pause()
            playB.config(image=pauseimg)
            playB2.config(image=pauseimg2)
        if vol > 0:
            pygame.mixer.music.unpause()
            playB.config(image=playimg)
            playB2.config(image=playimg2)
        

        if get100 < 100:
            #vol += 0.1010 #[:2]
            print("PLus ", vol)
            
            pygame.mixer.music.set_volume(vol)
            resultv = pygame.mixer.music.get_volume()
            #print("volume: ", resultv)
            volLabel.config(text=str(resultv)[:4])

            #volLabel.place(x=437, y=40)

            root.after(1000, clear)
            #volUp.after(5000, volUp.place_forget)
        
        
        if get100 >= 0:
            #vol -= 0.1010
            print("minus ", vol)
            
            pygame.mixer.music.set_volume(vol)
            volres = pygame.mixer.music.get_volume()
            #print("volume: ", volres)
            volLabel.config(text=str(volres)[:4])

            #volLabel.place(x=437, y=40)

            root.after(1000, clear)
            #volDown.after(5000, volDown.place_forget)
        
    


    def soundButtons(*args):
        


        #volUp.place(x=450, y=120)
        #volDown.place(x=450, y=150)


        def killFrame(*args):
            #volUp.place_forget()
            #volDown.place_forget()
            volumeSlider.place_forget()
            soundB.config(command=soundButtons)

        volumeSlider.place(x=437, y=110)
        soundB.config(command=killFrame)
        #soundB.bind("<Leave>",killFrame)
        #volUp.bind("<Leave>",killFrame)
        #volDown.bind("<Leave>",killFrame)


    volLabel = Label(root, text="", bg="#156f84", fg="white", font=("consolas", 14))
    #volUp = Button(root, bg="#156f84", image=volUpImg, borderwidth=0, command=Up)
    #volDown = Button(root, bg="#156f84", image=volDownImg, borderwidth=0, command=Down) 

    volumeSlider = Scale(root, 
        from_=100, to=0, 
        orient=VERTICAL, length=100,
        sliderrelief="flat",
        background="#156f84",
        foreground="cyan",
        activebackground="cyan",
        highlightbackground="#156f84",
        troughcolor="green",
        cursor="dot",
        command=slideVolume
        ) #command=slidefunc)
    #volumeSlider.place(x=437, y=110)

    volumeSlider.set(pygame.mixer.music.get_volume()/100)

    volLabel.place(x=437, y=40)

    soundImg = PhotoImage(file="Images/sound.png")

    popUpImg = PhotoImage(file="Images/on.png")
    popDownImg = PhotoImage(file="Images/off.png")
    addImg = PhotoImage(file="Images/add.png")

    global openB

    openB = Button(root, image=addImg,borderwidth=0, bg="#44bfd3", relief="flat", activebackground="#44bfd3", command=ask)     
    soundB = Button(root, image=soundImg, bd=0, relief="flat", bg="#156f84", activebackground="#156f84", command=soundButtons)
    
    def ChangePop():

        def rechangePop():
            topMostButton.config(image=popUpImg, command=ChangePop)
            root.attributes("-topmost", True)


        topMostButton.config(image=popDownImg, command=rechangePop)
        root.attributes("-topmost", False)


    topMostButton = Button(image=popUpImg, borderwidth=0, bg="#44bfd3", activebackground="#44bfd3", command=ChangePop)
    
    global topmlabel
    global openlabel

    topmlabel = Label(text="topmost on-off", font=("consolas", 10), bg="#156f84", fg="white")
    openlabel = Label(text="open file(s)", font=("consolas", 10), bg="#156f84", fg="white")
    playlabel = Label(text=" ", font=("consolas", 10), bg="#156f84", fg="white")
    nextlabel = Label(text=" ", font=("consolas", 10), bg="#156f84", fg="white")
    prevlabel = Label(text=" ", font=("consolas", 10), bg="#156f84", fg="white")
    popshowpathlabel = Label(text="Show path/directory", font=("consolas", 8), bg="#156f84", fg="white")
    

    def showtop(*args):

        openlabel.place_forget()
        popshowpathlabel.place_forget()
        
        topmlabel.place(x=70, y=45)
        topmlabel.after(4000, topmlabel.place_forget)

    def showOpen(*args):

        topmlabel.place_forget()
        popshowpathlabel.place_forget()
        
        openlabel.place(x=45, y=45)
        openlabel.after(4000, openlabel.place_forget)
        
    def showplay(*args):
        nextlabel.place_forget()
        prevlabel.place_forget()

        playlabel.config(text="Play/Pause")
        playlabel.place(x=200, y=475)
        playlabel.after(2500, playlabel.place_forget)

    def shownext(*args):
        
        playlabel.place_forget()
        prevlabel.place_forget()


        nextlabel.config(text="Play next track")
        nextlabel.place(x=300, y=480)
        nextlabel.after(2500, nextlabel.place_forget)

    def showprev(*args):
        playlabel.place_forget()
        nextlabel.place_forget()


        prevlabel.config(text="Play previous track")
        prevlabel.place(x=75, y=480)
        prevlabel.after(2500, prevlabel.place_forget)


    versionLabel = Label(
                text="by nusware, -v: 1.5.0", 
                bg="#156f84",
                font=("consolas", 10),
                fg="white"
                )
    versionLabel.place(y=590, anchor=CENTER, x =233)
    #versionLabel.place(x=10, y=580)

    #topMostButton.bind("<Enter>", showtop)
    #openB.bind("<Enter>", showOpen)
    #playB.bind("<Enter>", showplay)
    #nextB.bind("<Enter>", shownext)
    #prevB.bind("<Enter>", showprev)
    #soundB.bind("<Enter>", soundButtons)
    
    topMostButton.place(x=70, y=28)


    openB.place(x=45, y=28) #(relx=0, rely=0, anchor=NW)
    
    length_Label.place(y=535, anchor=CENTER, x=230)

    soundB.place(x=445, y=70)
    minimB.place(x=20, y=15)
    

    #minimB.place(x=125, y=15)
    mainloop()


#miniPlayer()

masterWin()

