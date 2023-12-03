clean_words = ['at', 'the', 'base', 'of', 'fossil', 'butte', 'are', 'the', 'bright', 'red', 'purple', 'yellow', 'and', 'gray', 'beds', 'of', 'the', 'wasatch', 'formation', 'eroded', 'portions', 'of', 'these', 'horizontal', 'beds', 'slope', 'gradually', 'upward', 'from', 'the', 'valley', 'floor', 'and', 'steepen', 'abruptly', 'overlying', 'them', 'and', 'extending', 'to', 'the', 'top', 'of', 'the', 'butte', 'are', 'the', 'much', 'steeper', 'buff-to-white', 'beds', 'of', 'the', 'green', 'river', 'formation', 'which', 'are', 'about', '300', 'feet', 'thick']

occurence = [len(word) for word in clean_words]

# Vytvoření množiny unikátních délek
unique_lengths = set(occurence)

max_occurrence_count = 0

# Pro každou délku v množině
for length in unique_lengths:
    # Spočítat počet výskytů této délky v původním seznamu
    count = occurence.count(length)

    # Pokud je aktuální počet větší než dosavadní maximální
    if count > max_occurrence_count:
        max_occurrence_count = count

print(f"Max occurrence count: {max_occurrence_count}")

#zkrácený tvar:
#clean_words = ['at', 'the', 'base', 'of', 'fossil', 'butte', 'are', 'the', 'bright', 'red', 'purple', 'yellow', 'and', 'gray', 'beds', 'of', 'the', 'wasatch', 'formation', 'eroded', 'portions', 'of', 'these', 'horizontal', 'beds', 'slope', 'gradually', 'upward', 'from', 'the', 'valley', 'floor', 'and', 'steepen', 'abruptly', 'overlying', 'them', 'and', 'extending', 'to', 'the', 'top', 'of', 'the', 'butte', 'are', 'the', 'much', 'steeper', 'buff-to-white', 'beds', 'of', 'the', 'green', 'river', 'formation', 'which', 'are', 'about', '300', 'feet', 'thick']

#occurence = [len(word) for word in clean_words]

#max_occurrence_count = max(occurence.count(length) for length in set(occurence))
#print(max_occurrence_count)