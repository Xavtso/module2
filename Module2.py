# Variant 17
class Znak:
    def __init__(self, name, zodiac, birth):
        self.name = name
        self.zodiac = zodiac
        self.birth = birth

    def make_dict(self):
        params = {
            "name": self.name,
            "zodiac": self.zodiac,
            "birth": self.birth,
        }
        return params


znaki = list([])

for i in range(1, 9):
    n = input("Enter name for Person #"+str(i)+"\n")
    g = input("Enter zodiac for Person #"+str(i)+"\n")
    gr = [input("Enter birth day for Person #" + str(i) + "\n"),
          input("Enter birth month for Person #" + str(i) + "\n"),
          input("Enter birth year for Person #" + str(i) + "\n")]
    a = Znak(n, g, gr)
    znaki.append(a.make_dict())
print(znaki)
arr = []
for i in range(len(znaki)):
    arr.append([znaki[i]['name'], znaki[i]['zodiac'], znaki[i]['birth']])

# сортування
print("Sort by zodiac and birth: Name | Zodiac | Birth")
print("\nBefore:")
print(arr)
print("\nAfter:")
sorted_arr = sorted(arr, key=lambda x: (x[1], x[2]))
print(sorted_arr)

# вивід за умовою
qualified = []
user_search = input("Enter month:\n")

for i in range(len(sorted_arr)):
    if sorted_arr[i][2][1] == user_search:
        qualified.append(sorted_arr[i])

print("\n\nPersons with entered month: Name / Zodiac / Birth")
if len(qualified) == 0:
    print("There are no persons born in this month")
else:
    for i in range(0, len(qualified)):
        print(f'\n\n{str(qualified[i][0])} / {str(qualified[i][1])} / {str(qualified[i][2])}')