const webpack = require('webpack')

module.exports = {
  "configureWebpack": {
    "plugins": [
        new webpack.DefinePlugin({
            'process.env': {
                title: 'URL Shortner',
                NODE_ENV: JSON.stringify(process.env.NODE_ENV)
            }
        })
    ]
  },
  "transpileDependencies": [
    "vuetify"
  ]
}