import functions

def draw(font1):
    background(0)
    
    functions.drawText(255, 255, 255, font1[1], "Player 1, Are you Mafia or Federal Agencies?", 960, 440 + font1[0] // 2)
    
    fill(0, 0, 255)
    rect(1160, 640, 100, 100)
    
    fill(255, 0, 0)
    rect(660, 640, 100, 100)
    
    functions.drawText(255, 255, 255, font1[1], "Mafia", 710, 685 + font1[0] // 2)
    functions.drawText(255, 255, 255, font1[1], "FA", 1210, 685 + font1[0] // 2)
    
def keyTyped():
    return key == " "
