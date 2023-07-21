#!/bin/bash

flutter test --coverage
genhtml coverage/lcov.info --output-directory coverage/coverage_report
xdg-open coverage/coverage_report/index.html &