class PDA:
    def __init__(self):
        
        self.stack = []
        self.state = 'q0'

    #Başlangıç durumu.
    def state_q0(self, symbol):
        """Durum q0 için geçiş fonksiyonu"""
        if symbol.isdigit():
            self.state = 'q1'
        elif symbol == '(':
            self.stack.append(symbol)
        elif symbol.isspace():
            pass  
        else:
            self.state = 'qf'

    #Bir rakam gördüğünde geçilen durum.
    def state_q1(self, symbol):
        """Durum q1 için geçiş fonksiyonu"""
        if symbol in  ['+', '-', '*', '/']:
            self.state = 'q2'
        elif symbol == ')':
            if self.stack and self.stack[-1] == '(':
                self.stack.pop()
            else:
                self.state = 'qf'
        elif symbol.isspace():
            pass 
        else:
            self.state = 'qf'

    #Bir operatör görüldüğünde geçilen durum.
    def state_q2(self, symbol):
        """Durum q2 için geçiş fonksiyonu"""
        if symbol.isdigit():
            self.state = 'q1'
        elif symbol == '(':
            self.stack.append(symbol)
        elif symbol.isspace():
            pass  # Boşlukları yok say
        else:
            self.state = 'qf'

    #Durumlar arası geçişi sağlayan fonksiyon.
    def transition(self, symbol):
        if self.state == 'q0':
            self.state_q0(symbol)
        elif self.state == 'q1':
            self.state_q1(symbol)
        elif self.state == 'q2':
            self.state_q2(symbol)
        
    #İfadenin geçerliliğini kontrol eden fonksiyon.
    def is_valid(self, expression):
        for symbol in expression:
            self.transition(symbol)
            if self.state == 'qf':
                return False

        return self.state == 'q1' and not self.stack


# Kullanıcıdan matematiksel ifadeleri al ve geçerliliğini kontrol et
def main():
    while True:
        expression = input(
            "Matematiksel ifadeyi giriniz (çıkmak için 'q' tuşuna basınız): ")
        if expression.lower() == 'q':
            break

        pda = PDA()
        result = pda.is_valid(expression)
        print(f"İfade: {expression} {'geçerli' if result else 'geçersiz'}")


if __name__ == "__main__":
    main()
