class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read().splitlines()
        file.close()
        return products


    def add(self, *products):
        exit_product = self.get_products()

        for product in products:
            product_str = str(product)

            for i in range(len(exit_product)):
                if product.name == exit_product[i].split(', ')[0] and product.category == exit_product[i].split(', ')[2]:
                    current_weight = float(exit_product[i].split(', ')[1])
                    new_weight = current_weight + product.weight
                    print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {new_weight}.')
                    exit_product[i] = f'{product.name}, {new_weight}, {product.category}'
                    break

            else:
                exit_product.append(product_str)

        file = open(self.__file_name, 'w')
        for item in exit_product:
            file.write(item + '\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1,p2,p3)
print(s1.get_products())
