import pygame
from block import Block, Vector, Colors, digits
from random import randint

def check_click(mouse_pos, grid):
    for line in grid:
        for i in line:
            cond_min = mouse_pos[0] > i.x and mouse_pos[1] > i.y
            cond_max = mouse_pos[0] < i.x + i.size and mouse_pos[1] < i.y + i.size
            if cond_min and cond_max:
                if i.visible is False:
                    i.color = Colors.active
                    i.draw(W)
                    print('Drawed №', i.__id__)
                    i.visible = True
                    return
                else:
                    i.color = Colors.empty
                    i.draw(W)
                    print('Deleted №', i.__id__)
                    i.visible = False
                    return
def gen_grid(width, height):
    grid = []
    line = []
    coords = Vector(0,0)
    size = 1
    count = 0
    for h in range(height):
        coords.x = 0
        for w in range(width):
            block = Block(count, coords.x, coords.y)
            line.append(block)
            coords.x += size
            count += 1
        coords.y += size
        grid.append(line)
    return grid
def check_win(grid, win_num=0):
    for line in grid:
        for i in line:
            if bool(digits[win_num][i.__id__]) != i.visible:
                return False
    print('YOU WIN!')
    return True


num = int(input('Enter digit for drawing (0-3): '))


pygame.init()
W = pygame.display.set_mode((300, 500))
pygame.display.set_caption("Plates")

grid = gen_grid(3, 5)
play = True

while play:
    pygame.time.delay(300)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = e.pos
            # print(mouse_pos[0])
            check_click(mouse_pos, grid)
            check_win(grid, num)



    # for line in grid:
    #     for i in line:
    #         pass
            # i.draw(W)
    pygame.display.update()


pygame.quit()
