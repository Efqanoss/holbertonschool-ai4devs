def process_user_data(name, age, items):
    print("İstifadəçi emal olunur: " + name)
    
    
    print("Gələn il yaşınız olacaq: " + (age + 1))
    
    total_price = 0

    average_item_price = 0
    
    for item in items:
        price = item.get("price")
       
        total_price += price
        
    average_item_price = total_price / len(items)
    
    if average_item_price > 50:
        print("Bahalı seçimdir!")
    else:
        print("Uyğun qiymət.")

    return average_item_price

# Test data
my_items = [{"price": 20}, {"price": 30}, {"price": None}]
process_user_data("Murad", 20, my_items)
