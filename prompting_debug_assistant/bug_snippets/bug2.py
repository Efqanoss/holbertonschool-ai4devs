def process_user_data(name, age, items):
    print("İstifadəçi emal olunur: " + name)
    
    # Xəta 1: Tip xətası (Mətnlə rəqəmi birbaşa toplamaq olmaz)
    print("Gələn il yaşınız olacaq: " + (age + 1))
    
    total_price = 0
    # Xəta 2: Məntiq xətası (Siyahı boşdursa, proqram qırılacaq - ZeroDivisionError)
    average_item_price = 0
    
    for item in items:
        price = item.get("price")
        # Xəta 3: 'NoneType' obyekti ilə toplama xətası ehtimalı
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
