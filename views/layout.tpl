<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
    <link rel="stylesheet" href="/static/css/user-form.css" />

    <style>
    </style>
</head>
<body>

    <div class="page">
        <div class="container">
            {{!base}}  <!-- O conteúdo das páginas filhas virá aqui -->
        </div>
    </div>

    <footer>
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
