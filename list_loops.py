# Q1
# Copy the `songs` list
songs = ["ROCKSTAR", "Do It", "For The Night"]


# Q2
# Print the first element and the last element of the list
first_song = songs[0]
print(f'The first song of the list: "{first_song}"')

last_song = songs[-1]
print(f'The last song of the list: "{last_song}"')

# Print out "Do It" and "For the Night" using a list slice on the `songs` list
print(songs[1:])


# Q3
# Update the last element of the `songs` list with a new song
songs[-1] = "The World Is Yours"
print(songs)


# Q4
# Add three songs to the list
songs.extend(["We Major", "Thief's Theme", "It Ain't Hard to Tell"])
print(songs)

# Delete the first element
del songs[0]
print(songs)
print()


# Q6
# Create a list called `animals` with 3 animal strings
animals = ["Shark", "Bear", "Tiger"]

# Add another animal to the list
animals.append("Komodo Dragon")

# Print out the third animal of the list
print(animals[2])
print()

# Delete the first animal of the list
del animals[0]

# Print out all the elements of the list with a for-loop
for animal in animals:
    print(animal)




