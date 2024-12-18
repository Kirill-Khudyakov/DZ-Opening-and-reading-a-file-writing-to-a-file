import os
import time

# Задача №1
# Должен получится следующий словарь:

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ingredients = []
            for _ in range(count):
                ingredient_line = f.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            f.readline()
    return cook_book


def main():
    cook_book = read_cookbook()
    for dish, ingredients in cook_book.items():
        print(f"{dish}:")
        for ingredient in ingredients:
            print(f"  {ingredient['ingredient_name']} - {ingredient['quantity']} {ingredient['measure']}")
        print()  

if __name__ == '__main__':
    main()


# Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    for dish in dishes:
      if dish in cook_book:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
          ingredient_name = ingredient['ingredient_name']
          quantity = ingredient['quantity'] * person_count
          measure = ingredient['measure']
          if ingredient_name in ingredients_list:
            ingredients_list[ingredient_name]['quantity'] += quantity
          else:
            ingredients_list[ingredient_name] = {
              'measure' : measure,
              'quantity' : quantity
            }
      else:
        print(f'\n"Такого блюда нет в списке!"\n')

    return ingredients_list

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
start_time = time.time()
result = get_shop_list_by_dishes(dishes, person_count)
end_time = time.time()
for ingredient, details in result.items():
  print(f"{ingredient}: {details['quantity']} {details['measure']}")

execution_time = end_time - start_time
print(f"Время выполнения кода: {execution_time:.10f} секунд")

 