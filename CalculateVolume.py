import math

#
def calculateVolume(shape, sideX, sideY, topX, topY):
    #Return the volume of a given object based on its shape


    volume = None
    baseArea = topX * topY
    height = sideY
    width = sideX

    if shape is "cube":
        volume = baseArea*height
    elif shape is "pyramid":
        volume = (1/3)*baseArea*height
    elif shape is "sphere":
        radius = sideX/2
        volume = (3/4)*(math.pi)*(radius^3)

    return volume