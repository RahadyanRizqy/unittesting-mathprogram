class Operations:
    def __init__(self) -> None:
        pass

    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def substract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

    @staticmethod
    def factorialize(x):
        if x <= 1:
            return 1
        else:
            return x * Operations.factorialize(x-1)
        
print('=' * 25)
print('Operasi Matematika')
print('1. Jumlah \t [+]')
print('2. Kurang \t [-]')
print('3. Kali \t [*]')
print('4. Bagi \t [/]')
print('5. Faktorial \t [!]')
print('=' * 25)

global operasi
global bilangan_1, bilangan_2
operasi = input('Pilih operasi (1/2/3/4/5): ')
if not (1 <= int(operasi) <= 5):
    print('Tidak valid')
elif operasi == '5':
    bilangan_1 = eval(input('Masukkan bilangan: '))
else:
    bilangan_1 = eval(input('Masukkan bilangan pertama: '))
    bilangan_2 = eval(input('Masukkan bilangan kedua: '))

print('=' * 25)

add = Operations.add
substract = Operations.substract
multiply = Operations.multiply
divide = Operations.divide
factorialize = Operations.factorialize

if operasi == '1':
    hasil = add(bilangan_1, bilangan_2)
    print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
    hasil = substract(bilangan_1, bilangan_2)
    print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
    hasil = multiply(bilangan_1, bilangan_2)
    print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
    hasil = divide(bilangan_1, bilangan_2)
    print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
elif operasi == '5':
    hasil = factorialize(bilangan_1)
    print(f'Hasil faktorialisasi dari {bilangan_1} = {hasil}')