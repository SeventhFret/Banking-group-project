# GROUP BANKING PROJECT

1. Banking Project - in Groups
   - with presentation! (excalidraw or similar)
   - has to include classes, objects, methods, attributes, super() and inheritance
   - User wants to: 
      1. access his bank account,
      2. deposit money, 
      3. withdraw money, 
      4. see balance, 
      5. be able to create new accounts,
      6. be able to go into the red


> For colorful output open Terminal and paste the command: \
`pip3 install string-color`

## Quick explination for the user:
   - This code allows the user to creat a new account in the bank and:
      1. Enter a new user name 
      2. Enter a new password with this characteristics:
      -> At least one digit [0-9]
      -> At least one lowercase character [a-z]
      -> At least one uppercase character [A-Z]
      -> At least one special character [#?!@$%^&*-/.]
      -> At least 8 characters in length, but no more than 32.
      3. Then it returns a random IBAN and waits for an user input for Menu acces.
      4. MENU:
            [1] - balance
               ### return and stored your money balance. 
            [2] - withdraw 
               ### withdraw money and deduct it from money balance.
            [3] - deposit
               ### deposit money in your bank account and adds it to your money balance
            [4] - statement
               ### returns a HISTORY of all your money transactions
            [x] - exit 
               ### exit de bank menu.