import React from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import '../styles/EMFMonitoring.css';

class EMFMonitoring extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      emfData: [],
      isLoading: true,
      error: null,
    };
  }

  componentDidMount() {
    this.fetchEMFData();
  }

  fetchEMFData() {
    axios.get('/api/emf')
      .then(response => {
        this.setState({
          emfData: response.data,
          isLoading: false,
        });
      })
      .catch(error => this.setState({ error, isLoading: false }));
  }

  render() {
    const { emfData, isLoading, error } = this.state;

    if (isLoading) {
      return <div className="loader">Loading...</div>;
    }

    if (error) {
      return <div className="error">{error.message}</div>;
    }

    return (
      <div id="emfMonitoringContainer">
        <h2>EMF Monitoring</h2>
        <div className="emfDataContainer">
          {emfData.map((data, index) => (
            <div key={index} className="emfDataItem">
              <p><strong>Timestamp:</strong> {data.timestamp}</p>
              <p><strong>EMF Level:</strong> {data.level}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

EMFMonitoring.propTypes = {
  emfData: PropTypes.array.isRequired,
};

export default EMFMonitoring;