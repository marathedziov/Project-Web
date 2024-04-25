document.querySelectorAll('.key').forEach(key => {
    key.addEventListener('click', () => {
        const textInput = document.getElementById('text-input');
        const keyValue = key.textContent;

        if (keyValue === '⌫') {
            word.value = word.value.slice(0, -1);
        } else {
            word.value += keyValue;
        }
    });
});
