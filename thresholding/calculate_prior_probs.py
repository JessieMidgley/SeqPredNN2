def calculate_probabilities(class_freq, total_samples):
    probabilities = []
    for value in class_freq.values():
        prob = value/total_samples     
        probabilities.append(prob)
    print("Prior probabilities:", probabilities)


def txt_to_data(file):
    class_freq = {}
    with open(file) as data:
        for line in data:
            k, v = line.strip().split('  ')
            class_freq[k] = int(v)
    print("Frequencies: ", class_freq)
    total_samples = sum(class_freq.values())
    calculate_probabilities(class_freq, total_samples)


txt_to_data('../counting_residues/res_dict.txt')



