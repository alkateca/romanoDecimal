# romanoDecimal

Conversão de número Romano para Inteiro

Os algarismos romanos são representados por sete símbolos diferentes: I, V, X, L, C, D e M.

| Símbolo | Valor |
|---------|-------|
| I       | 1     |
| V       | 5     |
| X       | 10    |
| L       | 50    |
| C       | 100   |
| D       | 500   |
| M       | 1000  |

Por exemplo, 2 é escrito como II em algarismos romanos, que é simplesmente I + I. 12 é escrito como XII, que é simplesmente X + II. O número 27 é escrito como XXVII, que é XX + V + II.

Os algarismos romanos são geralmente escritos do maior para o menor, da esquerda para a direita. No entanto, o algarismo para quatro não é IIII. Em vez disso, o número quatro é escrito como IV. Como o um está antes do cinco, nós o subtraímos, resultando em quatro. O mesmo princípio se aplica ao número nove, que é escrito como IX. Há seis casos em que a subtração é usada:

I pode ser colocado antes de V (5) e X (10) para fazer 4 e 9.
X pode ser colocado antes de L (50) e C (100) para fazer 40 e 90.
C pode ser colocado antes de D (500) e M (1000) para fazer 400 e 900.

Dado um numeral romano, converta-o em um inteiro.

Exemplo 1:

Entrada: s = "III"
Saída: 3
Explicação: III = 3.

Exemplo 2:

Entrada: s = "LVIII"
Saída: 58
Explicação: L = 50, V= 5, III = 3.

Exemplo 3:

Entrada: s = "MCMXCIV"
Saída: 1994
Explicação: M = 1000, CM = 900, XC = 90 e IV = 4.
