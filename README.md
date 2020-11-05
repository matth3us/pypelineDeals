# pipelinedeals-wrapper
Unofficial Python wrapper for Pipeline Deals API

## Em construção!
- Documentação da API: https://app.pipelinedeals.com/api/docs

## 2nov
- Passar método _checkKeys()_ para classe master pipelineDeals; testar método
- Criar e testar método _checkId()_ no pipelineDealsObjects;
- _commit here!_
- Testar método _create()_ em pipelineDealsObjects; funcionando, os outros vão ser consideravelmente mais fáceis
- _commit here!_
- Gerar a classe pipelineDealsLists; as lista devem devolver Listas (objeto de python) ordenadas pelo id dos objetos; deve criar um objeto para cada item da lista, com o seu respectivo id e com os valores de key passados 
- _commit here!_
- Preparar documentação básica do wrapper no ReadMe; seguir o formato de uma vignette!

## No futuro

- usar o conceito de parâmetros permitidos, criando um dicionário com todos os parâmetros permitidos de cada objeto para facilitar manutenção futura (criar branch)
- Criar notebook functions/pipelinedeals_functions para usar dentro do Databricks; descobrir como guardar segredos no Databricks; 
- Preparar documentação desse wrapper: https://readthedocs.org
- Gerar testes: https://realpython.com/python-testing/; https://semaphoreci.com/community/tutorials/building-and-testing-an-api-wrapper-in-python
- Expandir para mais objetos da API; planejar expansão; (criar branches)
