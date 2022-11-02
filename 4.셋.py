game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(game)
print(set("Funny"))
print(set([2048, "Tetris", "Cube"]))
print(set((2560, 1440)))
print(set({"google": "google.com", 18: "unesco.org"}))
print(set(range(3)))

game.add("Fifa")
print(game)
game.update(("NBA", "MLB"))
print(game)

game.remove("LOL")

s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
print(s3 & s4)
print(s3.intersection(s4))

print(s3 | s4)
print(s3.union(s4))

print(s3 - s4)
print(s3.difference(s4))

print(s3 ^ s4)
print(s3.symmetric_difference(s4))
