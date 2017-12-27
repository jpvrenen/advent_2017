""" Find the distance to 1 """
import math

puzzle_input = 289326
#puzzle_input = 21

def find_outer_layer(data):
    """ Find square number to create matrix """
    while True:
        wortel = math.sqrt(data)
        if not wortel%1:
            if not wortel%2:
                data += 1
            else:
                return wortel
        else:
            data += 1

def define_layers(outer_layer):
    """ Define memory layers and their entries """
    layer_dict = dict()
    for layer in range(3, (outer_layer+1), 2):
        layer_begin = ((layer-2)**2)+1 #begin of each layer is end of last layer
        layer_end = layer**2
        layer_dict[layer] = [layer_begin, layer_end]
    return layer_dict

outer_layer = int(find_outer_layer(puzzle_input))
print(outer_layer)

all_layers = define_layers(outer_layer)
print("Number of layers: {0}".format(len(all_layers)))
print(all_layers)
