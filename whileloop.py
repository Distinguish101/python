
from multiprocessing import Condition


i = 1
while i <= 10:
    print(i)
    i = i + 1 # or i += 1(increment i)

print("Done with loop")