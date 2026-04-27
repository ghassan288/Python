from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def des_program():
    print("--- برنامج تشفير وفك تشفير DES ---")
    
    # طلب اختيار العملية
    print("1. تشفير (Encryption)")
    print("2. فك تشفير (Decryption)")
    choice = input("اختر رقم العملية (1 أو 2): ")

    if choice not in ['1', '2']:
        print("اختيار غير صحيح، يرجى تشغيل البرنامج مرة أخرى.")
        return

    # طلب المفتاح (يجب أن يكون 8 أحرف)
    key_input = input("أدخل المفتاح (8 أحرف بالضبط): ")
    if len(key_input) != 8:
        print("خطأ: يجب أن يكون المفتاح مكوناً من 8 بايت (8 أحرف).")
        return
    key = key_input.encode('utf-8')

    # إنشاء كائن التشفير بنمط ECB
    cipher = DES.new(key, DES.MODE_ECB)

    if choice == '1':
        # --- التشفير ---
        text = input("أدخل النص المراد تشفيره: ").encode('utf-8')
        
        # إضافة الحشو لتناسب حجم الكتلة (8 بايت)
        padded_text = pad(text, DES.block_size)
        encrypted_bytes = cipher.encrypt(padded_text)
        
        # تحويل النتيجة إلى Hex لتسهيل القراءة
        encrypted_hex = binascii.hexlify(encrypted_bytes).decode('utf-8')
        print(f"\n✅ النص المشفر (Hex): {encrypted_hex}")

    elif choice == '2':
        # --- فك التشفير ---
        hex_input = input("أدخل النص المشفر (بصيغة Hex): ")
        
        try:
            # تحويل النص من Hex إلى بايتات
            encrypted_bytes = binascii.unhexlify(hex_input)
            
            # فك التشفير وإزالة الحشو
            decrypted_padded = cipher.decrypt(encrypted_bytes)
            original_text = unpad(decrypted_padded, DES.block_size).decode('utf-8')
            
            print(f"\n✅ النص الأصلي: {original_text}")
        except Exception as e:
            print(f"\n❌ خطأ: لم نتمكن من فك التشفير. تأكد من صحة المفتاح والنص المشفر.")

# تشغيل البرنامج
if __name__ == "__main__":
    des_program()