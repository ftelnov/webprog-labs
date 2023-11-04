function defaultTask(cb) {
  console.log("Default task is being executed");
  cb();
}

exports.default = defaultTask;
