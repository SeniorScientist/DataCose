export default function ({ $axios, $auth, redirect }) {
    // Request interceptor
    $axios.onRequest((config) => {
        // Get the authentication token from your Vuex store or any other source
        // const token = $auth.token.get();

        // // If a token is available, attach it to the request headers
        // if (token) {
        //     config.headers.common.Authorization = `Bearer ${token}`
        // }

        // Modify the request configuration before sending
        console.log('Making a request to ' + config.url)
        // You can also add headers, authentication, etc. here
    });

    // Response interceptor
    $axios.onResponse((response) => {
        // Modify the response data before it's used
        console.log('Received a response with data:', response.data)

        return Promise.resolve(response.data)
    });

    // Error interceptor
    $axios.onError((error) => {
        console.log('Response error', error)
        // Handle errors here
        if (error.response.status === 400) {
            redirect('/sorry')
        } else {
            nuxtError({
                statusCode: error.response.status,
                message: error.message,
            });
            return Promise.reject(error)
        }
    });
}