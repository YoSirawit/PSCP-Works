"""Phasmo"""

def find():
    """Find Ghost's type"""
    evidence_set = set()
    all_ghost = {"Banshee", "Demon", "Jinn", "Mare", "Oni", "Phantom", \
        "Poltergeist", "Revenant", "Shade", "Spirit", "Wraith", "Yurei"}

    for _ in range(3):
        evidence = input()
        if evidence != "No evidence":
            evidence_set.add(evidence)

    if "EMF Level 5" in evidence_set:
        all_ghost = all_ghost - all_ghost.intersection({"Demon", "Mare", "Poltergeist",\
            "Spirit", "Wraith", "Yurei"})
    if "Ghost Writing" in evidence_set:
        all_ghost = all_ghost - all_ghost.intersection({"Banshee", "Jinn", "Mare", "Phantom",\
             "Poltergeist", "Wraith"})
    if "Fingerprints" in evidence_set:
        all_ghost = all_ghost - all_ghost.intersection({"Demon", "Jinn", "Mare", "Oni", "Phantom",\
             "Shade", "Yurei"})
    if "Spirit Box" in evidence_set:
        all_ghost = all_ghost - all_ghost.intersection({"Banshee", "Phantom", "Revenant",\
             "Shade", "Yurei"})
    if "Freezing Temperatures" in evidence_set:
        all_ghost = all_ghost - all_ghost.intersection({"Jinn", "Oni", "Poltergeist", "Revenant",\
             "Shade", "Spirit"})
    if "Ghost Orb" in evidence_set:
        all_ghost = all_ghost - all_ghost.intersection({"Banshee", "Demon", "Oni", "Revenant",\
             "Spirit", "Wraith"})
    result = list(all_ghost)
    result.sort(key=first_char)

    if len(result) != 0:
        print(*result, sep="\n")
    else:
        print("Not yet discovered")

def first_char(sentence):
    """Return first character"""
    return sentence[0]

find()
