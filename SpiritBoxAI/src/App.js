```javascript
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import RealTimeAnalysis from './components/RealTimeAnalysis';
import DataInterpretation from './components/DataInterpretation';
import PhenomenaAnalysis from './components/PhenomenaAnalysis';
import EMFMonitoring from './components/EMFMonitoring';
import UserInterface from './components/UserInterface';
import BackendAPIIntegration from './components/BackendAPIIntegration';
import HistoricalDataAnalysis from './components/HistoricalDataAnalysis';
import DeploymentHosting from './components/DeploymentHosting';
import Header from './components/Header';
import Footer from './components/Footer';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Switch>
          <Route path="/real-time-analysis" component={RealTimeAnalysis} />
          <Route path="/data-interpretation" component={DataInterpretation} />
          <Route path="/phenomena-analysis" component={PhenomenaAnalysis} />
          <Route path="/emf-monitoring" component={EMFMonitoring} />
          <Route path="/user-interface" component={UserInterface} />
          <Route path="/backend-api-integration" component={BackendAPIIntegration} />
          <Route path="/historical-data-analysis" component={HistoricalDataAnalysis} />
          <Route path="/deployment-hosting" component={DeploymentHosting} />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
```