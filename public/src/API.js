import axios from 'axios';

async function APIRequest(path, method = 'get', data = {}) {
    try {
        let response;
        if (method.toLowerCase() === 'post') {
            response = await axios.post('http://localhost:8080/api/v1/' + path, data);
        } else {
            response = await axios.get('http://localhost:8080/api/v1/' + path);
        }
        
        if (parseInt(response.data.status) !== 1 && response.data.msg !== undefined) {
            console.error(response.data.msg);
        }
        return response.data;
    } catch (error) {
        console.error('API request failed:', error);
        return null;
    }
}

export default APIRequest;
