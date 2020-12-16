
import os
print(os.listdir("demo_projects/keras/models/"))
print(os.path.abspath(__file__))
entire = os.path.abspath(__file__)
direc,filename = os.path.split(entire)
print(direc)