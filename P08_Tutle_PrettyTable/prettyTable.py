from prettyTable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikaachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)