# Predicted roles and dates for weekly book club

user_members =
roles = input("")

people = ["Student1", "Student2", "Student3", "Student4"]

roles = ["Analyst", "Critic", "Artist", "Director"]

for x in range(1, 8):
  print("Day:", x)
  print("-------")
  print("Member:", people[0], "-", roles[0], "\nMember:", people[1], "-", roles[1], "\nMember:", people[2], "-", roles[2], "\nMember:", people[3], "-", roles[3])
  print("\n\n")
  people.append(people.pop(people.index(people[0])))
  
