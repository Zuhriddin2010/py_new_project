from googletrans import Translator

def tarjimon():
    # Google Translate xizmatini ulaymiz
    translator = Translator()

    print("--- O'zbekcha-Inglizcha Tarjimon ishga tushdi ---")
    
    while True:
        # Siz xohlagan matn konsolda chiqadi:
        print("\nO'zbekcha so'z kiriting, men uni inglizchaga tarjima qilib beraman:")
        soz = input(">>> ")

        # Dasturdan chiqish uchun
        if soz.lower() in ['exit', 'stop', 'chiqish']:
            print("Dastur tugatildi.")
            break

        try:
            # src='uz' (o'zbekchadan) -> dest='en' (inglizchaga)
            natija = translator.translate(soz, src='uz', dest='en')
            
            print(f"Inglizcha tarjimasi: {natija.text}")
            
        except Exception:
            print("Xatolik: Internet ulanishini tekshiring!")

if __name__ == "__main__":
    tarjimon()