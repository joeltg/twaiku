import syllables

#complete
test1 = [
    "an old silent pond",
    "a frog jumps into the pond",
    "splash silence again"
]

#complete
test2 = [
    "northern life is cold",
    "july brings unheard of heat",
    "ice cream cones for all"
]

#incomplete
test3 = [
    "my name is",
    "hello are you there",
    "test input input"
]

#incomplete
test4 = [
    "sleeping weird word",
    "metric segmentation",
    "orange"
]

print syllables.count_syllables_haiku(test1)
print syllables.count_syllables_haiku(test2)
print syllables.count_syllables_haiku(test3)
print syllables.count_syllables_haiku(test4)
