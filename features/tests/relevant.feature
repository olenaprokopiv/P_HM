 #Created by lena at 3/6/2020
Feature: Test for H&M Search functionality

  Scenario: User is taken to the search results page
  Given Open H&M page
  When  Search product Accessories
  Then Search results for Accessories is shown
