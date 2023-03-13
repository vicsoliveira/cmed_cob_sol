# Cmed_cob_sol
> Script em Python para calcular o coeficiente de runoff (Cmed) para diferentes tipos de cobertura do solo - Python script to calculate the runoff coefficient (cmed) of different land types


## Preparação dos arquivos necessários:

Para rodar o script é necessário anteriormente a geração de dois arquivos. Um arquivo deve conter os polígonos que delimitam as área de bacias de contribuição da  região em estudo, em formato vetorial georreferenciado (shp). O segundo arquivo deve ser uma tabela (csv) com os diferentes tipos de cobertura do solo presentes na região e os seus respectivos valores do coeficiente de runoff.

O arquivo com os polígonos das bacias de contribuição foi gerada no software QGIS com as ferramentas de processamento nativas e com a extensão do SAGA.

### Camada com polígonos das bacias de contribuição:

![cob_sol_bc_p_a](https://user-images.githubusercontent.com/116915472/224740093-508c8fa0-15aa-4207-b946-426da0723c2a.PNG)


No QGIS, foram inseridos também diferentes arquivos vetoriais para cada tipo de cobertura do solo, contendo polígonos delimitando as áreas da região onde se encontram o tipo de cobertura referido. Com o arquivo das bacias de contribuição e os representando os diferentes tipos de cobertura do solo foi utilizado no QGIS o algortimo 'calculatevectoroverlaps' que calcula para cada polígono referente a uma bacia de contribuição a área dos polígonos do arquivo de cobertura do solo contida dentro da área da bacia, e a porcentagem correspondente a área total da bacia.

### Tabela de atributos do arquivo contendo os polígonos das bacias de contribuição:

![tabela_atributos](https://user-images.githubusercontent.com/116915472/224802591-c7236f94-8f4c-40df-bb5a-7589319e6c14.PNG)


Na tabela de atributos do arquivo com as bacias de contribuição foram editados os nomes das colunas referentes à porcentagem de área de cada tipo de cobertura do solo para cada bacia, inserindo um termo de identificação do tipo de cobertura do solo e o sufixo 'p', de porcentagem. Além disso, foi adicionada uma coluna na tabela de atributos das bacias denominado 'Cmed' para o cálculo do coeiciente de runoff médio para cada bacia. Após a edição o arquivo foi exportado com o nome de cob_sol_bc_p_a.shp.

### Tabela csv com dados dos tipos de cobertura do solo e os coeficientes de runoff correspondentes: 

![tabela_csv](https://user-images.githubusercontent.com/116915472/224802894-fe2f3a80-acd7-447a-bb0c-ce90d65a99cb.PNG)


Em seguida, foi criado o arquivo csv com os nomes dos tipos de cobertura do solo iguais aos nomes do título das colunas da tabela do arquivo das bacias cob_sol_bc_p_a (mesma grafia). Os nomes dos tipos de cobertura foram inseridos na coluna denominada ‘rua’ do arquivo csv. Foram criadas as colunas de identificação, id, e a coluna ‘c’ para os valores do coeficiente de runoff para cada tipo de cobertura do solo. O arquivo csv foi exportado com nome c_tip_rua.csv.


## Cálculo do coeficiente de runoff médio para cada polígono de bacia de contribuição:

Os arquivos cob_sol_bc_p_a.shp e o c_tip_rua.csv foram colocados em uma pasta no drive chamada qgis. O código em Python desenvolvido no Google Colab soma para cada tipo de cobertura do solo presente na tablea c_tip_rua.csv, a área desse tipo de cobertura dentro da área de cada polígono referente a cada bacia do arquivos de bacias de contribuição (cob_sol_bc_p_a), de acordo com a porcentagem da área em relação à área total da bacia, registrada na tabela de atributos do arquivo dcob_sol_bc_p_a.shp. O coeiciente de runoff médio foi calculada a partir da média dos valores de coeficiente de runoff de cada tipo de cobertura em proporção à área ocupada por ela em cada bacia de contribuição.  Os valores calculados do coeficiente de runoff são inseridos na coluna de nome 'Cmed' do arquivo 'cob_sol_bc_p_a.shp'.
