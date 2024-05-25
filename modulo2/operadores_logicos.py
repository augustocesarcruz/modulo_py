# AND = para ser TRUE tudo tem que ser TRUE
# OR = para ser TRUE apenas um tem que ser TRUE

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


# OPERADOR E
# SE HOUVER ALGUM FALSO NO OPERADOR, ENTÃO SERÁ FALSO

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite

# OPERADOR OU
# APENAS 1 PRECISA SER VERDADEIRO

saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite


##################################

saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp = (saldo >= saque and saque <= limite) or (conta_especial and saque >= saque)
print(exp)