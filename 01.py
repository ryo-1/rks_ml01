def ponpokona(txt):
    pon = ["ぽ", "ん", "ぽ", "こ", "な", "あー"]
    for i, s in enumerate(txt):
        print(pon[i % len(pon)], end="")

while True:
    txt = input()
    if txt == ":q":
        break
    ponpokona(txt)
    print()