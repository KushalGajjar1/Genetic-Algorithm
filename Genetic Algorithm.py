import random


def find_value(population):
    population_size = len(population)
    values = []
    for i in range(population_size):
        value = 0
        for j in range(5):
            value = 2 * value + population[i][j]
        values.append(value)
    for i in range(population_size):
        values[i] = values[i] ** 2
    return values


def select_parent(population):
    population_size = len(population)
    values = find_value(population)
    average = 0.0
    for i in range(population_size):
        average = average + values[i]
    average = average / population_size
    actual_count = []
    for i in range(population_size):
        actual_count.append(round(values[i] / average))
    parent = []
    for i in range(population_size):
        for j in range(actual_count[i]):
            parent.append(population[i])
    random.shuffle(parent)
    return parent


def initialize_population(p):
    population_list = []
    for i in range(p):
        element = []
        for j in range(5):
            element.append(random.randint(0, 1))
        population_list.append(element)
    return population_list


def one_point_crossover(parent):
    size = len(parent)
    after_crossover = []
    crossover_point = 2
    for i in range(int(size / 2)):
        after_crossover.append(parent[2 * i][0:crossover_point] + parent[(2 * i) + 1][crossover_point: 6])
        after_crossover.append(parent[(2 * i) + 1][0:crossover_point] + parent[2 * i][crossover_point: 6])
    return after_crossover


def two_point_crossover(parent):
    size = len(parent)
    after_crossover = []
    point1 = 2
    point2 = 3
    for i in range(int(size / 2)):
        after_crossover.append(parent[2 * i][0:point1] + parent[(2 * i) + 1][point1:point2] + parent[2 * i][point2: 6])
        after_crossover.append(parent[(2 * i)+1][0:point1] + parent[2 * i][point1:point2] + parent[(2 * i)+1][point2: 6])
    return after_crossover


def bit_flip(after_crossover):
    size = len(after_crossover)
    for i in range(size):
        if after_crossover[i][4] == 1:
            after_crossover[i][4] = 0
        elif after_crossover[i][4] == 0:
            after_crossover[i][4] = 1
    return after_crossover


def swap_mutation(after_crossover):
    size = len(after_crossover)
    point1 = 2
    point2 = 3
    for i in range(size):
        temp = after_crossover[i][point2]
        after_crossover[i][point2] = after_crossover[i][point1]
        after_crossover[i][point1] = temp
    return after_crossover


def crossover_mutation(parent, c, m):
    after_crossover = []
    if c == 0:
        after_crossover = one_point_crossover(parent)
    elif c == 1:
        after_crossover = two_point_crossover(parent)
    after_mutation = []
    if m == 0:
        after_mutation = bit_flip(after_crossover)
    elif m == 1:
        after_mutation = swap_mutation(after_crossover)
    return after_mutation


def find_max(offspring):
    population_size = len(offspring)
    values = []
    for i in range(population_size):
        value = 0
        for j in range(5):
            value = 2 * value + population[i][j]
        values.append(value)
    return max(values)


if __name__ == '__main__':
    p = int(input("Enter the population size : "))
    population = initialize_population(p)

    c = 0
    c = int(input("Enter crossover type, 0 for one point or 1 for two point : "))

    m = 0
    m = int(input("Enter 0 for bit flip or 1 for swap mutation : "))

    t = int(input("Enter the termination condition t=0 for no improvement for x iteration or t=1 for predefined iteration for termination : "))

    ans = 0
    if t == 0:
        x = int(input("Enter x :"))
        flag = 0
        while (flag != x):

            parent = select_parent(population)
            offspring = crossover_mutation(parent, c, m)
            population = offspring

            if ans < find_max(offspring):
                flag = 0
                ans = find_max(offspring)
            elif ans >= find_max(offspring):
                flag = flag + 1

    elif t == 1:
        i = int(input("Enter i : "))
        for j in range (i):
            parent = select_parent(population)
            offspring = crossover_mutation(parent, c, m)
            population = offspring
        ans = find_max(population)

    print(ans)