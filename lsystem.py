rules = { 'A': '[A]A'}
axiom = 'A'

def successor(rules, axiom):
    output = []
    for token in axiom:
        if token in rules:
            output.append(rules[token])
    return ''.join(output)

output = axiom
for _ in range(5):
    output = successor(rules, output)
    print(output)
