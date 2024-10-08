import Calculator
import BookStore
import DLList

def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is an invalid expression")

def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option == "6":
            best_seller = bookStore.getCartBestSeller()
            if best_seller:
                print(f"Best-seller in cart: {best_seller}")
            else:
                print("No books are added to the shopping cart.")

        ''' 
        Add the menu options when needed
        '''
def is_palindrome_test(expression):
    dll = DLList.DLList()
    for char in expression:
        dll.append(char)
    if dll.isPalindrome():
        print("Palindrome")
    else:
        print("Not a palindrome")


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            expression = input("Enter a word/phrase to check if it's a palindrome: ")
            result = is_palindrome_test(expression)
            print(result)
        elif option == "6":
            best_seller = bookStore.getCartBestSeller()
            if best_seller:
                print(f"Best-seller in cart: {best_seller}")
            else:
                print("No Books are added to the Shopping Cart...")

if __name__ == "__main__":
    main()