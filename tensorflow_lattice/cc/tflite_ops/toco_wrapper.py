# Copyright 2018 The TensorFlow Lattice Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Runs TOCO tflite_converter after importing tensorflow_lattice ops."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

# Dependency imports
# tensorflow_lattice must be imported in order for tensorflow to recognize its
# custom ops, which is necessary for toco to find them
import tensorflow_lattice  # pylint: disable=unused-import
from tensorflow.lite.python import tflite_convert


def main():
  return tflite_convert.app.run(main=tflite_convert.run_main, argv=sys.argv[:1])


if __name__ == '__main__':
  main()
