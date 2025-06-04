import random

def get_user_choice():
    choices = ['batu', 'gunting', 'kertas']
    user = input("Pilih (batu/gunting/kertas): ").lower()
    while user not in choices:
        print("Pilihan tidak valid.")
        user = input("Pilih (batu/gunting/kertas): ").lower()
    return user

def get_computer_choice():
    return random.choice(['batu', 'gunting', 'kertas'])

def determine_winner(user, computer):
    if user == computer:
        return "Seri!"
    elif (user == 'batu' and computer == 'gunting') or \
         (user == 'gunting' and computer == 'kertas') or \
         (user == 'kertas' and computer == 'batu'):
        return "Kamu menang!"
    else:
        return "Kamu kalah!"

def main():
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"Kamu memilih: {user}")
    print(f"Komputer memilih: {computer}")
    print(determine_winner(user, computer))

if __name__ == "__main__":
    main()