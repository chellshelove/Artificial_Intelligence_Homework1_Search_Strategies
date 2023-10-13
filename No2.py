import random

NAN = 2147483647
V = 7
GENES = "ABCDEFG"

class Individual:
    def __init__(self, gnome=None):
        if gnome is None:
            self.gnome = random.sample(range(1, V), V - 1)
        else:
            self.gnome = gnome
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness

def calculate_fitness(gnome, graph):
    f = 0
    starting_point = 0
    for gene in gnome:
        if graph[starting_point][gene - 1] == NAN:
            return NAN
        f += graph[starting_point][gene - 1]
        starting_point = gene - 1
    f += graph[starting_point][0]  # Return to the starting point
    return f

def genetic_tsp(graph, pop_size, max_gen):
    population = [Individual() for _ in range(pop_size)]

    for individual in population:
        individual.fitness = calculate_fitness(individual.gnome, graph)

    population.sort()

    for gen in range(max_gen):
        new_population = []

        for i in range(pop_size):
            p1 = population[i]
            new_g = list(p1.gnome)
            r = random.randint(0, V - 2)
            r1 = random.randint(0, V - 2)
            if r != r1:
                new_g[r], new_g[r1] = new_g[r1], new_g[r]

            new_individual = Individual(new_g)
            new_individual.fitness = calculate_fitness(new_individual.gnome, graph)

            if new_individual.fitness <= population[i].fitness:
                new_population.append(new_individual)
            else:
                new_population.append(population[i])

        population = new_population
        population.sort()

    best_individual = population[0]

    print("Best Route:", gnome_to_cities(best_individual.gnome))
    print("Shortest Distance:", best_individual.fitness)

def gnome_to_cities(gnome):
    cities = "A -> "
    for gene in gnome:
        cities += GENES[gene - 1] + " -> "
    cities += "A"
    return cities

if __name__ == '__main__':
    graph = [
        [0, 12, 10, NAN, NAN, NAN, 12],
        [12, 0, 8, 12, NAN, NAN, NAN],
        [10, 8, 0, 11, 3, NAN, 9],
        [NAN, 12, 11, 0, 11, 10, NAN],
        [NAN, NAN, 3, 11, 0, 6, 7],
        [NAN, NAN, NAN, 10, 6, 0, 9],
        [12, NAN, 9, NAN, 7, 9, 0],
    ]
    genetic_tsp(graph, 10, 100)