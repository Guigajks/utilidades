if __name__ == '__main__':
    parsed_cpfs = []

    with open('./cpfs.txt', 'r') as f:
        cpfs = f.readlines()
        
        for cpf in cpfs:
            cpf = cpf.strip('\n')
            cpf = cpf.zfill(11)
            cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}\n'

            parsed_cpfs.append(cpf)

    with open('./parsed_cpfs.txt', 'w') as f:
        f.write(''.join(parsed_cpfs))

    print('Cpfs parseados')
