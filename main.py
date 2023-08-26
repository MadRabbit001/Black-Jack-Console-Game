import random

# BLACK JACK GAME

full_deck_cards = {
    "hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
}
player_cards = []
computer_cards = []
game_actions = {
    "is_won": False,
    "is_break": False,
    "keep_play": True,
    "who_wins": ""
}

my_str = "                                      .------.\n                   .------.           |A .   |\n                   |A_  _ |    .------; / \  |\n                   |( \/ )|-----. _   |(_,_) |\n                   | \  / | /\  |( )  |  I  A|\n                   |  \/ A|/  \ |_x_) |------'\n                   `-----+'\  / | Y  A|\n                         |  \/ A|-----'\n                         `------'"
print(my_str)


def give_start_cards():
    curr_rand_sign = random.choice(list(full_deck_cards.keys()))
    curr_rand_card = random.choice(full_deck_cards[curr_rand_sign])
    if len(computer_cards) > len(player_cards) and len(player_cards) < 2:
        player_cards.append(curr_rand_card)
    elif len(computer_cards) < 2:
        computer_cards.append(curr_rand_card)


def draw_card(pl_or_pc):
    curr_rand_sign = random.choice(list(full_deck_cards.keys()))
    curr_rand_card = random.choice(full_deck_cards[curr_rand_sign])
    if pl_or_pc:
        player_cards.append(curr_rand_card)
    else:
        computer_cards.append(curr_rand_card)


def cards_value(pl_or_pc):
    temp_val = 0
    if pl_or_pc:
        for card in player_cards:
            if card > 10:
                card = 10
            temp_val += card
    else:
        for card in computer_cards:
            if card > 10:
                card = 10
            temp_val += card
    return temp_val


def check_for_ace(my_list, pl_or_pc):
    count = 0
    index = []
    for card in my_list:
        if card == 14:
            index.append(my_list.index(card))
    if 1 <= len(index) == count and cards_value(True) > 21:
        count += 1
        for i in range(len(index)):
            if pl_or_pc:
                player_cards[i] = 1
            else:
                computer_cards[i] = 1
            check_for_ace(my_list, pl_or_pc)
            break
    return


def show_image(card_list):
    temp_list = []
    for card in card_list:
        if card == 11:
            temp_list.append("J")
        elif card == 12:
            temp_list.append("Q")
        elif card == 13:
            temp_list.append("K")
        elif card == 1 or card == 14:
            temp_list.append("A")
        else:
            temp_list.append(str(card))
    return temp_list


def start_game():
    if game_actions["keep_play"]:
        if not game_actions["is_won"]:
            if len(computer_cards) < 2 or len(player_cards) < 2:
                give_start_cards()
                game_actions["is_break"] = False
                start_game()
                return
            if not game_actions["is_break"] and cards_value(True) < 22:
                print(show_image(player_cards), [show_image(computer_cards)[0], "X"])
            if cards_value(True) > 21:
                check_for_ace(player_cards, True)
                if cards_value(True) > 21:
                    print(show_image(player_cards), show_image(computer_cards))
                    game_actions["who_wins"] = "Computer Wins!"
                    game_actions["is_won"] = True
                    if game_actions["is_won"]:
                        start_game()
                        return
            if len(player_cards) >= 2 and not game_actions["is_break"] and input(
                    "Draw Card? y/n  ").lower() == "y":
                draw_card(True)
                start_game()
                return
            elif len(player_cards) >= 2 and not game_actions["is_break"]:
                game_actions["is_break"] = True
            if game_actions["is_break"]:
                if cards_value(True) < cards_value(False) < 22:
                    print(show_image(player_cards), show_image(computer_cards))
                    game_actions["who_wins"] = "Computer Wins!"
                    game_actions["is_won"] = True
                    if game_actions["is_won"]:
                        start_game()
                        return
                if cards_value(True) == cards_value(False):
                    print(show_image(player_cards), show_image(computer_cards))
                    game_actions["who_wins"] = "It's a Draw!"
                    game_actions["is_won"] = True
                    if game_actions["is_won"]:
                        start_game()
                        return
                elif 16 < cards_value(False) < cards_value(True):
                    print(show_image(player_cards), show_image(computer_cards))
                    game_actions["who_wins"] = "Player Wins!"
                    game_actions["is_won"] = True
                    if game_actions["is_won"]:
                        start_game()
                        return
                elif 16 > cards_value(False) and cards_value(False) < cards_value(True):
                    draw_card(False)
                    start_game()
                    return
                elif cards_value(False) > 21:
                    check_for_ace(computer_cards, False)
                    if cards_value(False) > 21:
                        print(show_image(player_cards), show_image(computer_cards))
                        game_actions["who_wins"] = "Player Wins!"
                        game_actions["is_won"] = True
                        if game_actions["is_won"]:
                            start_game()
                            return
        else:
            print(game_actions["who_wins"])
            if input("Wanna Play Again? y/n  ").lower() == 'y':
                player_cards.clear()
                computer_cards.clear()
                game_actions["is_break"] = False
                game_actions["is_won"] = False
                game_actions["who_wins"] = ""
                game_actions["keep_play"] = True
                start_game()
                return
            else:
                game_actions["keep_play"] = False
                start_game()
                return
    return


start_game()

print("GAME OVER!!!")
