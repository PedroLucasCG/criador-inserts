# Criador de Inserts

## Criador de inserts para auxiliar no teste de tabelas, principalmente em views com mais de algumas tabelas.

### Modo de uso

0 - Preencha o dotenv com sua credenciais de acesso ao banco de dados.

1 - Se você possuir chaves estrageiras coloque as no arquivo "fkidValues.txt" no formato: nome_da_chave:valor_chave_primaria. Obs.: não precisa ser o mesmo que está no banco de dados.

2 - Caso você não tenha chaves primárias apenas execute main.py e selecione para gerar as chaves, escolhendo int ou uuid para ser o tipo de chave que deseja.
