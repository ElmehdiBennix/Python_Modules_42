from DiamondTrap import King


def main() -> None:

    try:
        print(King.__mro__)
        
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)
    except TypeError as error:
        print(f"King Error: {error}")
        
if __name__ == "__main__":
    main()
