import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_List = data["Primary Fur Color"].to_list()

grey_count = data_List.count("Gray")
nan_count = data_List.count("Black")
cinnamon_count = data_List.count("Cinnamon")

fur_count = {
    "Fur Color": ["gray", "red", "black"],
    "count": [grey_count, cinnamon_count, nan_count]
}

new_data = pandas.DataFrame(fur_count)
new_data.to_csv("squirrel_count.csv")
