import axios from 'axios';

async function APIRequest(path) {
    try {
        const response = await axios.get('http://localhost:8080/api/v1/' + path);
        
        if (parseInt(response.data.status) !== 1) {
            console.error(response.data.msg);
        }

        return response.data;
    } catch (error) {
        console.error('API request failed:', error);
        return null;
    }
}

export default APIRequest;
