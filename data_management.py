import sys

def process_data(a, b, c, d, e):
    # Checks if all inputs are numeric; if not, return an error message.
    try:
        numbers = [int(a), int(b), int(c), int(d), int(e)]
    except ValueError:
        return "<h2>Error</h2><p>All inputs must be numeric.</p>"
    
    html_output = "<h2>Results:</h2>\n"
    
    # Add original values
    html_output += f"<p>Original Values: {', '.join(map(str, numbers))}</p>\n"
    
    # Checks if any value is negative and displays a message if so.
    negative_values = [num for num in numbers if num < 0]
    if negative_values:
        html_output += f"<p>Found {len(negative_values)} negative value(s): {', '.join(map(str, negative_values))}</p>\n"
    
    # Calculates the average of the numbers and checks if it's greater than 50.
    average = sum(numbers) / len(numbers)
    avg_status = "greater than" if average > 50 else "not greater than"
    html_output += f"<p>The average is: {average:.2f} ({avg_status} 50)</p>\n"
    
    # Count positive numbers
    positive_count = sum(1 for num in numbers if num > 0)
    
    # Uses bitwise operations to determine if the count of positive numbers is even or odd.
    is_even = "even" if (positive_count & 1) == 0 else "odd"
    html_output += f"<p>Count of positive numbers: {positive_count} (This count is {is_even})</p>\n"
    
    # Creates a new list with values greater than 10, sorts it
    values_gt_10 = [num for num in numbers if num > 10]
    sorted_values = sorted(values_gt_10)
    
    # Add sorted values to output
    html_output += f"<p>Sorted Values(greater than 10): {', '.join(map(str, sorted_values))}</p>\n"
    
    return html_output

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("<h2>Error</h2><p>Exactly 5 numeric arguments are required.</p>")
        sys.exit(1)
    
    a, b, c, d, e = sys.argv[1:6]
    html_result = process_data(a, b, c, d, e)
    
    # Output HTML
    print(html_result)