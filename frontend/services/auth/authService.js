import axios from '../axiosInstance';

export async function login(username, password) {
    return await axios.post('v1/auth/login/', {
        username,
        password,
    });
}

export async function getProfile() {
    const response = await axios.get('v1/users/me');
    return response.data;
}

export async function refreshAccessToken() {
    const response = await axios.post('v1/auth/token');
    return response.data;
}
