D={'U':(1,0),'D':(-1,0),'R':(0,1),'L':(0,-1)}
def solution(dirs):
    x=y=0;v=set()
    for d in dirs:
        dx,dy=D[d]
        if -5<=(nx:=x+dx)<=5 and -5<=(ny:=y+dy)<=5:
            if dx:v.update({((x,nx),y),((nx,x),y)})
            else:v.update({(x,(y,ny)),(x,(ny,y))})
            x=nx;y=ny
    return len(v)//2