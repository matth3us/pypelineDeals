# pipelinedeals-wrapper
Unofficial Python wrapper for Pipeline Deals API


1. Repassar documentação e classes para organizar tarefas
 - documentação: https://app.pipelinedeals.com/api/docs
 - pensar em formato das classes: https://docs.python.org/3/tutorial/classes.html
 - classes para construir:
  1. activities
  2. companies
  3. customers
  4. customFields (incluir também os groups, labels e dropdown entries)
  5. deals
  6. people
  7. users
- Criar uma classe pipelineDeals com dois métodos:
	1. authentication: guardar informações de autenticação da API
	1. archive: acessar dados e listas de de dados; todos os outros métodos estão derivados do archive, inclusive os lists
 - usar pyspark para já converter resultados das classes em Spark Data Frames
2. Usar gist para inspiração:
 - https://gist.github.com/rickcnagy/9820052
3. Criar notebook functions/pipelinedeals_functions para usar dentro do Databricks; descobrir como guardar segredos no Databricks
4. Gerar testes: https://realpython.com/python-testing/





