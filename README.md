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
 - usar pyspark para já converter resultados das classes em Spark Data Frames
2. Preparar autenticação e funções para autenticação
 - construir uma classe para autenticação? Um função para autenticar? Usar algo parecido com a autenticação do pygsheets
 - No caso do Databricks, descobrir com os data-engineers como guardá-los
3. Usar gist para inspiração:
 - https://gist.github.com/rickcnagy/9820052
4. Criar notebook functions/pipelinedeals_functions para usar dentro do Databricks





