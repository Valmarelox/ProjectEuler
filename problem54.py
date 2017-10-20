

values = dict({str(x):x for x in xrange(2, 11)}, **{'J': 11, 'Q': 12, 'K': 13, 'A': 14})
wins = ('highCard', 'onePair', two)
class Card:
    def __init__(self, value, suite):
        self.value = values[value]
        self.suite = suite

    def __cmp__(self, other):
        return cmp(self.value, other.value)
    def __repr__(self):
        return "%d %s" % (self.value, self.suite)

def highCard(hand):
    return sorted(hand)[-1]


def counts(hand):
    counter = {}
    for card in hand:
        counter[card.value] = hand.count(card)
    return counter


def deduceHand(hand):


hand = (Card('5', 'D'), Card('5', 'D'), Card('6', 'D'), Card('7', 'D'), Card('A', 'D'))

print highCard(hand)
print counts(hand)
