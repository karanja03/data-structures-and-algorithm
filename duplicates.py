def remove_duplicates(sequence):
    seen = set()    # Create an empty set to keep track of seen items
    result = []     # Create an empty list to store the result with duplicates removed
    
    for item in sequence:
        if item not in seen:
            # If the item is not already in the 'seen' set
            result.append(item)  # Add the item to the result list
            seen.add(item)       # Add the item to the 'seen' set
    
    return result   # Return the list with duplicates removed

# Test the function with a sample input
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]