__author__ = 'SO'

if __name__ == "__main__":
    print "Calculating Expected Offspring(IEV task)"
    with open("datasets/iev") as f:
        couples = map(lambda x: int(x), f.readline().strip().split())
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    print sum([x[0] * x[1] for x in zip(couples, probabilities)]) * 2
