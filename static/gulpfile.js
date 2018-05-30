var gulp = require('gulp');
var sass = require("gulp-sass");
var cssmin = require("gulp-cssmin");
var  rename = require("gulp-rename");
var clean = require('gulp-clean');
var runSequence = require('run-sequence');

//-------------Configuration------------------>

var source = 'css/app.scss';          // The location of the main scss file.
var partials = [
    'node_modules/bootstrap/scss'
]                                     // The locations of all sass partials.
var dest = 'css/';                    // Destination folder for transpiled css.

//--------------End configuration------------->

/*
 * Uses source file to generate css file.
 */
gulp.task('css', function () {
    return gulp.src(source)
        .pipe(sass({
            outputStyle: 'nested',
            precison: 4,
            errLogToConsole: true,
            includePaths: partials
        }))
        .pipe(gulp.dest(dest));
});

/*
 * Minifies generated css file.
 */ 
gulp.task('minify:css', function (done) {
    gulp.src(dest + '*.css')
        .pipe(cssmin())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(dest));
    done();
});

/*
 * Removes generated css files (scss source files remain intact)
 */ 
gulp.task('clean:css', function () {
    return gulp.src('css/*.css', {read: false})
        .pipe(clean());
});

/*
 * Default gulp task (executed when task is not specified)
 */ 
gulp.task('default', gulp.series('clean:css', 'css', 'minify:css'))