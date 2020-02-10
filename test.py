f = open("info.txt", 'r', encoding='utf-8')

lines = f.readlines()
values = []
for line in lines:
    values.append(line.strip().split(":")[1])
print(values)
# id = lines.split(":")[1].strip()
# pw = lines.split(":")[1].strip()
