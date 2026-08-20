"""2. Show Menu — Print each item with its price, nicely formatted, numbered so customers can select by number."""

store_hours = ("8:00 AM","6:00 PM") #Fixed store hours between 8:00 AM - 6:00 PM
menu = {"Latte" : 4.50, "Cappuccino" : 4.00, "Muffin" : 3.00, "Bagel" : 2.75, "Croissant" : 3.25} #Menu as a dictionary mapped with there prices
menu_allergens = {"dairy","gluten","eggs","dairy"} #I created a set of allergens but it is not yet specified to what menu does it belong

equal_sign = "="
space = " "

welcome_banner = f"""{equal_sign.center(40, equal_sign)}
{space.ljust(4,space)}"☕ Welcome to PyBrew Café! ☕"
{equal_sign.center(40, equal_sign)}
Open: {store_hours[0]} - {store_hours[1]}"""

print(welcome_banner)

"""Greet the customer and print the store hours. Ask if they're a loyalty member and store the answer as a boolean. Run a loop that shows the menu and lets them keep adding items. 
Use match to handle their command: order more, checkout, or quit. On checkout, calculate the total, print the receipt, and end the loop."""





"""Sample Output 1

==========================================
   ☕ Welcome to PyBrew Café! ☕
==========================================
Open: 8:00 AM - 6:00 PM

Are you a loyalty member? (y/n): y

--- MENU ---
1. Latte ........... $4.50
2. Cappuccino ....... $4.00
3. Muffin ........... $3.00
4. Bagel ............ $2.75
5. Croissant ........ $3.25

Enter item number: 1
Latte added to cart. 🧾
Add another item? (y/n): y

--- MENU ---
1. Latte ........... $4.50
2. Cappuccino ....... $4.00
3. Muffin ........... $3.00
4. Bagel ............ $2.75
5. Croissant ........ $3.25

Enter item number: 3
Muffin added to cart. 🧾
Add another item? (y/n): y

--- MENU ---
1. Latte ........... $4.50
2. Cappuccino ....... $4.00
3. Muffin ........... $3.00
4. Bagel ............ $2.75
5. Croissant ........ $3.25

Enter item number: 9
❌ Invalid item number. Please try again.
Add another item? (y/n): n

Checking out...

==========================================
            🧾 RECEIPT 🧾
==========================================
1x Latte  ........... $4.50
1x Muffin ........... $3.00
------------------------------------------
Subtotal:            $7.50
Tax (8%):             $0.60
Loyalty Discount:    -$0.00  (subtotal under $10, no discount applied)
------------------------------------------
TOTAL:                $8.10
------------------------------------------
⚠️  Contains allergens: dairy, eggs, gluten

Thanks for visiting PyBrew Café! ☕ Come again soon!
==========================================

Sample Output 2

==========================================
   ☕ Welcome to PyBrew Café! ☕
==========================================
Open: 8:00 AM - 6:00 PM

Are you a loyalty member? (y/n): y

--- MENU ---
1. Latte ........... $4.50
2. Cappuccino ....... $4.00
3. Muffin ........... $3.00
4. Bagel ............ $2.75
5. Croissant ........ $3.25

Enter item number: 1
Latte added to cart. 🧾
Add another item? (y/n): y

--- MENU ---
1. Latte ........... $4.50
2. Cappuccino ....... $4.00
3. Muffin ........... $3.00
4. Bagel ............ $2.75
5. Croissant ........ $3.25

Enter item number: 2
Cappuccino added to cart. 🧾
Add another item? (y/n): y

--- MENU ---
1. Latte ........... $4.50
2. Cappuccino ....... $4.00
3. Muffin ........... $3.00
4. Bagel ............ $2.75
5. Croissant ........ $3.25

Enter item number: 5
Croissant added to cart. 🧾
Add another item? (y/n): n

Checking out...

==========================================
            🧾 RECEIPT 🧾
==========================================
1x Latte      ........... $4.50
1x Cappuccino ........... $4.00
1x Croissant  ........... $3.25
------------------------------------------
Subtotal:              $11.75
Tax (8%):               $0.94
Loyalty Discount:      -$1.18  (10% off, member + subtotal over $10)
------------------------------------------
TOTAL:                 $11.51
------------------------------------------
⚠️  Contains allergens: dairy, gluten

Thanks for visiting PyBrew Café! ☕ Come again soon!
=========================================="""