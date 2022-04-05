is_male = False
is_tall = False

if is_male:
    print("you are a male")
else:
    print("you are not a male")


if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither male nor tall")

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are a short male")
elif not(is_male) and not(is_tall):
    print("you are not a male but is tall")
else:
    print("you are either not male or not tall or both")



