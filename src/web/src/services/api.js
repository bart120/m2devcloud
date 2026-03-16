import axios from "axios";

const api = axios.create({
    baseURL: "https://api-doc-vl.azurewebsites.net",
});

export default api;