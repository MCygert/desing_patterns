from iterator import WordsCollection

if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("Uno")
    collection.add_item("Dos")
    collection.add_item("Tres")

    print("Simple traversal")
    print("\n".join(collection))

    print("Reversed traversal")
    print("\n".join(collection.get_reverse_iterator()))
