const pages = {
  index: 'src/main.js',
};

module.exports = {
  publicPath: "/static/vue/",
  outputDir: './build/static/vue/',
  indexPath: "../../templates/vue_index.html",

  chainWebpack: config => {
      config.optimization
  .splitChunks(false);

  config.resolve.alias
  .set('__STATIC__', 'static');

  config.devServer
  .public('http://0.0.0.0:8080')
      .host('0.0.0.0')
      .port(8080)
      .hotOnly(true)
      .watchOptions({poll: 1000})
      .https(false)
      .headers({"Access-Control-Allow-Origin": ["*"]});
  },

  pages: pages,

};
