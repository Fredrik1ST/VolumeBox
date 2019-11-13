import math

#
def calculateVolume(shape, sideX, sideY, topX, topY):
    """ Calculate the volume of an object of a specified geometric shape
    :param shape: String describing the shape of the object, e.g. "cube" "pyramid" "sphere"
    :param sideX: object width (x-plane) as seen from the side
    :param sideY: object height (y-plane) as seen from the side
    :param topX:  object side length (x-plane) as seen from the top
    :param topY: object side length (y-plane) as seen from the top
    :return: The volume of the object described by the parameters
    """


    volume = None
    baseArea = topX * topY
    height = sideY
    width = sideX

    if shape is "cube":
        volume = baseArea*height
    elif shape is "pyramid":
        volume = (1/3)*baseArea*height
    elif shape is "sphere":
        radius = topY/2
        volume = (3/4)*(math.pi)*(radius^3)

    return volume