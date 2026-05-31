import turtle as t
t.speed(100)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(36):
    t.circle(100)
    t.color(colors[i % len(colors)]) 
    t.right(10)
t.done()