#Menu Design
from functions import searching_a_neighborhood
from functions import adding_new_neighborhood
print("\tThis is your menu "
      "\n\t1. Search for a neighborhood" 
      "\n\t2. List them"
      "\n\t3. Add"
      "\n\t4. Delete a neighborhood"
      "\n\t5. Update a neighborhood"
      "\n\t6. Moving a neighborhood"
      "\n\t7. Plot the number of neighborhoods"
      "\n\t8. Analyzing"
      "\n\t0. Exit")
try:
      choice=int(input("Make a choice: "))
      if choice>=8:
            pass
except ValueError:
      print("An exception occured")

if choice ==1:
            print("Search 1.1=")
elif choice==3:
        adding_new_neighborhood()