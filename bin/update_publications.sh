#!/bin/bash

echo "Running BibTeX conversion..."
cd "$(dirname "$0")/.."
ruby bin/bibtex_to_yaml.rb -f
echo "Conversion complete! Publications list updated."
