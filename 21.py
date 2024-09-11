import random

def calculate_probability(hand, dealer_card):
    remaining_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # колода
    possible_outcomes = {"win": 0, "lose": 0, "push": 0}

    for _ in range(10000):  # 10 000 симуляций
        deck = remaining_deck.copy()
        random.shuffle(deck)

        # Симулируем действия игрока
        player_hand = hand[:]
        while sum(player_hand) < 17:
            player_hand.append(deck.pop())

        # Определяем исход
        player_score = sum(player_hand)
        dealer_hand = [dealer_card, deck.pop()]

        while sum(dealer_hand) < 17:
            dealer_hand.append(deck.pop())

        dealer_score = sum(dealer_hand)

        if player_score > 21:
            possible_outcomes["lose"] += 1
        elif dealer_score > 21 or player_score > dealer_score:
            possible_outcomes["win"] += 1
        elif player_score == dealer_score:
            possible_outcomes["push"] += 1
        else:
            possible_outcomes["lose"] += 1

    total = sum(possible_outcomes.values())
    for outcome, count in possible_outcomes.items():
        print(f"Вероятность {outcome}: {count / total:.2%}")

# Пример использования
calculate_probability([10, 6], 6)  # У вас 16, у дилера 6
