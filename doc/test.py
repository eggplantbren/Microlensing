# Quick Python test to make sure I got my derivation correct
from pylab import *

seed(0)
# Some data
N = 101
t = linspace(0, 10, N)
sig = -log(rand(N))
mprime = sin(t)
y = mprime + sig*randn(N)
errorbar(t, y, yerr=sig, fmt='b.')
show()

# Stuff derived from the data
logC = -0.5*N*log(2*pi) - sum(log(sigma))

# Conditional on b
def log_likelihood(b):
	chisq = sum((y - (mprime + b))**2)
	return logC - 0.5*chisq

# Marginalised over b
def log_likelihood():
	pass

