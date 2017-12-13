p_ball = PVector(500, 300)
CPT_ball1 = PVector(800, 350)
CPT_ball2 = PVector(200, 100)
CPT_ball3 = PVector(120, 500)
CPT_ball4 = PVector(700, 50)

def setup():
    size(1000, 600)
    
def draw():
    
    global p_ball
    global CPT_ball1
    
    #player ball
    ellipse(p_ball.x, p_ball.y, 30, 30)

    #CPT ball 1
    ellipse(CPT_ball1.x, CPT_ball1.y, 40, 40)
    
    #CPT ball 2
    ellipse(CPT_ball2.x, CPT_ball2.y, 40, 40)
    
    #CPT ball 3
    ellipse(CPT_ball3.x, CPT_ball3.y, 40, 40)
    
    #CPT ball 4
    ellipse(CPT_ball4.x, CPT_ball4.y, 40, 40)
