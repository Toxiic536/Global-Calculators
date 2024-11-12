let input = '';

function addCharacter(character) {
    input += character;
    document.getElementById('screen').value = input;
}

function clearScreen() {
    input = '';
    document.getElementById('screen').value = '';
}

function operate(operator) {
    if (operator === 'sqrt') {
        input = Math.sqrt(eval(input)).toString();
    } else if (operator === 'sin') {
        input = Math.sin(eval(input)).toString();
    } else if (operator === 'cos') {
        input = Math.cos(eval(input)).toString();
    } else if (operator === 'log') {
        input = Math.log(eval(input)).toString();
    } else if (operator === 'pi') {
        input = Math.PI.toString();
    } else if (operator === 'exp') {
        input = Math.exp(eval(input)).toString();
    } else {
        input += operator;
    }
    document.getElementById('screen').value = input;
}

function calculate() {
    try {
        input = eval(input).toString();
        document.getElementById('screen').value = input;
    } catch (e) {
        document.getElementById('screen').value = 'Error';
        input = '';
    }
}
