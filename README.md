# 🐢 Python Turtle Random Walk

A colorful random-walk visualization built using **Python Turtle**.

The turtle moves in random directions using only **0°, 90°, 180°, and 270°**, creating a squared/maze-like pattern. Each movement is assigned a randomly selected color.

## 🎨 Output

![Python Turtle Random Walk]()

## 🛠️ Concepts Used

* Python `turtle` module
* Random color selection
* Random direction selection
* `for` loops
* Lists
* Functions such as `choice()`
* Turtle pen size and movement

## 💻 Code

```python
from turtle import *
from random import choice

tim = Turtle()
tim.pensize(15)

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "Wheat",
    "SlateGray",
    "SeaGreen"
]

directions = [0, 90, 180, 270]

for i in range(100):
    tim.color(choice(colours))
    tim.forward(30)
    tim.setheading(choice(directions))

screen = Screen()
screen.exitonclick()
```

## 🚀 How It Works

1. A turtle is created with a pen size of `15`.
2. A random color is selected from the `colours` list.
3. The turtle moves forward by `30` pixels.
4. A random direction is selected from:

   * `0°`
   * `90°`
   * `180°`
   * `270°`
5. The process repeats **100 times**.

