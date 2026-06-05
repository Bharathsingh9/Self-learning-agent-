javascript
// Import dependencies
import { default as express } from 'express';
import { renderFile } from 'express-handlebars';

// Initialize Express and Handlebars
const app = express();
const hbs = renderFile;

// Middleware
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

// Handlebars layout and template files
const mainLayout = 'layouts/main';
const indexTemplate = 'views/index';
const mathTemplate = 'views/math';

// Initial state
let expression = '';
let result = '';

// Render index template
app.get('/', (req, res) => {
    res.render(mainLayout, {
        layout: 'layout',
        template: indexTemplate,
        title: 'Scientific Calculator'
    });
});

// Handle math operations
app.post('/math', (req, res) => {
    expression = req.body.expression;
    result = eval(expression);
    res.redirect('/calculator');
});

// Render math template
app.get('/calculator', (req, res) => {
    res.render(mainLayout, {
        layout: 'layout',
        template: mathTemplate,
        title: 'Scientific Calculator',
        expression,
        result
    });
});

// Clear expression and result
app.get('/clear', (req, res) => {
    expression = '';
    result = '';
    res.redirect('/calculator');
});

// Handle button clicks
app.post('/buttons/:operation', (req, res) => {
    const operation = req.params.operation;
    switch (operation) {
        case 'clear':
            expression = '';
            result = '';
            break;
        case 'backspace':
            expression = expression.slice(0, -1);
            result = '';
            break;
        default:
            expression += operation;
            try {
                result = eval(expression);
            } catch (error) {
                // Do nothing, just set the result to an error message
                result = 'Error!';
            }
    }
    res.redirect('/calculator');
});

// Listen on port 3000
const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});



// Import dependencies
import express from 'express';

const app = express();

// Handle button clicks
app.get('/num/:num', (req, res) => {
    const num = req.params.num;
    res.cookie('num', num);
    res.redirect('/calculator');
});

// Handle math operations
app.get('/operator/:operator', (req, res) => {
    const operator = req.params.operator;
    res.cookie('operator', operator);
    res.redirect('/calculator');
});

// Export the app
export default app;



// Import dependencies
import express from 'express';
const num = express cookieParser.num;
const operator = express cookieParser.operator;

const app = express();

// Render math template
app.get('/calculator', (req, res) => {
    res.render('calc', {
        num,
        operator
    });
});

// Clear cookies
app.get('/clear', (req, res) => {
    res.cookie('num', '');
    res.cookie('operator', '');
    res.redirect('/calculator');
});

// Export the app
export default app;


This code provides functionality for a scientific calculator with features such as number entry, operator selection, and expression evaluation. It also includes support for common arithmetic operations and advanced mathematical functions.


// Import dependencies
import express from 'express';

const app = express();
const mathOperations = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => b !== 0 ? a / b : 'Error!',
    '%': (a, b) => b !== 0 ? a % b : 'Error!',
    '^': (a, b) => Math.pow(a, b)
};

app.get('/operations', (req, res) => {
    const num = req.query.num1;
    const operator = req.query.operator;
    const num2 = req.query.num2;
    const result = mathOperations[operator] ? mathOperations[operator](num, num2) : 'Error!';
    res.send(result);
});

// Export the app
export default app;


This code handles operations such as number entry, operator selection, and expression evaluation. 

handlebars
<div>
    <h1>Scientific Calculator</h1>
    <h2>Expression: {{expression}}</h2>
    <h2>Result: {{result}}</h2>
</div>


handlebars
<div>
    <h1>Scientific Calculator</h1>
    Number: {{num}}<br />
    Operator: {{operator}}
</div>


This code is used for the Handlebars templates. It uses Mustache-style syntax for placeholders.


// Import dependencies
const handlebars = require('handlebars');

// Compile the templates
const indexTemplate = handlebars.compile('{{> layout -- title="Scientific Calculator" -- expression="" -- result=""}}');
const mathTemplate = handlebars.compile('{{> layout -- title="Scientific Calculator" -- expression="{{expression}}" -- result="{{result}}"}}');
const calcTemplate = handlebars.compile('{{> layout -- title="Scientific Calculator" -- expression="{{expression}}" -- result="{{result}}"}}');

// Export the templates
export { indexTemplate, mathTemplate, calcTemplate };
