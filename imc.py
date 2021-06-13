class IMC:
    """
    Cálculo do IMC baseado em OO
    """
    def __init__(self, peso=80, altura=1.65):
        """
        Construtor de objetos IMC para cálculo do IMC de cada objeto.

        Args:
            peso (int, optional): Peso da pessoa. Padrão 80.
            altura (float, optional): Altura da pesso. Padrão 1.65.
        """
        self.peso = peso
        self.altura = altura
        self.imc = self.calculo()
    
    def calculo(self):
        """
        Método para cálculo do IMC
        """
        return self.peso / (self.altura * self.altura)