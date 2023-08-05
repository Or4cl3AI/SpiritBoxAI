import React from 'react';
import PropTypes from 'prop-types';
import '../styles/UserInterface.css';

const UserInterface = ({ data }) => {
  return (
    <div className="userInterfaceContainer">
      <div className="navigation">
        {/* Navigation code goes here */}
      </div>
      <div className="visualizations">
        {/* Visualization code goes here */}
      </div>
      <div className="reports">
        {/* Reports generation code goes here */}
      </div>
    </div>
  );
};

UserInterface.propTypes = {
  data: PropTypes.object.isRequired,
};

export default UserInterface;