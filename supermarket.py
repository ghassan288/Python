# نظام سوبر ماركت بسيط
def supermarket_system():
    # قائمة المنتجات المتوفرة (قاعدة بيانات مصغرة)
    products = {
        "أرز": 5.0,
        "حليب": 3.5,
        "خبز": 1.0,
        "سكر": 4.0,
        "زيت": 12.0
    }
    
    cart = [] # سلة التسوق
    total_bill = 0
    
    print("--- مرحباً بك في نظام السوبر ماركت الذكي ---")
    print("المنتجات المتوفرة وأسعارها:")
    for item, price in products.items():
        print(f"- {item}: {price} ريال")
    
    print("\n(اكتب 'خروج' لإنهاء عملية الشراء وطباعة الفاتورة)")

    while True:
        product_name = input("\nأدخل اسم المنتج: ").strip()
        
        if product_name == 'خروج':
            break
            
        if product_name in products:
            try:
                quantity = int(input(f"أدخل الكمية من {product_name}: "))
                if quantity <= 0:
                    print("عذراً، يجب أن تكون الكمية أكبر من صفر.")
                    continue
                
                price = products[product_name]
                item_total = price * quantity
                
                # إضافة المنتج للسلة
                cart.append({
                    "المنتج": product_name,
                    "الكمية": quantity,
                    "السعر_للوحدة": price,
                    "الإجمالي": item_total
                })
                
                print(f"تمت إضافة {quantity} {product_name} بنجاح.")
            except ValueError:
                print("خطأ! يرجى إدخال رقم صحيح للكمية.")
        else:
            print("عذراً، هذا المنتج غير متوفر حالياً.")

    # عرض الفاتورة النهائية
    if cart:
        print("\n" + "="*30)
        print("      الفاتورة النهائية")
        print("="*30)
        print(f"{'المنتج':<10} | {'الكمية':<5} | {'السعر':<7} | {'الإجمالي':<8}")
        print("-" * 35)
        
        for item in cart:
            print(f"{item['المنتج']:<10} | {item['الكمية']:<5} | {item['السعر_للوحدة']:<7} | {item['الإجمالي']:<8}")
            total_bill += item['الإجمالي']
        
        print("-" * 35)
        print(f"السعر النهائي المطلوب دفعه: {total_bill} ريال")
        print("="*30)
        print("شكراً لزيارتكم!")
    else:
        print("\nالسلة فارغة، نتمنى رؤيتك قريباً.")

# تشغيل النظام
if __name__ == "__main__":
    supermarket_system()
