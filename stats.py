def word_count(text):
    list = text.split()
    return len(list)

def character_count(text):
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_character_count(char_counts):
    # make the dictionary with a list two key-valued pairs. char and num
    sorted_char_count = []
    for ch, count in char_counts.items():
        if ch.isalpha(): #keep only letters
            sorted_char_count.append({"char": ch, "num": count})
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count

def sort_on(n): #helper function. It takes the dictionary in the list spot and returns the value for the num key
    return n["num"]

