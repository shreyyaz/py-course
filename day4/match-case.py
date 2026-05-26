#Match Case Statement(SWITCH IN C AND JAVA): alternative to using elif statements

def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Saturday":
            return True
        case "Monday"| "Tuesday" | "Wednesday" |"Thursday" | "Friday": #| pipe operator is used as
            return False
        case _: #basically else, anything except days will be treated here
            return False

print(is_weekend("Sunday"))
print(is_weekend("Friday"))
print(is_weekend("Brocode"))

