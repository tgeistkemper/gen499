#!/Users/tgeistkemper/anaconda3/bin/python3.7

user_sequence = input("Please enter a sequence: ")
print("Your sequence is: " + user_sequence)

nucleotide_list = list(user_sequence)
nucleotide_number = len(nucleotide_list)
print("Nucleotide count: " + str(nucleotide_number))

input_type = input("Enter DNA if DNA sequence of protein if protein sequence: ")
input_type = input_type.upper()

if input_type == "DNA":
	possible_sequences = 4 ** nucleotide_number
elif input_type == "PROTEIN":
	possible_sequences = 20 ** nucleotide_number

print(input_type, "sequences possible from sequence of length", str(nucleotide_number),":",str(possible_sequences))