def hello(greeting,title,first,last):
    print(f"{greeting}{title}{first}{last}")

hello("Hey there ", "Mr. ", "Bro ", "Code ")
hello("Hey there ",title="Mr. ",last="Code ",first="Bro ")   
#order of args dont matter, argument preceded by an indentifier helps with readability

print("1","2","3","4","5", sep="-")  #separate by - is a keyword arg to the fcn