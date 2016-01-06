
var webpack = require("webpack");
var path = require("path");

module.exports = {
    entry: {
        "auth/login": "./static/js/auth/login.js",
        "auth/register": "./static/js/auth/register.js",
        "index": "./static/js/thought/index.js",
        "account/home": "./static/js/account/home.js"

    },
    output: {
        path: "./static/dist",
        publicPth: "./static/dist/",
        filename: '[name].js'
    },
    module: {
        loaders: [
            //{
            //    test: require.resolve('jquery'), // 暴露 jquery到全局
            //    loader: 'expose?jQuery'
            //},
            {
                test: /\.vue$/,
                loader: 'vue'
            },
            {
                test: /\.css$/,
                loaders: ['style', 'css'],
            }
        ]
    }
};