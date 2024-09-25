function calculate(operation) {
    let num1 = parseFloat(document.getElementById('num1').value);
    let num2 = parseFloat(document.getElementById('num2').value);
    let result;
    
    if (operation === 'add') {
        result = num1 + num2;
    } else if (operation === 'sub') {
        result = num1 - num2;
    } else if (operation === 'mul') {
        result = num1 * num2;
    } else if (operation === 'div') {
        result = num1 / num2;
    }
    document.getElementById('result').value = result;
}