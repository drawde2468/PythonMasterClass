def python_food():
    width = 80
    text = "Spam and eggs"


def center_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


center_text("spam and eggs")
center_text(13)
center_text("spam, spam, and eggs")
center_text("spam, spam, spam, and eggs")
