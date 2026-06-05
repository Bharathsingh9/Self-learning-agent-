javascript
import mathquill from 'mathquill';

const mathConfig = {
  mathjax: {
    inlineMath: [
      ['$', '$'],
      ['\\(', '\\)']
    ],
    displayMath: [
      ['$$', '$$'],
      ['\\[', '\\]'],
      ['\\begin{align*}', '\\end{align*}']
    ],
    processEscapes: true
  },
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [
      ['$$', '$$'],
      ['\\[', '\\]'],
      ['\\begin{align*}', '\\end{align*}']
    ],
    processEscapes: true
  },
  katex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [
      ['$$', '$$'],
      ['\\[', '\\]'],
      ['\\begin{align*}', '\\end{align*}']
    ],
    processEscapes: true
  },
  mathquill: {
    spaceBehavesLikeParentheses: true,
    mathInputConstructor: mathquill.MathInput,
    mathFieldConstructor: mathquill.MathField,
    mathMMLConstructor: mathquill.MathMML,
    previewFilter: null,
    preview: true,
    mathQuill: {
      handlers: {
        edit: function(mathField, delta) {
          const inputManager = mathField.inputManager;
          inputManager.delete(delta.ops.length - 1);
        }
      }
    },
    render: {
      mathElement: (formula, renderer) => {
        const math = new mathquill.MathField({
          selectors: ['.math'],
          // override any default render options
          render: renderer,
          handlers: {}
        });
        math.update(Math.quill.parseMathML(formula));
        return math.domElement;
      }
    }
  }
};

export default mathConfig;
