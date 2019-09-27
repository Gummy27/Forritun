# ip = input('Ip/subnet here! : ')

ip = '192.168.2.1/26'
ip, subnet = ip.split('/')

mask = []
for x in range(32):
    if x >= int(subnet):
        mask.append('0')
    else:
        mask.append('1')

    if (x+1) % 8 == 0 and x != 31:
        mask.append('.')

mask = ''.join(mask)

for bits in mask.split('.'):
    hr = 0
    for seat, bit in enumerate(bits[::-1]):
        if bit == '1':
            hr += 2**seat
    print(hr, end=".")




