import random

# BLACK JACK GAME

full_deck_cards = {
    "hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "spades": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
}
player_cards = []
computer_cards = []
game_actions = {
    "is_won": False,
    "is_break": False,
    "keep_play": True,
    "who_wins": "",
    "is_split": False,
    "is_game_started": True
}

my_str = "                                      .------.\n                   .------.           |A .   |\n                   |A_  _ |    .------; / \  |\n                   |( \/ )|-----. _   |(_,_) |\n                   | \  / | /\  |( )  |  I  A|\n                   |  \/ A|/  \ |_x_) |------'\n                   `-----+'\  / | Y  A|\n                         |  \/ A|-----'\n                         `------'"



def give_start_cards():
    curr_rand_sign = random.choice(list(full_deck_cards.keys()))
    curr_rand_card = random.choice(full_deck_cards[curr_rand_sign])
    if len(computer_cards) > len(player_cards) and len(player_cards) < 2:
        player_cards.append(curr_rand_card)
    elif len(computer_cards) < 2:
        computer_cards.append(curr_rand_card)
    full_deck_cards[curr_rand_sign].remove(curr_rand_card)


def draw_card(pl_or_pc):
    curr_rand_sign = random.choice(list(full_deck_cards.keys()))
    curr_rand_card = random.choice(full_deck_cards[curr_rand_sign])
    if pl_or_pc == 1:
        player_cards.append(curr_rand_card)
    elif pl_or_pc == 0:
        computer_cards.append(curr_rand_card)
    full_deck_cards[curr_rand_sign].remove(curr_rand_card)
    return curr_rand_card


def cards_value(pl_or_pc):
    temp_val = 0
    if pl_or_pc:
        for card in player_cards:
            if card == 14:
                temp_val += 11
            elif 14 > card > 10:
                temp_val += 10
            else:
                temp_val += card
    else:
        for card in computer_cards:
            if card == 14:
                temp_val += 11
            elif 14 > card > 10:
                temp_val += 10
            else:
                temp_val += card
    return temp_val


def check_for_ace(my_list, pl_or_pc):
    count = 0
    index = []
    for card in my_list:
        if card == 14:
            index.append(my_list.index(card))
    if pl_or_pc:
        if 1 <= len(index) <= count and cards_value(True) > 21:
            print("changed ace value from 11 -> 1: ", my_list)
            count += 1
            for i in range(len(index)):
                player_cards[i] = 1
                check_for_ace(my_list, pl_or_pc)
                break
    else:
        if 1 <= len(index) <= count and cards_value(False) > 21:
            print("changed ace value from 11 -> 1: ", my_list)
            count += 1
            for i in range(len(index)):
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


def split_cards(pl_cards):
    continue_play = True
    first_split = [pl_cards[0], draw_card(2)]
    while continue_play:
        if cards_value(first_split) > 21:
            continue_play = False
        elif input("") == "y":
            first_split.append(draw_card(2))
        else:
            continue_play = False
    continue_play = True
    second_split = [pl_cards[1], draw_card(2)]
    while continue_play:
        if cards_value(second_split) > 21:
            continue_play = False
        elif input("") == "y":
            second_split.append(draw_card(2))
        else:
            continue_play = False


def check_split_option(card_list):
    if 10 < card_list[0] < 14 and 10 < card_list[1] < 14:
        return True
    return False


def start_game():
    if game_actions["is_game_started"]:
        print(my_str)
        game_actions["is_game_started"] = False
    if len(computer_cards) == 2 and len(player_cards) == 2 and check_split_option(player_cards) and 1 == 0:
        if input("wanna split hand? y/n  ") == "y":
            game_actions["is_split"] = True
            # split_cards(player_cards)

    if game_actions["keep_play"]:
        if not game_actions["is_won"]:
            if len(computer_cards) < 2 or len(player_cards) < 2:
                give_start_cards()
                game_actions["is_break"] = False
                start_game()
                return
            if not game_actions["is_break"] and cards_value(True) < 22:
                print(show_image(player_cards), [show_image(computer_cards)[0], "X"],
                      f"pl_val: {cards_value(True)} {player_cards}", f"pc_val: {cards_value(False)} {computer_cards}")
            if cards_value(True) > 21:
                check_for_ace(player_cards, True)
                if cards_value(True) > 21:
                    print(show_image(player_cards), show_image(computer_cards),
                          f"pl_val: {cards_value(True)} {player_cards}",
                          f"pc_val: {cards_value(False)} {computer_cards}")
                    game_actions["who_wins"] = "Computer Wins!"
                    game_actions["is_won"] = True
                    if game_actions["is_won"]:
                        start_game()
                        return
            print(game_actions["is_break"])
            if len(player_cards) >= 2 and not game_actions["is_break"] and input(
                    "Draw Card? y/n  ").lower() == "y":
                draw_card(1)
                start_game()
                return
            elif len(player_cards) >= 2 and not game_actions["is_break"]:
                game_actions["is_break"] = True
            if game_actions["is_break"]:
                if cards_value(True) < cards_value(False) < 22:
                    print(show_image(player_cards), show_image(computer_cards),
                          f"pl_val: {cards_value(True)} {player_cards}",
                          f"pc_val: {cards_value(False)} {computer_cards}")
                    check_for_ace(player_cards, True)
                    if cards_value(True) < cards_value(False) < 22:
                        game_actions["who_wins"] = "Computer Wins!"
                        game_actions["is_won"] = True
                        if game_actions["is_won"]:
                            start_game()
                            return
                if cards_value(True) == cards_value(False):
                    check_for_ace(player_cards, True)
                    check_for_ace(computer_cards, False)
                    if cards_value(True) == cards_value(False):
                        print(show_image(player_cards), show_image(computer_cards),
                              f"pl_val: {cards_value(True)} {player_cards}",
                              f"pc_val: {cards_value(False)} {computer_cards}")
                        game_actions["who_wins"] = "It's a Draw!"
                        game_actions["is_won"] = True
                        if game_actions["is_won"]:
                            start_game()
                            return
                elif 16 < cards_value(False) < cards_value(True):
                    check_for_ace(computer_cards, False)
                    if 16 < cards_value(False) < cards_value(True):
                        print(show_image(player_cards), show_image(computer_cards),
                              f"pl_val: {cards_value(True)} {player_cards}",
                              f"pc_val: {cards_value(False)} {computer_cards}")
                        game_actions["who_wins"] = "Player Wins!"
                        game_actions["is_won"] = True
                        if game_actions["is_won"]:
                            start_game()
                            return
                elif 16 > cards_value(False) and cards_value(False) < cards_value(True):
                    draw_card(0)
                    start_game()
                    return
                elif cards_value(False) > 21:
                    check_for_ace(computer_cards, False)
                    if cards_value(False) > 21:
                        check_for_ace(computer_cards, False)
                        if cards_value(False) > 21:
                            print(show_image(player_cards), show_image(computer_cards),
                                  f"pl_val: {cards_value(True)} {player_cards}",
                                  f"pc_val: {cards_value(False)} {computer_cards}")
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
                game_actions["is_game_started"] = True
                start_game()
                return
            else:
                game_actions["keep_play"] = False
                start_game()
                return
    return


start_game()

print("GAME OVER!!!")
