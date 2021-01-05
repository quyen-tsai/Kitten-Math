from game import Game


g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    g.add_loop()
    g.sub_loop()
    g.count_loop()
    g.option_loop()



