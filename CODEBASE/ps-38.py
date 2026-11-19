from datetime import datetime
import os

FILE_NAME = "diary.txt"


# Load notes from file
def load_notes():
    notes = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if "|" in line:
                    date, text = line.split("|", 1)

                    notes.append({
                        "date": date,
                        "text": text
                    })

    return notes


# Save notes to file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        for note in notes:
            file.write(
                note["date"] + "|" +
                note["text"] + "\n"
            )


# Validate date format
def validate_date(date):
    try:
        parsed = datetime.strptime(date, "%Y-%m-%d")
        return parsed.strftime("%Y-%m-%d") == date
    except ValueError:
        return False


# Add a new note
def add_note(notes):

    date = input("Enter date (YYYY-MM-DD): ").strip()

    if not validate_date(date):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    text = input("Enter note text: ").strip()

    if text == "":
        print("Note text cannot be empty.")
        return

    notes.append({
        "date": date,
        "text": text
    })

    save_notes(notes)

    print("Note saved.")


# View all notes
def view_notes(notes):

    if len(notes) == 0:
        print("No notes found. Your diary is empty.")
        return

    print("\n----- ALL NOTES -----")

    for i, note in enumerate(notes, start=1):
        print(
            i, "|",
            note["date"], "|",
            note["text"]
        )


# Search notes by keyword
def search_notes(notes):

    keyword = input("Enter keyword to search: ").strip()

    if keyword == "":
        print("Search keyword cannot be empty.")
        return

    count = 0

    for i, note in enumerate(notes, start=1):

        if keyword.lower() in note["text"].lower():

            if count == 0:
                print("\nSearch Results:")

            print(
                i, "|",
                note["date"], "|",
                note["text"]
            )

            count += 1

    if count == 0:
        print("No matching notes found.")

    else:
        print("Found", count, "notes")


# Delete a note
def delete_note(notes):

    if len(notes) == 0:
        print("No notes found. Your diary is empty.")
        return

    view_notes(notes)

    try:
        number = int(input("Enter note number to delete: "))

        if number < 1 or number > len(notes):
            print("Note number", number, "not found.")
            return

        notes.pop(number - 1)

        save_notes(notes)

        print(
            "Note", number,
            "deleted. Notes left:", len(notes)
        )

    except ValueError:
        print("Invalid note number.")


# Main menu
def main():

    notes = load_notes()

    while True:

        print("\n================================")
        print("   DIGITAL DIARY / NOTES MANAGER")
        print("================================")
        print("1. Add")
        print("2. View all")
        print("3. Search")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_note(notes)

        elif choice == "2":

            view_notes(notes)

        elif choice == "3":

            search_notes(notes)

        elif choice == "4":

            delete_note(notes)

        elif choice == "5":

            print("Thank you for using Digital Diary!")
            break

        else:

            print("Invalid menu option. Try again.")


# Program execution
if __name__ == "__main__":
    main()
