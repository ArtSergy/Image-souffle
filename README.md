# <img src="https://i.imgur.com/js2tatp.png" alt="drawing" width="75"/> Image-Soufflé



Very useful python script to randomize pixels position in any image. For now only .jpg supported. To use the program place the file named input.jpg in the main directory. All pictures and the final gif will be created in the output directory

![Sample gif](https://i.imgur.com/sEhaYFS.gif)

you can override the following values to alter the gif's properties:
```python
12 | # Configuration:
13 | FPS = 30                #Frames per second
14 | duration = 2            #Duration in seconds
```
---
## What's new

###JIT

For images with more than 62500 pixels (e.g 250x250 image), JIT compilation is performed. Due to the time needed for compilation, when operating on smaller images, the program executes faster without JIT, that's why it's off then. You can see the mode in use when you start the program.

![Performance plot](https://i.imgur.com/Dfmzo0P.png)
