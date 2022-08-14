# most repeated char in a sentence

def most_repeated_character(sentence):
    mapping = {}

    for letter in sentence:
        if letter != " ":
            if letter not in mapping:
                mapping[letter] = 1
            else:
                mapping[letter] += 1

    most_repeated = sorted(mapping.items(), key=lambda x: x[1], reverse=True)

    print(f"{most_repeated[0][0]} is repeated {most_repeated[0][1]} times.")

    # most_repeated_times = 0
    # most_repeated_letter = ""

    # for letter, repeated in mapping.items():
    #     if (repeated > most_repeated_times):
    #         most_repeated_times = repeated
    #         most_repeated_letter = letter

    # print(f"{most_repeated_letter} is repeated {most_repeated_times} times.")


sample_sentence = "This is a common interview question "
most_repeated_character(sample_sentence)
