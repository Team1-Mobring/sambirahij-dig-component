import menu2

def setup():
    global font1, gameStage
    
    font1 = [24, createFont("Ariel", 24)]
    gameStage = 0
    
    size(1920, 1080)
    
def draw():
    global font1, gameStage
    
        
    if gameStage == 0:
        menu2.draw(font1)
        
def keyTyped():
    global gameStage
    
