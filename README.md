# controle de serviços 

1. Documentação
2. justificativas
3. deploy

## Documentação
### minimundo
O planejamento portuário precisa organizar os Serviços na operação e movimentação do navio. Com o grande volume de Serviços, continuar controlando em planilhas é um trabalho mais demorado e você também não consegue ter uma base de dados centralizada alinhadas com outras necessidades do negócio.

Até o momento temos 4 serviços: Cabotagem, Granito, Gusa e Siderúrgico e todo serviço é associado a um navio já contratado. Alinhe o escopo de dados para o cadastro do Serviço.

O desejo de solução é um tipo de ficha, onde o usuário terá que inserir os seguintes dados de cada Controle de Serviço ao ser cadastrado: Mês, Ano, Nome Porto Embarque, Nº Ordem Venda, Nome Cliente, Nome Porto Destino, Nome Navio, Nome Usina, Nome Serviço e Quantidade Orçada [toneladas].

|Nome servico|Mês|Ano| Porto embarque | Porto destino | Ordem venda | Cliente  | Nome navio |  Nome usina |  qte Orçada |
|---|---|---|---|---|---|---|---|---|---|
| Cabotagem |  07 | 2020  | Santos | Recife  | 0100AB  | ServiceLTDA |  Perola negra | Usina 1 | 15 |
| Granito |  07 | 2020 | Vitória | Santos | 27BC  | CenterLTDA | Holandes voador | Usina 2  | 4,5  |
| Gusa  |  07 | 2020 | Recife | Vitória  |  0007 | MainSA | Titanic  |  Usina 3 | 24 |

Ter as opções de cadastro caso não exista: Navio[nome, IMO], Porto Embarque[nome, país], Porto Destino[nome, país], Cliente[nome] e Usina[nome].

### modelagem

