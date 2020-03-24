# Created by lena at 3/24/2020
Feature: Test for H&M Search functionality
  # Enter feature description here

  Scenario Outline: Verify that Auto-suggestion works for t-shirt
    # Enter steps here
    Given Open H&M page
    When Input in Search Box <product>
    Then Count <Number> suggestions

    Examples: Products
    | product         | Number |
    | Men t-shirt     | 2      |
    | Jeans           | 5      |
    | Sweatshirt      | 5      |
    | Hoodie          | 5      |



