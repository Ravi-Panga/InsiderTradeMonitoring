from nltk.corpus import wordnet
# To extract synsets

syns = wordnet.synsets("trade")

print("\nall the elements in synset:\n",syns)

print("\n first element from synset: \n",syns[0])

# Lemmas from the first word of synset
print("\n lemmas of first element from synset: \n",syns[0].lemmas()[0].name())

print("\n definition of the first element from synset is:\n",syns[0].definition())

print("\n examples of the first element from synset is:\n",syns[0].examples())

# Empty lists to collect the synonyms and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("\n synonyms are:",set(synonyms))
print("\n antonyms are:",set(antonyms))

# Word similarity measure using wup_similarity algorithm
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print("Ship and Boat similarity is:",w1.wup_similarity(w2)*100,"% ")

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print("Ship and Car similarity is:",w1.wup_similarity(w2)*100,"% ")

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("hip.n.01")
print("Ship and Hip similarity is:",w1.wup_similarity(w2)*100,"%")


