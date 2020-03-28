from demos import bisection_iter, analyze_func, generate_emails

# Add domains to list below for additional email extensions
list_of_domains = ['yaexample.com','goexample.com','example.com']

# Generate emails
emails = generate_emails(10,list_of_domains,1000000) #Length of email and number of emails present in list

# Test email to add to list of emails, followed by append to list
email = 'hello@example.com'
emails.append(email)

# Sort list of generated emails
sorted_emails = sorted(emails)

# Run bisection search to find test email in sorted list of emails
index, found = bisection_iter(email, sorted_emails)
#changed function form a string to a tuple - see bisection_iter
# Print result from function
print(found)

# Print index returned by function used on the list of sorted emails
if index:   print(f"element at index: {index} is {sorted_emails[index]}")

# Run analysis of functions
analyze_func(bisection_iter, email, sorted_emails)
analyze_func(generate_emails, 10, list_of_domains, 1000000)
