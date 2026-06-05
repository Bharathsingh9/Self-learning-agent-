javascript
import { calculate } from '../script.js';
import { expect } from 'chai';

describe('Calculator Application', () => {
  it('should perform addition correctly', () => {
    const result = calculate('+', 10, 5);
    expect(result).to.equal(15);
  });

  it('should perform subtraction correctly', () => {
    const result = calculate('-', 10, 5);
    expect(result).to.equal(5);
  });

  it('should perform multiplication correctly', () => {
    const result = calculate('*', 10, 5);
    expect(result).to.equal(50);
  });

  it('should perform division correctly', () => {
    const result = calculate('/', 10, 5);
    expect(result).to.equal(2);
  });

  it('should handle division by zero correctly', () => {
    expect(() => calculate('/', 10, 0)).to.throw();
  });

  it('should handle invalid operators correctly', () => {
    expect(() => calculate('^', 10, 5)).to.throw();
  });

  it('should handle non-numeric inputs correctly', () => {
    expect(() => calculate('+', 'a', 5)).to.throw();
  });
});
