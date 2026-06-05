javascript
// script.js
function add(num) {
    document.getElementById('current').value += num;
}

function equals() {
    try {
        document.getElementById('current').value = eval(document.getElementById('current').value);
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function clearInput() {
    document.getElementById('current').value = '';
}

function clearExpression() {
    document.getElementById('current').value = '';
}

function changeSign() {
    if (document.getElementById('current').value.startsWith('-')) {
        document.getElementById('current').value = document.getElementById('current').value.slice(1);
    } else {
        document.getElementById('current').value = '-' + document.getElementById('current').value;
    }
}

function sqrt() {
    try {
        document.getElementById('current').value = Math.sqrt(eval(document.getElementById('current').value));
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function sin() {
    try {
        document.getElementById('current').value = Math.sin(eval(document.getElementById('current').value));
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function cos() {
    try {
        document.getElementById('current').value = Math.cos(eval(document.getElementById('current').value));
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function tan() {
    try {
        document.getElementById('current').value = Math.tan(eval(document.getElementById('current').value));
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function log() {
    try {
        document.getElementById('current').value = Math.log(eval(document.getElementById('current').value));
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function percent() {
    try {
        document.getElementById('current').value = (eval(document.getElementById('current').value) / 100);
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function exp() {
    try {
        document.getElementById('current').value = Math.exp(eval(document.getElementById('current').value));
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function ln() {
    try {
        document.getElementById('current').value = Math.log(eval(document.getElementById('current').value));
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}

function pow(x) {
    try {
        document.getElementById('current').value = Math.pow(x.value, eval(document.getElementById('current').value));
    } catch (e) {
        document.getElementById('current').value = 'Error';
    }
}
