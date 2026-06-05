javascript
import React, { useEffect, useState } from 'react';
import { math } from 'mathjs';

const HistoryDisplay = ({ history }) => {
  const [calculatedResults, setCalculatedResults] = useState({});

  useEffect(() => {
    if (history.length > 0) {
      const results = history.map((item, index) => {
        let result = '';
        try {
          const output = math.evaluate(item.formula);
          result = output.toString();
        } catch (error) {
          result = 'Invalid formula';
        }
        return { formula: item.formula, result };
      });
      setCalculatedResults(results);
    }
  }, [history]);

  return (
    <div>
      {calculatedResults.map((result, index) => (
        <div key={`${result.formula}-${index}`}>
          <p>
            Formula: {result.formula}
          </p>
          <p>
            Result: {result.result}
          </p>
        </div>
      ))}
    </div>
  );
};

export default HistoryDisplay;
