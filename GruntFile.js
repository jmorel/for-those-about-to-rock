module.exports = function(grunt) {
  grunt.initConfig({
    less: {
      development: {
        options: {
          compress: true,
          yuicompress: true,
          optimization: 2,
          path: "assets/css"
        },
        files: {
          "assets/css/design.css": "assets/css/design.less",
          // "assets/css/project.css": "assets/css/project.less",
          // "assets/css/homepage.css": "assets/css/homepage.less"
        }
      }
    },
    watch: {
      styles: {
        files: ['assets/css/*.less', '*.html'], // which files to watch
        tasks: ['less'],
        options: {
          nospawn: true,
          livereload: true,
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['watch']);
};