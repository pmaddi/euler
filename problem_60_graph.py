'''
I didnt write this
but it's cool
'''
import sympy.ntheory as spn
import networkx as nx

prime_range = list(spn.generate.primerange(1, 10000))

G = nx.Graph()
for prime in prime_range:
    G.add_node(prime)
for prime1 in prime_range:
    for prime2 in prime_range:
        if prime2 > prime1:
            concatenated = [int(str(prime1) + str(prime2))] + [int(str(prime2) + str(prime1))]
            if all([spn.isprime(x) for x in concatenated]):
                G.add_edge(prime1, prime2)

print(min([sum(l) for l in nx.find_cliques(G) if len(l) == 5]))
