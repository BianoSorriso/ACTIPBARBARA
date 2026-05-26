# projetoONG

Projeto da ACITP - A Casa do Idoso para Todos os Povos.

## Nova Estrutura

- Aplicacao migrada para `Python + Django`
- Layout reorganizado com `templates` e `static` unificados
- Interface ajustada para melhor responsividade em desktop, tablet e mobile
- Banco de dados configurado com `SQLite`
- Painel administrativo Django preparado para gerenciar:
- Configuracao do site
- Estatisticas
- Servicos
- Eventos
- Depoimentos
- Faixas de doacao
- Inscricoes de voluntarios
- Mensagens de contato
- Perfis de usuarios

## Como Executar

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Acessos

- Site: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
