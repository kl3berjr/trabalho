document.addEventListener('DOMContentLoaded', () => {
    const senha = document.getElementById('senha');
    const confirmarSenha = document.getElementById('confirmar_senha');

    if (confirmarSenha) {
        confirmarSenha.addEventListener('input', () => {
            if (senha.value !== confirmarSenha.value) {
                confirmarSenha.setCustomValidity('As senhas não conferem pamonha!');
            } else {
                confirmarSenha.setCustomValidity('');
            }
        });
    }
});
