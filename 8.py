import csv

try:
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    with open("user_data.txt", "w") as file:   
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")

    print("Data written to user_data.txt")

    with open("user_data.txt", "r") as file:
        content = file.read()
        print("\nFile Contents:")
        print(content)

    city = input("Enter your city: ")
    with open("user_data.txt", "a") as file:
        file.write(f"City: {city}\n")

    print("City appended successfully.")

except Exception as e:  
    print("File error occurred:", e)



try:
    with open("students.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        
        writer.writerow(["ID", "Name", "Marks"])

        writer.writerow([101, "Afshan", 88])
        writer.writerow([102, "Deeksha", 92])
        writer.writerow([103, "Rahul", 75])

    print("\nCSV file created successfully.")

    print("\nReading CSV Data:")
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

except Exception as e:
    print("CSV error occurred:", e)

