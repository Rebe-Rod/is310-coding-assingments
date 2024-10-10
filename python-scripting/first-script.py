favorite_movies =[
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    }
]


print("what's your favorite movie?")
new_favorite_movie = input()
print("New fsvorite movie",
      new_favorite_movie)

favorite_movies[0]['long_description'] = "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. The Waschowskis created a plot set in a dystopian future where humanity is unknowingly trapped inside a simulated reality, the Matrix, created by intelligent machines to distract humans while using their bodies as an energy source. In the movie, the main character, Neo, is a computer programmer who learns this truth and is drawn into a rebellion against the machines, which involves other people who have been freed from the Matrix."
print(favorite_movies[0]['long_description'].split('kesnu reeves')[0])

favorite_movies[0]['short_description'] = ' '.join(split_description[:10])
print(favorite_movies[0]['short_description'])



favorite_movie = {
    "name": "Everything Everywhere All at Once",
    "release_year": 2022
}
favorite_book ={
    "name": "Don Quixote"
    "release_year": 1605,
}
#favorite_movie[0]['Short_description'] = "Everything Everywhere All at Once is a 2022 American science fiction action comedy film directed by Daniel Kwan and Daniel Scheinert. The film stars Michelle Yeoh as Evelyn Wang, a Chinese American laundromat owner who is pulled into a multiverse of her alternate selves to stop a cosmic disaster. The film also stars Ke Huy Quan, Stephanie Hsu, Jamie Lee Curtis, and James Hong. The film premiered at the 2022 South by Southwest festival and was released in the United States on March 25, 2022, by A24."
#favorite_book[0]['Short_descriptiIt was  The novel follows the aon'] = "Don Quixote is a novel by Miguel de Cervantes. dventures of an

#print(favorite_movie)
#print(favorite_book)

#for movie in favorite_movies:
    #print(movie['name'])
    #print(movie['release_year'])

for header, info in favorite_movies[0].items():
    return header, info