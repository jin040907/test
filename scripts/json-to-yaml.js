const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

/**
 * Convert JSON file to YAML file
 * @param {string} jsonPath - Path to input JSON file
 * @param {string} yamlPath - Path to output YAML file (optional)
 */
function convertJsonToYaml(jsonPath, yamlPath = null) {
  try {
    // Read JSON file
    const jsonContent = fs.readFileSync(jsonPath, 'utf8');
    const jsonData = JSON.parse(jsonContent);

    // Convert to YAML
    const yamlContent = yaml.dump(jsonData, {
      indent: 2,
      lineWidth: -1, // No line wrapping
      noRefs: true, // Don't use YAML references
      quotingType: '"',
      forceQuotes: false
    });

    // Determine output path
    const outputPath = yamlPath || jsonPath.replace(/\.json$/, '.yml');

    // Write YAML file
    fs.writeFileSync(outputPath, yamlContent, 'utf8');
    console.log(`✅ Successfully converted ${jsonPath} to ${outputPath}`);
    return outputPath;
  } catch (error) {
    console.error(`❌ Error converting file: ${error.message}`);
    process.exit(1);
  }
}

// If run directly, convert person.json
if (require.main === module) {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    // Default: convert person.json
    const jsonFile = path.join(__dirname, 'person.json');
    if (fs.existsSync(jsonFile)) {
      convertJsonToYaml(jsonFile);
    } else {
      console.error('❌ person.json not found');
      process.exit(1);
    }
  } else {
    // Convert specified file
    const jsonPath = args[0];
    const yamlPath = args[1] || null;
    convertJsonToYaml(jsonPath, yamlPath);
  }
}

module.exports = convertJsonToYaml;

