def complementDNA(sequence):

    DNA2 = {"A":"T","T":"A","G":"C","C":"G"}

    for i in DNA2.keys():
        for j in sequence:
            if i in j:
                print(DNA2.get(i))
    #     if i in sequence:
    #         sequence.replace("A","T")
        
    #     elif sequence == "T":
    #         sequence.replace("T","A")
        
    #     elif sequence == "G":
    #         sequence.replace("G","C")

    #     elif sequence == "C":
    #         sequence.replace("C","G")

    # return sequence

#driver code
Dna = input("Enter DNA sequence: ")
complementDNA(Dna)