class kangaroo:
    def __init__(self, pos, vel):
        self.pos=pos
        self.vel=vel

    def move(self):
        self.pos=self.pos+self.vel


kang1 = kangaroo(int (input()), int (input()))
kang2 = kangaroo(int (input()), int (input()))

def reflect(k1, k2):
    if k1.pos < k2.pos:
        aux = k1.pos
        k1.pos = k2.pos
        k2.pos = aux
        aux = k1.vel
        k1.vel = k2.vel
        k2.vel = aux


while kang1.vel>kang2.vel:
        if kang1.pos == kang2.pos:
            print("YES")
            break
        if kang1.pos > kang2.pos:
            print("NO")
            break
        kang1.move()
        kang2.move()