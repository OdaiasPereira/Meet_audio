import docx2txt

cost_per_token = 0.05

def calculate_cost(token_count):
    # Calculate the estimated cost by multiplying the number of tokens by the cost per token
    return token_count * cost_per_token / 1000  # Divide by 1000 to get the cost per thousand tokens

def manage_cost(text):
    # Cost per token in dollars

    try:
        # Count the number of words
        word_count = len(text.split())

        # Use an approximate conversion factor of tokens per word (e.g., 1.2 to 1.4)
        conversion_factor_lower = 1.2
        token_count_lower = int(word_count * conversion_factor_lower)

        conversion_factor_upper = 1.4
        token_count_upper = int(word_count * conversion_factor_upper)

        # Calculate the estimated cost for the token count range
        cost_lower = calculate_cost(token_count_lower)
        cost_upper = calculate_cost(token_count_upper)

        print(f"Approximate token count: between {token_count_lower} and {token_count_upper}")
        print(f"Estimated cost: between ${cost_lower:.2f} and ${cost_upper:.2f}")

        return token_count_upper, cost_upper

    except Exception as e:
        print(f"An error occurred: {e}")