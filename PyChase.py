import pygame
import pygame.locals

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    if image_width % width != 0 or image_height % height != 0:
        raise "Image Tiles must be an even multiple of the given tile size"

    for tile_x in range(0, int(image_width/width)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height/height)):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

def create_map():
    map = {}
    for row in range(8):
        for col in range(8):
            map[(row, col)] = 0

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
table = load_tile_table("sprites.png", 16, 16)
for x, row in enumerate(table):
    for y, tile in enumerate(row):
        screen.blit(tile, (x*32, y*24))
pygame.display.flip()
while pygame.event.wait().type != pygame.locals.QUIT:
    pass
#The function load_tile_table() will load tiles from a tileset file, and return them sliced up as a list of lists. At first I did that by creating separate surfa