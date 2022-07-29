string  = "AASDASDDAAAAAAAAERQREQREQRAAAAREWQRWERAAA"
count   = 0
pattern = "AA"
while pattern in string:
    count += 1
    pattern += "AA"
print(count)
print(pattern)
