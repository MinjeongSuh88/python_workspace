ang=int(input("각을 입력하시오"))


import turtle as t
t.shape('turtle') 
t.color('pink') 

print(360/ang)
for i in range(ang):
    t.forward(100)
    t.right(360/ang)
t.mainloop()