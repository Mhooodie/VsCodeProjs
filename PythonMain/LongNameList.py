people: list[str] = ["James", "Charlotte", "Stephany", "Mario", "Sandra"] # : list[str] specifies that it is a list of string, this can be removed and still work.

long_names: list[str] = []
for i in people:
    if len(i) > 7:
        long_names.append(i)

print(long_names)
