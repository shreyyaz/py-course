#Making a Num Pad: will use a tuple becasue ordered and immutable
numpad=((1,2,3),
        (4,5,6),
        (7,8,9),
        ("*",0,"#"))

for row in numpad:
    for num in row:  #mistake did instead of row used numpad/
        print(num, end=" ")
    print()
