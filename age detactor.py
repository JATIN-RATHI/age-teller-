if __name__ == '__main__':
    print("\nWelcome to this Program\tcreated by Jatin Rathi")
    age = int(input("Enter your age/year of birth to know when you will complete 100 years on earth : "))
    if age >= 1 and age < 100:
        remaining_years = 100 - age
        print(f"You will be 100 after : {remaining_years} years")
    elif age >= 1920 and age < 2020:
        age_now = 2020 - age
        remainder_years = 100 - age_now
        print(f"You are now {age_now} years old and  will be 100 after : {remainder_years} years")
    elif age < 1920 and age >1800:
        age_now = 2020 - age
        print(f"You are now {age_now} years old.")
    elif age >= 2021:
        print("I think you are under construction. Hope you are enjoying inside your mamma.")
    elif age > 100 and age <= 117:
        print("OMG!! You already crossed your 100 years of presence on earth.\n\t Hope you we'll break the oldest human record. \n\tBest of Luck")

    elif age > 117 and age <200:
        print("Congratuation!! you are the oldest man on the planet Earth.")
    else:
        print("You can't live this long if you are a human.")