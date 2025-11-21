RST Table Examples
==================

This document demonstrates all types of tables supported in reStructuredText.

Contents
--------

- `Grid Tables`_
- `Simple Tables`_
- `CSV Tables`_
- `List Tables`_

.. _grid-tables:

Grid Tables
-----------

Grid tables provide the most control over table formatting. They use characters to create borders around cells.

Basic Grid Table
----------------

+-----------+----------+-----------+
| Name      | Age      | City      |
+===========+==========+===========+
| Alice     | 25       | Seoul     |
+-----------+----------+-----------+
| Bob       | 30       | Busan     |
+-----------+----------+-----------+
| Charlie   | 35       | Incheon   |
+-----------+----------+-----------+

Grid Table with Alignment
--------------------------

+-----------+----------+-----------+
| Product   | Price    | Stock     |
+===========+==========+===========+
| Laptop    | 1,200,000|      15   |
+-----------+----------+-----------+
| Mouse     |    25,000|     120   |
+-----------+----------+-----------+
| Keyboard  |    80,000|      45   |
+-----------+----------+-----------+

Complex Grid Table
------------------

+----------------+--------+--------+--------+
| Semester       | 2023-1 | 2023-2 | 2024-1 |
+================+========+========+========+
| Students       |   120  |   135  |   142  |
+----------------+--------+--------+--------+
| Courses        |    15  |    18  |    20  |
+----------------+--------+--------+--------+
| Avg GPA        |   3.45 |   3.52 |   3.58 |
+----------------+--------+--------+--------+
| Graduates      |    28  |    32  |    35  |
+----------------+--------+--------+--------+

.. _simple-tables:

Simple Tables
-------------

Simple tables are easier to create but have less formatting control.

Basic Simple Table
------------------

=====  =========  ============
Name   Role       Department
=====  =========  ============
Kim    Manager    Sales
Lee    Developer  IT
Park   Designer   Marketing
=====  =========  ============

Simple Table with Multi-word Headers
-------------------------------------

=====  =============  ===================
ID     Full Name      Email
=====  =============  ===================
E001   Kim Minseo     kim.m@company.com
E002   Lee Joonho     lee.j@company.com
E003   Park Sooyoung  park.s@company.com
=====  =============  ===================

Simple Table with Numbers
--------------------------

=====  =======  ==========
Month  Revenue  Expenses
=====  =======  ==========
Jan    5,000    3,500
Feb    5,500    3,800
Mar    6,200    4,100
=====  =======  ==========

.. _csv-tables:

CSV Tables
----------

CSV tables are created from comma-separated values. They're simple but less flexible.

Basic CSV Table
---------------

.. csv-table:: Employee Information
   :header: "Name", "Position", "Salary"
   :widths: 20, 20, 15
   
   Kim Minseo, Software Engineer, 5000000
   Lee Joonho, Data Analyst, 4500000
   Park Sooyoung, UI Designer, 4800000

CSV Table with Multiple Columns
--------------------------------

.. csv-table:: Course Schedule
   :header: "Course", "Instructor", "Students", "Room"
   :widths: 25, 20, 10, 10
   
   Data Structures, Prof. Kim, 45, A-101
   Algorithms, Prof. Lee, 42, B-205
   Database Systems, Prof. Park, 38, C-301

CSV Table without Headers
--------------------------

.. csv-table:: 
   :widths: 15, 20, 15
   
   Project A, In Progress, 75%
   Project B, Completed, 100%
   Project C, Planning, 25%

.. _list-tables:

List Tables
-----------

List tables use simple lists to create two-column tables.

Basic List Table
----------------

.. list-table:: Product Features
   :widths: 30 50
   :header-rows: 1
   
   * - Feature
     - Description
   * - Security
     - Encrypted data transmission with SSL/TLS
   * - Performance
     - Optimized for high-speed processing
   * - Scalability
     - Supports horizontal scaling up to 1000 nodes

List Table with Multiple Columns
----------------------------------

.. list-table:: System Requirements
   :widths: 20 20 20 20
   :header-rows: 1
   
   * - Component
     - Minimum
     - Recommended
     - Optimal
   * - CPU
     - 2 cores
     - 4 cores
     - 8 cores
   * - RAM
     - 4 GB
     - 8 GB
     - 16 GB
   * - Storage
     - 50 GB
     - 100 GB
     - 250 GB

List Table without Headers
---------------------------

.. list-table::
   :widths: 25 25 25 25
   
   * - Python
     - JavaScript
     - Java
     - C++
   * - 3.12
     - ES2023
     - 21
     - C++23

Mixed Content Table
-------------------

.. list-table:: Project Status
   :widths: 25 50 25
   :header-rows: 1
   
   * - Project
     - Status & Notes
     - Completion
   * - Website Redesign
     - In progress. UI mockups approved, development started.
     - 60%
   * - Mobile App
     - Testing phase. Beta release scheduled next month.
     - 85%
   * - API Integration
     - Planning stage. Requirements gathering in progress.
     - 15%

Summary
=======

This document demonstrates four main types of RST tables:

1. **Grid Tables**: Full control, uses ASCII characters for borders
2. **Simple Tables**: Easy to create, less formatting options
3. **CSV Tables**: Good for data imported from spreadsheets
4. **List Tables**: Flexible, supports multi-line content

Each table type has its own use case. Choose based on your formatting needs and data complexity.

