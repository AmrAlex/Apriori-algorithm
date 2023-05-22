import math
import pandas as pd
import csv
def read_csv_to_list(file_path):
    data = []
    
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    
    return data


# Example usage
csv_file_path = 'Market_Basket_TDB.csv'  # Replace with the path to your CSV file
data = read_csv_to_list(csv_file_path)
df = pd.read_csv('Market_Basket_TDB.csv')
def get_unique_items(df):
    
    unique_items = set()

    for column in df.columns:
        unique_items.update(df[column].unique())
    return list(unique_items)

# Example usage:


from itertools import combinations
from collections import defaultdict

def generate_combinations(items, length):
    return list(combinations(items, length))

def count_support(transactions, combinations):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for combination in combinations:
            if set(combination).issubset(set(transaction)):
                item_counts[combination] += 1
    return item_counts

def filter_combinations(item_counts, min_support):
    return [combination for combination, count in item_counts.items() if count >= min_support]

items = get_unique_items(df)

max_length=input("length of items needed:  ")
min_support=input("min support :  ")

for i in range(1,int(max_length)+1):
    combinations_list1 = generate_combinations(items, i)
    item_counts = count_support(data, combinations_list1)
    filtered_combinations = filter_combinations(item_counts, int(min_support))
    df_after= pd.DataFrame(filtered_combinations) 
    items = get_unique_items(df_after)
    print(items,len(items))


print(filtered_combinations)

