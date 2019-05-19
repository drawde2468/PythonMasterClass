import shelve

books = shelve.open("books")

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread", ],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled_eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]
                    }
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled_eggs"])
print(books["maintenance"]["loose"])
books.close()
