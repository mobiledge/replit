import random
import string

def pr(x):
    print("\n", x, "\n")


l1 = [1, 2, 3, 4]
print(l1)

# ordered ints
l2 = list(range(10))
print("\nl2:\n", l2)

# shuffled ints
random.shuffle(l2)
print("\nl2:\n", l2)

# non-repeating random ints
l3 = random.sample(range(100, 1000), 10)
print("\nl3:\n", l3)

# repeating random ints
ran_int = lambda x: random.randint(0, 10)
l3 = list(map(ran_int, range(100)))
print("\nl3:\n", l3)

# ordered chars
l4 = list(string.ascii_lowercase)
print("\nl4:\n", l4)

# shuffled chars
random.shuffle(l4)
print("\nl4:\n", l4)

# non-repeating random chars
l5 = random.sample(string.ascii_lowercase, 10)
print("\nl5:\n", l5)

# repeating random chars
ran_char = lambda x: random.choice(string.ascii_lowercase)
l5 = list(map(ran_char, range(100)))
print("\nl5:\n", l5)

# words
str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
words = str.split(" ")

# random words non-repeating
pr(random.sample(words, 5))

# random words repeating
l7 = list(map(lambda x: random.choice(words), range(100)))
pr(l7)
