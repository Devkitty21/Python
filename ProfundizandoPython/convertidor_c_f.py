class ConvertidorTemperatura:

    # Definimos constantes
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls,celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura C demasiado alta: {celsius}')
        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls,fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura F demasiado alta: {fahrenheit}')
        return (fahrenheit-32) * 5/9

if __name__ == '__main__':
    resultado = ConvertidorTemperatura.c_f(15)
    print(f'15 C a F: {resultado:.2f}')
    resultado = ConvertidorTemperatura.f_c(213)
    print(f'100 F a C: {resultado:.2f}')