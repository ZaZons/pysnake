get()
for event in events:
    if event.type == pygame.QUIT:
        running = False

menu.update(events)
menu.draw(screen)
pygame.display.update(