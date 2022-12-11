thriller = ['Thriller', 'Billie Jean', 'Beat It']
print(thriller[1])

thriller = ['Thriller', 'Billie Jean', 'Beat It']
print(thriller[-1])


thriller = ['Thriller', 'Billie Jean', 'Beat It']
print(thriller[0:2:2])

thriller = ['Thriller', 'Billie Jean', 'Beat It']
# thriller.append('That Girl is Mine')
thriller.insert(0, 'That Girl is Mine')
print(thriller)

bad_1 = ['bad', 'Smooth Criminal', 'Speed Demon']
bad_2 = ['Man in the Mirror', 'Dirty Diana']
bad_1.insert(1, bad_2)
print(bad_1)

bad_1 = ['bad', 'Smooth Criminal', 'Speed Demon']
bad_2 = ['Man in the Mirror', 'Dirty Diana']
bad_1.extend(bad_2)
print(bad_1)

bad = ['bad', 'Smooth Criminal', 'Speed Demon', 'Man in the Mirror', 'Dirty Diana']
bad.remove('Smooth Criminal')
print(bad)

bad = ['bad', 'Smooth Criminal', 'Speed Demon', 'Man in the Mirror', 'Dirty Diana']
popped = bad.pop()
print(bad)
print(popped)
