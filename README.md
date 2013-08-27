zookeeper-gyp
=============

build zookeeper C library and cli tool using gyp

This repo contains GYP configure file to generate multi-platform build configuration for zookeeper native C library and client. Zookeeper version is based on 3.4.5.

For visual studio, you may need to disable Treat Warnings As Errors setting in the zookeeper property page

For Xcode, you may need to change C Language dialects to -std=gnu99.

This gyp only builds static library and generates zookeeper.lib and zkcli executeble.

