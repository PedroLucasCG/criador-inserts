# Criador de Inserts

## Criador para auxiliar no teste de tabelas, principalmente em views com mais de algumas tabelas.

### Modo de uso

1 - Se você possuir chaves estrageiras coloque as no arquivo "fkidValues.txt" no formato: nome_da_chave:valor_chave_primaria. Obs.: não precisa ser o mesmo que está no banco de dados. \n
2 - Caso você não tenha chaves primárias apenas execute main.py e selecione para gerar as chaves, escolhendo int ou uuid para ser o tipo de chave que deseja.
