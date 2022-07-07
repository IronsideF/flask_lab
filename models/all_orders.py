from models.order import Order
# from PIL import Image
# dune_cover = Image.open('img/Dune_Cover.jpeg')
# ti_cover = Image.open('img/Treasure Island_Cover.jpeg')
# pp_cover = Image.open('img/Pride & Prejudice_Cover.png')
# keith = Image.open('img/Keith_Pic.jpeg')
# sky = Image.open('img/Sky_Pic.jpeg')
# ben = Image.open('img/Ben_Pic.png')
order_1 = Order('Keith', '27/04/2021', 7, 'Treasure Island', 'Robert Louis Stevenson', 'Treasure Island_Cover.jpeg', 'Keith_Pic.jpeg')
order_2 = Order('Sky', '30/06/2022', 1500, 'Dune', 'Frank Herbert', 'Dune_Cover.jpeg', 'Sky_Pic.jpeg')
order_3 = Order('Ben', '01/07/2022', 89, 'Pride & Prejudice', 'Jane Austen', 'Pride & Prejudice_Cover.png', 'Ben_Pic.png')

order_list = [order_1, order_2, order_3]
