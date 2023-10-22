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
    plugins: [
        {
            src: '~/plugins/axios.js',
            mode: 'client',
            ssr: false
        }
    ],

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
        '@nuxtjs/auth-next',
        '@nuxtjs/toast'
    ],

    publicRuntimeConfig: {
        axios: {
            baseURL: process.env.BASEURL || 'http://127.0.0.1:8000',
        },
    },

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
        // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
        baseURL: process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:8000' : process.env.BASEURL,
    },

    router: {
        middleware: ['auth']
    },

    watchers: {
        webpack: {
            poll: 1000,
            ignored: /node_modules/
        }
    },

    toast: {
        position: 'top-right',
        register: [ // Register custom toasts
            {
                name: 'my-error',
                message: 'Oops...Something went wrong',
                options: {
                    type: 'error'
                }
            }
        ]
    },

    // Loading module configuration: https://go.nuxtjs.dev/config-loading
    loading: {
        name: 'chasing-dots',
        color: '#ff5638',
        background: 'white',
        height: '4px'
    },

    auth: {
        strategies: {
            local: {
                // scheme: 'refresh',
                autoLogout: true,
                token: {
                    property: 'access_token',
                    maxAge: 31536000,
                    required: true,
                    type: 'Bearer'
                },
                property: 'refresh_token',
                refreshToken: {
                    data: 'refresh_token',
                    maxAge: 60 * 60 * 24 * 30
                },
                endpoints: {
                    login: {
                        url: '/auth/login',
                        method: 'post',
                        propertyName: 'data.access_token',
                    },
                    refresh: { url: '/auth/refresh', method: 'post' },
                    logout: { url: '/auth/logout', method: 'post', },
                    user: false,
                },
                autoFetchUser: false,
            }
        },
        // redirect: {
        //     logout: '/',
        //     callback: '/callback'
        // }
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
        transpile: ['@nuxtjs/auth-next'],
        extend(config, ctx) {
            if (ctx.isDev) {
                config.devtool = ctx.isClient ? 'source-map' : 'inline-source-map'
            }
        }
    },
};
