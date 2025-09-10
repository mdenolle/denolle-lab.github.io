# Managing Publications with BibTeX

This site uses a BibTeX-based system to manage and display publications. This approach allows you to:

1. Maintain all publications in a standard BibTeX file
2. Automatically generate the publication list on the website
3. Filter publications by research areas
4. Display BibTeX citations for each publication

## Initial Setup

Before using the BibTeX system, you need to install the required Ruby gems:

```bash
# Run this once to install dependencies
./bin/install_bibtex_deps.sh
```

## How to Update Publications

### Option 1: Automatic Processing (Plugin-based)

The site includes a Jekyll plugin that automatically processes your BibTeX file when the site is built:

1. Edit the `publications.bib` file in the root directory
2. Add or update your publications in BibTeX format
3. The site will automatically rebuild the publication list when you run Jekyll

### Option 2: Manual Processing

You can also manually convert the BibTeX file to YAML:

```bash
# Convert publications.bib to _data/publist.yml
./bin/bibtex_to_yaml.rb
```

Options:
- `-i, --input FILE`: Input BibTeX file (default: publications.bib)
- `-o, --output FILE`: Output YAML file (default: _data/publist.yml)
- `-f, --force`: Force overwrite of output file
- `-h, --help`: Show help message

## BibTeX Format

### Research Areas

To tag publications with research areas, use the `keywords` or `research_areas` field:

```bibtex
@article{smith2023example,
  title={Example Publication},
  author={Smith, John and Doe, Jane},
  journal={Journal of Examples},
  year={2023},
  research_areas={earthquakes, environment, geoscience-ai}
}
```

The research areas should match the keys used in your research pages.

### Required Fields

For best results, include these fields in your BibTeX entries:

- `title`: Publication title
- `author`: Author list (using standard BibTeX format)
- `journal` or `booktitle`: Where the work was published
- `year`: Publication year
- `research_areas` or `keywords`: Comma-separated list of research areas
- `doi` (optional): Digital Object Identifier
- `url` (optional): Link to the publication

## Troubleshooting

If publications aren't appearing correctly:

1. Validate your BibTeX file with a tool like [BibTeX Validator](https://www.bibtex.com/validate/)
2. Check that the Ruby gems are installed correctly
3. Run the manual conversion script to see if there are any errors
4. Check the Jekyll build log for warnings or errors
