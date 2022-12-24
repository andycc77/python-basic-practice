movie_1 = {'name': 'Saving Private Ryan',  # 電影名稱
         'year': 1998,
         'directory': 'Steven Spielberg',
         'Writer': 'Robert Rodat'}

movie_2 = dict(name='Saving Private Ryan',  # 電影名稱
               year=1998,
               directory='Steven Spielberg',
               Writer='Robert Rodat')

print(movie_1.get('name'))
print(movie_2.get('year'))
print(movie_2.get('ggg'))

movie_1['start'] = 'Tom Hank'
movie_1['year'] = '1999'
print(movie_1)

del movie_1['year']
print(movie_1)

writer = movie_1.pop('Writer')
print(writer)
print(movie_1)

print('count: ' + str(len(movie_1)))

print('keys: ' + str(movie_1.keys()))

print('keys: ' + str(movie_1.values()))

print('items: ' + str(movie_1.items()))
