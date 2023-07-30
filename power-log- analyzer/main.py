import re

def change_password(new_password):
    # Save the new password to a file (for example, a text file named "password.txt").
    with open('password.txt', 'w') as password_file:
        password_file.write(new_password)

def main():
    f = open('access.log')
    log_contents = filter(None, f.read().split('\n'))

    for line in log_contents:
        entries = re.findall(r'"([^"]*)"', line)
        url = entries[0].split(' ')[1]
        url_parts = url.split('?')

        if len(url_parts) > 1:
            query = url_parts[1]
            if query.find('password') > -1:
                print("Likely credentials found:")
                print(query)
                print("\n")
                # Here you can add an option to change the password
                change_option = input("Do you want to change the password? (yes/no): ").lower()
                if change_option == "yes":
                    new_password = input("Enter the new password: ")
                    change_password(new_password)
                    print("Password successfully changed!")
                    break  # Assuming you want to change the password only once.

if __name__ == "__main__":
    main()
