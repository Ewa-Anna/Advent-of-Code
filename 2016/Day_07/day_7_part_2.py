import re

def has_aba(sequence):
    return {a + b + a for a, b, c in zip(sequence, sequence[1:], sequence[2:]) if a == c and a != b}


def supports_ssl(ip):
    parts = re.split(r'\[|\]', ip)
    supernets = parts[::2]  
    hypernets = parts[1::2] 
    
    abas = set()
    for part in supernets:
        abas.update(has_aba(part))
    
    for part in hypernets:
        for aba in abas:
            bab = aba[1] + aba[0] + aba[1] 
            if bab in part:
                return True
    
    return False

def count_ssl_ips(filename):
    with open(filename, 'r') as file:
        ips = file.read().splitlines()
    
    return sum(supports_ssl(ip) for ip in ips)

print(count_ssl_ips('input.txt'))
