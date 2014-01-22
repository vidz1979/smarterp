SmartERP
========

O SmartERP será um sistema ERP composto por diversos aplicativos (módulos) que abrangerão todas as operações de uma empresa:

1. Compras
2. Vendas
3. Estoques
4. Financeiro
5. Contabilidade e auditoria
6. Análise de Crédito
7. Cobrança
8. Logística
9. Recursos Humanos

Através dos controles operacionais, será possível gerar uma grande quantidade de informações que estarão disponíveis em relatórios, que irão auxiliar a tomada de decisão.

Arquitetura RESTful
-------------------

A arquitetura RESTful permitirá a construção de múltiplos frontend utilizando as mesmas regras de negócio. Os frontends podem conter apenas partes da aplicação (ex: liberações e dashboards no smartphone).
API backend deve tornar simples o desenvolvimento de frontend, mascarando a complexidade das regras de negócio e estrutura interna do banco de dados com uma interface intuitiva. 
Os frontends podem se utilizar de dicionário de metadados para compor dinamicamente as telas, permitindo a flexibilização do sistema e maior aderência.
Tecnologia backend: Django e PostgreSQL.
Tecnologia frontend:
Interface Web: HTML + CSS + framework Javascript (AngularJS, Backbone ou outro).
Interface Mobile: iOS e Android.
Interface Desktop: QT, TkInter ou wxPython.

Qualidade de Software
---------------------

Qualidade é inegociável.
Uso de TDD sempre, em todos os níveis da aplicação (backend e frontend).
Uso de BDD quando possível.
Somente utilizar pacotes com testes.

Requisitos
----------

Multiempresas e multifilial
Segmento inicial: varejo de calçados, confecções e acessórios
Adoção das melhores práticas contábeis e auditoria
ERP leve e ágil, em código aberto adequado às regras brasileiras
Roteiro de trabalho
1. Concepção
2. Desenvolvimento backend no conceito MVP (produto mínimo viável)
3. Desenvolvimento frontend
4. Desenvolvimento e integração contínua de funcionalidades (backend e frontend)