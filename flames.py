print("FLAMES game ")
userinp1 = input("Enter the first person's name: ").lower().replace(" ", "")
userinp2 = input("Enter the second person's name: ").lower().replace(" ", "")

userinputs1 = list(userinp1)
userinputs2 = list(userinp2)

common_chars = set(userinputs1) & set(userinputs2)
userinputs1 = [char for char in userinputs1 if char not in common_chars]
userinputs2 = [char for char in userinputs2 if char not in common_chars]

count = len(userinputs1) + len(userinputs2)

categories = ["Friend", "Love", "Affection", "Marriage", "Enemies", "Siblings"]

result = categories[count % len(categories)]

print(f"FLAMES game result: {result}")
