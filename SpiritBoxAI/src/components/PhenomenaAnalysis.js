```javascript
import React from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import '../styles/PhenomenaAnalysis.css';

class PhenomenaAnalysis extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      phenomena: [],
      selectedPhenomenon: '',
    };
  }

  componentDidMount() {
    axios.get('/api/phenomena')
      .then(response => {
        this.setState({ phenomena: response.data });
      })
      .catch(error => {
        console.error('Error fetching data', error);
      });
  }

  handlePhenomenonChange = (event) => {
    this.setState({ selectedPhenomenon: event.target.value });
  }

  render() {
    const { phenomena, selectedPhenomenon } = this.state;

    return (
      <div id="phenomenaAnalysisContainer">
        <h2>Customizable Phenomena Analysis</h2>
        <select value={selectedPhenomenon} onChange={this.handlePhenomenonChange}>
          {phenomena.map(phenomenon => (
            <option key={phenomenon.id} value={phenomenon.name}>
              {phenomenon.name}
            </option>
          ))}
        </select>
        <div id="phenomenonDetails">
          {/* Details of the selected phenomenon will be displayed here */}
        </div>
      </div>
    );
  }
}

PhenomenaAnalysis.propTypes = {
  phenomena: PropTypes.array,
  selectedPhenomenon: PropTypes.string,
};

export default PhenomenaAnalysis;
```