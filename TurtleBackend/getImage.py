from turtle import *
from tkinter import *
import os
import sys

def TextToCommand(text: str):
    turtle = Turtle()
    if text == "":
        return ""
    
    splited = text.split(" ")
    command = splited[0]
    args = splited[1]

    if command == "go":
        forward(int(args))
    elif command == "gr":
        right(int(args))
    elif command == "gi":
        left(int(args))
    elif command == "dir":
        radians(int(args))
    
    # Save the image
    ts = turtle.getscreen()
    #ts.getcanvas().create_image(0, 0, image=ts._image, anchor="nw")
    svg = getscreen().getcanvas().postscript(file="temp.eps")
    # eps to svg
    os.system("convert temp.eps temp2.svg")
    # load the image and convert it to Blob
    # with open("temp.svg", "rb") as f:
    #     data = f.read()
    # delete the image
    #os.remove("temp.svg")
    return data

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(TextToCommand(sys.argv[1]))
    else:
        print("No arguments")