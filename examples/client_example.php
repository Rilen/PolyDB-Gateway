<?php
/**
 * Exemplo de Cliente PHP para o PolyDB Gateway
 * Este script demonstra como um serviço Back-end pode consumir dados
 * de múltiplos bancos de dados sem precisar de drivers específicos.
 */

// 1. Configurações do pedido
$url = 'http://localhost:8000/query';

// Vamos pedir dados de faturamento do PostgreSQL
$pedido = [
    "database" => "postgres_prod",
    "query"    => "SELECT product, amount, region FROM sales ORDER BY amount DESC LIMIT 3"
];

// 2. Preparando a chamada via cURL (o padrão do PHP para APIs)
$ch = curl_init($url);
$payload = json_encode($pedido);

curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type:application/json']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 5);

// 3. Executando e recebendo a resposta
echo "--- Iniciando consulta via PolyDB Gateway ---\n";
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "Erro na conexão: " . curl_error($ch) . "\n";
} else {
    $dados = json_decode($response, true);

    if ($httpCode === 200 && $dados['status'] === 'success') {
        echo "Sucesso! Recebidos " . $dados['rows_count'] . " registros do PostgreSQL.\n\n";
        
        echo "TOP 3 VENDAS:\n";
        foreach ($dados['data'] as $linha) {
            echo "- " . $linha['product'] . " (" . $linha['region'] . "): R$ " . $linha['amount'] . "\n";
        }
    } else {
        echo "Erro na API: " . ($dados['detail'] ?? 'Erro desconhecido') . "\n";
    }
}

curl_close($ch);
echo "\n--- Fim do processamento PHP ---";
?>
