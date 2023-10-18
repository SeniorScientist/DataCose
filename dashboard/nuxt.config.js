export default {
    // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
    ssr: false,

    // Target: https://go.nuxtjs.dev/config-target
    target: 'static',

    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'DC Full Stack Code Challenge',
        htmlAttrs: {
            lang: 'en',
        },
        meta: [
            { charset: 'utf-8' },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1',
            },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' },
        ],
        link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],

    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
        // https://go.nuxtjs.dev/typescript
        '@nuxt/typescript-build',
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/bootstrap
        ['bootstrap-vue/nuxt', { icons: true, css: true }],
        // https://go.nuxtjs.dev/axios
        '@nuxtjs/axios',
        '@nuxtjs/auth',
        // '@nuxtjs/toast'
    ],

    publicRuntimeConfig: {
        axios: {
            baseURL: process.env.BASEURL || 'http://127.0.0.1:8000',
        },
    },

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
        // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
        baseURL: process.env.NODE_ENV == 'development' ? 'http://127.0.0.1:8000' : process.env.BASEURL,
    },

    // toast: {
    //     position: 'top-right',
    //     duration: 2000
    // },

    // Loading module configuration: https://go.nuxtjs.dev/config-loading
    loading: {
        name: 'chasing-dots',
        color: '#ff5638',
        background: 'white',
        height: '4px'
    },

    // Auth module configuration: https://go.nuxtjs.dev/config-auth
    auth: {
        strategies: {
            local: {
                endpoints: {
                    login: { url: '/user/login', method: 'post', propertyName: 'token' },
                    logout: false,
                    user: { url: '/user/user', method: 'get', propertyName: 'data' },
                },
                tokenRequired: true,
                tokenType: 'Bearer'
            }
        },
        redirect: {
            login: '/?login=1',
            logout: '/',
            callback: '/'
        }
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {},
};
