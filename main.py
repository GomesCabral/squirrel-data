import pandas

data = pandas.read_csv("squirrel_data.csv")
data_dict = data['Primary Fur Color'].to_list()
#print(data_dict)


gray = []
red = []
black = []

for color in data_dict:
    if color == 'Gray':
        gray.append(color)
    elif color == 'Cinnamon':
        red.append(color)
    elif color == 'Black':
        black.append(color)

#print(len(gray))
#print(len(red))
#print(len(black))

my_data = {
    "Color": [
        "grey",
        "red",
        "black"
        ],
    "Count": [
        len(gray),
        len(red),
        len(black)
    ]
}

#print(my_data)


my_final_data = pandas.DataFrame(my_data)
print(my_final_data)

my_final_data.to_csv("squirrel_count_by_color.csv")
