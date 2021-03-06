
var webpack = require("webpack");
var path = require("path");

module.exports = {
    entry: {
        "auth/login": "./static/js/auth/login.js",
        "auth/register": "./static/js/auth/register.js"
    },
    output: {
        path: "./static/dist",
        publicPth: "./static/dist/",
        filename: '[name].js'
    },
    module: {
/*        loaders:[
            {
                test: require.resolve('jquery'), // 暴露 jquery到全局
                loader: 'expose?jQuery'
            }
        ]*/
        loaders: [
            {
                test: /\.vue$/,
                loader: 'vue'
            }
        ]
    }
};