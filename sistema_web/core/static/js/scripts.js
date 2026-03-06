// Função de preenchimento automatico
function preencherAutomaticamente() {
    // --- 1. DADOS ALEATÓRIOS PARA CAMPOS ÚNICOS ---
    const randomId = Math.floor(Math.random() * 99999);
    const randomCode = "789" + Math.floor(Math.random() * 1000000000);
    
    // --- 2. PREENCHER CAMPOS DO DJANGO (Pelo name="") ---
    // Tenta achar os campos pelo name (padrão do Django)
    try {
        document.querySelector('[name="codigodebarra"]').value = randomCode;
        document.querySelector('[name="descricao"]').value = `PRODUTO DE TESTE AUTOMÁTICO #${randomId}`;
        document.querySelector('[name="precocusto"]').value = "50.00";
        document.querySelector('[name="precovenda"]').value = "120.00";
        document.querySelector('[name="estoqueatual"]').value = "100";
        document.querySelector('[name="estoqueminimo"]').value = "10";
        
        // Data de hoje para o campo validade (formato YYYY-MM-DD)
        const hoje = new Date().toISOString().split('T')[0];
        const campoValidade = document.querySelector('[name="validade"]');
        if (campoValidade) campoValidade.value = hoje;
    } catch (e) {
        console.log("Algum campo principal não foi encontrado, continuando...");
    }

    // --- 3. PREENCHER CAMPOS VISUAIS (HTML PURO) ---
    // Seleciona todos os inputs de texto da página
    const todosInputs = document.querySelectorAll('input[type="text"]');
    
    todosInputs.forEach(input => {
        // Só preenche se estiver vazio para não apagar o que já fizemos acima
        if (input.value === "") {
            // Lógica simples: Se o label perto dele for "Vermelho", poe valor fiscal padrão
            // Senão, põe "0" ou texto genérico.
            
            // Pega o label anterior para tentar adivinhar o contexto
            let label = input.previousElementSibling ? input.previousElementSibling.textContent : "";
            
            if (label.includes("C.F.O.P")) {
                input.value = "5405";
            } else if (label.includes("CST")) {
                input.value = "00"; // Tributado integralmente
            } else if (label.includes("NCM")) {
                input.value = "2202.10.00"; // Exemplo Coca-Cola
            } else if (label.includes("Aliquota") || label.includes("%") || label.includes("Aliq")) {
                input.value = "18.00";
            } else {
                input.value = "0"; // Valor padrão para campos numéricos/texto genéricos
            }
        }
    });

    // --- 4. AJUSTAR SELECTS ---
    const todosSelects = document.querySelectorAll('select[class="form-select"]');
    todosSelects.forEach(select => {
        // Seleciona a segunda opção (índice 1) se houver, para não ficar no padrão
        if (select.options.length > 1) {
            select.selectedIndex = 0; 
        }
    });


}




// Função de cancelamento do preenchimento

// --- Função para Limpar/Cancelar ---
function limparFormulario() {
    // Seleciona todos os inputs que NÃO sejam:
    // - Botões (submit, button)
    // - Ocultos (hidden - como o token CSRF)
    // - Leitura (readonly - como a Unidade 'UN')
    const campos = document.querySelectorAll('input:not([type="button"]):not([type="submit"]):not([type="hidden"]):not([readonly]), select, textarea');

    campos.forEach(campo => {
        // Se for caixa de seleção (Select), volta para a primeira opção
        if (campo.tagName === 'SELECT') {
            campo.selectedIndex = 0;
        } 
        // Se for Checkbox ou Radio, desmarca
        else if (campo.type === 'checkbox' || campo.type === 'radio') {
            campo.checked = false;
        } 
        // Para todo o resto (texto, número, data), apaga o valor
        else {
            campo.value = "";
        }
    });

    //Coloca o foco de volta no primeiro campo (Código de Barra)
    const primeiroCampo = document.querySelector('[name="codigodebarra"]');
    if (primeiroCampo) primeiroCampo.focus();
}    
