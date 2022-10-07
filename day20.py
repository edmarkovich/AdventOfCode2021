from operator import mod


light_spots = None
dimensions = None
algorithm  = None


def load_initial():
    file1 = open('day20.txt', 'r')
    Lines = file1.readlines()

    global algorithm 
    algorithm = Lines[0]

    global dimensions
    dimensions = ((0,0), (len(Lines)-2, len(Lines[3].strip())))

    global light_spots
    light_spots={} #set()

    for y in range(2, len(Lines)):
        line = Lines[y].strip()
        for x in range(0, len(line)):
            #if line[x]=="#":
            light_spots[(y-2,x)]=line[x]

def next_dimension():
    return ( (dimensions[0][0]-2, dimensions[0][1]-2), (dimensions[1][0]+2, dimensions[1][1]+2) )

def binary3x3(y,x, default):

    top  = dimensions[0][0]
    left = dimensions[0][1]
    bottom = dimensions[1][0]
    right  = dimensions[1][1]

    out = ""
    for row in range(y-1,y+2):
        for col in range(x-1,x+2):
            if (row,col) not in light_spots:
                out += default
            else:
                out += "1" if light_spots[(row,col)] == "#" else "0"
    return int(out,2)

def enhance(default):
    global dimensions 
    next_dim = next_dimension()

    next_frame={}#set()

    #scan through each point
    for y in range(next_dim[0][0], next_dim[1][0]+1):
        for x in range(next_dim[0][1], next_dim[1][1]+1):

            #get 9 digit binnary
            algo_key = binary3x3(y,x, default)

            #translate via algo
            #add to next frame
            #if algorithm[algo_key] == "#":
            next_frame[(y,x)] = algorithm[algo_key]

    #swap old frame for new
    global light_spots
    light_spots = next_frame
    dimensions = next_dim



def print_grid(debug):
    count_light = 0
    for y in range(dimensions[0][0], dimensions[1][0]):
        out = ""
        for x in range(dimensions[0][1], dimensions[1][1]):
            out += light_spots[(y,x)]
            if light_spots[(y,x)]=="#":
                count_light += 1
        if debug:
            print(out)
    print(count_light)

load_initial()
print_grid(False)

for i in range(0, 50):
    if i % 2 == 0:
        enhance("0")
    else:
        enhance("1")

    print_grid(False)

