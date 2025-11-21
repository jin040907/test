const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

/**
 * Parser for conf.yml file
 * Handles YAML anchors, aliases, and merge keys
 */
class ConfParser {
  constructor(configPath = '../config/conf.yml') {
    this.configPath = path.resolve(configPath);
    this.config = null;
  }

  /**
   * Load and parse the YAML configuration file
   * @returns {Object} Parsed configuration object
   */
  load() {
    try {
      const fileContents = fs.readFileSync(this.configPath, 'utf8');
      this.config = yaml.load(fileContents, {
        // Enable schema that supports YAML anchors and aliases
        schema: yaml.DEFAULT_SCHEMA
      });
      return this.config;
    } catch (error) {
      throw new Error(`Failed to parse ${this.configPath}: ${error.message}`);
    }
  }

  /**
   * Get a specific value from the configuration
   * @param {string} key - Dot-notation path to the value (e.g., 'student.name')
   * @returns {*} The value at the specified path
   */
  get(key) {
    if (!this.config) {
      this.load();
    }

    const keys = key.split('.');
    let value = this.config;

    for (const k of keys) {
      if (value && typeof value === 'object' && k in value) {
        value = value[k];
      } else {
        return undefined;
      }
    }

    return value;
  }

  /**
   * Get all students
   * @returns {Array} Array of student objects
   */
  getStudents() {
    if (!this.config) {
      this.load();
    }

    const students = [];
    for (const key in this.config) {
      // Only include actual student entries (not templates)
      if (key.startsWith('student') && 
          !key.includes('_template') && 
          !key.includes('_details') &&
          typeof this.config[key] === 'object' &&
          this.config[key].name) {
        students.push({
          id: key,
          ...this.config[key]
        });
      }
    }
    return students;
  }

  /**
   * Get the entire configuration object
   * @returns {Object} The full configuration
   */
  getAll() {
    if (!this.config) {
      this.load();
    }
    return this.config;
  }

  /**
   * Validate the configuration structure
   * @returns {Object} Validation result with isValid and errors
   */
  validate() {
    if (!this.config) {
      this.load();
    }

    const errors = [];

    // Validate required fields
    if (!this.config.site) {
      errors.push('Missing required field: site');
    }
    if (!this.config.theme) {
      errors.push('Missing required field: theme');
    }

    // Validate student structure if exists
    if (this.config.student) {
      if (!this.config.student.name) {
        errors.push('Student missing required field: name');
      }
      if (this.config.student.details) {
        if (!this.config.student.details.fatherName) {
          errors.push('Student details missing: fatherName');
        }
        if (!this.config.student.details.motherName) {
          errors.push('Student details missing: motherName');
        }
      }
    }

    return {
      isValid: errors.length === 0,
      errors
    };
  }

  /**
   * Pretty print the configuration
   */
  print() {
    if (!this.config) {
      this.load();
    }
    console.log(JSON.stringify(this.config, null, 2));
  }
}

// If run directly, parse and display the configuration
if (require.main === module) {
  const parser = new ConfParser('../config/conf.yml');
  
  try {
    const config = parser.load();
    console.log('=== Configuration loaded successfully ===\n');
    
    // Display parsed configuration
    parser.print();
    
    console.log('\n=== Accessing specific values ===');
    console.log('Site:', parser.get('site'));
    console.log('Theme:', parser.get('theme'));
    console.log('Items:', parser.get('items'));
    console.log('Student name:', parser.get('student.name'));
    console.log('Student details:', parser.get('student.details'));
    console.log('Student subjects:', parser.get('student.more'));
    
    console.log('\n=== All students ===');
    const students = parser.getStudents();
    console.log(JSON.stringify(students, null, 2));
    
    console.log('\n=== Validation ===');
    const validation = parser.validate();
    console.log('Valid:', validation.isValid);
    if (validation.errors.length > 0) {
      console.log('Errors:', validation.errors);
    }
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

module.exports = ConfParser;

