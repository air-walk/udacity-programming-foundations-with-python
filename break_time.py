import time
import webbrowser

i = 0
print("This program started on: " + time.ctime())
while(i < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=PMivT7MJ41M")
    i = i + 1
