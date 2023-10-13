cook_book = {}
all_dishes = [[]]
count = 0

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:   
        if line == '\n':  
            all_dishes.append([])
            count += 1
        else:
            all_dishes[count].append([line.strip()])
    
for dish in all_dishes:
    cook_book[''.join(dish[0])] = []
    for ingredient in dish[2:]:
        ingredient_information =''.join(ingredient).split(" | ")
        print(ingredient_information)
        new_ingredient = {
            'ingredient_name': ingredient_information[0],
            'quantity': int(ingredient_information[1]), 
            'measure': ingredient_information[2]
        }
        cook_book[''.join(dish[0])].append(new_ingredient)
            
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_common_list = {}

    for dish in dishes:
        for dish_item, ingredients in cook_book.items():
            if dish == dish_item:
                for ingredient in ingredients:
                    ingredient_name_for_common_list = ingredient['ingredient_name']
                    if ingredient_name_for_common_list in ingredients_common_list:
                        ingredients_common_list[ingredient_name_for_common_list]['quantity'] += ingredient['quantity'] * person_count
                    else:
                        ingredients_common_list[ingredient_name_for_common_list] = {
                            'measure': ingredient['measure'],
                            'quantity': ingredient['quantity'] * person_count                            
                        }
    return ingredients_common_list

# print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
                        
