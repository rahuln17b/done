import scipy.stats as stats

prob = stats.binom.pmf(3, 10, 0.5)
print("Probability of getting 3")
print(prob)

prob2 = 1 - stats.binom.pmf(0, n=10, p=.5)- stats.binom.pmf(1, n=10, p=.5) -stats.binom.pmf(2, n=10, p=.5)
print("prob of more than 2 heads")
print(prob2)