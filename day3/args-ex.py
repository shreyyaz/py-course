#Python function parameters follow this order for execution: normal, default=0, *args, **kwargs

def shipping_label(*args,**kwargs):
    for x in args:
        print(x,end=" ") #looping through tuple
    print()
    for x in kwargs.values():
        print(x, end=" ") #looping through dict
    print()

    #GETTING OUTPUT IN DIFF LINES
    print(f"{kwargs.get('street')} {kwargs.get('city')}")
    print(f"{kwargs.get('state')} {kwargs.get('zip')}") 


shipping_label("Dr.","Bro","Code",
               street="123 Fake St",
               city="Detroit",
               state="MI",
               zip="54321")     
#"Dr.", "Bro", "Code" are unnamed/positional arguments. so they go into args as TUPLE.
#street="123 Fake St"city="Detroit"state="MI"zip="54321" are keyword arguments so they go into kwargs as DICTIONARY.