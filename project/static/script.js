document.querySelectorAll('.key').forEach(key => {
    key.addEventListener('click', () => {
        const textInput = document.getElementById('text-input');
        const keyValue = key.textContent;

        if (keyValue === 'Enter') {
            // Действия при нажатии на Enter
            // Например, можно отправить данные на сервер или что-то еще
            console.log('Enter key pressed');
        } else if (keyValue === '⌦') {
            // Удалить последний символ
            word.value = word.value.slice(0, -1);
        } else {
            word.value += keyValue;
        }
    });
});
