def calculate_voting_year(current_age):
    """
    Calculate the year in which the user will be eligible to vote.
    
    Args:
        current_age (int): The user's current age.
    
    Returns:
        int: The year in which the user will be eligible to vote.
    """
    current_year = 2023  # Assuming the current year is 2023
    voting_age = 18
    
    if current_age >= voting_age:
        return current_year
    else:
        years_until_eligible = voting_age - current_age
        return current_year + years_until_eligible

def main():
    current_age = int(input("Enter your current age: "))
    voting_year = calculate_voting_year(current_age)
    
    print(f"You will be eligible to vote in the year {voting_year}.")

if __name__ == "__main__":
    main()