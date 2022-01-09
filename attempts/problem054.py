
def parse_file():
    hands = []
    with open('poker.txt', 'rb') as f:
        for line in f:
                line = line.strip()
                a1, a2, a3, a4, a5, b1, b2, b3, b4, b5 = line.split(' ')
                hand1 = sorted(map(Card.from_string, (a1, a2, a3, a4, a5)))
                hand2 = sorted(map(Card.from_string, (b1, b2, b3, b4, b5)))
                hands.append((
                    hand1, 
                    hand2
                    ))

    return hands

class Suit(object):
    def __init__(self, string):
        assert string in ('D', 'S', 'H', 'C')
        self.value = string

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return self.value

class CardValue(object):
    d = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    def __init__(self, string):
        assert string in CardValue.d
        self.value = CardValue.d.index(string)

    def __repr__(self):
        return CardValue.d[self.value]

    def __cmp__(self, other):
        return self - other

    def __sub__(self, other):
        return self.value - other.value

    def __eq__(self, other):
        if isinstance(other, CardValue):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == CardValue.d.index(other)
        assert False


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @classmethod
    def from_string(cls, string):
        assert len(string) == 2
        return Card(CardValue(string[0]), Suit(string[1]))

    def __cmp__(self, other):
        return self - other

    def __sub__(self, other):
        return self.value - other.value

    def __repr__(self):
        return "'" + repr(self.value) + repr(self.suit) + "'"

def rev_card_vals(hand):
    return [card.value for card in hand[::-1]]

def royal_flush(hand):
    is_straight_flush, secondary = straight_flush(hand)
    return (is_straight_flush and secondary[0] == 'A', secondary)

def high_card(hand):
    return (True, rev_card_vals(hand))

def straight(hand):
    return (hand[1] - hand[0] == 1 and hand[2] - hand[1] == 1 and hand[3] - hand[2] == 1 and hand[4] - hand[3] == 1, rev_card_vals(hand))

def flush(hand):
    return (hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit, rev_card_vals(hand))

def straight_flush(hand):
    return (straight(hand)[0] and flush(hand)[0], rev_card_vals(hand))

def four_of_kind(hand):
    is_four_of_kind = lambda cards: cards[0].value == cards[1].value == cards[2].value == cards[3].value
    if hand[0].value == hand[1].value:
        return (is_four_of_kind(hand[0:4]), hand[4].value)
    else:
        return (is_four_of_kind(hand[1:]), hand[0].value)

def three_of_kind(hand):
    is_three_of_kind = lambda cards: cards[0].value == cards[1].value == cards[2].value
    if is_three_of_kind(hand[0:3]):
        return (True, (hand[0].value, hand[4].value, hand[3].value))
    elif is_three_of_kind(hand[1:4]):
        return (True, (hand[1].value, hand[4].value, hand[0].value))
    elif is_three_of_kind(hand[2:5]):
        return (True, (hand[2].value, hand[1].value, hand[0].value))
    else:
        return (False, (0,))

def full_house(hand):
    has_three, secondary = three_of_kind(hand)
    if not has_three:
        return (has_three, secondary)
    if secondary[1] == secondary[2]:
        return (True, secondary[:2])
    
    return (False, (0,))

def one_pair(hand):
    for i, _ in enumerate(hand[1:]):
        if hand[i].value == hand[i - 1].value:
            return (True, [hand[i].value] + rev_card_vals(filter(
                lambda card: card.value != hand[i].value,
                hand)))
    else:
        return (False, (0,))

def two_pairs(hand):
    has_pair1, secondary1 = one_pair(hand)
    if has_pair1:
        first_pair = secondary1[0]
        has_pair2, secondary2 = one_pair([Card(i , 'S') for i in secondary1[1:]])
        if has_pair2:
            second_pair = secondary2[0]
            return (True, sorted((first_pair, second_pair), reverse=True) + [filter(lambda card: card.value != first_pair and card.value != second_pair, hand)[0].value])
    return (False, (0,))

Wins = (royal_flush, straight_flush, four_of_kind, full_house, flush, straight, three_of_kind, two_pairs, one_pair, high_card)

def get_hand_wintype(hand):
    for i, wintype in enumerate(Wins):
        win, secondary = wintype(hand)
        if win:
            return i, secondary

    assert False

wins_dict = {i:0 for i in xrange(10)}

def is_player1_winner(hands):
    win1, secondary1 = get_hand_wintype(hands[0])
    win2, secondary2 = get_hand_wintype(hands[1])
    #print win1, win2, secondary1, secondary2
    if win1 < win2:
        wins_dict[win1] += 1
        return True
    elif win2 < win1:
        return False
    else:
        assert secondary1 != secondary2, hands
        for strong1, strong2 in zip(secondary1, secondary2):
            if strong1 != strong2:
                if strong1 > strong2:
                    wins_dict[win1] += 1
                return strong1 > strong2
            elif secondary1[0] == 'A':
                print win1, secondary1, secondary2
                print hands
        else:
            assert False


def solve():
    print len(filter(is_player1_winner, parse_file()))
