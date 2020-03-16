# Created by lena at 3/5/2020
Feature: Test for H&M Search functionality

  Scenario: Verify that Auto-suggestion works for t-shirt
    Given Open H&M page
    When Input in Search Box Men t-shirt
    Then Count 2 suggestions

  Scenario: Verify that Auto-suggestion works for jeans
    Given Open H&M page
    When Input in Search Box Jeans
    Then Count 5 suggestions

  Scenario: Verify that Auto-suggestion works for sweatshirt
    Given Open H&M page
    When Input in Search Box Sweatshirt
    Then Count 5 suggestions

  Scenario: Verify that Auto-suggestion works for hoodie
    Given Open H&M page
    When Input in Search Box Hoodie
    Then Count 5 suggestions