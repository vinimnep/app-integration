# Automatização Personalizada

Esta é uma integração personalizada não nativa entre RD Station CRM e ZapCloud que executa ações com base em horários predefinidos e em campos personalizados de negociações do RD Station CRM.

## Funcionalidades

- A aplicação é aberta manualmente no horário comercial e verifica a cada minuto se é um dos horários de execução (9 AM e 2 PM).

- Ela verifica as negociações no RD Station CRM usando a API e procura por negociações que possuam um campo personalizado específico marcado como visível.

- Se a negociação atender aos critérios, a aplicação envia os dados da negociação para um webhook (que dispara mensagens automáticas.

- A aplicação exibe mensagens na janela para informar o status das ações.

## Configuração

Antes de executar a aplicação, certifique-se de configurar as seguintes variáveis no código:

- `url_deals`: URL da API de negociações do RD Station CRM.

- `url_webhook`: URL do webhook onde os dados serão enviados.

- `custom_field_id`: ID do campo personalizado que será verificado nas negociações.

## Executando a Aplicação

1. Execute o código Python.

2. A janela da aplicação será aberta.

3. A aplicação verificará os horários definidos para execução e os campos personalizados nas negociações.

4. Os resultados das ações serão exibidos na janela da aplicação.


Este é um projeto de automatização personalizada desenvolvido em Python usando a biblioteca Tkinter e requests. Sinta-se à vontade para personalizar e adaptar conforme suas necessidades específicas.

**Nota:** Certifique-se de manter as credenciais e informações sensíveis seguras e não compartilhe-as no código-fonte.

