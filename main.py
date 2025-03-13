file = open("Book1.csv",mode="r",encoding='utf-8-sig')
key = file.readline().strip()
keys = key.split(",")

value = file.readline().strip()
data_ranking = []
while value!="":
    index = 0
    values = value.split(",")
    index_data = {}
    for index in range(len(keys)):
        if keys[index] == 'score' or keys[index] == 'rank':
            values[index] = int(values[index])
        my_dict = {keys[index]:values[index]}
        index_data.update(my_dict)   
    data_ranking.append(index_data)
    value = file.readline().strip()
print(data_ranking)