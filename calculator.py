
class Operation:

    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b

    @staticmethod
    def multiplica(a, b):
        return a * b

    @staticmethod
    def divisao(a, b):
        if b != 0:
            return a / b
        else:
            return 'ERROR'
