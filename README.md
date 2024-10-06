# Criador de Inserts

## Criador de inserts para auxiliar no teste de tabelas, principalmente em views com mais de algumas tabelas.

### Modo de uso

0 - Preencha o dotenv com suas credenciais de acesso ao banco de dados.

1 - Se você possuir chaves estrageiras coloque as no arquivo "fkidValues.txt" no formato: nome_da_chave:valor_chave_primaria. Obs.: não precisa ser o mesmo que está no banco de dados.

2 - Agora vá no arquivo "fknames.txt" e insira entradas nesse formato: tabela>chave1,chave2=valor_chave_primaria1,valor_chave_primaria_2

3 - Execute main.py e selecione para gerar as chaves, escolhendo int ou uuid para ser o tipo de chave que deseja.
