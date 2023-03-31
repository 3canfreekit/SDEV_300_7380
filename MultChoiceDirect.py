
print("Welcome to the PythonProject4 application!")

print("Please choose an option to get started:")
print("1. Generate Secure Password")
print("2. Calculate and Format a Percentage")
print("3. How Many Day's From Today Until July 4, 2025?")
print("4. Use the Law of Cosines to Calculate the Leg of a Triangle")
print("5. Calculate the Volume of a Right Circular Cylinder")
print("6. Exit")

choice = int(input("Enter your choice (1-6): "))

if choice == 1:
  import Password
elif choice == 2:
  import Percentage
elif choice == 3:
  import Daystill4th
elif choice == 4:
  import Cosines
elif choice == 5:
  import Volume
elif choice == 6:
  print("Thank you for using the PythonProject4 application!")
  exit()
else:
  print("Invalid choice. Please try again.")