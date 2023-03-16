# Cmed_cob_sol
> Script em Python para calcular o coeficiente de runoff médio (Cmed) para diferentes tipos de cobertura do solo - Python script to calculate the mean runoff coefficient (cmed) of different land types

O projeto possibilitou a automatização do cálculo dos coeficientes de runoff médios de bacias de contribuição em uma região onde se pretende realizar um estudo ou projeto de drenagem, por meio de um script desenvolvido em Python. O software QGIS foi utilizado inicialmente para gerar, com o auxílio das ferramentas de processamento, um arquivo georreferenciado com polígonos que delimitam as áreas de cada bacia de contribuição dentro de uma área de drenagem urbana, assim como, calcular a distribuição dos tipos de cobertura do solo para as áreas das bacias. Por fim, o script possibilita a automatização do cálculo dos coeficientes de runoff médios para as bacias de contribuição.


## Preparação dos arquivos necessários:

Para rodar o script é necessária, anteriormente, a geração de dois arquivos. Um arquivo deve conter os polígonos que delimitam as áreas das bacias de contribuição para o estudo de drenagem em uma determinada região urbana, em formato vetorial georreferenciado (shp), contendo a porcentagem em relação à área total de cada bacia correspondente a um tipo de cobertura do solo. O segundo arquivo deve ser uma tabela (csv) com os diferentes tipos de cobertura do solo presentes na região e os seus respectivos valores do coeficiente de runoff.

O arquivo com os polígonos das bacias de contribuição foi gerada no software QGIS com as ferramentas de processamento nativas e com a extensão do SAGA, para automatização parcial das tarefas. 

### Camada com polígonos das bacias de contribuição para a região de exemplo da subbacia da Bacia do Rio Camarajipe (Salvador - BA):

![bacias_cont](https://user-images.githubusercontent.com/116915472/225761771-3c110cb1-9e0a-4075-973a-ed5fe5c8c880.png)


### Camada com polígonos para cada tipo de cobertura do solo encontrado na região de exemplo da subbacia da Bacia do Rio Camarajipe (Salvador - BA):

![cob_solo](https://user-images.githubusercontent.com/116915472/225760827-b976a2b5-6238-4668-8a4d-9f1474c1fea2.png)


No QGIS, foram inseridos diferentes arquivos vetoriais, para cada tipo de cobertura do solo, contendo polígonos delimitando as áreas da região de drenagem onde se encontram cada tipo de cobertura. Com o arquivo das bacias de contribuição e o arquivo com os polígonos representando os diferentes tipos de cobertura do solo, foi utilizado no QGIS o algortimo 'calculatevectoroverlaps' para calcular para cada bacia de contribuição a parcela da área dos polígonos de cobertura do solo contida dentro da área da bacia, e a porcentagem correspondente em relação à área total.

### Tabela de atributos do arquivo contendo os polígonos das bacias de contribuição:

![tabela_atributos](https://user-images.githubusercontent.com/116915472/224802591-c7236f94-8f4c-40df-bb5a-7589319e6c14.PNG)


Na tabela de atributos do arquivo com as bacias de contribuição foram editados os nomes das colunas referentes à porcentagem de área de cada tipo de cobertura do solo, inserindo um termo de identificação do tipo de cobertura e o sufixo 'p', de porcentagem. Além disso, foi adicionada uma coluna na tabela de atributos das bacias denominada 'Cmed' para o cálculo do coeficiente de runoff médio. Após a edição o arquivo foi exportado com o nome de cob_sol_bc_p_a.shp.

### Tabela csv com dados dos tipos de cobertura do solo e os coeficientes de runoff correspondentes: 

![tabela_csv](https://user-images.githubusercontent.com/116915472/224802894-fe2f3a80-acd7-447a-bb0c-ce90d65a99cb.PNG)

Em seguida, foi criado o arquivo csv com os nomes dos tipos de cobertura do solo iguais aos termos utilizados nos nomes atribuídos às colunas referentes à porcentagem de cada tipo de cobertura na tabela do arquivo das bacias, cob_sol_bc_p_a (mesma grafia). Os nomes dos tipos de cobertura foram inseridos na coluna denominada ‘rua’ na tabela do arquivo csv. Foram criadas as colunas de identificação, id, e a coluna ‘c’ para os valores do coeficiente de runoff para cada tipo de cobertura do solo. O arquivo csv foi exportado com o nome c_tip_rua.csv.


## Cálculo do coeficiente de runoff médio para cada polígono de bacia de contribuição:

Os arquivos cob_sol_bc_p_a.shp e o c_tip_rua.csv foram colocados em uma pasta no drive chamada qgis. O código em Python executado no Google Colab seleciona o valor, para cada tipo de cobertura do solo presente na tabela, da porcentagem da área da cobertura inserida dentro da área da bacia em relação à área total, para cada polígono de delimitação das bacias de contribuição, de acordo com sua tabela de atributos.

O coeficiente de runoff médio foi calculado a partir da média ponderada dos valores dos coeficientes para cada tipo de cobertura do solo em proporção à área ocupada por ela em cada bacia de contribuição. Os valores calculados do coeficiente de runoff são inseridos na coluna de nome 'Cmed' do arquivo 'cob_sol_bc_p_a.shp'.
