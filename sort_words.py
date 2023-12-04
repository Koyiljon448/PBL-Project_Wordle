def main():
    # Open the input file
    try:
        with open("c:/users/user/OneDrive/Рабочий Стол/PBL project/words.txt", "r") as input_file:
            words = input_file.read().split()
    except FileNotFoundError:
        print("Error: Could not open input file.")
        return 1

    # Sort the words based on their length
    sorted_words = sorted(words, key=len)

    # Open the output file
    try:
        with open("c:/users/user/onedrive/рабочий стол/PBL Project/words(sorted).txt", "w") as output_file:
            # Write the sorted words to the output file
            output_file.write(" ".join(sorted_words))
    except IOError:
        print("Error: Could not open output file.")
        return 1

    print("Words sorted and written to output.txt.")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
