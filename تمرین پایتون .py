import random


def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0

    print("\nبه بازی حدس عدد خوش آمدید!")
    print("من یک عدد بین 1 تا 100 انتخاب کرده‌ام.")
    print("شما 5 فرصت برای حدس زدن دارید.")

    while attempts < max_attempts:
        print(f"\nتلاش {attempts + 1} از 5")
        print(f"جان باقی‌مانده: {max_attempts - attempts}")

        try:
            guess = int(input("عدد مورد نظر خود را وارد کنید: "))
        except ValueError:
            print("لطفاً فقط عدد وارد کنید!")
            continue

        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشد!")
            continue

        attempts += 1

        if guess == secret_number:
            print("\nآفرین! شما برنده شدید!")

            if attempts == 1:
                print("رتبه شما: نمونه ای")
            elif attempts == 2:
                print("رتبه شما: بسیار خوبی")
            elif attempts == 3:
                print("رتبه شما: خوب")
            elif attempts == 4:
                print("رتبه شما: قبول")
            else:
                print("رتبه شما: با شانس بردی!")

            break

        difference = abs(guess - secret_number)

        if guess > secret_number:
            print("عدد کوچک‌تری وارد کن!")
        else:
            print("عدد بزرگ‌تری وارد کن!")

        if difference <= 5:
            print("خیلی نزدیکی!")
        elif difference <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

    else:
        print("\nمتأسفانه فرصت‌های شما تمام شد!")
        print(f"عدد صحیح برابر بود با: {secret_number}")
        print("این بار موفق به حدس زدن نشدی!")


def main():
    while True:
        play_game()

        while True:
            answer = input(
                "\nآیا می‌خواهید دوباره بازی کنید؟ (yes/no): "
            ).lower().strip()

            if answer in ["yes", "y"]:
                break
            elif answer in ["no", "n"]:
                print("\nخدانگهدار! ممنون از بازی شما.")
                return
            else:
                print("لطفاً yes یا no وارد کنید.")


main()
