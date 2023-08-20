import db_api

# db = db_api.Database('db_api/database/shop_database.db')
# db.add_item(id=1, name='Помидоры', count=30, photo_path=r'db_api/database/product_photo/tomat.jpg')
# db.add_item(id=2, name='Огурцы', count=20, photo_path='db_api/database/product_photo/cucumber.jpg')
# db.add_item(id=3, name='Тыква', count=45, photo_path='db_api/database/product_photo/punpkin.jpg')
# db.add_item(id=4, name='Кабачки', count=15, photo_path='db_api/database/product_photo/marrow.jpg')
# print(db.select_all_items())
# print(db.select_all_basket())
#
# print(db.get_items_count())
# user_basket = ''
# current_item_id = '2'
# current_count = 10
# user_basket = [item_data.split(':') for item_data in user_basket.split()]
# print(user_basket)
# for i in range(len(user_basket)):
#     item_id, item_count = user_basket[i]
#     if current_item_id == item_id:
#         user_basket[i][1] = str(int(item_count) + current_count)
#         break
# else:
#     user_basket += [[current_item_id, str(current_count)]]
# print(user_basket)
# user_basket = ' '.join([':'.join(dbl) for dbl in user_basket])
#
# print(user_basket)
