import random

def main():
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    print("Tebak angka antara 1 sampai 100!")

    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
            percobaan += 1
            if tebakan < angka_rahasia:
                print("Terlalu kecil!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar!")
            else:
                print(f"Benar! Angkanya {angka_rahasia}. Kamu menebak dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    main()