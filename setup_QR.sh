#!/bin/bash
BUILD_DIR="mpo_application/build"
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"
cmake ..
make