def process_cities(filename):
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            # if 'quit' in line.lower():
            if 'quit' == line.lower():
                return
            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')

if __name__ == '__main__':
    import sys
    process_cities(sys.argv[1])


# python capitals.py cities.csv

# python -m pdb capitals.py cities.csv

# (Pdb) c
# (Pdb) s
# (Pdb) l
# (Pdb) b 6
# (Pdb) p line
# (Pdb) l 1