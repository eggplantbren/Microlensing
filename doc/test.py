# Quick Python test to make sure I got my derivation correct
from pylab import *

# Some data
seed(0)
N = 101
t = linspace(0, 10, N)
sig = -log(rand(N))
mprime = sin(t)
y = mprime + sig*randn(N)
errorbar(t, y, yerr=sig, fmt='b.')
show()

# Stuff derived from the data
C = prod(1./sig)*(2*pi)**(-0.5*N)
alpha = sum((y - mprime)**2/sig**2)
beta = -2.*sum((y - mprime)/sig**2)
gamma = sum(1./sig**2)

# For the numerical marginalisation
b = linspace(-20, 20, 10001)
L = b.max() - b.min()

# If b is given, it's conditional on b
# otherwise, it's marginalised over b
def log_likelihood(b=None):
	if b is not None:
		chisq = sum((y - (mprime + b))**2/sig**2)
		return log(C) - 0.5*chisq

# The numerical marginalisation
logL = zeros(len(b))
for i in range(0, len(b)):
	logL[i] = log_likelihood(b[i])
print(trapz(exp(logL)/L, x=b))

# The analytical marginalisation
result = C/L*exp(-0.5*gamma*(alpha/gamma - beta**2/4/gamma**2))*sqrt(2*pi/gamma)
print(result)

