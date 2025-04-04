from menu import show_main_menu

def main():
    try:
        students = []
        show_main_menu(students)
    except Exception as e:
        print("\nAn error occurred:", str(e))
        print("Please try again.")

if __name__ == "__main__":
    main()