import re


def has_abba(sequence):
    return any(
        a != b and a + b == d + c
        for a, b, c, d in zip(sequence, sequence[1:], sequence[2:], sequence[3:])
    )


def supports_tls(ip):
    parts = re.split(r"\[|\]", ip)
    supernets = parts[::2]
    hypernets = parts[1::2]

    return any(has_abba(part) for part in supernets) and not any(
        has_abba(part) for part in hypernets
    )


def count_tls_ips(filename):
    with open(filename, "r") as file:
        ips = file.read().splitlines()

    return sum(supports_tls(ip) for ip in ips)


print(count_tls_ips("input.txt"))
