import React from 'react';
import PropTypes from 'prop-types';
import '../styles/DeploymentHosting.css';

function DeploymentHosting({ deploymentPlatform }) {
  return (
    <div id="deploymentHostingContainer">
      <h2>Deployment and Hosting</h2>
      <p>
        Once you have built your SpiritBoxAI application using Create React App, you can deploy it to a hosting platform such as Heroku, Netlify, or AWS. This ensures that your AI-enhanced paranormal investigation assistant is accessible to fellow investigators and enthusiasts worldwide.
      </p>
      <p>Current Deployment Platform: {deploymentPlatform}</p>
    </div>
  );
}

DeploymentHosting.propTypes = {
  deploymentPlatform: PropTypes.string.isRequired,
};

export default DeploymentHosting;