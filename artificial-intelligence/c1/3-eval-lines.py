def count_correct_lines(reference_file, output_file):
    with open(reference_file, encoding="utf-8") as f:
        ref_lines = [line.strip() for line in f if line.strip()]
        
    with open(output_file, encoding="utf-8") as f:
        out_lines = [line.strip() for line in f if line.strip()]    
    
    correct = sum(1 for ref, out in zip(ref_lines, out_lines) if ref == out)
    total = len(ref_lines)
    return correct, total

correct_longest, total_longest = count_correct_lines("pantad_orig_cleaned.txt", "zad3_output_algo.txt")
correct_random, total_random = count_correct_lines("pantad_orig_cleaned.txt", "zad3_output_random.txt")
correct_random_jednolite, total_random_jednolite = count_correct_lines("pantad_orig_cleaned.txt", "zad3_output_random-jednolite.txt")

print("Algorytm preferujący najdłuższe słowa:")
print(f"Poprawnych linii: {correct_longest} / {total_longest}")

print("\nAlgorytm losowy wazony:")
print(f"Poprawnych linii: {correct_random} / {total_random}")

print("\nAlgorytm losowy jednolity:")
print(f"Poprawnych linii: {correct_random_jednolite} / {total_random_jednolite}")