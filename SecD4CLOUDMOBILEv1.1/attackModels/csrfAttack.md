# Cross Site Request Forgery Attacks
O Cross Site Request Forgery (CSRF) é um ataque que força um utilizador final a executar acções indesejadas numa aplicação na qual está autenticado  naquele momento.

## Definition
Este tipo de ataque tem como finalidade a mudança de estado e não o roubo de dados, dado que o  invasor fica impedido de ver a resposta à solicitação falsificada. A condição
necessária para que este tipo de ataque tenha sucesso é a existência da permissão de alterações através de solicitações GET.

## Technical Impact
* Bypass Protection Mechanism;
* Gain Privileges;
* DoS: Crash, Exit, or Restart;
* Read and Modify Data.

## Risk Analysis
* High.

## Likelihood of Exploit
* High.

## Attacker's Powers
* Furtar valores monetários de forma simulada;
* Realização de outros tipos de ataques;
* Acesso a dados confidenciais (histórico da vítima) ou criticos (número de cartão de crédito) do utilizador.

## Recommendations
In order to ensure that the mobile application is resilient or immune to the CSRF attacks, it is recommended 
that the measures described in the good practice report and the security tests present in the full report are followed.

## References
1. [https://capec.mitre.org/data/definitions/62.html];
2. [https://cwe.mitre.org/data/definitions/352.html]
