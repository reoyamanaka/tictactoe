import wx
import pandas as pd
import sys

#wx app setup
app = wx.App()
window = wx.Frame(None, title = "Tic Tac Toe", size = (360, 260))
popup = wx.Frame(None, title = "Game Over", size = (220, 100))
panel = wx.Panel(popup)

#function and button to close window
def closeWindow(event):
    window.Destroy()
    sys.exit()

closeButton = wx.Button(window, label = "Exit", pos = (220, 165), size = (100, 25))
closeButton.Bind(wx.EVT_BUTTON, closeWindow)

#Function and button to close the popup
def closePopup(event):
    popup.Destroy()

popupButton = wx.Button(panel, label = "Okay", pos = (65, 45))
popupButton.Bind(wx.EVT_BUTTON, closePopup)

#Setting up gameboard

wx.StaticText(window, label = "Note: Click 'Submit Move' after every move!", pos = (50, 30))

verticalLine = wx.Bitmap("vertical.png", wx.BITMAP_TYPE_ANY)
horizontalLine = wx.Bitmap("horizontal.png", wx.BITMAP_TYPE_ANY)

v1 = wx.StaticBitmap(window, -1, verticalLine, pos = (95, 80))
v2 = wx.StaticBitmap(window, -1, verticalLine, pos = (145, 80))

h1 = wx.StaticBitmap(window, -1, horizontalLine, pos = (50, 110))
h2 = wx.StaticBitmap(window, -1, horizontalLine, pos = (50, 150))

tlinput = wx.Choice(window, pos = (50, 80), size = (40, 20), choices = ['', 'X', 'O'])
tminput = wx.Choice(window, pos = (100, 80), size = (40, 20), choices = ['', 'X', 'O'])
trinput = wx.Choice(window, pos = (150, 80), size = (40, 20), choices = ['', 'X', 'O'])

mlinput = wx.Choice(window, pos = (50, 125), size = (40, 20), choices = ['', 'X', 'O'])
mminput = wx.Choice(window, pos = (100, 125), size = (40, 20), choices = ['', 'X', 'O'])
mrinput = wx.Choice(window, pos = (150, 125), size = (40, 20), choices = ['', 'X', 'O'])

blinput = wx.Choice(window, pos = (50, 170), size = (40, 20), choices = ['', 'X', 'O'])
bminput = wx.Choice(window, pos = (100, 170), size = (40, 20), choices = ['', 'X', 'O'])
brinput = wx.Choice(window, pos = (150, 170), size = (40, 20), choices = ['', 'X', 'O'])

eng_tl = wx.StaticText(window, label = "", pos = (70, 80))
eng_tm = wx.StaticText(window, label = "", pos = (115, 80))
eng_tr = wx.StaticText(window, label = "", pos = (160, 80))

eng_ml = wx.StaticText(window, label = "", pos = (70, 125))
eng_mm = wx.StaticText(window, label = "", pos = (115, 125))
eng_mr = wx.StaticText(window, label = "", pos = (160, 125))

eng_bl = wx.StaticText(window, label = "", pos = (70, 170))
eng_bm = wx.StaticText(window, label = "", pos = (115, 170))
eng_br = wx.StaticText(window, label = "", pos = (160, 170))

#submit function
def take_inputs(event):
    
    tr=trinput.GetStringSelection()
    tm=tminput.GetStringSelection()
    tl=tlinput.GetStringSelection()

    mr=mrinput.GetStringSelection()
    mm=mminput.GetStringSelection()
    ml=mlinput.GetStringSelection()

    br=brinput.GetStringSelection()
    bm=bminput.GetStringSelection()
    bl=blinput.GetStringSelection()

    
    if tlinput.GetSelection() != 0:
        tlinput.Hide()
        eng_tl.SetLabel(tl)

    if tminput.GetSelection() != 0:
        tminput.Hide()
        eng_tm.SetLabel(tm)
        
    if trinput.GetSelection() != 0:
        trinput.Hide()
        eng_tr.SetLabel(tr)

    if mlinput.GetSelection() != 0:
        mlinput.Hide()
        eng_ml.SetLabel(ml)
    
    if mminput.GetSelection() != 0:
        mminput.Hide()
        eng_mm.SetLabel(mm)

    if mrinput.GetSelection() != 0:
        mrinput.Hide()
        eng_mr.SetLabel(mr)

    if blinput.GetSelection() != 0:
        blinput.Hide()
        eng_bl.SetLabel(bl)

    if bminput.GetSelection() != 0:
        bminput.Hide()
        eng_bm.SetLabel(bm)

    if brinput.GetSelection() != 0:
        brinput.Hide()
        eng_br.SetLabel(br)
        
    def engrave_all_inputs():
        
        if tlinput.GetSelection() == 0:
            tlinput.Hide()
            eng_tl=wx.StaticText(window, label = tl, pos = (70, 80))

        if tminput.GetSelection() == 0:
            tminput.Hide()
            eng_tm=wx.StaticText(window, label = tm, pos = (115, 80))
            
        if trinput.GetSelection() == 0:
            trinput.Hide()
            eng_tr = wx.StaticText(window, label = tr, pos = (160, 80))
            
        if mlinput.GetSelection() == 0:
            mlinput.Hide()
            eng_ml = wx.StaticText(window, label = ml, pos = (70, 125))

        if mminput.GetSelection() == 0:
            mminput.Hide()
            eng_mm = wx.StaticText(window, label = mm, pos = (115, 125))

        if mrinput.GetSelection() == 0:
            mrinput.Hide()
            eng_mr = wx.StaticText(window, label = mr, pos = (160, 125))

        if blinput.GetSelection() == 0:
            blinput.Hide()
            eng_bl = wx.StaticText(window, label = bl, pos = (70, 170))
            
        if bminput.GetSelection() == 0:
            bminput.Hide()
            eng_bm = wx.StaticText(window, label = bm, pos = (115, 170))
            
        if brinput.GetSelection() == 0:
            brinput.Hide()
            eng_br = wx.StaticText(window, label = br, pos = (160, 170))
                
    if tl == tm == tr == "X" or ml == mm == mr == "X" or bl == bm == br == "X" or tl == ml == bl == "X" or tm == mm == bm == "X" or tr == mr == br == "X" or tl == mm == br == "X" or tr == mm == bl == "X":
        engrave_all_inputs()
        print("Game over, Player X wins.")

        popup.Show(True)

        wx.StaticText(popup, label = "Game Over, Player X wins!", pos = (30, 10)) 
        
    if tl == tm == tr == "O" or ml == mm == mr == "O" or bl == bm == br == "O" or tl == ml == bl == "O" or tm == mm == bm == "O" or tr == mr == br == "O" or tl == mm == br == "O" or tr == mm == bl == "O":
        engrave_all_inputs()
        print("Game over, Player O wins.")

        popup.Show(True)

        wx.StaticText(popup, label = "Game Over, Player O wins!", pos = (30, 10)) 

    else:
        gameboard = pd.DataFrame(
            [[tl, tm, tr],
             [ml, mm, mr],
             [bl, bm, br]],
            index = ["", "", ""],
            columns = ["", "", ""])

        print(gameboard)

submitButton=wx.Button(window, label = "Submit Move", pos = (220, 120), size = (100, 25))
submitButton.Bind(wx.EVT_BUTTON, take_inputs)

window.Show(True)
app.MainLoop()

