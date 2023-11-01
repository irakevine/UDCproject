import thirdOuiUD  as tq
print(2+5)
print(tq.num)



scores = [88, 92, 79, 93, 85]

mean = tq.mean(scores)
curved = tq.add_five(scores)

mean_c = tq.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(tq.__name__)