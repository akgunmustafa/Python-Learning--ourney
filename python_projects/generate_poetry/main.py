# Generate a random poem based on a set structure

import random

noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verb = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]
adjective = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]
preposition = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverb = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]


def make_poem():
    """Create a random generated poem, returned a multi-line string."""

    # Pull three different nouns randomly
    noun1 = random.choice(noun)
    noun2 = random.choice(noun)
    noun3 = random.choice(noun)
    while noun1 == noun2:
        noun1 = random.choice(noun)
    while noun2 == noun3 or noun1 == noun3:
        noun3 = random.choice(noun)

    # Pull three different verbs randomly
    verb1 = random.choice(verb)
    verb2 = random.choice(verb)
    verb3 = random.choice(verb)
    while verb1 == verb2 or verb1 == verb3:
        verb1 = random.choice(verb)
    while verb2 == verb3:
        verb2 = random.choice(verb)

    # Pull three different adjectives randomly
    adj1 = random.choice(adjective)
    adj2 = random.choice(adjective)
    adj3 = random.choice(adjective)
    while adj1 == adj2:
        adj1 = random.choice(adjective)
    while adj2 == adj3 or adj3 == adj1:
        adj3 = random.choice(adjective)

    # Pull three different prepositions
    pr1 = random.choice(preposition)
    pr2 = random.choice(preposition)
    pr3 = random.choice(preposition)
    while pr1 == pr2 or pr1 == pr3:
        pr1 = random.choice(preposition)
    while pr2 == pr3:
        pr2 = random.choice(preposition)

    # Pull one adverb
    adverb1 = random.choice(adverb)

    if "aeiou".find(adj1[0]) != -1:  # First letter is a vowel
        article = "An"
    else:
        article = "A"

    # Create the Poem
    poems = (
        f"{article} {adj1} {noun1}\n\n"
        f"{article} {adj1} {noun1} {verb1} the {adj2} {noun2}\n"
        f"{adverb1}, the {noun1} {noun2}\n"
        f"the {noun2} {verb3} {pr2} a {adj3} {noun3}"
    )

    return poems


print(make_poem())
