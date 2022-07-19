import scipy
def build_population(N , p):
    """
    N es el numero de indiduos y p la probalidad 
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p: 
            allele2 = "a"
        population.append((allele1, allele2))
    return population 

def compute_frequencies(population):
    """ 
    Se cuenta los geneotipos
    """
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return ({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})


def reproduce_population(population):
    """ 
    Crea nueva generación al azar 
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        new_generation.append(offspring)
        
     
    return new_generation


