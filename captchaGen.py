from pygame import *
from random import *
size=length,width=(200,70)#dimensions of screen
screen=display.set_mode(size)
init()
fntSize=30
fnt1=font.SysFont("Times New Roman",fntSize)
fnt2=font.SysFont("Papyrus",fntSize)
fnt3=font.SysFont("Calibri",fntSize)
fnt4=font.SysFont("Times New Roman",fntSize)
fnt5=font.SysFont("Papyrus",fntSize)
fonts=[fnt1,fnt2,fnt3,fnt4,fnt5]
fileName=raw_input("What file do you want to save the results to?")
out=open(fileName,'w')
allLets="ABCDEFGHIJKLMNOPQRSTUVQWXYZabcdefghijklmnopqrstuvwxyz0123456789"
output="["
for i in range(30):
    screen.fill((0,0,0))
    lets=""
    for j in range(5):
        fontChosen=fonts[randint(0,4)]
        let=allLets[randint(0,61)]
        h,w=fontChosen.size(let)
        ltp=fontChosen.render(let,1,(255,0,0))
        screen.blit(ltp,(40*j+5,10))
        lets+=let
    out.write(lets+"\n")
    output+='"'+lets+'",'
    display.flip()
    screencopy=screen.copy()
    image.save(screencopy,"results\\captcha"+str(i+1)+".png")
quit()
out.close()
output=output[:-1]
output+="]"
print output
del fnt1,fnt2,fnt3,fnt4,fnt5
