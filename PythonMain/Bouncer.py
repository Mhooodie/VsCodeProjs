def enter_club(name: str, age: int, has_id: bool) -> None:
    if name.lower() == "bob":
        print("GET OUT OF HERE BOB!")
        return
    if age >= 21 and has_id: # No need to put has_id == true 
        print("You may enter the club.")
    else:
        print("You may not enter the club.")

def main() -> None:
    enter_club("Bob", 29, has_id=True)
    enter_club("Amy", 25, has_id=True)
    enter_club("Darrel", 20, has_id=True)
    enter_club("Lily", 24, has_id=False)

if __name__ == "__main__":
    main()