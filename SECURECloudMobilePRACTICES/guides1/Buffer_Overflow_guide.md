## Buffer Overflow Guide

Um buffer overflow ocorre quando são colocados num buffer dados que excedam a sua capacidade. Este facto ocorre em programas concretizados em C ou C++, uma vez que estas linguagens de programação não verificam se os limites dos buffers são violados.

De modos a evitar este tipo de vulnerabilidade torna-se necessário adotar uma programação defensiva que deverá consistir em:
 * Verificar sempre os limites do buffer;
 * Evitar a utilização de funções perigosas que não fazem a verificação dos limites de buffer (e.g., gets, strcpy, sprintf, scanf, strcat);
 * Utilizar as versões mais seguras das funções anteriores, tais como strbcpy, strncat e snprintf;
 * Ter muito cuidado ao utilizar variáveis de ambiente tais como os dados retornados pela função getenv.

**Nota**
Adicionalmente, o programador deve utilizar de forma correta de funções de bibliotecas, de acordo com o seu nível de perigosidade intrínseco (e.g., stdin).

## Not addressing this requirement may lead to vulnerabilities explored by attacks such as:

 * Buffer overflow: Buffer overflows is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory. It can be triggered by non-validated inputs that are designed to execute code.
