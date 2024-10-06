INSERT INTO
    Pessoa (
        idPessoa,
        nome,
        data_nasc,
        cpf,
        rg,
        senha,
        usuario,
        email,
        Endereco,
        data_registro
    )
VALUES
    (
        654,
        'Patrick Sanchez',
        '2024-10-06',
        'Brian Yang',
        'Leslie Johnson',
        'David Guzman',
        'Michelle Miles',
        'Jerry Ramirez',
        '067029dd-0163-75fb-8000-c7cab53d0afa',
        'Olivia Moore'
    )
INSERT INTO
    Telefone (idTelefone, telefone, Pessoa)
VALUES
    (
        432,
        'Christopher Bernard',
        '067029dd-0163-75fb-8001-d820513f0545'
    )
INSERT INTO
    Avaliacao (idAvaliacao, comentario, Acordo, Grau)
VALUES
    (
        344,
        'James Howard',
        '067029dd-0163-75fb-8002-a909aba6ec95',
        '067029dd-0163-75fb-8003-a584e02bd21c'
    )