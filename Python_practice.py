voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
i = 0
while i < len(voting_data):
    print(f"{(voting_data[i]['county'])} has {(voting_data[i]['registered_voters'])} registered voters.")
    i = 1 + i