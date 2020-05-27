import axios from 'axios'

const api = {
    addShortUrl(short_url) {
        return new Promise((resolve) => {
            axios
            .post(process.env.VUE_APP_API_BASE_URL + 'generate', {
                'url': short_url.url
            })
            .then(response => (resolve({
                'url': short_url.url,
                'short_code': response.data.short_code
            })))
        })
    },
    fetchShortUrls() {
        return new Promise((resolve) => {
            axios
            .get(process.env.VUE_APP_API_BASE_URL + 'urls')
            .then(response => (resolve(response.data)))
        })
    },
    
}

export default api;