def population_change(filename):
    population_data = {}
    with open(filename, "r") as f:
        for line in f:
            country, year, population = line.strip().split(",")
            if country not in population_data:
                population_data[country] = {}
            population_data[country][int(year)] = int(population)
    result = {}
    for country, data in population_data.items():
        years = sorted(data.keys())
        population_changes = []
        for i in range(len(years) - 1):
            year1 = years[i]
            year2 = years[i+1]
            population1 = data[year1]
            population2 = data[year2]
            population_change = population2 - population1
            population_changes.append((year1, year2, population_change))
        result[country] = population_changes
    return result

print(population_change('Test information.txt'))