# Cmed_cob_sol
> Calculates the runoff coefficient (cmed) of different land types -
> Calcula o coeficiente de runoff (Cmed) para diferentes tipos de cobertura do solo


## Preparação dos arquivos de entrada necessários:

Para esse código inicialmente são gerados o shapefile com os polígonos das bacias de contribuição da área em estudo e o arquivo csv com os tipos de cobertura do solo e os respectivos valores do coeficiente de runoff.

A camada com as bacias de contribuição foi gerada no qgis com as ferramentas de processamento nativas e com a extensão do SAGA. Foi utilizada a ferramenta do SAGA 'watershedbasins' para gerar as bacias de contribuição, resultando em um arquivo do tipo raster, que foi vetorizado e pós-processado.

![cob_sol_bc_p_a](cob_sol_bc_p_a.png)


Diferentes camadas para cada tipo de cobertura do solo, com os polígonos delimitando as áreas com o tipo de cobertura, foram utilizadas com o algortimo 'calculatevectoroverlaps' com a camada de bacias de contribuição como camada de entrada. Para cada feição da camada das bacias de concentração foi calculada a área das camadas de cobertura do solo contidas dentro da bacia e a porcentagem dessa área correspondente a área total da feição da bacia.

Foram renomeados os campos com nome das camadas de sobreposição de cobertura do solo, da camada resultante do processamento anterior, retirando os prefixos e sufixos deixando apenas uma identificação do tipo de cobertura do solo e o sufixo p ou a que representam os valores de porcentagem e area de cada tipo de cobertura para cada feição, respectivamente. Além disso, foi adicionado um campo na tabela de atributos 'Cmed' para o cálculo do coeiciente de runoff médio. Após a edição a camada foi exportada com o nome de cob_sol_bc_p_a.

Em seguida, foi criada a camada csv com os nomes dos tipos de rua iguais aos dos campos da camada cob_sol_bc_p_a (mesma grafia) com nome da coluna ‘rua’, campo de identificação de feições, id, e valores do coeficiente C para cada tipo de cobertura com o nome da coluna ‘c’.


## Cálculo do coeficiente de runoff médio para cada polígono de bacia de contribuição da camada de entrada:

Os shapes de cob_sol_bc_p_a.shp e o csv c_tip_rua foram colocados em uma pasta no drive chamada qgis. O código em Python desenvolvido no google colab calcula para cada feição da camada de cobertura do solo por bacia de contribuição (cob_sol_bc_p_a) o coeiciente de runoff médio de acordo com os valores de porcentagem de área (campo com sufixo '_p') para cada tipo de cobertura do solo.  Os valores calculados são inseridos no campo 'Cmed' da camda 'cob_sol_bc_p_a'.
