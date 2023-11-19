const gulp = require("gulp");
const browserSync = require("browser-sync").create();

gulp.task("task1", function (callback) {
  console.log("Task 1 is called");
  callback();
});

gulp.task("task2", function (callback) {
  console.log("Task 2 is called");
  callback();
});

gulp.task("browserSync", function () {
  browserSync.init({
    server: {
      baseDir: "./",
    },
  });

  gulp.watch("*.html").on("change", browserSync.reload);
});

gulp.task("default", gulp.series("browserSync"));
// gulp.task("default", gulp.parallel("task1", "task2"));
// gulp.task("default", gulp.series("task1", "task2"));
