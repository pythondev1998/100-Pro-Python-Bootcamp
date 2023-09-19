from data.create_tables import create_tables
from view.console_view import ConsoleView

def main():
    create_tables()
    view = ConsoleView()
    view.run()

if __name__ == "__main__":
    main()
