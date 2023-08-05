```javascript
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const BackendAPIIntegration = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:5000/api/data');
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data from API', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div id="backendAPIIntegrationContainer">
            {data ? (
                <div>
                    <h2>Data from Backend API</h2>
                    <pre>{JSON.stringify(data, null, 2)}</pre>
                </div>
            ) : (
                <p>Loading data...</p>
            )}
        </div>
    );
};

export default BackendAPIIntegration;
```