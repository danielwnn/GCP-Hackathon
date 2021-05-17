Dart web application
--------------------
This sample shows how to build a web application using Dart code served by App Engine Flex.

To run the code locally a separate `pub serve` process is required to handle the Dart transformers involved when building a Dart web app.

```
$ pub serve --port 7777 web
Loading source assets...
Serving front_end web on http://localhost:7777
Build completed successfully
```

The application can subsequently be run locally:

```
$ export GCLOUD_PROJECT=<project-id>
$ export GCLOUD_KEY=<service-account-key.json>
$ export DART_PUB_SERVE=http://localhost:7777
$ dart bin/server.dart
```

Navigate to the following URL to see the app: http://localhost:8080

`pub run build_runner build` needs to be called before deploying the app to create the static version of the app. After this, the application can be deployed with `gcloud app deploy`:

```
$ pub run build_runner build
$ gcloud app deploy app.yaml
```
